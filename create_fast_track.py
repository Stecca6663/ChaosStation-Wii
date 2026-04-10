"""
Build NSMBW-style "fast" (hurry) BRSTMs from a normal looped BRSTM.

Matches vanilla behavior: ~1.15x speed via asetrate + resample to 32000 Hz,
with loop points scaled to the new length. Works for 2ch and 4ch BRSTMs.
"""
import os
import re
import subprocess
import sys
import tempfile
import wave

_HERE = os.path.dirname(os.path.abspath(__file__))
VGAUDIO = os.path.join(_HERE, "VGAudioCli.exe")
FFMPEG = os.path.join(_HERE, "lac", "tools", "ffmpeg", "ffmpeg.exe")


def _parse_meta(stdout: str) -> dict:
    meta = {"sample_rate": 0, "loop_start": 0, "loop_end": 0, "looping": False}
    for line in stdout.split("\n"):
        if "Sample rate:" in line:
            m = re.search(r"Sample rate:\s*(\d+)", line)
            if m:
                meta["sample_rate"] = int(m.group(1))
        elif "Loop start:" in line:
            meta["looping"] = True
            m = re.search(r"Loop start:\s*(\d+)", line)
            if m:
                meta["loop_start"] = int(m.group(1))
        elif "Loop end:" in line:
            m = re.search(r"Loop end:\s*(\d+)", line)
            if m:
                meta["loop_end"] = int(m.group(1))
    return meta


def create_fast(input_brstm: str, output_brstm: str) -> None:
    input_brstm = os.path.abspath(input_brstm)
    output_brstm = os.path.abspath(output_brstm)
    os.makedirs(os.path.dirname(output_brstm) or ".", exist_ok=True)

    print(f"--- Fast Track Generator: {os.path.basename(input_brstm)} ---")
    if not os.path.isfile(VGAUDIO):
        raise FileNotFoundError(f"Missing {VGAUDIO}")
    if not os.path.isfile(FFMPEG):
        raise FileNotFoundError(f"Missing {FFMPEG}")

    res = subprocess.run(
        [VGAUDIO, "-m", "-i", input_brstm],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    meta = _parse_meta(res.stdout or "")
    if meta["sample_rate"] <= 0:
        raise RuntimeError("Could not read sample rate from BRSTM")

    fast_sr = int(meta["sample_rate"] * 1.15)
    print(
        f" > {meta['sample_rate']} Hz -> speed step via asetrate={fast_sr} Hz, then 32000 Hz BRSTM"
    )

    tmpd = tempfile.mkdtemp(prefix="fast_brstm_")
    try:
        temp_wav = os.path.join(tmpd, "decode.wav")
        fast_wav = os.path.join(tmpd, "fast.wav")

        subprocess.run(
            [VGAUDIO, "-c", "-i", input_brstm, "-o", temp_wav],
            check=True,
            capture_output=True,
        )
        subprocess.run(
            [
                FFMPEG,
                "-y",
                "-i",
                temp_wav,
                "-af",
                f"asetrate={fast_sr},aresample=32000",
                "-c:a",
                "pcm_s16le",
                fast_wav,
            ],
            check=True,
            capture_output=True,
        )

        real_sample_count = 0
        try:
            with wave.open(fast_wav, "rb") as w:
                real_sample_count = w.getnframes()
        except Exception:
            pass
        if real_sample_count <= 0:
            r2 = subprocess.run(
                [VGAUDIO, "-m", "-i", fast_wav],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
            for line in (r2.stdout or "").split("\n"):
                if "Sample count:" in line:
                    m = re.search(r"Sample count:\s*(\d+)", line)
                    if m:
                        real_sample_count = int(m.group(1))
                    break

        loop_args = []
        if meta["looping"] and meta["loop_end"] > meta["loop_start"]:
            ratio = 32000 / fast_sr
            new_start = int(meta["loop_start"] * ratio)
            new_end = int(meta["loop_end"] * ratio)
            if new_end >= real_sample_count > 0:
                print(
                    f" [Warning] Loop end {new_end} >= length {real_sample_count}, capping."
                )
                new_end = real_sample_count
            loop_args = ["-l", f"{new_start}-{new_end}"]
            print(f" > Fast loop: {new_start}-{new_end}")
        else:
            loop_args = ["--no-loop"]

        subprocess.run(
            [VGAUDIO, "-c", "-i", fast_wav, "-o", output_brstm] + loop_args,
            check=True,
            capture_output=True,
        )
        print(f" -> Wrote {output_brstm} ({os.path.getsize(output_brstm)} bytes)")
    finally:
        for base in (tmpd,):
            try:
                for name in os.listdir(base):
                    try:
                        os.remove(os.path.join(base, name))
                    except OSError:
                        pass
                os.rmdir(base)
            except OSError:
                pass


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python create_fast_track.py <input.brstm> <output.brstm>")
        sys.exit(1)
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    if not os.path.exists(in_file):
        print(f"File not found: {in_file}")
        sys.exit(1)
    try:
        create_fast(in_file, out_file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
