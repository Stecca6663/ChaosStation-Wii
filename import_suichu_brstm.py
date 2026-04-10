"""
Convert any looped BRSTM (e.g. 44100 Hz) to 32 kHz stereo and install as BGM_SUICHU.32.brstm.
"""
import os
import shutil
import subprocess
import sys
import wave

import fix_all_music as fam

_HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(_HERE)

STREAM = fam.INPUT_DIR
TARGET = os.path.join(STREAM, "BGM_SUICHU.32.brstm")


def main() -> int:
    src = sys.argv[1] if len(sys.argv) > 1 else (
        "The Legend of Zelda_ Majora's Mask - Great Bay Temple.brstm"
    )
    src = os.path.abspath(src)
    if not os.path.isfile(src):
        print(f"Not found: {src}")
        return 1

    base = "_suichu_work"
    temp_wav = os.path.join(STREAM, f"{base}_dec.wav")
    resampled = os.path.join(STREAM, f"{base}_32k.wav")
    out_new = os.path.join(STREAM, f"{base}_out.brstm")

    meta = fam.get_brstm_meta(src)
    print(f"Source: {meta['channels']}ch {meta['sample_rate']}Hz loop={meta['looping']}")

    for p in (temp_wav, resampled, out_new):
        if os.path.exists(p):
            os.remove(p)

    subprocess.run(
        [fam.VGAUDIO, "-c", "-i", src, "-o", temp_wav],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            fam.FFMPEG,
            "-y",
            "-i",
            temp_wav,
            "-ar",
            str(fam.TARGET_SAMPLERATE),
            "-c:a",
            "pcm_s16le",
            resampled,
        ],
        check=True,
        capture_output=True,
    )

    with wave.open(resampled, "rb") as w:
        real_n = w.getnframes()

    loop_args = []
    if meta["looping"]:
        ratio = fam.TARGET_SAMPLERATE / meta["sample_rate"]
        ns = int(meta["loop_start"] * ratio)
        ne = int(meta["loop_end"] * ratio)
        if ne >= real_n > 0:
            ne = real_n
        loop_args = ["-l", f"{ns}-{ne}"]
        print(f"Loop @ 32kHz: {ns}-{ne} (frames={real_n})")
    else:
        loop_args = ["--no-loop"]

    subprocess.run(
        [fam.VGAUDIO, "-c", "-i", resampled, "-o", out_new] + loop_args,
        check=True,
        capture_output=True,
    )

    shutil.copy2(out_new, TARGET)
    print(f"Installed: {TARGET} ({os.path.getsize(TARGET)} bytes)")

    for p in (temp_wav, resampled, out_new):
        if os.path.exists(p):
            os.remove(p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
