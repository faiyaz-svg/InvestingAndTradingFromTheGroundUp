"""Check and build the chart drill sets.

Each tools/drills_src/<set>.yml is a list of items with these keys: id, chart
(fence text), q, type (level, choice or number), explain, and per type:
answer and tolerance (level, number), choices and answer_choice (choice).
Optional: unit, reveal (extra fence lines drawn after answering).

This script validates every item and writes docs/assets/drills/<set>.json as
{"set": ..., "items": [...]}.

Run from the repo root:  .venv/Scripts/python tools/build_drills.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "drills_src"
OUT = ROOT / "docs" / "assets" / "drills"
CHARTS = ROOT / "docs" / "assets" / "charts"

CHART_KEYS = {"data", "title", "caption", "type", "height", "show", "level", "zone", "marker", "line", "range"}
TYPES = ("level", "choice", "number")
BASE = ("id", "chart", "q", "type", "explain")
EXTRA = {"level": ("answer", "tolerance"), "number": ("answer", "tolerance"), "choice": ("choices", "answer_choice")}
ALLOWED = set(BASE) | {"answer", "tolerance", "unit", "choices", "answer_choice", "reveal"}


def check_chart_text(text: str, where: str, errs: list[str]) -> str | None:
    """Check the fence keys. Return the data path."""
    data = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        key, sep, val = line.partition(":")
        key = key.strip()
        if not sep or key not in CHART_KEYS:
            errs.append(f"{where}: bad chart line {line!r}")
            continue
        if key == "data":
            data = val.strip()
        if key == "range" and " to " not in val:
            errs.append(f"{where}: range needs 'FROM to TO'")
        if key in ("level", "zone", "marker", "line") and not val.strip():
            errs.append(f"{where}: empty {key}")
    return data


def check_item(it: dict, where: str, errs: list[str]) -> None:
    if not isinstance(it, dict):
        errs.append(f"{where}: not a mapping")
        return
    t = it.get("type")
    if t not in TYPES:
        errs.append(f"{where}: type must be one of {TYPES}")
        return
    for k in BASE + EXTRA[t]:
        if k not in it:
            errs.append(f"{where}: missing {k}")
    for k in it:
        if k not in ALLOWED:
            errs.append(f"{where}: unknown key {k}")
    if "chart" not in it:
        return
    data = check_chart_text(str(it["chart"]), where, errs)
    if not data:
        errs.append(f"{where}: chart has no data line")
    if "reveal" in it:
        check_chart_text(str(it["reveal"]), where + " reveal", errs)
    bars = None
    if data:
        path = CHARTS / data
        if not path.is_file():
            errs.append(f"{where}: data file {data} not found")
        else:
            bars = json.loads(path.read_text(encoding="utf-8"))["bars"]
    if t in ("level", "number"):
        for k in ("answer", "tolerance"):
            if k in it and (isinstance(it[k], bool) or not isinstance(it[k], (int, float))):
                errs.append(f"{where}: {k} must be a number")
        if isinstance(it.get("tolerance"), (int, float)) and it["tolerance"] <= 0:
            errs.append(f"{where}: tolerance must be positive")
    if t == "level" and bars and isinstance(it.get("answer"), (int, float)):
        lo = min(b[3] for b in bars)
        hi = max(b[2] for b in bars)
        if not lo <= it["answer"] <= hi:
            errs.append(f"{where}: answer {it['answer']} is outside the data range {lo} to {hi}")
    if t == "choice":
        ch = it.get("choices")
        if not isinstance(ch, list) or len(ch) < 2 or not all(isinstance(c, str) for c in ch):
            errs.append(f"{where}: choices must be a list of 2 or more strings")
        elif not isinstance(it.get("answer_choice"), int) or not 0 <= it["answer_choice"] < len(ch):
            errs.append(f"{where}: answer_choice out of range")


def main() -> int:
    errs: list[str] = []
    OUT.mkdir(parents=True, exist_ok=True)
    summary = []
    for path in sorted(SRC.glob("*.yml")):
        items = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        if not isinstance(items, list):
            errs.append(f"{path.name}: top level must be a list")
            continue
        seen: set = set()
        before = len(errs)
        for i, it in enumerate(items):
            iid = it.get("id") if isinstance(it, dict) else None
            where = f"{path.name}[{iid or i}]"
            if iid in seen:
                errs.append(f"{where}: duplicate id")
            seen.add(iid)
            check_item(it, where, errs)
        if len(errs) == before:
            for it in items:
                it["chart"] = str(it["chart"]).strip()
                if "reveal" in it:
                    it["reveal"] = str(it["reveal"]).strip()
            out = OUT / (path.stem + ".json")
            out.write_text(json.dumps({"set": path.stem, "items": items}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            counts = {t: sum(1 for it in items if it["type"] == t) for t in TYPES}
            summary.append(f"{path.stem}: {len(items)} items {counts}")
    for s in summary:
        print(s)
    for e in errs:
        print("ERROR", e)
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
