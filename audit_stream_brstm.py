"""
Compare mod BRSTMs (patch_brsar ENTRIES) to vanilla: channels, sample rate, looping.
Also flags total_samples %% 14 != 0 for ADPCM alignment (soft warning).
"""
import os
import re
import struct
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(_HERE)

from patch_brsar import ENTRIES, BRSAR_OUT, STREAM_DIR

VGAUDIO = os.path.join(_HERE, "VGAudioCli.exe")
VANILLA_STREAM = os.path.join(_HERE, r"extracted files\Sound\stream")


def vgaudio_quick(path: str) -> dict:
    out = {"channels": None, "rate": None, "samples": None, "loops": False, "loop_start": None, "error": None}
    if not os.path.isfile(path):
        out["error"] = "missing"
        return out
    if not os.path.isfile(VGAUDIO):
        out["error"] = "no VGAudioCli"
        return out
    r = subprocess.run(
        [VGAUDIO, "-m", "-i", path],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    text = r.stdout or ""
    m = re.search(r"Channel count:\s*(\d+)", text)
    if m:
        out["channels"] = int(m.group(1))
    m = re.search(r"Sample rate:\s*(\d+)\s*Hz", text)
    if m:
        out["rate"] = int(m.group(1))
    m = re.search(r"Sample count:\s*(\d+)", text)
    if m:
        out["samples"] = int(m.group(1))
    if "Loop start:" in text:
        out["loops"] = True
        m = re.search(r"Loop start:\s*(\d+)", text)
        if m:
            out["loop_start"] = int(m.group(1))
    return out


def header_loop_flag(path: str) -> int:
    with open(path, "rb") as f:
        data = f.read(0x100)
    if data[:4] != b"RSTM":
        return -1
    head_offset = struct.unpack_from(">I", data, 0x10)[0]
    if data[head_offset : head_offset + 4] != b"HEAD":
        return -1
    ref1_off = struct.unpack_from(">I", data, head_offset + 0x0C)[0]
    si = head_offset + 0x08 + ref1_off
    return data[si + 1]


def brsar_embedded_size(offset: int) -> int:
    with open(BRSAR_OUT, "rb") as f:
        f.seek(offset)
        return struct.unpack(">I", f.read(4))[0]


def main() -> int:
    lines = []
    issues = []

    lines.append("Stream BRSTM audit (mod vs vanilla)")
    lines.append(f"Mod stream dir: {STREAM_DIR}")
    lines.append(f"Vanilla: {VANILLA_STREAM}")
    lines.append("=" * 88)

    if not os.path.isfile(BRSAR_OUT):
        lines.append("ERROR: BRSAR_OUT missing — run patch_brsar.py first.")
        print("\n".join(lines))
        return 2

    for entry_num, filename, off in ENTRIES:
        mod_p = os.path.join(STREAM_DIR, filename)
        van_p = os.path.join(VANILLA_STREAM, filename)

        vm = vgaudio_quick(mod_p)
        vv = vgaudio_quick(van_p)

        disk = os.path.getsize(mod_p) if os.path.isfile(mod_p) else None
        emb = brsar_embedded_size(off) if disk is not None else None
        size_ok = disk == emb if disk is not None and emb is not None else False

        ch_ok = vm["channels"] == vv["channels"] if vm["channels"] and vv["channels"] else None
        rate_ok = vm["rate"] == 32000 if vm["rate"] else None
        loop_hdr = header_loop_flag(mod_p) if os.path.isfile(mod_p) else -1

        align_note = ""
        if vm["samples"]:
            r = vm["samples"] % 14
            if r != 0:
                align_note = f"  [align] total_samples%{14}={r}"

        row = (
            f"#{entry_num:3} {filename}\n"
            f"      mod:  {vm['channels']}ch {vm['rate']}Hz loops={vm['loops']} size={disk}  hdr_loop={loop_hdr}\n"
            f"      van:  {vv['channels']}ch {vv['rate']}Hz loops={vv['loops']}\n"
            f"      BRSAR embedded size == disk: {size_ok} ({emb}){align_note}"
        )

        if vm.get("error") == "missing":
            row = f"#{entry_num:3} {filename}\n      ERROR: mod file missing"
            issues.append(f"{filename}: mod missing")
        elif vv.get("error") == "missing":
            row += "\n      (vanilla missing — skipped compare)"
        elif ch_ok is False:
            issues.append(
                f"{filename}: CHANNEL MISMATCH mod={vm['channels']} van={vv['channels']} "
                f"(duplicate stereo to match vanilla if 4ch expected)"
            )
            row += "\n      *** CHANNEL COUNT != VANILLA ***"
        if disk is not None and emb is not None and not size_ok:
            issues.append(f"{filename}: BRSAR size mismatch embedded={emb} disk={disk}")
            row += "\n      *** BRSAR SIZE != DISK ***"
        if rate_ok is False:
            issues.append(f"{filename}: sample rate {vm['rate']} (expect 32000)")
            row += "\n      *** SAMPLE RATE != 320k ***"
        if vv["loops"] and not vm["loops"]:
            issues.append(f"{filename}: vanilla loops but mod VGAudio reports no loop")
            row += "\n      *** LOOP: vanilla yes, mod no ***"
        if loop_hdr not in (-1, 0, 1):
            row += f"\n      [warn] odd loop flag byte: {loop_hdr}"
        elif vm["loops"] and loop_hdr != 1:
            issues.append(f"{filename}: VGAudio says loop but header loop_flag={loop_hdr}")

        lines.append(row)
        lines.append("")

    lines.append("=" * 88)
    if issues:
        lines.append("SUMMARY — fix these:")
        for i in issues:
            lines.append(f"  - {i}")
    else:
        lines.append("SUMMARY: no channel/BRSAR/rate/loop mismatches detected.")

    report = os.path.join(_HERE, "audit_stream_brstm_report.txt")
    text = "\n".join(lines) + "\n"
    with open(report, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"Wrote {report}")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
