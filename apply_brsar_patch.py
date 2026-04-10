import subprocess
import os

entries = {
    72: 'STRM_BGM_MENU.brstm',
    70: 'STRM_BGM_LAST_BOSS2.brstm',
    71: 'STRM_BGM_LAST_BOSS2_FAST.brstm',
    13: 'BGM_LAST_BOSS1_lr.ry.32.brstm',
    12: 'BGM_LAST_BOSS1_fast_lr.ry.32.brstm',
    17: 'BGM_MAP_W5.32.brstm',
    18: 'BGM_MAP_W7.32.brstm',
    19: 'BGM_MAP_W8.32.brstm',
    55: 'select_map01_nohara_lr.n.32.brstm',
    56: 'select_map02_sabaku.ry.32.brstm',
    57: 'select_map03_yuki.ry.32.brstm',
    58: 'select_map04_umii.ry.32.brstm',
    59: 'select_map06_cliff_lr.n.32.brstm',
    60: 'select_map09_rainbow_lr.n.32.brstm',
    83: 'title_lr.ry.32.brstm'
}

cwd = os.path.abspath(r'output\ChaosStation\Sound')
patcher_path = os.path.join(cwd, 'BTRWIIBRSTMBRSARPATCH.EXE')

for num, name in entries.items():
    print(f'Patching Entry #{num}: {name}...')
    if not os.path.exists(os.path.join(cwd, name)):
        print(f' [!] Error: {name} not found in {cwd}. Skipping.')
        continue
        
    cmd = [patcher_path, 'DEFAULT.BPTH', '-b', 'wii_mj2d_sound.brsar', '-d', f'{num} {name}']
    p = subprocess.Popen(cmd, cwd=cwd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = p.communicate(input='Y\n')
    
    if 'SUCCESS' in out.upper() or 'PATCH' in out.upper():
        print(f' -> Success!')
    else:
        if 'WAS UPDATED' in out.upper() or 'WAS PATCHED' in out.upper():
             print(f' -> Already patched or success.')
        else:
             print(f' -> Failed. Output snippet: {out[-100:].strip()}')
             if err: print('    ERROR:', err.strip())
