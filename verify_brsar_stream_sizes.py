"""
Verify embedded BRSTM sizes in wii_mj2d_sound.brsar match on-disk files.
Uses the same ENTRIES and paths as patch_brsar.py (no duplication).
"""
import os
import struct
import sys

# Import from patch_brsar so offsets stay in sync
from patch_brsar import ENTRIES, BRSAR_OUT, STREAM_DIR


def main() -> int:
    _here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(_here)

    if not os.path.isfile(BRSAR_OUT):
        print(f"ERROR: BRSAR not found: {BRSAR_OUT}")
        return 2

    with open(BRSAR_OUT, "rb") as f:
        data = f.read()

    mismatches = []
    missing = []
    ok = []

    for entry_num, filename, offset in ENTRIES:
        path = os.path.join(STREAM_DIR, filename)
        if not os.path.isfile(path):
            missing.append((entry_num, filename))
            continue
        disk = os.path.getsize(path)
        if offset + 4 > len(data):
            mismatches.append((entry_num, filename, "offset past EOF", disk, None))
            continue
        embedded = struct.unpack_from(">I", data, offset)[0]
        if embedded != disk:
            mismatches.append((entry_num, filename, embedded, disk, offset))
        else:
            ok.append((entry_num, filename, disk))

    report_path = os.path.join(_here, "brsar_stream_size_verify.txt")
    with open(report_path, "w", encoding="utf-8") as out:
        out.write("BRSAR stream size verification\n")
        out.write(f"BRSAR: {BRSAR_OUT}\n")
        out.write(f"STREAM_DIR: {STREAM_DIR}\n")
        out.write("=" * 72 + "\n\n")
        out.write(f"OK: {len(ok)} entries\n")
        for e in ok:
            out.write(f"  #{e[0]:3} {e[1]}  embedded == disk == {e[2]} bytes\n")
        out.write("\n")
        if missing:
            out.write(f"MISSING files ({len(missing)}):\n")
            for e in missing:
                out.write(f"  #{e[0]:3} {e[1]} (not on disk, skipped)\n")
            out.write("\n")
        if mismatches:
            out.write(f"MISMATCHES ({len(mismatches)}):\n")
            for row in mismatches:
                if row[2] == "offset past EOF":
                    out.write(f"  #{row[0]:3} {row[1]}  {row[2]}  disk={row[3]}\n")
                else:
                    out.write(
                        f"  #{row[0]:3} {row[1]}  embedded={row[2]}  disk={row[3]}  @0x{row[4]:X}\n"
                    )
        else:
            out.write("MISMATCHES: none\n")

    print(f"Wrote {report_path}")
    print(f"OK: {len(ok)}  missing: {len(missing)}  mismatches: {len(mismatches)}")
    if mismatches:
        print("Run patch_brsar.py to fix embedded sizes.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
