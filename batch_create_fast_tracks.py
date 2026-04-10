"""
Generate all NSMBW "fast" hurry variants from your custom normal BRSTMs.

Uses create_fast_track.create_fast (1.15x, same method as vanilla-style hurry).
Run from project root, then: python patch_brsar.py
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(_HERE)

from create_fast_track import create_fast

STREAM_DIR = os.path.join(_HERE, r"output\ChaosStation\Sound\stream")

# (normal_filename, fast_filename) — fast BRSAR offsets live in patch_brsar.py
FAST_PAIRS = [
    ("STRM_BGM_CHIJOU.brstm", "STRM_BGM_CHIJOU_FAST.brstm"),
    ("STRM_BGM_CHIKA.brstm", "STRM_BGM_CHIKA_FAST.brstm"),
    ("athletic_lr.n.32.brstm", "athletic_fast_lr.n.32.brstm"),
    ("toride_lr.n.32.brstm", "toride_fast_lr.n.32.brstm"),
    ("shiro_boss_lr.n.32.brstm", "shiro_boss_fast_lr.n.32.brstm"),
    ("BGM_HIKOUSEN.32.brstm", "BGM_HIKOUSEN_fast.32.brstm"),
    ("BGM_OBAKE.32.brstm", "BGM_OBAKE_fast.32.brstm"),
    ("BGM_SIRO.32.brstm", "BGM_SIRO_fast.32.brstm"),
    ("BGM_TORIDE_BOSS.32.brstm", "BGM_TORIDE_BOSS_fast.32.brstm"),
    ("BGM_SUICHU.32.brstm", "BGM_SUICHU_fast.32.brstm"),
]


def main() -> int:
    skip_existing = "--skip-existing" in sys.argv
    ok = 0
    skipped = 0
    failed = 0
    for normal_name, fast_name in FAST_PAIRS:
        src = os.path.join(STREAM_DIR, normal_name)
        dst = os.path.join(STREAM_DIR, fast_name)
        if not os.path.isfile(src):
            print(f"SKIP (no source): {normal_name}")
            skipped += 1
            continue
        if os.path.isfile(dst) and skip_existing:
            print(f"SKIP (--skip-existing): {fast_name}")
            skipped += 1
            continue
        try:
            create_fast(src, dst)
            ok += 1
        except Exception as e:
            print(f"FAIL {normal_name}: {e}")
            failed += 1
    print(f"\nDone: built={ok} skipped={skipped} failed={failed}")
    if ok and failed == 0:
        print("Next: python patch_brsar.py")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
