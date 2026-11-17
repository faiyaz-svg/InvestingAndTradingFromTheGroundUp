"""Helpers for the number checks in tools/checks/<folder>.py.

Each part has one check file. It recomputes every worked example and answer
in the part's lessons and asserts that the lesson prints the result:

    from _lib import lesson, has, usd, num, pct

    t = lesson("03-risk-and-position-sizing", 4)     # the text of lesson 4
    risk = 0.01 * 25_000
    shares = int(risk / (48.20 - 46.70))
    assert shares == 166
    has(t, "166 shares", usd(risk))                  # "US$250.00" must appear

Formatting helpers return the forms STYLE.md uses, so the strings match:
    usd(1250.5)      -> "US$1,250.50"     usd(250, 0) -> "US$250"
    cad(1710.25)     -> "C$1,710.25"
    num(1250.5)      -> "1,250.50"        num(0.0475, 4) -> "0.0475"
    pct(0.025)       -> "2.5%"            pct(0.0412, 2) -> "4.12%"
A has() miss prints the nearest lines of the lesson to help find the typo.
"""

from __future__ import annotations

import difflib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
_LESSONS = yaml.safe_load((ROOT / "tools" / "lessons.yml").read_text(encoding="utf-8"))


def lesson_path(folder: str, n: int) -> Path:
    for f in _LESSONS["folders"]:
        if f["folder"] == folder:
            slug = f["lessons"][n - 1][0]
            return DOCS / folder / f"{n:02d}-{slug}.md"
    raise KeyError(folder)


def lesson(folder: str, n: int) -> str:
    """The lesson's text with line breaks folded, so a phrase split across lines still matches."""
    text = lesson_path(folder, n).read_text(encoding="utf-8")
    return " ".join(text.split())


def has(text: str, *needles: str) -> None:
    for needle in needles:
        if needle not in text:
            words = text.split(". ")
            near = difflib.get_close_matches(needle, words, n=2, cutoff=0.3)
            hint = "\n      ".join(near) if near else "(no close match)"
            raise AssertionError(f"not in the lesson: {needle!r}\n   nearest:\n      {hint}")


def num(x: float, d: int = 2) -> str:
    return f"{x:,.{d}f}"


def usd(x: float, d: int = 2) -> str:
    sign = "-" if x < 0 else ""
    return f"{sign}US${abs(x):,.{d}f}"


def cad(x: float, d: int = 2) -> str:
    sign = "-" if x < 0 else ""
    return f"{sign}C${abs(x):,.{d}f}"


def pct(x: float, d: int = 1) -> str:
    """A fraction as a percentage: pct(0.025) -> '2.5%'."""
    return f"{100 * x:.{d}f}%"
