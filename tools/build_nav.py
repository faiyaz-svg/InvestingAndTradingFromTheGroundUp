"""Update the site navigation, the progress page, the home watchlist and the part pages.

Reads tools/lessons.yml and writes:
  - the nav block in mkdocs.yml (between "# nav:start" and "# nav:end")
  - docs/progress.md (written lessons only, keeping any ticked boxes)
  - the watchlist table in docs/index.md (between "watchlist:start" and "watchlist:end")
  - docs/assets/parts.json (parts and lessons, read by the lesson-page strip)
  - the lesson list in each docs/<folder>/index.md (between the
    "lessons:start" and "lessons:end" comments); a missing index.md is
    created as a skeleton

Only pages that exist are linked or added to the nav, so the site never
has links to lessons that haven't been written.

Run from the repo root:  .venv/Scripts/python tools/build_nav.py
With --tracked, only pages committed to git count, so drafts on disk stay
out of the nav.
"""

from __future__ import annotations

import html
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"
LESSONS = ROOT / "tools" / "lessons.yml"
PROGRESS = DOCS / "progress.md"
HOME = DOCS / "index.md"
PARTS_JSON = DOCS / "assets" / "parts.json"

NAV_START = "# nav:start"
NAV_END = "# nav:end"
LIST_START = "<!-- lessons:start -->"
LIST_END = "<!-- lessons:end -->"
HOME_START = "<!-- watchlist:start -->"
HOME_END = "<!-- watchlist:end -->"

START_HERE = [
    ("How to use this book", "00-start-here/index.md"),
    ("The 30-minute routine", "00-start-here/the-30-minute-routine.md"),
    ("Set up your tools", "00-start-here/set-up-your-tools.md"),
    ("Canada and the US at a glance", "00-start-here/canada-and-us-at-a-glance.md"),
    ("Tickers and symbols", "00-start-here/tickers-and-symbols.md"),
    ("Not financial advice", "00-start-here/not-financial-advice.md"),
    ("Credits and sources", "00-start-here/credits-and-sources.md"),
    ("Progress", "progress.md"),
]

PRACTICE = [
    ("Practice", "practice/index.md"),
    ("Chart drills", "practice/chart-drills.md"),
    ("Paper trading", "practice/paper-trading.md"),
    ("Trade journal", "practice/trade-journal.md"),
]

REFERENCE = [
    ("Reference", "reference/index.md"),
    ("Glossary", "reference/glossary.md"),
    ("Formulas", "reference/formulas.md"),
    ("Ratios", "reference/ratios.md"),
    ("Order types", "reference/order-types.md"),
    ("Economic calendar", "reference/economic-calendar.md"),
    ("Options strategies", "reference/options-strategies.md"),
    ("Futures contract specs", "reference/futures-contract-specs.md"),
    ("Canadian tax quick reference", "reference/canadian-tax-quick-reference.md"),
    ("Data sources", "reference/data-sources.md"),
    ("Case study timeline", "reference/case-study-timeline.md"),
    ("Common mistakes", "reference/common-mistakes.md"),
]

KINDS = {
    "idea": "Idea",
    "skill": "Skill",
    "strategy": "Strategy",
    "data": "Data",
    "canada": "Canada",
    "code": "Code",
    "case": "Case study",
    "career": "Career",
}
EXTRA_FLAGS = {"review"}

# Set by --tracked: the paths (relative to docs/) that git knows about.
TRACKED: set[str] | None = None


@dataclass
class Lesson:
    num: int
    slug: str
    title: str
    path: str  # relative to docs/
    flags: list[str]

    @property
    def exists(self) -> bool:
        return exists(self.path)

    @property
    def kind(self) -> str:
        return next(flag for flag in self.flags if flag in KINDS)

    @property
    def url(self) -> str:
        """The page's URL path relative to the site root, with a trailing slash."""
        return self.path.removesuffix(".md") + "/"

    def notes(self) -> str:
        """The kind and any extra flags, as shown after the title in lists."""
        return ", ".join([KINDS[self.kind].lower()] + [flag for flag in self.flags if flag in EXTRA_FLAGS])


@dataclass
class Folder:
    num: int
    folder: str
    code: str
    group: str
    title: str
    summary: str
    before: str
    lessons: list[Lesson] = field(default_factory=list)

    @property
    def heading(self) -> str:
        return f"Part {self.num}: {self.title}"


def parse_lesson(entry: list, folder: str, number: int) -> Lesson:
    # A title with an unquoted comma turns into extra list items, so check the shape.
    if not 2 <= len(entry) <= 3 or (len(entry) == 3 and not isinstance(entry[2], list)):
        raise SystemExit(f"bad lesson entry {entry!r}: quote titles that contain commas")
    slug, title = str(entry[0]), entry[1]
    flags = list(entry[2]) if len(entry) > 2 else []
    kinds = [flag for flag in flags if flag in KINDS]
    if len(kinds) != 1 or not set(flags) <= set(KINDS) | EXTRA_FLAGS:
        raise SystemExit(f"bad flags in lesson entry {entry!r}: need one kind, then optional review")
    return Lesson(number, slug, title, f"{folder}/{number:02d}-{slug}.md", flags)


