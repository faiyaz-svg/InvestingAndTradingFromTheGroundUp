"""Run the number checks: every tools/checks/NN-*.py, or the parts named.

    .venv/Scripts/python tools/checks/run.py          all parts
    .venv/Scripts/python tools/checks/run.py 03 05    parts 3 and 5

Each check file is a plain script that asserts; a failure prints the file and
the message. Exit status is non-zero if any check fails.
"""

from __future__ import annotations

import runpy
import sys
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    sys.path.insert(0, str(HERE))
    want = sys.argv[1:]
    files = sorted(p for p in HERE.glob("[0-9][0-9]-*.py"))
    if want:
        files = [p for p in files if p.name[:2] in {w.zfill(2) for w in want}]
    failed = 0
    for path in files:
        try:
            runpy.run_path(str(path), run_name="__main__")
            print(f"ok    {path.name}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL  {path.name}: {e}")
        except Exception:
            failed += 1
            print(f"ERROR {path.name}")
            traceback.print_exc()
    print(f"{len(files) - failed} of {len(files)} check files passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
