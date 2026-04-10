"""
Chaos Station v2 - Complete texture color shift.
Processes ALL texture modifications in one pass, using original files as source.

Shifts:
- Coins: gold -> teal
- Star/Collection coins: gold -> teal
- Powerup icons: desaturated/darker
- Mario portrait: darkened
"""

import sys, struct, os
import colorsys
sys.path.insert(0, '.')
from tools.u8archive import U8Archive


def is_skin(r, g, b):
    """Detect skin tones - don't shift these."""
    if r > 180 and g > 140 and b > 100 and r > g > b:
        if (r - b) > 40 and (g - b) > 15:
            return True
    if 100 < r < 230 and 80 < g < 190 and 50 < b < 150:
        if r > g > b and (r - b) > 25:
            h, s, _ = colorsys.rgb_to_hsv(r/255, g/255, b/255)
            if 0.0 <= h <= 0.15 and s < 0.6:
                return True
    return False


def shift_icon_rgb5a3(data, target_hue_range, new_hue, sat_mult, val_mult):
    """Process an RGB5A3 icon with targeted color shifting.
    Only shifts pixels matching the target hue range.
    Preserves skin tones, black outlines, and white areas.
    """
    header = data[:0x20]
    result = bytearray(header) + bytearray(data[0x20:])

    width = struct.unpack_from('>H', result, 0x16)[0]
    height = struct.unpack_from('>H', result, 0x14)[0]
    tiles_w = (width + 3) // 4

    def decode(val):
        if val & 0x8000:
            a = 255; r = ((val >> 10) & 0x1F) * 255 // 31
            g = ((val >> 5) & 0x1F) * 255 // 31; b = (val & 0x1F) * 255 // 31
        else:
            a = ((val >> 12) & 0x07) * 255 // 7; r = ((val >> 8) & 0x0F) * 255 // 15
            g = ((val >> 4) & 0x0F) * 255 // 15; b = (val & 0x0F) * 255 // 15
        return r, g, b, a

    def encode(r, g, b, a):
        if a >= 248:
            return 0x8000 | ((max(0,min(31,r*31//255))<<10)|(max(0,min(31,g*31//255))<<5)|max(0,min(31,b*31//255)))
        else:
            return ((max(0,min(7,a*7//255))<<12)|(max(0,min(15,r*15//255))<<8)|(max(0,min(15,g*15//255))<<4)|max(0,min(15,b*15//255)))

    h_min, h_max = target_hue_range

    for tile_y in range((height + 3) // 4):
        for tile_row in range(4):
            py = tile_y * 4 + tile_row
            if py >= height: continue
            for tile_x in range(tiles_w):
                tile_idx = tile_y * tiles_w + tile_x
                for tile_col in range(4):
                    px = tile_x * 4 + tile_col
                    if px >= width: continue
                    off = 0x20 + tile_idx * 32 + tile_row * 8 + tile_col * 2
                    if off + 2 > len(result): continue

                    val = struct.unpack_from('>H', result, off)[0]
                    r, g, b, a = decode(val)

                    if a > 10 and not is_skin(r, g, b) and not (r > 230 and g > 230 and b > 230) and not (r < 30 and g < 30 and b < 30):
                        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
                        if s >= 0.15:
                            in_range = (h_min <= h <= h_max) if h_min <= h_max else (h >= h_min or h <= h_max)
                            if in_range:
                                hue_offset = h - (h_min + h_max) / 2
                                new_h = (new_hue + hue_offset * 0.2) % 1.0
                                new_s = min(1.0, s * sat_mult)
                                new_v = min(1.0, v * val_mult)
                                nr, ng, nb = colorsys.hsv_to_rgb(new_h, new_s, new_v)
                                struct.pack_into('>H', result, off, encode(int(nr*255), int(ng*255), int(nb*255), a))

    return bytes(result)


def shift_rgb5a3_tile(data, hue_shift, sat_mult, val_mult):
    """Process RGB5A3 tiled pixel data with HSV shift.
    Handles the 4x4 tile format used by GC/Wii textures.
    Pixel data starts at offset 0x20.
    """
    header = data[:0x20]
    pixel_data = data[0x20:]

    def decode(val):
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
        return r, g, b, a

    def encode(r, g, b, a):
        if a >= 248:
            return 0x8000 | ((max(0, min(31, r * 31 // 255)) << 10) |
                             (max(0, min(31, g * 31 // 255)) << 5) |
                             (max(0, min(31, b * 31 // 255))))
        else:
            return ((max(0, min(7, a * 7 // 255)) << 12) |
                    (max(0, min(15, r * 15 // 255)) << 8) |
                    (max(0, min(15, g * 15 // 255)) << 4) |
                    (max(0, min(15, b * 15 // 255))))

    result = bytearray(pixel_data)
    for i in range(0, len(result) - 1, 2):
        val = struct.unpack_from('>H', result, i)[0]
        r, g, b, a = decode(val)
        if a > 10:
            h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
            h = (h + hue_shift) % 1.0
            s = min(1.0, s * sat_mult)
            v = min(1.0, v * val_mult)
            nr, ng, nb = colorsys.hsv_to_rgb(h, s, v)
            struct.pack_into('>H', result, i, encode(int(nr * 255), int(ng * 255), int(nb * 255), a))

    return bytes(header) + bytes(result)


# Format: (tpl_path, hue_shift, sat_mult, val_mult, label) for simple shifts
# or (tpl_path, 'icon', target_hue_range, new_hue, sat_mult, val_mult, label) for icon shifts
TEXTURE_SHIFTS = {
    'pauseMenu': [
        ('arc/timg/im_coin_00.tpl', 0.45, 0.8, 0.9, 'coin gold->teal'),
    ],
    'gameScene': [
        ('arc/timg/im_coin_01.tpl', 0.45, 0.8, 0.9, 'coin gold->teal'),
        ('arc/timg/im_collectionCoin_01.tpl', 0.45, 0.8, 0.9, 'collection coin teal'),
        ('arc/timg/im_marioIcon_01.tpl', 'icon', (0.90, 0.08), 0.75, 0.4, 0.35, 'mario icon purple'),
        ('arc/timg/im_luijiIcon_01.tpl', 'icon', (0.20, 0.45), 0.52, 1.1, 0.7, 'luigi icon teal'),
        ('arc/timg/im_kinopioIcon_Blue_01.tpl', 'icon', (0.55, 0.72), 0.78, 1.1, 0.75, 'blue toad icon purple'),
        ('arc/timg/im_kinopioIcon_Yellow_01.tpl', 'icon', (0.08, 0.18), 0.03, 1.2, 0.85, 'yellow toad icon orange'),
    ],
    'preGame': [
        ('arc/timg/im_coin_00.tpl', 0.45, 0.8, 0.9, 'coin gold->teal'),
        ('arc/timg/im_marioIcon_01.tpl', 'icon', (0.90, 0.08), 0.75, 0.4, 0.35, 'mario icon'),
        ('arc/timg/im_luijiIcon_01.tpl', 'icon', (0.20, 0.45), 0.52, 1.1, 0.7, 'luigi icon'),
        ('arc/timg/im_kinopioIcon_Blue_01.tpl', 'icon', (0.55, 0.72), 0.78, 1.1, 0.75, 'blue toad icon'),
        ('arc/timg/im_kinopioIcon_Yellow_01.tpl', 'icon', (0.08, 0.18), 0.03, 1.2, 0.85, 'yellow toad icon'),
    ],
    'staffCredit': [
        ('arc/timg/im_coin_01.tpl', 0.45, 0.8, 0.9, 'coin gold->teal'),
        ('arc/timg/im_marioIcon_01.tpl', 'icon', (0.90, 0.08), 0.75, 0.4, 0.35, 'mario icon'),
        ('arc/timg/im_luijiIcon_01.tpl', 'icon', (0.20, 0.45), 0.52, 1.1, 0.7, 'luigi icon'),
        ('arc/timg/im_kinopioIcon_Blue_01.tpl', 'icon', (0.55, 0.72), 0.78, 1.1, 0.75, 'blue toad icon'),
        ('arc/timg/im_kinopioIcon_Yellow_01.tpl', 'icon', (0.08, 0.18), 0.03, 1.2, 0.85, 'yellow toad icon'),
    ],
    'stockItem': [
        ('arc/timg/im_fireFlower_02.tpl', 0.0, 1.0, 0.8, 'fireflower darker'),
        ('arc/timg/im_iceFlower_02.tpl', 0.45, 1.1, 0.9, 'iceflower teal'),
        ('arc/timg/im_kinoko_02.tpl', 0.0, 0.7, 0.8, 'mushroom desaturated'),
        ('arc/timg/im_mameKinoko_02.tpl', 0.0, 0.7, 0.8, 'mini mushroom'),
        ('arc/timg/im_propeller_02.tpl', 0.0, 0.8, 0.85, 'propeller darker'),
        ('arc/timg/im_star_02.tpl', 0.1, 1.2, 1.0, 'star golden'),
    ],
    'miniGameWire': [
        ('arc/timg/im_fireFlower_02.tpl', 0.0, 1.0, 0.8, 'fireflower'),
        ('arc/timg/im_iceFlower_02.tpl', 0.45, 1.1, 0.9, 'iceflower'),
        ('arc/timg/im_kinoko_02.tpl', 0.0, 0.7, 0.8, 'mushroom'),
        ('arc/timg/im_mameKinoko_02.tpl', 0.0, 0.7, 0.8, 'mini mushroom'),
        ('arc/timg/im_propeller_02.tpl', 0.0, 0.8, 0.85, 'propeller'),
        ('arc/timg/im_star_02.tpl', 0.1, 1.2, 1.0, 'star golden'),
        ('arc/timg/im_marioIcon_01.tpl', 'icon', (0.90, 0.08), 0.75, 0.4, 0.35, 'mario icon'),
        ('arc/timg/im_luijiIcon_01.tpl', 'icon', (0.20, 0.45), 0.52, 1.1, 0.7, 'luigi icon'),
        ('arc/timg/im_kinopioIcon_Blue_01.tpl', 'icon', (0.55, 0.72), 0.78, 1.1, 0.75, 'blue toad icon'),
        ('arc/timg/im_kinopioIcon_Yellow_01.tpl', 'icon', (0.08, 0.18), 0.03, 1.2, 0.85, 'yellow toad icon'),
    ],
    'miniGameCannon': [
        ('arc/timg/im_marioIcon_01.tpl', 'icon', (0.90, 0.08), 0.75, 0.4, 0.35, 'mario icon'),
        ('arc/timg/im_luijiIcon_01.tpl', 'icon', (0.20, 0.45), 0.52, 1.1, 0.7, 'luigi icon'),
        ('arc/timg/im_kinopioIcon_Blue_01.tpl', 'icon', (0.55, 0.72), 0.78, 1.1, 0.75, 'blue toad icon'),
        ('arc/timg/im_kinopioIcon_Yellow_01.tpl', 'icon', (0.08, 0.18), 0.03, 1.2, 0.85, 'yellow toad icon'),
    ],
    'continue': [
        ('arc/timg/im_marioIcon_01.tpl', 'icon', (0.90, 0.08), 0.75, 0.4, 0.35, 'mario icon'),
        ('arc/timg/im_luijiIcon_01.tpl', 'icon', (0.20, 0.45), 0.52, 1.1, 0.7, 'luigi icon'),
        ('arc/timg/im_kinopioIcon_Blue_01.tpl', 'icon', (0.55, 0.72), 0.78, 1.1, 0.75, 'blue toad icon'),
        ('arc/timg/im_kinopioIcon_Yellow_01.tpl', 'icon', (0.08, 0.18), 0.03, 1.2, 0.85, 'yellow toad icon'),
    ],
    'MultiCourseSelect': [
        ('arc/timg/im_marioIcon_01.tpl', 'icon', (0.90, 0.08), 0.75, 0.4, 0.35, 'mario icon'),
        ('arc/timg/im_luijiIcon_01.tpl', 'icon', (0.20, 0.45), 0.52, 1.1, 0.7, 'luigi icon'),
        ('arc/timg/im_kinopioIcon_Blue_01.tpl', 'icon', (0.55, 0.72), 0.78, 1.1, 0.75, 'blue toad icon'),
        ('arc/timg/im_kinopioIcon_Yellow_01.tpl', 'icon', (0.08, 0.18), 0.03, 1.2, 0.85, 'yellow toad icon'),
    ],
    'pointResultDateFile': [
        ('arc/timg/im_marioIcon_01.tpl', 'icon', (0.90, 0.08), 0.75, 0.4, 0.35, 'mario icon'),
        ('arc/timg/im_luijiIcon_01.tpl', 'icon', (0.20, 0.45), 0.52, 1.1, 0.7, 'luigi icon'),
        ('arc/timg/im_kinopioIcon_Blue_01.tpl', 'icon', (0.55, 0.72), 0.78, 1.1, 0.75, 'blue toad icon'),
        ('arc/timg/im_kinopioIcon_Yellow_01.tpl', 'icon', (0.08, 0.18), 0.03, 1.2, 0.85, 'yellow toad icon'),
    ],
    'pointResultDateFileFree': [
        ('arc/timg/im_marioIcon_01.tpl', 'icon', (0.90, 0.08), 0.75, 0.4, 0.35, 'mario icon'),
        ('arc/timg/im_luijiIcon_01.tpl', 'icon', (0.20, 0.45), 0.52, 1.1, 0.7, 'luigi icon'),
        ('arc/timg/im_kinopioIcon_Blue_01.tpl', 'icon', (0.55, 0.72), 0.78, 1.1, 0.75, 'blue toad icon'),
        ('arc/timg/im_kinopioIcon_Yellow_01.tpl', 'icon', (0.08, 0.18), 0.03, 1.2, 0.85, 'yellow toad icon'),
    ],
    'dateFile': [
        ('arc/timg/im_marioIcon_01.tpl', 'icon', (0.90, 0.08), 0.75, 0.4, 0.35, 'mario icon'),
    ],
    'MultiCourseSelectContents': [
        ('arc/timg/im_coin_00.tpl', 0.45, 0.8, 0.9, 'coin teal'),
    ],
    'MultiCourseSelectContents': [
        ('arc/timg/im_coin_00.tpl', 0.45, 0.8, 0.9, 'coin teal'),
    ],
    'corseSelectUIGuide': [
        ('arc/timg/im_collectionCoin_01.tpl', 0.45, 0.8, 0.9, 'collection coin teal'),
        ('arc/timg/im_marioIcon_01.tpl', 'icon', (0.90, 0.08), 0.75, 0.4, 0.35, 'mario icon'),
        ('arc/timg/im_luijiIcon_01.tpl', 'icon', (0.20, 0.45), 0.52, 1.1, 0.7, 'luigi icon'),
        ('arc/timg/im_kinopioIcon_Blue_00.tpl', 'icon', (0.55, 0.72), 0.78, 1.1, 0.75, 'blue toad icon'),
        ('arc/timg/im_kinopioIcon_Yellow_00.tpl', 'icon', (0.08, 0.18), 0.03, 1.2, 0.85, 'yellow toad icon'),
    ],
    'modelPlayDate': [
        ('arc/timg/im_collectionCoin_01.tpl', 0.45, 0.8, 0.9, 'collection coin teal'),
    ],
    'worldCollectionCoinDate': [
        ('arc/timg/im_collectionCoin_01.tpl', 0.45, 0.8, 0.9, 'collection coin teal'),
        ('arc/timg/msk_coin.tpl', 0.45, 0.8, 0.9, 'star coin teal'),
    ],
}


def build_item_textures():
    """Build all modified texture archives from originals."""
    print('=== Chaos Station - All Texture Color Shifts ===\n')

    for arc_name, shifts in TEXTURE_SHIFTS.items():
        src_path = f'extracted files/Layout/{arc_name}/{arc_name}.arc'
        dst_path = f'output/ChaosStation/Layout/{arc_name}/{arc_name}.arc'

        if not os.path.exists(src_path):
            print(f'SKIP: {arc_name} (source not found)')
            continue

        print(f'{arc_name}:')

        # Load ORIGINAL archive each time
        with open(src_path, 'rb') as f:
            arc = U8Archive.load(f.read())

        for shift_args in shifts:
            tpl = shift_args[0]
            if tpl not in arc.list_files():
                continue

            orig = arc.get_file(tpl)

            if shift_args[1] == 'icon':
                # Icon shift: (tpl, 'icon', target_hue_range, new_hue, sat, val, label)
                _, _, target_range, new_h, sat, val, label = shift_args
                shifted = shift_icon_rgb5a3(orig, target_range, new_h, sat, val)
            else:
                # Simple shift: (tpl, hue_shift, sat_mult, val_mult, label)
                _, hue, sat, val, label = shift_args
                shifted = shift_rgb5a3_tile(orig, hue, sat, val)

            arc.set_file(tpl, shifted)
            print(f'    {tpl.split("/")[-1]}: {label}')

        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        with open(dst_path, 'wb') as f:
            f.write(arc.pack())

    print('\nDone!')


if __name__ == '__main__':
    build_item_textures()