def load() -> tuple[list[str], list[Folder]]:
    data = yaml.safe_load(LESSONS.read_text(encoding="utf-8"))
    groups = list(data["groups"])
    folders = []
    for n, f in enumerate(data["folders"], 1):
        if f["group"] not in groups:
            raise SystemExit(f"bad group {f['group']!r} in {f['folder']}")
        folder = Folder(
            num=n,
            folder=f["folder"],
            code=f["code"],
            group=f["group"],
            title=f["title"],
            summary=f.get("summary", ""),
            before=f.get("before", ""),
        )
        folder.lessons = [parse_lesson(e, f["folder"], i) for i, e in enumerate(f["lessons"], 1)]
        folders.append(folder)
    return groups, folders


def exists(path: str) -> bool:
    if TRACKED is not None:
        return path in TRACKED
    return (DOCS / path).is_file()


def tracked_paths() -> set[str]:
    out = subprocess.run(
        ["git", "ls-files", "docs"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout
    return {line.removeprefix("docs/") for line in out.splitlines()}


def q(text: str) -> str:
    """Quote a title for YAML (JSON strings are valid YAML)."""
    return json.dumps(text, ensure_ascii=False)


def build_nav(groups: list[str], folders: list[Folder]) -> str:
    # The home page is the index of the "Start here" tab; the site title also links home.
    lines = [NAV_START, "nav:", "  - Start here:", "      - index.md"]
    for title, path in START_HERE:
        if exists(path):
            lines.append(f"      - {q(title)}: {path}")

    for group in groups:
        members = [f for f in folders if f.group == group and exists(f"{f.folder}/index.md")]
        if not members:
            continue
        lines.append(f"  - {q(group)}:")
        for f in members:
            lines.append(f"      - {q(f.title)}:")
            lines.append(f"          - {f.folder}/index.md")
            for lesson in f.lessons:
                if lesson.exists:
                    lines.append(f"          - {q(lesson.title)}: {lesson.path}")

    for tab, pages in (("Practice", PRACTICE), ("Reference", REFERENCE)):
        found = [(t, p) for t, p in pages if exists(p)]
        if not found:
            continue
        lines.append(f"  - {tab}:")
        for title, path in found:
            if path.endswith("/index.md"):
                lines.append(f"      - {path}")
            else:
                lines.append(f"      - {q(title)}: {path}")

    lines.append(NAV_END)
    return "\n".join(lines)


def write_nav(groups: list[str], folders: list[Folder]) -> None:
    text = MKDOCS.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(NAV_START) + r".*?" + re.escape(NAV_END), re.S)
    if not pattern.search(text):
        raise SystemExit(f"mkdocs.yml has no '{NAV_START}' ... '{NAV_END}' block")
    MKDOCS.write_text(pattern.sub(lambda _: build_nav(groups, folders), text), encoding="utf-8", newline="\n")


def ticked_paths() -> set[str]:
    if not PROGRESS.is_file():
        return set()
    done = set()
    for line in PROGRESS.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\s*- \[[xX]\] \[.*?\]\((.*?)\)", line)
        if m:
            done.add(m.group(1))
    return done


def write_progress(groups: list[str], folders: list[Folder]) -> None:
    done = ticked_paths()
    total = sum(len(f.lessons) for f in folders)
    written = sum(1 for f in folders for lesson in f.lessons if lesson.exists)
    out = [
        "# Progress",
        "",
        "Tick each lesson when you finish it. On the website, ticks are saved in the "
        "browser you use, so each device keeps its own list, and the DONE column on the "
        "home page fills in too. In VS Code, change `[ ]` to `[x]` in `docs/progress.md`.",
        "",
        f"Lessons written so far: {written} of {total}. New lessons appear here as they are added.",
        "",
    ]
    for group in groups:
        members = [f for f in folders if f.group == group and any(lesson.exists for lesson in f.lessons)]
        if not members:
            continue
        out += [f"## {group}", ""]
        for f in members:
            out += [f"### {f.heading}", ""]
            for lesson in f.lessons:
                if not lesson.exists:
                    continue
                box = "x" if lesson.path in done else " "
                out.append(f"- [{box}] [{lesson.title}]({lesson.path}) ({lesson.notes()})")
            out.append("")
    PROGRESS.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8", newline="\n")


def lesson_list(f: Folder) -> str:
    lines = [LIST_START, "## Lessons", ""]
    for lesson in f.lessons:
        rel = lesson.path.removeprefix(f.folder + "/")
        text = f"[{lesson.title}]({rel})" if lesson.exists else f"{lesson.title} (not written yet)"
        lines.append(f"{lesson.num}. {text} ({lesson.notes()})")
    lines += ["", LIST_END]
    return "\n".join(lines)


def write_folder_index(f: Folder) -> None:
    path = DOCS / f.folder / "index.md"
    block = lesson_list(f)
    if not path.is_file():
        path.parent.mkdir(parents=True, exist_ok=True)
        skeleton = [
            f"# {f.heading}",
            "",
            f.summary,
            "",
            f"Before this part: {f.before}",
            "",
            block,
            "",
            "## Cheat sheet",
            "",
            "<!-- to be written -->",
            "",
        ]
        path.write_text("\n".join(skeleton), encoding="utf-8", newline="\n")
        return
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(LIST_START) + r".*?" + re.escape(LIST_END), re.S)
    if pattern.search(text):
        text = pattern.sub(lambda _: block, text)
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    path.write_text(text, encoding="utf-8", newline="\n")


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def watchlist(groups: list[str], folders: list[Folder]) -> str:
    """The home page table: one row per part, grouped like the site tabs."""
    out = [
        HOME_START,
        '<div class="tw-watch-wrap">',
        '<table class="tw-watch">',
        "<thead><tr><th>Code</th><th>Part</th><th class=\"tw-num\">Lessons</th><th>Done</th></tr></thead>",
    ]
    for group in groups:
        out.append(f'<tbody data-group="{esc(group)}">')
        out.append(f'<tr class="tw-group"><th colspan="4">{esc(group)}</th></tr>')
        for f in (f for f in folders if f.group == group):
            written = [lesson for lesson in f.lessons if lesson.exists]
            linked = exists(f"{f.folder}/index.md")
            code = f'<a href="{f.folder}/">{esc(f.code)}</a>' if linked else esc(f.code)
            name = f'<a href="{f.folder}/">{esc(f.title)}</a>' if linked else esc(f.title)
            count = str(len(f.lessons)) if len(written) == len(f.lessons) else f"{len(written)}/{len(f.lessons)}"
            urls = " ".join(lesson.url for lesson in written)
            out.append(
                f'<tr class="tw-part" data-part="{f.num:02d}" data-total="{len(f.lessons)}" data-lessons="{esc(urls)}">'
                f'<td class="tw-code">{code}</td>'
                f'<td class="tw-name">{name}<span class="tw-sum">{esc(f.summary)}</span></td>'
                f'<td class="tw-num">{count}</td>'
                '<td class="tw-done"><span class="tw-bar"><span class="tw-fill"></span></span>'
                '<span class="tw-pct">0%</span></td></tr>'
            )
        out.append("</tbody>")
    out += ["</table>", "</div>", HOME_END]
    return "\n".join(out)


