import os
import subprocess
import re
import wave

VGAUDIO = "VGAudioCli.exe"
FFMPEG = r"lac\tools\ffmpeg\ffmpeg.exe"
INPUT_DIR = r"output\ChaosStation\Sound\stream"

TARGET_SAMPLERATE = 32000

needs_4 = ["STRM_BGM_LAST_BOSS2.brstm", "STRM_BGM_MENU.brstm"]
needs_fast = {
    "BGM_LAST_BOSS1_lr.ry.32.brstm": "BGM_LAST_BOSS1_fast_lr.ry.32.brstm",
    "STRM_BGM_LAST_BOSS2.brstm": "STRM_BGM_LAST_BOSS2_FAST.brstm"
}

def get_brstm_meta(filepath):
    res = subprocess.run([VGAUDIO, "-m", "-i", filepath], capture_output=True, text=True)
    meta = {
        "sample_count": 0,
        "sample_rate": 0,
        "loop_start": 0,
        "loop_end": 0,
        "channels": 0,
        "looping": False
    }
    for line in res.stdout.split('\n'):
        if "Sample count:" in line:
            meta["sample_count"] = int(re.search(r'\d+', line).group())
        elif "Sample rate:" in line:
            meta["sample_rate"] = int(re.search(r'\d+', line).group())
        elif "Channel count:" in line:
            meta["channels"] = int(re.search(r'\d+', line).group())
        elif "Loop start:" in line:
            meta["looping"] = True
            meta["loop_start"] = int(re.search(r'\d+', line).group())
        elif "Loop end:" in line:
            meta["loop_end"] = int(re.search(r'\d+', line).group())
    return meta

def rebuild_track(brstm_path):
    file_name = os.path.basename(brstm_path)
    base_name, _ = os.path.splitext(file_name)
    
    print(f"\n--- Processing {file_name} ---")
    
    meta = get_brstm_meta(brstm_path)
    target_channels = 4 if file_name in needs_4 else 2
    if meta["sample_rate"] == TARGET_SAMPLERATE and meta["channels"] == target_channels:
        print(" > Already optimal, skipping.")
        return
        
    print(f" > Original format: {meta['channels']}CH, {meta['sample_rate']}Hz, Looping: {meta['looping']}")
    
    temp_wav = os.path.join(INPUT_DIR, f"{base_name}_temp.wav")
    resampled_wav = os.path.join(INPUT_DIR, f"{base_name}_resampled.wav")
    out_brstm = os.path.join(INPUT_DIR, f"{base_name}_new.brstm")
    
    # 1. Decode to WAV
    print(f" [Action] Decoding BRSTM to WAV via VGAudio...")
    if os.path.exists(temp_wav): os.remove(temp_wav)
    subprocess.call(f'{VGAUDIO} -c -i "{brstm_path}" -o "{temp_wav}"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # 2. Duplicate channels if needed
    current_wav = temp_wav
    if file_name in needs_4:
        print(f" [Action] 4-Channel dynamic track detected. Duplicating stereo tracks...")
        with wave.open(temp_wav, 'rb') as w_in:
            params = list(w_in.getparams())
            frames = w_in.readframes(params[3])
        params[0] = 4
        current_wav = os.path.join(INPUT_DIR, f"{base_name}_4ch_temp.wav")
        with wave.open(current_wav, 'wb') as w_out:
            w_out.setparams(tuple(params))
            frame_size = 2 * params[1]
            new_frames = bytearray()
            for i in range(0, len(frames), frame_size):
                sample_pair = frames[i : i + frame_size]
                new_frames.extend(sample_pair) # L/R
                new_frames.extend(sample_pair) # L/R copy
            w_out.writeframes(new_frames)
            
    # 3. Resample using FFmpeg
    print(f" [Action] Resampling to {TARGET_SAMPLERATE}Hz via FFmpeg...")
    if os.path.exists(resampled_wav): os.remove(resampled_wav)
    subprocess.call(f'{FFMPEG} -y -i "{current_wav}" -ar {TARGET_SAMPLERATE} -c:a pcm_s16le "{resampled_wav}"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Check true resampled length to prevent Wii Engine truncation crashes
    res_wav = subprocess.run([VGAUDIO, "-m", "-i", resampled_wav], capture_output=True, text=True)
    real_sample_count = 0
    for line in res_wav.stdout.split('\n'):
        if "Sample count:" in line:
            real_sample_count = int(re.search(r'\d+', line).group())
            break
            
    # 4. Calculate new loop points
    loop_args = ""
    if meta["looping"]:
        ratio = TARGET_SAMPLERATE / meta["sample_rate"]
        new_start = int(meta["loop_start"] * ratio)
        new_end = int(meta["loop_end"] * ratio)
        
        # Capping logic for engine safety
        if new_end >= real_sample_count:
            print(f" [Warning] Math overshot real length ({new_end} > {real_sample_count}). Capping length.")
            new_end = real_sample_count
            
        loop_args = f"-l {new_start}-{new_end}"
        print(f" [Action] Loop adjusted to {new_start}-{new_end}")
    
    # 5. Encode via VGAudioCli
    print(f" [Action] Encoding optimized BRSTM via VGAudioCli...")
    if os.path.exists(out_brstm): os.remove(out_brstm)
    subprocess.call(f'{VGAUDIO} -c -i "{resampled_wav}" -o "{out_brstm}" {loop_args}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # 6. Safe replace
    if os.path.exists(out_brstm) and os.path.getsize(out_brstm) > 1000:
        os.remove(brstm_path)
        os.rename(out_brstm, brstm_path)
        print(f" -> Sucessfully built optimal {file_name}")
    
    # Clean up
    for f in [temp_wav, current_wav, resampled_wav]:
        if os.path.exists(f) and f != temp_wav: os.remove(f)
    os.remove(temp_wav) if os.path.exists(temp_wav) else None

def main():
    print("--- Chaos Station Batch Music Optimizer ---")
    print("Using stable VGAudioCli + FFmpeg headless pipeline.")
    for f in os.listdir(INPUT_DIR):
        if f.endswith(".brstm") and "fast" not in f.lower():
            rebuild_track(os.path.join(INPUT_DIR, f))
    print("Done!")

if __name__ == "__main__":
    main()
