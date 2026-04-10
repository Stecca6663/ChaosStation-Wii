"""
Fix BRSTM loop points by ensuring the loop data is properly aligned.
For NSMBW, the game needs:
1. Loop flag set to 1
2. Loop start sample properly block-aligned
3. ADPCM history/context samples at the loop point

This script reads each problematic BRSTM, verifies the loop data,
and if needed, rewrites the loop header to force looping from the start.
"""
import struct, os, shutil

STREAM_DIR = r'output\ChaosStation\Sound\stream'

# Files that the user reports don't loop
PROBLEM_FILES = [
    'title_lr.ry.32.brstm',
    'STRM_BGM_MENU.brstm',
    'STRM_BGM_LAST_BOSS2.brstm',
    'STRM_BGM_LAST_BOSS2_FAST.brstm',
    'BGM_LAST_BOSS1_lr.ry.32.brstm',
    'BGM_LAST_BOSS1_fast_lr.ry.32.brstm',
]

def get_brstm_info(data):
    """Parse BRSTM header and return stream info location + values."""
    if data[:4] != b'RSTM':
        return None
    
    head_offset = struct.unpack_from('>I', data, 0x10)[0]
    if data[head_offset:head_offset+4] != b'HEAD':
        return None
    
    ref1_off = struct.unpack_from('>I', data, head_offset + 0x0C)[0]
    stream_info_abs = head_offset + 0x08 + ref1_off
    
    codec = data[stream_info_abs]
    loop_flag = data[stream_info_abs + 1]
    num_channels = data[stream_info_abs + 2]
    sample_rate = struct.unpack_from('>H', data, stream_info_abs + 4)[0]
    loop_start = struct.unpack_from('>I', data, stream_info_abs + 8)[0]
    total_samples = struct.unpack_from('>I', data, stream_info_abs + 0xC)[0]
    
    return {
        'stream_info_offset': stream_info_abs,
        'codec': codec,
        'loop_flag': loop_flag,
        'loop_flag_offset': stream_info_abs + 1,
        'channels': num_channels,
        'sample_rate': sample_rate,
        'loop_start': loop_start,
        'loop_start_offset': stream_info_abs + 8,
        'total_samples': total_samples,
        'total_samples_offset': stream_info_abs + 0xC,
    }

def fix_brstm_loop(filepath):
    """Ensure a BRSTM file has proper loop flag and loop_start."""
    with open(filepath, 'rb') as f:
        data = bytearray(f.read())
    
    info = get_brstm_info(data)
    if info is None:
        return f"SKIP: Not a valid BRSTM"
    
    fname = os.path.basename(filepath)
    changes = []
    
    # Check loop flag
    if info['loop_flag'] != 1:
        data[info['loop_flag_offset']] = 1
        changes.append(f"Set loop flag to 1 (was {info['loop_flag']})")
    
    # Verify loop_start is reasonable
    if info['loop_start'] >= info['total_samples']:
        # Loop start is past the end — set to 0 (loop from beginning)
        struct.pack_into('>I', data, info['loop_start_offset'], 0)
        changes.append(f"Fixed loop_start: was {info['loop_start']} (past total {info['total_samples']}), set to 0")
    
    if changes:
        # Back up original
        backup = filepath + '.bak'
        if not os.path.exists(backup):
            shutil.copy2(filepath, backup)
        
        with open(filepath, 'wb') as f:
            f.write(data)
        return f"FIXED: {'; '.join(changes)}"
    else:
        return f"OK: loop_flag={info['loop_flag']}, loop_start={info['loop_start']}, total={info['total_samples']}, {info['channels']}ch {info['sample_rate']}Hz"


with open('loop_fix_results.txt', 'w') as log:
    log.write("BRSTM Loop Fix Results\n")
    log.write("=" * 80 + "\n\n")
    
    for fname in PROBLEM_FILES:
        path = os.path.join(STREAM_DIR, fname)
        if not os.path.exists(path):
            log.write(f"{fname}: FILE NOT FOUND\n\n")
            continue
        
        result = fix_brstm_loop(path)
        log.write(f"{fname}: {result}\n\n")
    
    # Also check all other files for good measure
    log.write("\n--- All other files ---\n\n")
    for path in sorted(os.listdir(STREAM_DIR)):
        if path.endswith('.brstm') and path not in PROBLEM_FILES:
            full = os.path.join(STREAM_DIR, path)
            result = fix_brstm_loop(full)
            log.write(f"{path}: {result}\n")

print("Results written to loop_fix_results.txt")
