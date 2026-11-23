"""Style and template check for the book's pages (the STYLE.md self-check, as a script).

Run from the repo root:
  .venv/Scripts/python tools/lint.py                          every page in docs/
  .venv/Scripts/python tools/lint.py docs/03-risk-and-position-sizing
  .venv/Scripts/python tools/lint.py docs/03-risk-and-position-sizing/02-r-multiples.md

Checks:
  - typography everywhere: em dashes, en dashes outside numeric ranges, curly
    quotes, emoji
  - prose: banned and sparing words, bold-label bullets, Title Case headings
  - balanced <details> and <div>
  - chart fences: known keys, the data file exists, levels inside the data's range
  - figures: each -dark.svg#only-dark has its -light.svg#only-light partner, and both files exist
  - lessons: tag line, goal, "Before this:", required sections, Next line,
    practice minutes adding up to 10, prose word count, In code boxes hold a python fence
Some hits are false positives (a word in a quotation, a name); read each one.
A page can allow a "use rarely" word it needs, with a reason:
  <!-- lint-ok: significant (statistical sense) -->
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CHARTS = DOCS / "assets" / "charts"

BANNED = re.compile(
    r"\b(delve|tapestry|testament|pivotal|underscores?|underscored|intricat\w*|meticulous\w*|showcas\w*|"
    r"garner\w*|bolster\w*|interplay|vibrant|multifaceted|realms?|groundbreaking|renowned|nestled|"
    r"seamless\w*|commendable|noteworthy|invaluable|transformative|unparalleled|unveil\w*|harness\w*|"
    r"elucidat\w*|burgeoning|foster\w*|quietly|deep dive|boasts?|journey|unlock\w*|"
    r"elevat(?:e|es|ed|ing)\b|"
    r"key (?:role|factor|takeaway|insight|concept)s?|"
    r"serves? as|stands? as|functions? as|important to note|worth noting|worth mentioning|in summary|"
    r"in conclusion|to sum up|not only|let'?s dive|let'?s unpack|clearly|obviously|it is easy|"
    r"simply|trivially|great question|i hope this helps|holy grail|foolproof|can'?t lose|to the moon|"
    r"timeless|beloved|iconic|masterpiece|breathtaking|game-changing|supercharge\w*|revolutioni[sz]e)\b",
    re.I,
)
SPARING = re.compile(
    r"\b(crucial|vital|essential|comprehensive|notably|additionally|moreover|furthermore|consequently|"
    r"ultimately|enhance\w*|valuable|insights?|remarkable|nuanced|significant|robust|powerful|lush|"
    r"guaranteed|just|master(?:ed|ing|s)?)\b",
    re.I,
)

# Mixed-case words allowed to keep a capital in a heading (besides the first word).
# All-caps tokens (ETF, TFSA, US, EPS, P/E, 0DTE ...) are allowed automatically.
HEADING_OK = {
    "I", "Canada", "Canadian", "Canadians", "Toronto", "Ontario", "Quebec", "Montreal", "New", "York",
    "America", "American", "US", "United", "States", "Fed", "Federal", "Reserve", "Treasury", "Treasuries",
    "Bank", "Wealthsimple", "Nasdaq", "Cboe", "Dow", "Jones", "Russell", "Bollinger", "Keltner", "Kelly",
    "Norbert's", "Black-Scholes", "Black", "Scholes", "Greeks", "Ethereum", "Bitcoin", "DeFi", "Form",
    "Python", "Excel", "Google", "Sheets", "TradingView", "Interactive", "Brokers", "GameStop", "Archegos",
    "COVID", "Wall", "Street", "Bay", "Exchange", "Montreal", "Commitments", "Traders", "Questrade",
    "Coinbase", "Kraken", "Kalshi", "Polymarket", "Fama", "French", "Markowitz", "Sharpe", "Sortino",
    "Monte", "Carlo", "Taylor", "Phillips", "Sahm", "Beige", "Book", "Powell", "Volcker", "Lehman",
    "Brothers", "Bear", "Stearns", "Enron", "FTX", "Terra", "Luna", "Tether", "Circle", "Binance",
    "US-listed", "Canadian-listed", "US-based", "Canadian-based",
    "Math", "From", "Ground", "Up", "VS", "Code", "Zensical", "Mermaid", "KaTeX", "Lightweight", "Charts",
    "Plex", "IBM", "Anki", "Windows", "Mac", "Linux", "Chrome", "Edge", "Firefox", "Android", "iPhone",
    "Yahoo", "Finance", "Investor's", "Business", "Daily", "Barron's", "Reuters", "Morningstar", "Vanguard",
    "BlackRock", "iShares", "BMO", "CIBC", "TD", "RBC", "Scotia", "Desjardins", "Fidelity", "Schwab",
    "Robinhood", "Hong", "Kong", "London", "Tokyo", "Asia", "Europe", "European", "Japan", "China",
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "January", "February", "March", "April",
    "May", "June", "July", "August", "September", "October", "November", "December",
}
SHORT_CAPS = re.compile(r"^[A-Z0-9][A-Z0-9&.\-/']*s?$")

SECTIONS = ["## The idea", "## Try it", "## Practice today (10 min)", "## Key terms"]
GOAL_MARKER = "After this lesson you can"
BEFORE_MARKER = "Before this:"
NEXT_LINE = re.compile(r"^Next: ", re.M)
CHART_KEYS = {"data", "title", "show", "type", "level", "zone", "marker", "line", "range", "height", "caption"}
SHOW_NAMES = {"volume", "sma", "ema", "vwap", "avwap", "bb", "keltner", "rsi", "macd", "atr", "stoch"}
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
FIGURE = re.compile(r"!\[[^\]]*\]\(([^)\s]+?)-(dark|light)\.svg#only-(dark|light)\)")


def strip_inline(line: str) -> str:
    """Remove inline code, math and URLs from a prose line."""
    line = re.sub(r"`[^`]*`", "", line)
    line = re.sub(r"\\\(.*?\\\)", "", line)
    line = re.sub(r"\]\([^)]*\)", "]", line)
    line = re.sub(r"https?://\S+", "", line)
    return line


def paragraphs(lines: list[tuple[int, str]]) -> list[tuple[int, list[str]]]:
    blocks, cur, start = [], [], 0
    for no, line in lines:
        if line.strip():
            if not cur:
                start = no
            cur.append(line)
        elif cur:
            blocks.append((start, cur))
            cur = []
    if cur:
        blocks.append((start, cur))
    return blocks


def prose_words(blocks: list[tuple[int, list[str]]]) -> int:
    count = 0
    for _, block in blocks:
        text = "\n".join(ln for ln in block if not ln.lstrip().startswith("|"))
        text = re.sub(r"\\\[.*?\\\]", " ", text, flags=re.S)
        text = re.sub(r"\\\(.*?\\\)", " x ", text)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"\{:[^}]*\}", " ", text)
        text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
        text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
        count += len(re.findall(r"[A-Za-z0-9']+", text))
    return count


def practice_minutes(text: str) -> list[int]:
    totals = []
    for block in re.findall(r'<div class="practice" markdown>(.*?)</div>', text, flags=re.S):
        mins = 0
        for row in block.splitlines():
            m = re.match(r"^\|\s*(\d+)\s*\|", row)
            if m:
                mins += int(m.group(1))
        totals.append(mins)
    return totals


def chart_issues(spec_lines: list[tuple[int, str]]) -> list[str]:
    issues = []
    data_path = None
    levels = []
    times = []  # (line, time text) from range, marker, zone spans and lines
    for no, line in spec_lines:
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        m = re.match(r"^([a-z]+):\s*(.*)$", s)
        if not m or m.group(1) not in CHART_KEYS:
            issues.append(f"{no}: chart fence: unknown line '{s[:40]}'")
            continue
        key, val = m.groups()
        if key == "data":
            data_path = (no, val)
        elif key == "show":
            for item in val.split(","):
                name = item.strip().split(" ")[0]
                if name and name not in SHOW_NAMES:
                    issues.append(f"{no}: chart fence: unknown indicator '{name}'")
        elif key == "level":
            try:
                levels.append((no, float(val.split("|")[0])))
            except ValueError:
                issues.append(f"{no}: chart fence: level needs a number first")
        elif key == "zone":
            if not re.match(r"^\d+(\.\d+)?\s*-\s*\d+(\.\d+)?\s*(\||$)", val):
                issues.append(f"{no}: chart fence: zone needs 'low-high | ...'")
        elif key == "marker":
            if val.count("|") != 2 or val.split("|")[1].strip() not in ("above", "below"):
                issues.append(f"{no}: chart fence: marker needs 'time | above or below | text'")
            times.append((no, val.split("|")[0].strip()))
        elif key == "range":
            times += [(no, x.strip()) for x in val.split(" to ")]
        if key == "zone" and val.count("|") >= 2:
            times += [(no, x.strip()) for x in val.split("|")[1].split(" to ")]
        if key == "line":
            m2 = re.match(r"^(\S+(?: \d\d:\d\d)?)\s+[\d.]+\s+to\s+(\S+(?: \d\d:\d\d)?)\s+[\d.]+", val)
            if m2:
                times += [(no, m2.group(1)), (no, m2.group(2))]
    if not data_path:
        issues.append(f"{spec_lines[0][0] if spec_lines else 0}: chart fence without data")
        return issues
    no, rel = data_path
    path = CHARTS / rel
    if not path.is_file():
        issues.append(f"{no}: chart data not found: docs/assets/charts/{rel}")
        return issues
    bars = json.loads(path.read_text(encoding="utf-8"))["bars"]
    lo = min(b[3] for b in bars)
    hi = max(b[2] for b in bars)
    for lno, price in levels:
        if not lo * 0.9 <= price <= hi * 1.1:
            issues.append(f"{lno}: chart level {price} is far outside the data ({lo} to {hi})")
    # Dates in the fence must fall inside the data (daily and weekly data; intraday times are skipped).
    if isinstance(bars[0][0], str):
        first, last = bars[0][0], bars[-1][0]
        for tno, when in times:
            day = when[:10]
            if re.match(r"^\d{4}-\d\d-\d\d$", day) and not first <= day <= last:
                issues.append(f"{tno}: chart date {day} is outside the data ({first} to {last})")
    return issues


def heading_issue(line: str) -> bool:
    line = re.sub(r"^(#+\s*)Part \d+:\s*", r"\1", line)
    words = re.sub(r"[()\[\]]", " ", line.lstrip("#")).split()
    for w in words[1:]:
        core = w.strip(".,:;!?\"'")
        if not core or not core[:1].isupper():
            continue
        if core in HEADING_OK or SHORT_CAPS.match(core) or core[:1].isdigit():
            continue
        if core.endswith("'s") and core[:-2] in HEADING_OK:
            continue
        return True
    return False


def check(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []
    lint_ok = {w.lower() for w in re.findall(r"<!-- lint-ok: (\w+)", text)}
    section = ""
    in_fence = ""
    fence_lines: list[tuple[int, str]] = []
    code_box = False
    code_box_has_python = False
    prose_lines: list[tuple[int, str]] = []
    in_math = False
    for no, line in enumerate(text.splitlines(), 1):
        fence = re.match(r"^\s*(```+|~~~+)\s*([\w-]*)", line)
        if fence:
            if not in_fence:
                in_fence = fence.group(2) or "plain"
                fence_lines = []
                if in_fence == "python" and code_box:
                    code_box_has_python = True
            else:
                if in_fence == "chart":
                    issues += chart_issues(fence_lines)
                in_fence = ""
            continue
        if "—" in line:
            issues.append(f"{no}: em dash")
        if "–" in line and not re.search(r"\d–\d", line):
            issues.append(f"{no}: en dash outside a numeric range")
        if re.search("[“”‘’]", line):
            issues.append(f"{no}: curly quote")
        if EMOJI.search(line):
            issues.append(f"{no}: emoji or symbol")
        if re.search("[\x00-\x08\x0b\x0c\x0e-\x1f]", line):
            issues.append(f"{no}: control character (a lost backslash, such as \\b or \\f in LaTeX?)")
        if in_fence:
            fence_lines.append((no, line))
            continue
        if line.strip().startswith("\\["):
            in_math = True
        if in_math:
            if line.strip().endswith("\\]"):
                in_math = False
            continue
        if '<details class="code"' in line:
            code_box, code_box_has_python = True, False
        if "</details>" in line and code_box:
            if not code_box_has_python:
                issues.append(f"{no}: In code box without a python fence")
            code_box = False
        prose_lines.append((no, line))

        if line.startswith("## "):
            section = line.strip()

        prose = strip_inline(line)
        if line.lstrip().startswith("<!--"):
            continue
        for m in BANNED.finditer(prose):
            issues.append(f"{no}: banned '{m.group(0)}'")
        for m in SPARING.finditer(prose):
            word = m.group(0).lower()
            if word in lint_ok:
                continue
            if word.startswith("master") and re.search(r"master account", prose, re.I):
                continue
            issues.append(f"{no}: use rarely '{m.group(0)}'")
        if section != "## Key terms" and path.name != "glossary.md" and (
            re.match(r"^\s*[-*] \*\*[^*]+:\*\*", line) or re.match(r"^\s*[-*] \*\*[^*]+\*\*[ \xa0]?:", line)
        ):
            issues.append(f"{no}: bold label bullet")
        if re.match(r"^#{2,6} ", line) and heading_issue(line):
            issues.append(f"{no}: Title Case? {line.strip()}")

    if in_fence:
        issues.append(f"unclosed {in_fence} fence")
    if text.count("<details") != text.count("</details>"):
        issues.append("unbalanced <details>")
    if len(re.findall(r"<div ", text)) != text.count("</div>"):
        issues.append("unbalanced <div>")

    # Figure pairs: every dark image has its light partner, and both files exist.
    figs = FIGURE.findall(text)
    seen = {(base, theme) for base, theme, _ in figs}
    for base, theme, only in figs:
        if theme != only:
            issues.append(f"figure {base}-{theme}.svg is marked #only-{only}")
        other = "light" if theme == "dark" else "dark"
        if (base, other) not in seen:
            issues.append(f"figure {base}-{theme}.svg has no {other} partner")
        target = (path.parent / f"{base}-{theme}.svg").resolve()
        if not target.is_file():
            issues.append(f"figure file not found: {base}-{theme}.svg")

    # Template checks apply to lessons: files in a part folder other than index.md.
    if path.name != "index.md" and re.match(r"(0[1-9]|1\d|2[0-2])-", path.parent.name):
        if GOAL_MARKER not in text:
            issues.append(f"missing the goal ('{GOAL_MARKER} ...')")
        if BEFORE_MARKER not in text:
            issues.append("missing the 'Before this:' line")
        for name in SECTIONS:
            if not re.search(rf"^{re.escape(name)}\s*$", text, re.M):
                issues.append(f"missing section '{name}'")
        if not NEXT_LINE.search(text):
            issues.append("missing 'Next:' line")
        if not re.search(r"^# .+$", text, re.M):
            issues.append("missing the H1 title")
        if not re.search(r'class="tag tag-part"', text):
            issues.append("missing the tag line under the title")
        totals = practice_minutes(text)
        if not totals:
            issues.append('practice box (<div class="practice" markdown>) not found')
        for total in totals:
            if total != 10:
                issues.append(f"practice minutes add up to {total}, not 10")
        words = prose_words(paragraphs(prose_lines))
        if words > 1500:
            issues.append(f"{words} words of prose (cap 1500)")
        elif words < 500:
            issues.append(f"{words} words of prose (short?)")
    return issues


def main() -> None:
    paths = []
    for arg in sys.argv[1:] or ["docs"]:
        p = Path(arg)
        paths += sorted(p.rglob("*.md")) if p.is_dir() else [p]
    total = 0
    for path in paths:
        if path.name == "style-sample.md":
            continue
        found = check(path)
        total += len(found)
        if found:
            print(f"== {path}: {len(found)} issue(s)")
            for item in found[:40]:
                print("   ", item)
    print(f"{total} issue(s) in {len(paths)} file(s)")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
