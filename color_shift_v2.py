"""
Chaos Station v2 - Smart character color shift.
Uses HSV-based masking to shift specific color ranges (overalls, outfits)
while preserving skin tones, eyes, and other neutral colors.

Character outfit colors:
- Mario: Red overalls/cap -> Dark black-purple (shadow king)
- Luigi: Green overalls -> Teal/cyan (ice)
- Toad (Blue): Blue vest -> Purple (mystical)
- Toad (Yellow): Yellow vest/spots -> Orange-red (fire)
"""

import sys, struct, os
import colorsys
sys.path.insert(0, '.')
from tools.u8archive import U8Archive


def rgb565_to_rgb(val):
    r = ((val >> 11) & 0x1F) * 255 // 31
    g = ((val >> 5) & 0x3F) * 255 // 63
    b = (val & 0x1F) * 255 // 31
    return r, g, b


def rgb_to_rgb565(r, g, b):
    return ((max(0,min(31, r * 31 // 255)) << 11) |
            (max(0,min(63, g * 63 // 255)) << 5) |
            (max(0,min(31, b * 31 // 255))))


def is_skin_tone(r, g, b):
    """Detect if a pixel is a skin tone (peachy/beige)."""
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    # Skin: low saturation, medium brightness, warm hue (orange-ish)
    if s < 0.25 and 0.15 < v < 0.95:
        if 0.0 < h < 0.15 or h > 0.9:  # Orange-red hue range
            return True
    # Light beige skin
    if r > 180 and g > 140 and b > 100 and r > g > b:
        if (r - b) > 50 and (g - b) > 20:
            return True
    # Darker skin
    if 100 < r < 220 and 80 < g < 180 and 60 < b < 140:
        if r > g and g > b and (r - b) > 30:
            return True
    return False


def is_eye_or_white(r, g, b):
    """Detect white/gray (eyes, buttons, etc)."""
    if r > 200 and g > 200 and b > 200:
        return True
    if r < 60 and g < 60 and b < 60:
        return True  # Pure black (outlines)
    return False


def should_shift(r, g, b, target_hue_range, sat_threshold=0.25):
    """Check if this pixel should be color-shifted based on hue."""
    if is_skin_tone(r, g, b):
        return False
    if is_eye_or_white(r, g, b):
        return False

    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)

    # Only shift saturated colors (outfit, not background grays)
    if s < sat_threshold:
        return False

    h_min, h_max = target_hue_range
    if h_min <= h_max:
        return h_min <= h <= h_max
    else:  # Wraps around 0
        return h >= h_min or h <= h_max


def smart_shift(r, g, b, target_hue_range, new_hue, new_sat_mult, new_val_mult):
    """Shift only outfit-colored pixels to new colors."""
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)

    if should_shift(r, g, b, target_hue_range):
        # Shift to new hue, adjust sat/val
        new_h = (new_hue + (h - sum(target_hue_range) / 2) * 0.3) % 1.0
        new_s = min(1.0, s * new_sat_mult)
        new_v = min(1.0, v * new_val_mult)
        nr, ng, nb = colorsys.hsv_to_rgb(new_h, new_s, new_v)
        return int(nr * 255), int(ng * 255), int(nb * 255)
    return r, g, b


def shift_cmpr_smart(data, pixel_shifter):
    """Process CMPR texture with smart pixel shifting."""
    result = bytearray(data)

    for i in range(0, len(result) - 7, 8):
        c0 = struct.unpack_from('>H', result, i)[0]
        c1 = struct.unpack_from('>H', result, i + 2)[0]

        r0, g0, b0 = rgb565_to_rgb(c0)
        r1, g1, b1 = rgb565_to_rgb(c1)

        nr0, ng0, nb0 = pixel_shifter(r0, g0, b0)
        nr1, ng1, nb1 = pixel_shifter(r1, g1, b1)

        struct.pack_into('>H', result, i, rgb_to_rgb565(nr0, ng0, nb0))
        struct.pack_into('>H', result, i + 2, rgb_to_rgb565(nr1, ng1, nb1))

    return bytes(result)


def shift_rgb5a3_brres(data, pixel_shifter):
    """Process RGB5A3 tiled texture with smart pixel shifting."""
    result = bytearray(data)

    for i in range(0, len(result) - 1, 2):
        val = struct.unpack_from('>H', result, i)[0]
        if val & 0x8000:
            a = 255
            r = ((val >> 10) & 0x1F) * 255 // 31
            g = ((val >> 5) & 0x1F) * 255 // 31
            b = (val & 0x1F) * 255 // 31
        else:
            a = ((val >> 12) & 0x07) * 255 // 7
            r = ((val >> 8) & 0x0F) * 255 // 15
            g = ((val >> 4) & 0x0F) * 255 // 15
            b = (val & 0x0F) * 255 // 15

        if a > 10:
            nr, ng, nb = pixel_shifter(r, g, b)
            if a >= 248:
                new_val = 0x8000 | ((max(0, min(31, nr * 31 // 255)) << 10) |
                                   (max(0, min(31, ng * 31 // 255)) << 5) |
                                   (max(0, min(31, nb * 31 // 255))))
            else:
                new_val = ((max(0, min(7, a * 7 // 255)) << 12) |
                          (max(0, min(15, nr * 15 // 255)) << 8) |
                          (max(0, min(15, ng * 15 // 255)) << 4) |
                          (max(0, min(15, nb * 15 // 255))))
            struct.pack_into('>H', result, i, new_val)

    return bytes(result)


def process_brres(brres_data, pixel_shifter, formats=(14,)):
    """Process textures in a BRRES. Default: CMPR only.
    Pass formats=(14, 5) to also process RGB5A3.
    """
    data = bytearray(brres_data)
    pos = 0
    count = 0

    while True:
        pos = data.find(b'TEX0', pos)
        if pos == -1:
            break

        section_size = struct.unpack_from('>I', data, pos + 4)[0]
        dims = struct.unpack_from('>I', data, pos + 0x1C)[0]
        width = (dims >> 16) & 0xFFFF
        height = dims & 0xFFFF
        fmt = struct.unpack_from('>I', data, pos + 0x20)[0]

        if width > 0 and height > 0 and section_size > 0x40 and fmt in formats:
            data_start = pos + 0x40
            data_size = section_size - 0x40
            if data_start + data_size <= len(data):
                pixel_data = bytes(data[data_start:data_start + data_size])
                if fmt == 14:
                    shifted = shift_cmpr_smart(pixel_data, pixel_shifter)
                elif fmt == 5:
                    shifted = shift_rgb5a3_brres(pixel_data, pixel_shifter)
                else:
                    shifted = None
                if shifted:
                    data[data_start:data_start + len(shifted)] = shifted
                    count += 1
        pos += 4

    print(f'    Shifted {count} textures')
    return bytes(data)


def process_character(arc_path, output_path, pixel_shifter, label):
    """Process a character archive - handles both CMPR and RGB5A3 textures."""
    print(f'\n=== {label} ===')
    with open(arc_path, 'rb') as f:
        arc = U8Archive.load(f.read())

    for fpath in arc.list_files():
        if fpath.endswith('.brres'):
            orig = arc.get_file(fpath)
            # Process both CMPR (14) and RGB5A3 (5) textures
            shifted = process_brres(orig, pixel_shifter, formats=(14, 5))
            arc.set_file(fpath, shifted)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'wb') as f:
        f.write(arc.pack())
    print(f'    Saved: {output_path}')


if __name__ == '__main__':
    print('=== Chaos Station v2 - Smart Character Color Shifts ===')

    # Mario: Red (hue 0.95-1.0, 0.0-0.05) -> Dark purple-black
    def mario_shifter(r, g, b):
        return smart_shift(r, g, b,
            target_hue_range=(0.92, 0.06),  # Red range
            new_hue=0.75,  # Purple
            new_sat_mult=0.5,  # Desaturated
            new_val_mult=0.45   # Very dark
        )

    process_character(
        'extracted files/Object/Mario.arc',
        'output/ChaosStation/Object/Mario.arc',
        mario_shifter,
        'Mario (Red -> Dark Purple-Black)'
    )

    # Luigi: Green (hue 0.25-0.45) -> Teal/Cyan
    def luigi_shifter(r, g, b):
        return smart_shift(r, g, b,
            target_hue_range=(0.20, 0.45),  # Green range
            new_hue=0.52,  # Teal/cyan
            new_sat_mult=1.1,  # Slightly more saturated
            new_val_mult=0.75  # Darker
        )

    process_character(
        'extracted files/Object/Luigi.arc',
        'output/ChaosStation/Object/Luigi.arc',
        luigi_shifter,
        'Luigi (Green -> Teal)'
    )

    # Toad (Kinopio): Blue (hue 0.55-0.70) -> Purple, Yellow (hue 0.12-0.18) -> Orange-red
    # This shifts BOTH Blue Toad and Yellow Toad's outfit colors
    def toad_shifter(r, g, b):
        h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)

        # Check if it's a blue outfit color (Blue Toad's vest/spots)
        if should_shift(r, g, b, (0.55, 0.72), sat_threshold=0.2):
            # Blue -> Deep Purple
            return smart_shift(r, g, b, (0.55, 0.72), 0.78, 1.1, 0.8)

        # Check if it's a yellow outfit color (Yellow Toad's vest/spots)
        if should_shift(r, g, b, (0.08, 0.18), sat_threshold=0.2):
            # Yellow -> Fiery Orange-Red
            return smart_shift(r, g, b, (0.08, 0.18), 0.03, 1.2, 0.9)

        # Red accents -> darker red
        if should_shift(r, g, b, (0.92, 0.06), sat_threshold=0.2):
            return smart_shift(r, g, b, (0.92, 0.06), 0.98, 0.8, 0.7)

        return r, g, b

    process_character(
        'extracted files/Object/Kinopio.arc',
        'output/ChaosStation/Object/Kinopio.arc',
        toad_shifter,
        'Toads (Blue->Purple, Yellow->Orange-Red)'
    )

    # Peach: Pink dress -> Dark purple (to match Mario)
    def peach_shifter(r, g, b):
        return smart_shift(r, g, b,
            target_hue_range=(0.82, 0.95),  # Pink range
            new_hue=0.75,  # Purple
            new_sat_mult=0.6,
            new_val_mult=0.5
        )

    if os.path.exists('extracted files/Object/peach.arc'):
        process_character(
            'extracted files/Object/peach.arc',
            'output/ChaosStation/Object/peach.arc',
            peach_shifter,
            'Peach (Pink -> Dark Purple)'
        )

    # MG_Kinopio (mini-game Toad) - same as regular Toad
    if os.path.exists('extracted files/Object/MG_kinopio.arc'):
        process_character(
            'extracted files/Object/MG_kinopio.arc',
            'output/ChaosStation/Object/MG_kinopio.arc',
            toad_shifter,
            'MG_Toad (Blue->Purple, Yellow->Orange-Red)'
        )

    # Star Coin: Gold -> Teal
    def star_coin_shifter(r, g, b):
        h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
        if s < 0.1: return r, g, b
        # Gold (hue 0.08-0.18) -> Teal (hue 0.5)
        if 0.08 <= h <= 0.18:
            new_h = (h + 0.4) % 1.0  # shift toward teal
            new_s = min(1.0, s * 0.9)
            new_v = min(1.0, v * 0.9)
            nr, ng, nb = colorsys.hsv_to_rgb(new_h, new_s, new_v)
            return int(nr * 255), int(ng * 255), int(nb * 255)
        return r, g, b

    process_character(
        'extracted files/Object/star_coin.arc',
        'output/ChaosStation/Object/star_coin.arc',
        star_coin_shifter,
        'Star Coin (Gold -> Teal)'
    )

    # Regular Coins: Gold -> Teal
    for coin_name in ['coin', 'obj_coin', 'red_ring']:
        src = f'extracted files/Object/{coin_name}.arc'
        dst = f'output/ChaosStation/Object/{coin_name}.arc'
        if os.path.exists(src):
            process_character(
                src,
                dst,
                star_coin_shifter,
                f'{coin_name} (Gold -> Teal)'
            )

    print('\n=== Done! ===')
    print('\nCharacter themes:')
    print('  Mario: Dark purple-black shadow king')
    print('  Luigi: Icy teal/cyan')
    print('  Blue Toad: Deep purple mystic')
    print('  Yellow Toad: Fiery orange-red')
    print('  Star Coin & Coins: Teal')
