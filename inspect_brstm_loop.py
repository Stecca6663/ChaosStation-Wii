"""
Dump BRSTM header fields + VGAudio -m metadata to a text report.
Default target: STRM_BGM_CHIKA.brstm (patch_brsar STREAM_DIR).
"""
import os
import struct
import subprocess
import sys
from typing import Any, Dict, Union

_HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(_HERE)

from patch_brsar import STREAM_DIR

VGAUDIO = os.path.join(_HERE, "VGAudioCli.exe")


def header_info(path: str) -> Union[Dict[str, Any], str]:
    with open(path, "rb") as f:
        data = f.read(0x200)
    if data[:4] != b"RSTM":
        return f"NOT BRSTM magic={data[:4]!r}"
    head_offset = struct.unpack_from(">I", data, 0x10)[0]
    if data[head_offset : head_offset + 4] != b"HEAD":
        return "HEAD missing"
    ref1_off = struct.unpack_from(">I", data, head_offset + 0x0C)[0]
    si = head_offset + 0x08 + ref1_off
    codec = data[si]
    loop_flag = data[si + 1]
    ch = data[si + 2]
    rate = struct.unpack_from(">H", data, si + 4)[0]
    loop_start = struct.unpack_from(">I", data, si + 8)[0]
    total = struct.unpack_from(">I", data, si + 0xC)[0]
    codec_n = {0: "PCM8", 1: "PCM16", 2: "ADPCM"}.get(codec, str(codec))
    return {
        "codec": codec_n,
        "loop_flag": loop_flag,
        "channels": ch,
        "sample_rate": rate,
        "loop_start": loop_start,
        "total_samples": total,
        "stream_info_hex": f"0x{si:X}",
    }


def vgaudio_meta(path: str) -> str:
    if not os.path.isfile(VGAUDIO):
        return "(VGAudioCli.exe not found)\n"
    r = subprocess.run(
        [VGAUDIO, "-m", "-i", path],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    out = r.stdout or ""
    err = r.stderr or ""
    if err.strip():
        out += "\n--- stderr ---\n" + err
    return out


def main() -> int:
    rel = sys.argv[1] if len(sys.argv) > 1 else "STRM_BGM_CHIKA.brstm"
    path = rel if os.path.isabs(rel) else os.path.join(STREAM_DIR, rel)
    report = os.path.join(_HERE, "chika_brstm_inspect.txt")
    if rel != "STRM_BGM_CHIKA.brstm":
        base = os.path.splitext(os.path.basename(rel))[0]
        report = os.path.join(_HERE, f"brstm_inspect_{base}.txt")

    lines = [
        "BRSTM loop / metadata inspection",
        f"File: {path}",
        "=" * 72,
        "",
        "--- Header (HEAD stream info) ---",
    ]
    hi = header_info(path)
    if isinstance(hi, str):
        lines.append(hi)
    else:
        for k, v in hi.items():
            lines.append(f"  {k}: {v}")
    lines.extend(["", "--- VGAudio -m ---", vgaudio_meta(path)])

    text = "\n".join(lines) + "\n"
    with open(report, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"Wrote {report}")
    return 0 if os.path.isfile(path) else 1


if __name__ == "__main__":
    sys.exit(main())
