"""Run every "In code" snippet in the book.

Finds each ```python fence inside a <details class="code"> box, and runs it with
the venv's Python in a temporary folder that holds copies of the book's sample
data files (docs/assets/data/*), so a snippet can read "stock-a-daily.csv" by
name, as the reader does after downloading it.

A snippet whose first line is "# needs internet" is only compiled, unless
--network is given. A snippet fails if it raises or runs longer than 60 s.

Run from the repo root:
    .venv/Scripts/python tools/check_code.py                   every page
    .venv/Scripts/python tools/check_code.py docs/20-quant-track-in-python
    .venv/Scripts/python tools/check_code.py --network docs/20-quant-track-in-python/04-fundamentals-from-edgar.md
    .venv/Scripts/python tools/check_code.py --show docs/...   also print each snippet's output
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "docs" / "assets" / "data"
BOX = re.compile(r'<details class="code" markdown>(.*?)</details>', re.S)
FENCE = re.compile(r"```python\n(.*?)```", re.S)


def snippets(path: Path):
    text = path.read_text(encoding="utf-8")
    for box in BOX.finditer(text):
        line = text[: box.start()].count("\n") + 1
        for m in FENCE.finditer(box.group(1)):
            yield line, m.group(1)


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    network = "--network" in sys.argv
    show = "--show" in sys.argv
    paths = []
    for arg in args or ["docs"]:
        p = Path(arg)
        paths += sorted(p.rglob("*.md")) if p.is_dir() else [p]
    total = failed = compiled = 0
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        if DATA.is_dir():
            for f in DATA.iterdir():
                if f.is_file():
                    shutil.copy(f, work / f.name)
        for path in paths:
            for line, code in snippets(path):
                total += 1
                where = f"{path.as_posix()}:{line}"
                if code.lstrip().startswith("# needs internet") and not network:
                    try:
                        compile(code, where, "exec")
                        compiled += 1
                    except SyntaxError as e:
                        failed += 1
                        print(f"FAIL {where}: {e}")
                    continue
                script = work / "_snippet.py"
                script.write_text(code, encoding="utf-8")
                try:
                    run = subprocess.run(
                        [sys.executable, "-I", str(script)], cwd=work, capture_output=True, text=True, timeout=60,
                        encoding="utf-8", errors="replace",
                    )
                except subprocess.TimeoutExpired:
                    failed += 1
                    print(f"FAIL {where}: timed out")
                    continue
                if run.returncode != 0:
                    failed += 1
                    err = run.stderr.strip().splitlines()[-3:]
                    print(f"FAIL {where}:\n    " + "\n    ".join(err))
                elif show:
                    print(f"ok   {where}\n    " + "\n    ".join(run.stdout.strip().splitlines()[:12]))
    print(f"{total - failed} of {total} snippets passed ({compiled} only compiled: they need the internet)")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
