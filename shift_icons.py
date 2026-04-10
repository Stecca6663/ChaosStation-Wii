"""
Shift HUD character icons to match the new Chaos Station character colors.
Targets: gameScene.arc (in-game HUD) and other archives with the same icons.

Icons:
- im_marioIcon_01.tpl (48x48) - Mario -> dark purple-black
- im_luijiIcon_01.tpl (46x48) - Luigi -> teal
- im_kinopioIcon_Blue_01.tpl (48x48) - Blue Toad -> purple
- im_kinopioIcon_Yellow_01.tpl (48x48) - Yellow Toad -> orange-red
"""

import sys, struct, os
import colorsys
sys.path.insert(0, '.')
from tools.u8archive import U8Archive


def decode_rgb5a3(val):
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


def encode_rgb5a3(r, g, b, a):
    if a >= 248:
        return 0x8000 | ((max(0, min(31, r * 31 // 255)) << 10) |
                         (max(0, min(31, g * 31 // 255)) << 5) |
                         (max(0, min(31, b * 31 // 255))))
    else:
        return ((max(0, min(7, a * 7 // 255)) << 12) |
                (max(0, min(15, r * 15 // 255)) << 8) |
                (max(0, min(15, g * 15 // 255)) << 4) |
                (max(0, min(15, b * 15 // 255))))


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


def should_shift(r, g, b, target_hue_range):
    """Check if this pixel is an outfit color that should be shifted."""
    if is_skin(r, g, b):
        return False
    # Skip pure white/black/gray (outlines, eyes, buttons)
    if r > 230 and g > 230 and b > 230:
        return False
    if r < 30 and g < 30 and b < 30:
        return False

    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    if s < 0.15:  # Skip desaturated colors
        return False

    h_min, h_max = target_hue_range
    if h_min <= h_max:
        return h_min <= h <= h_max
    else:
        return h >= h_min or h <= h_max


def shift_icon_rgb5a3(data, target_hue_range, new_hue, sat_mult, val_mult):
    """Process an RGB5A3 icon with targeted color shifting."""
    result = bytearray(data)

    # Pixel data starts at 0x20, tiled in 4x4 blocks
    width = struct.unpack_from('>H', result, 0x16)[0]
    height = struct.unpack_from('>H', result, 0x14)[0]
    tiles_w = (width + 3) // 4
    tiles_h = (height + 3) // 4

    for tile_y in range(tiles_h):
        for tile_row in range(4):
            py = tile_y * 4 + tile_row
            if py >= height:
                continue
            for tile_x in range(tiles_w):
                tile_idx = tile_y * tiles_w + tile_x
                for tile_col in range(4):
                    px = tile_x * 4 + tile_col
                    if px >= width:
                        continue
                    off = 0x20 + tile_idx * 32 + tile_row * 8 + tile_col * 2
                    if off + 2 > len(result):
                        continue

                    val = struct.unpack_from('>H', result, off)[0]
                    r, g, b, a = decode_rgb5a3(val)

                    if a > 10 and should_shift(r, g, b, target_hue_range):
                        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
                        # Shift hue to target, preserve some original variation
                        hue_offset = h - sum(target_hue_range) / 2
                        new_h = (new_hue + hue_offset * 0.2) % 1.0
                        new_s = min(1.0, s * sat_mult)
                        new_v = min(1.0, v * val_mult)
                        nr, ng, nb = colorsys.hsv_to_rgb(new_h, new_s, new_v)
                        struct.pack_into('>H', result, off,
                                        encode_rgb5a3(int(nr*255), int(ng*255), int(nb*255), a))

    return bytes(result)


def process_icon(arc, tpl_path, target_hue, new_hue, sat_mult, val_mult, label):
    """Extract, shift, and re-inject an icon."""
    if tpl_path not in arc.list_files():
        print(f'    SKIP (not found): {tpl_path}')
        return

    orig = arc.get_file(tpl_path)
    shifted = shift_icon_rgb5a3(orig, target_hue, new_hue, sat_mult, val_mult)
    arc.set_file(tpl_path, shifted)
    print(f'    Shifted: {tpl_path} ({label})')


# All archives that contain these icons
ICON_ARCHIVES = [
    ('extracted files/Layout/gameScene/gameScene.arc',
     'output/ChaosStation/Layout/gameScene/gameScene.arc'),
    ('extracted files/Layout/continue/continue.arc',
     'output/ChaosStation/Layout/continue/continue.arc'),
    ('extracted files/Layout/preGame/preGame.arc',
     'output/ChaosStation/Layout/preGame/preGame.arc'),
    ('extracted files/Layout/miniGameCannon/miniGameCannon.arc',
     'output/ChaosStation/Layout/miniGameCannon/miniGameCannon.arc'),
    ('extracted files/Layout/miniGameWire/miniGameWire.arc',
     'output/ChaosStation/Layout/miniGameWire/miniGameWire.arc'),
    ('extracted files/Layout/MultiCourseSelect/MultiCourseSelect.arc',
     'output/ChaosStation/Layout/MultiCourseSelect/MultiCourseSelect.arc'),
    ('extracted files/Layout/pointResultDateFile/pointResultDateFile.arc',
     'output/ChaosStation/Layout/pointResultDateFile/pointResultDateFile.arc'),
    ('extracted files/Layout/pointResultDateFileFree/pointResultDateFileFree.arc',
     'output/ChaosStation/Layout/pointResultDateFileFree/pointResultDateFileFree.arc'),
    ('extracted files/Layout/corseSelectUIGuide/corseSelectUIGuide.arc',
     'output/ChaosStation/Layout/corseSelectUIGuide/corseSelectUIGuide.arc'),
    ('extracted files/Layout/pointResult/pointResult.arc',
     'output/ChaosStation/Layout/pointResult/pointResult.arc'),
    ('extracted files/Layout/fileSelectPlayer/fileSelectPlayer.arc',
     'output/ChaosStation/Layout/fileSelectPlayer/fileSelectPlayer.arc'),
    ('extracted files/Layout/charaChangeSelectContents/charaChangeSelectContents.arc',
     'output/ChaosStation/Layout/charaChangeSelectContents/charaChangeSelectContents.arc'),
    ('extracted files/Layout/staffCredit/staffCredit.arc',
     'output/ChaosStation/Layout/staffCredit/staffCredit.arc'),
    ('extracted files/Layout/dateFile/dateFile.arc',
     'output/ChaosStation/Layout/dateFile/dateFile.arc'),
    ('extracted files/Layout/wipeMario/wipeMario.arc',
     'output/ChaosStation/Layout/wipeMario/wipeMario.arc'),
    ('extracted files/Layout/pauseMenu/pauseMenu.arc',
     'output/ChaosStation/Layout/pauseMenu/pauseMenu.arc'),
]

# Icons to shift with their color targets
# Format: (path, hue_range, new_hue, sat_mult, val_mult, label)
ICON_SHIFTS = [
    # Standard _01 icons
    ('arc/timg/im_marioIcon_01.tpl', (0.90, 0.08), 0.75, 0.4, 0.35, 'Mario->Dark Purple'),
    ('arc/timg/im_luijiIcon_01.tpl', (0.20, 0.45), 0.52, 1.1, 0.7, 'Luigi->Teal'),
    ('arc/timg/im_kinopioIcon_Blue_01.tpl', (0.55, 0.72), 0.78, 1.1, 0.75, 'Blue Toad->Purple'),
    ('arc/timg/im_kinopioIcon_Yellow_01.tpl', (0.08, 0.18), 0.03, 1.2, 0.85, 'Yellow Toad->Orange'),
    # _00 variants (corseSelectUIGuide, file select)
    ('arc/timg/im_kinopioIcon_Blue_00.tpl', (0.55, 0.72), 0.78, 1.1, 0.75, 'Blue Toad->Purple'),
    ('arc/timg/im_kinopioIcon_Yellow_00.tpl', (0.08, 0.18), 0.03, 1.2, 0.85, 'Yellow Toad->Orange'),
    # pointResult naming convention
    ('arc/timg/im_kinopioBlue_00.tpl', (0.55, 0.72), 0.78, 1.1, 0.75, 'Blue Toad->Purple'),
    ('arc/timg/im_kinopioYellow_00.tpl', (0.08, 0.18), 0.03, 1.2, 0.85, 'Yellow Toad->Orange'),
    ('arc/timg/im_mario_00.tpl', (0.90, 0.08), 0.75, 0.4, 0.35, 'Mario->Dark Purple'),
    # fileSelectPlayer os_ prefix icons
    ('arc/timg/os_kinopio_00.tpl', (0.55, 0.72), 0.78, 1.1, 0.75, 'Blue Toad->Purple'),
    ('arc/timg/os_luigi_00.tpl', (0.20, 0.45), 0.52, 1.1, 0.7, 'Luigi->Teal'),
    ('arc/timg/os_mario_00.tpl', (0.90, 0.08), 0.75, 0.4, 0.35, 'Mario->Dark Purple'),
    ('arc/timg/os_mario_01.tpl', (0.90, 0.08), 0.75, 0.4, 0.35, 'Mario->Dark Purple'),
    # charaChangeSelectContents
    ('arc/timg/Im_plofileLuiji_00.tpl', (0.20, 0.45), 0.52, 1.1, 0.7, 'Luigi->Teal'),
    # gray variants (staffCredit)
    ('arc/timg/im_kinopioIcon_Blue_gray.tpl', (0.55, 0.72), 0.78, 1.1, 0.75, 'Blue Toad->Purple'),
    ('arc/timg/im_kinopioIcon_Yellow_gray.tpl', (0.08, 0.18), 0.03, 1.2, 0.85, 'Yellow Toad->Orange'),
    ('arc/timg/im_marioIcon_gray.tpl', (0.90, 0.08), 0.75, 0.4, 0.35, 'Mario->Dark Purple'),
    ('arc/timg/im_luijiIcon_gray.tpl', (0.20, 0.45), 0.52, 1.1, 0.7, 'Luigi->Teal'),
    # wipeMario
    ('arc/timg/im_wipeMario_01.tpl', (0.90, 0.08), 0.75, 0.4, 0.35, 'Mario->Dark Purple'),
]


def main():
    print('=== Chaos Station - HUD Icon Color Shifts ===\n')

    for src_path, dst_path in ICON_ARCHIVES:
        if not os.path.exists(src_path):
            print(f'SKIP (not found): {src_path}')
            continue

        print(f'Processing: {os.path.basename(src_path)}')

        with open(src_path, 'rb') as f:
            arc = U8Archive.load(f.read())

        for tpl, hue_range, new_hue, sat_m, val_m, label in ICON_SHIFTS:
            process_icon(arc, tpl, hue_range, new_hue, sat_m, val_m, label)

        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        with open(dst_path, 'wb') as f:
            f.write(arc.pack())

    print('\n=== Done! ===')


if __name__ == '__main__':
    main()
