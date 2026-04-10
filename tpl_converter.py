"""
TPL <-> PNG converter for Wii/GC textures.
Supports RGB5A3 format (used by NSMBW layout textures).
"""

import struct
from PIL import Image


def decode_rgb5a3(val):
    """Decode a 16-bit RGB5A3 pixel to (R, G, B, A)."""
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
    """Encode (R, G, B, A) to a 16-bit RGB5A3 value."""
    if a >= 248:
        val = 0x8000
        val |= (r * 31 // 255) << 10
        val |= (g * 31 // 255) << 5
        val |= (b * 31 // 255)
    else:
        val = (a * 7 // 255) << 12
        val |= (r * 15 // 255) << 8
        val |= (g * 15 // 255) << 4
        val |= (b * 15 // 255)
    return val


def tpl_to_png(tpl_data, output_path):
    """Convert TPL texture bytes to a PNG file.

    TPL layout (verified against NSMBW):
      0x00: magic 00 20 AF 30 (4 bytes)
      0x04: version 00 00 00 01 (4 bytes)
      0x08: num_images (2 bytes, big-endian)
      0x0A: header_size (2 bytes, big-endian)
      0x0C: image_data_offset (4 bytes, big-endian, always 0x14)
      0x10: ??? (4 bytes)
      0x14: start of image header (20 bytes)
        +0x00: ??? (4 bytes, always 0)
        +0x04: height (2 bytes)
        +0x06: width (2 bytes)
        +0x08: format (4 bytes) - 5 = RGB5A3
        +0x0C: wrap_s (4 bytes)
        +0x10: wrap_t (4 bytes)
      0x28: pixel data begins (tiled, 4x4, 2 bytes per pixel BE)
    """
    magic = tpl_data[0:4]
    expected = b'\x00\x20\xaf\x30'
    if magic != expected:
        raise ValueError(f"Not a valid TPL (magic: {magic!r})")

    # Image header starts at 0x14
    height = struct.unpack_from('>H', tpl_data, 0x14)[0]
    width = struct.unpack_from('>H', tpl_data, 0x16)[0]
    fmt = struct.unpack_from('>I', tpl_data, 0x18)[0]

    if fmt != 5:
        raise ValueError(f"Unsupported TPL format: {fmt} (only RGB5A3=5)")

    data_off = 0x20
    tiles_w = (width + 3) // 4
    tiles_h = (height + 3) // 4

    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    pixels = img.load()

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
                    off = data_off + tile_idx * 32 + tile_row * 8 + tile_col * 2
                    val = struct.unpack_from('>H', tpl_data, off)[0]
                    r, g, b, a = decode_rgb5a3(val)
                    pixels[px, py] = (r, g, b, a)

    img.save(output_path)
    return width, height, fmt


def png_to_tpl(png_path, output_path):
    """Convert a PNG file to TPL format (RGB5A3)."""
    img = Image.open(png_path).convert('RGBA')
    width, height = img.size
    pixels = img.load()

    tiles_w = (width + 3) // 4
    tiles_h = (height + 3) // 4

    # Build tiled pixel data
    data = bytearray()
    for tile_y in range(tiles_h):
        for tile_x in range(tiles_w):
            for tile_row in range(4):
                for tile_col in range(4):
                    px = tile_x * 4 + tile_col
                    py = tile_y * 4 + tile_row
                    if px < width and py < height:
                        r, g, b, a = pixels[px, py]
                    else:
                        r, g, b, a = 0, 0, 0, 0
                    val = encode_rgb5a3(r, g, b, a)
                    data.extend(struct.pack('>H', val))

    # Build TPL file (32-byte header, pixel data at 0x20)
    tpl = bytearray()
    tpl.extend(b'\x00\x20\xaf\x30')       # 0x00: magic
    tpl.extend(struct.pack('>I', 1))       # 0x04: version
    tpl.extend(struct.pack('>H', 0))       # 0x08: num_images
    tpl.extend(struct.pack('>H', 12))      # 0x0A: header_size
    tpl.extend(struct.pack('>I', 0x14))    # 0x0C: image_data_offset
    tpl.extend(struct.pack('>I', 0))       # 0x10: padding
    tpl.extend(struct.pack('>H', height))  # 0x14: height
    tpl.extend(struct.pack('>H', width))   # 0x16: width
    tpl.extend(struct.pack('>I', 5))       # 0x18: format = RGB5A3
    tpl.extend(struct.pack('>I', 0x40))    # 0x1C: wrap_s (0x40 = clamp)
    # 0x20: pixel data starts
    tpl.extend(data)

    with open(output_path, 'wb') as f:
        f.write(tpl)

    return width, height


def png_to_tpl_match_size(png_path, output_path, target_size):
    """Convert PNG to TPL, padding to match a target file size.

    Some TPLs have trailing padding bytes. This function ensures
    the output matches the original file size exactly.
    """
    img = Image.open(png_path).convert('RGBA')
    width, height = img.size
    pixels = img.load()

    tiles_w = (width + 3) // 4
    tiles_h = (height + 3) // 4

    data = bytearray()
    for tile_y in range(tiles_h):
        for tile_x in range(tiles_w):
            for tile_row in range(4):
                for tile_col in range(4):
                    px = tile_x * 4 + tile_col
                    py = tile_y * 4 + tile_row
                    if px < width and py < height:
                        r, g, b, a = pixels[px, py]
                    else:
                        r, g, b, a = 0, 0, 0, 0
                    val = encode_rgb5a3(r, g, b, a)
                    data.extend(struct.pack('>H', val))

    tpl = bytearray()
    tpl.extend(b'\x00\x20\xaf\x30')
    tpl.extend(struct.pack('>I', 1))
    tpl.extend(struct.pack('>H', 0))
    tpl.extend(struct.pack('>H', 12))
    tpl.extend(struct.pack('>I', 0x14))
    tpl.extend(struct.pack('>I', 0))
    tpl.extend(struct.pack('>H', height))
    tpl.extend(struct.pack('>H', width))
    tpl.extend(struct.pack('>I', 5))
    tpl.extend(struct.pack('>I', 0x40))
    tpl.extend(data)

    # Pad to target size
    if len(tpl) < target_size:
        tpl.extend(b'\x00' * (target_size - len(tpl)))
    elif len(tpl) > target_size:
        tpl = tpl[:target_size]

    with open(output_path, 'wb') as f:
        f.write(tpl)

    return width, height


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 4:
        print("Usage:")
        print("  tpl_converter.py extract <input.tpl> <output.png>")
        print("  tpl_converter.py create  <input.png> <output.tpl>")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == 'extract':
        with open(sys.argv[2], 'rb') as f:
            data = f.read()
        w, h, fmt = tpl_to_png(data, sys.argv[3])
        print(f"Extracted: {w}x{h} format={fmt} -> {sys.argv[3]}")
    elif cmd == 'create':
        w, h = png_to_tpl(sys.argv[2], sys.argv[3])
        print(f"Created: {w}x{h} -> {sys.argv[3]}")
    else:
        print(f"Unknown command: {cmd}")