def write_home(groups: list[str], folders: list[Folder]) -> bool:
    if not HOME.is_file():
        return False
    text = HOME.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(HOME_START) + r".*?" + re.escape(HOME_END), re.S)
    if not pattern.search(text):
        return False
    HOME.write_text(pattern.sub(lambda _: watchlist(groups, folders), text), encoding="utf-8", newline="\n")
    return True


def write_parts_json(folders: list[Folder]) -> None:
    data = {
        "parts": [
            {
                "num": f.num,
                "folder": f.folder,
                "code": f.code,
                "group": f.group,
                "title": f.title,
                "lessons": [
                    {
                        "num": lesson.num,
                        "path": lesson.url,
                        "title": lesson.title,
                        "kind": lesson.kind,
                        "published": lesson.exists,
                    }
                    for lesson in f.lessons
                ],
            }
            for f in folders
        ]
    }
    PARTS_JSON.parent.mkdir(parents=True, exist_ok=True)
    PARTS_JSON.write_text(
        json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8", newline="\n"
    )


def main() -> None:
    global TRACKED
    if "--tracked" in sys.argv[1:]:
        TRACKED = tracked_paths()
    groups, folders = load()
    for f in folders:
        # A part page appears once it has a lesson or an overview page. On disk
        # the skeleton is always created, so the nav lists every part.
        if TRACKED is None or any(lesson.exists for lesson in f.lessons) or exists(f"{f.folder}/index.md"):
            write_folder_index(f)
    write_progress(groups, folders)
    mapped = write_home(groups, folders)
    write_parts_json(folders)
    write_nav(groups, folders)
    total = sum(len(f.lessons) for f in folders)
    written = sum(1 for f in folders for lesson in f.lessons if lesson.exists)
    note = "" if mapped else " (docs/index.md has no watchlist markers yet)"
    print(f"{len(folders)} parts, {written} of {total} lessons written; nav, progress, watchlist and lists updated{note}")


if __name__ == "__main__":
    main()
