"""
Pure Python BRSAR patcher for NSMBW.
Patches the file size field (u32 at offset+0x00) for each stream entry
to match our custom BRSTM file sizes.

Root cause: the BRSAR tells the game how large each BRSTM file is.
If our custom file is larger, the game only reads the original size,
truncating the audio and preventing looping.
"""
import struct, os, hashlib, shutil

BRSAR_ORIG = r'extracted files\Sound\wii_mj2d_sound.brsar'
BRSAR_OUT  = r'output\ChaosStation\Sound\wii_mj2d_sound.brsar'
STREAM_DIR = r'output\ChaosStation\Sound\stream'

# BRSAR offsets from the patcher tool output
ENTRIES = [
    (55, 'select_map01_nohara_lr.n.32.brstm', 0x0004A71C),
    (56, 'select_map02_sabaku.ry.32.brstm',    0x0004A960),
    (57, 'select_map03_yuki.ry.32.brstm',      0x0004A9A8),
    (58, 'select_map04_umii.ry.32.brstm',      0x0004A9EC),
    (17, 'BGM_MAP_W5.32.brstm',                0x0004AA30),
    (59, 'select_map06_cliff_lr.n.32.brstm',   0x0004AA6C),
    (18, 'BGM_MAP_W7.32.brstm',                0x0004AAB4),
    (19, 'BGM_MAP_W8.32.brstm',                0x0004AAF0),
    (60, 'select_map09_rainbow_lr.n.32.brstm', 0x0004AB2C),
    (83, 'title_lr.ry.32.brstm',               0x0004AB78),
    (72, 'STRM_BGM_MENU.brstm',                0x0004ABB4),
    # --- In-level BGM (added for Chaos Station) ---
    ( 0, 'STRM_BGM_CHIJOU.brstm',             0x0004A820),  # Ground
    ( 0, 'athletic_lr.n.32.brstm',            0x0004A8DC),  # Athletic
    ( 0, 'STRM_BGM_CHIKA.brstm',              0x0004A85C),  # Underground
    ( 0, 'BGM_OBAKE.32.brstm',                0x0004B1D0),  # Ghost House
    ( 0, 'BGM_HIKOUSEN.32.brstm',             0x0004B038),  # Airship
    ( 0, 'toride_lr.n.32.brstm',              0x0004AEF8),  # Tower
    ( 0, 'BGM_SIRO.32.brstm',                 0x0004B2CC),  # Castle
    ( 0, 'BGM_TORIDE_BOSS.32.brstm',          0x0004B3C0),  # Tower Boss
    ( 0, 'shiro_boss_lr.n.32.brstm',          0x0004AF74),  # Castle Boss
    # Hurry variants (offsets from patchbasaar/DEFAULT.BPTH)
    ( 0, 'STRM_BGM_CHIJOU_FAST.brstm',        0x0004A898),
    ( 0, 'STRM_BGM_CHIKA_FAST.brstm',         0x0004A764),
    ( 0, 'athletic_fast_lr.n.32.brstm',       0x0004A91C),
    ( 0, 'toride_fast_lr.n.32.brstm',         0x0004AF34),
    ( 0, 'shiro_boss_fast_lr.n.32.brstm',     0x0004AFB4),
    ( 0, 'BGM_HIKOUSEN_fast.32.brstm',        0x0004B074),
    ( 0, 'BGM_OBAKE_fast.32.brstm',           0x0004B20C),
    ( 0, 'BGM_SIRO_fast.32.brstm',              0x0004B304),
    ( 0, 'BGM_TORIDE_BOSS_fast.32.brstm',     0x0004B400),
    ( 0, 'BGM_SUICHU.32.brstm',               0x0004B794),  # Underwater (add when ready)
    ( 0, 'BGM_SUICHU_fast.32.brstm',           0x0004B7D0),
    ( 0, 'mori_lr.ry.32.brstm',               0x0004B89C),  # Forest
    ( 0, 'mori_fast_lr.ry.32.brstm',          0x0004B8D8),  # Forest fast
    ( 0, 'kazan_lr.n.32.brstm',               0x0004ADF4),  # Lava
    ( 0, 'kazan_fast_lr.n.32.brstm',          0x0004AE30),  # Lava fast
    ( 0, 'STRM_BGM_SANBASHI.brstm',           0x0004B918),  # Sky
    ( 0, 'STRM_BGM_SANBASHI_FAST.brstm',      0x0004B958),  # Sky fast
    (13, 'BGM_LAST_BOSS1_lr.ry.32.brstm',      0x0004B52C),
    (12, 'BGM_LAST_BOSS1_fast_lr.ry.32.brstm', 0x0004B570),
    (70, 'STRM_BGM_LAST_BOSS2.brstm',          0x0004B640),
    (71, 'STRM_BGM_LAST_BOSS2_FAST.brstm',     0x0004B680),
]


def main():
    # Start from fresh original BRSAR
    shutil.copy2(BRSAR_ORIG, BRSAR_OUT)
    
    with open(BRSAR_OUT, 'rb') as f:
        data = bytearray(f.read())
    
    orig_md5 = hashlib.md5(bytes(data)).hexdigest()
    print(f'Original BRSAR: {len(data)} bytes, MD5: {orig_md5}')
    
    patched_count = 0
    for entry_num, filename, offset in ENTRIES:
        brstm_path = os.path.join(STREAM_DIR, filename)
        if not os.path.exists(brstm_path):
            print(f'  SKIP #{entry_num}: {filename} not found')
            continue
        
        custom_size = os.path.getsize(brstm_path)
        orig_size = struct.unpack_from('>I', data, offset)[0]
        
        if custom_size != orig_size:
            struct.pack_into('>I', data, offset, custom_size)
            print(f'  PATCHED #{entry_num}: {filename}  {orig_size} -> {custom_size} bytes')
            patched_count += 1
        else:
            print(f'  OK #{entry_num}: {filename} (size already matches: {custom_size})')
    
    # Write patched BRSAR
    with open(BRSAR_OUT, 'wb') as f:
        f.write(data)
    
    new_md5 = hashlib.md5(bytes(data)).hexdigest()
    print(f'\nPatched BRSAR: {len(data)} bytes, MD5: {new_md5}')
    print(f'Entries patched: {patched_count}')
    print(f'File changed: {orig_md5 != new_md5}')
    print(f'\nSaved to: {BRSAR_OUT}')


if __name__ == '__main__':
    main()
