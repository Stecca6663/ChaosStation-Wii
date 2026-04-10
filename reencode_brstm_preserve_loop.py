"""
Decode BRSTM -> WAV -> BRSTM with VGAudio, preserving loop points from metadata.
Refreshes Nintendo ADPCM loop predictor/history (can fix clicks / bad loop jumps).

After replacing files, run patch_brsar.py so BRSAR embedded sizes stay correct.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(_HERE)

from patch_brsar import STREAM_DIR

VGAUDIO = os.path.join(_HERE, "VGAudioCli.exe")

# User Galaxy replacements (same filenames as patch_brsar in-level BGM)
DEFAULT_TARGETS = [
    "STRM_BGM_CHIJOU.brstm",
    "athletic_lr.n.32.brstm",
    "STRM_BGM_CHIKA.brstm",
    "BGM_OBAKE.32.brstm",
    "BGM_HIKOUSEN.32.brstm",
    "toride_lr.n.32.brstm",
    "BGM_SIRO.32.brstm",
    "BGM_TORIDE_BOSS.32.brstm",
    "shiro_boss_lr.n.32.brstm",
]


def parse_vgaudio_meta(stdout: str) -> dict:
    meta = {
        "sample_count": 0,
        "looping": False,
        "loop_start": 0,
        "loop_end": 0,
    }
    for line in stdout.splitlines():
        if "Sample count:" in line:
            m = re.search(r"Sample count:\s*(\d+)", line)
            if m:
                meta["sample_count"] = int(m.group(1))
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


def reencode_one(brstm_path: str, backup: bool = True) -> str:
    if not os.path.isfile(VGAUDIO):
        return "SKIP: VGAudioCli.exe missing"
    if not os.path.isfile(brstm_path):
        return "SKIP: file not found"

    r = subprocess.run(
        [VGAUDIO, "-m", "-i", brstm_path],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    m = parse_vgaudio_meta(r.stdout or "")
    workdir = tempfile.mkdtemp(prefix="brstm_reenc_")
    try:
        wav = os.path.join(workdir, "x.wav")
        out = os.path.join(workdir, "x.brstm")
        subprocess.run(
            [VGAUDIO, "-c", "-i", brstm_path, "-o", wav],
            check=True,
            capture_output=True,
        )
        if m["looping"] and m["loop_end"] > m["loop_start"]:
            # VGAudio -l: second value matches metadata "Loop end" (see inspect tests)
            loop_arg = f"{m['loop_start']}-{m['loop_end']}"
            subprocess.run(
                [VGAUDIO, "-c", "-i", wav, "-o", out, "-l", loop_arg],
                check=True,
                capture_output=True,
            )
        else:
            subprocess.run(
                [VGAUDIO, "-c", "-i", wav, "-o", out, "--no-loop"],
                check=True,
                capture_output=True,
            )

        if not os.path.isfile(out) or os.path.getsize(out) < 1000:
            return "FAIL: output missing or tiny"

        if backup:
            bak = brstm_path + ".bak"
            if not os.path.exists(bak):
                shutil.copy2(brstm_path, bak)

        d = os.path.dirname(os.path.abspath(brstm_path)) or "."
        stage = os.path.join(
            d, ".tmp_reenc_" + os.path.basename(brstm_path) + "." + os.urandom(4).hex()
        )
        dst_abs = os.path.abspath(brstm_path)
        try:
            shutil.copyfile(out, stage)
            src_abs = os.path.abspath(stage)
            last_err = None
            for attempt in range(12):
                try:
                    os.replace(src_abs, dst_abs)
                    last_err = None
                    break
                except PermissionError as e:
                    last_err = e
                    time.sleep(0.4)
            if last_err is not None:
                pending = os.path.join(
                    os.path.dirname(dst_abs), "_reencoded_ready", os.path.basename(brstm_path)
                )
                os.makedirs(os.path.dirname(pending), exist_ok=True)
                shutil.copyfile(out, pending)
                if os.path.isfile(stage):
                    try:
                        os.remove(stage)
                    except OSError:
                        pass
                psz = os.path.getsize(pending)
                return (
                    f"PENDING -> {psz} bytes (loop={m['looping']}); "
                    f"could not replace locked file. Copy:\n  {pending}\n  -> {dst_abs}"
                )
        finally:
            if os.path.isfile(stage):
                try:
                    os.remove(stage)
                except OSError:
                    pass
        new_sz = os.path.getsize(brstm_path)
        return f"OK -> {new_sz} bytes (loop={m['looping']})"
    except subprocess.CalledProcessError as e:
        return f"FAIL: {e}"
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


def main() -> int:
    targets = sys.argv[1:] if len(sys.argv) > 1 else DEFAULT_TARGETS
    log_path = os.path.join(_HERE, "reencode_brstm_preserve_loop_log.txt")
    lines = []
    for name in targets:
        path = name if os.path.isabs(name) else os.path.join(STREAM_DIR, name)
        msg = reencode_one(path)
        line = f"{name}: {msg}"
        lines.append(line)
        print(line)
    with open(log_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote {log_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
