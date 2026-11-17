# Investing and Trading From the Ground Up

A self-study book on investing and trading US markets from Canada, for one reader: a 4th-year CS student with an economics minor in Toronto who trades US stocks from Canadian accounts (Wealthsimple and IBKR; TFSA, RRSP or FHSA, cash and margin) in USD or CAD. 22 parts, about 200 lessons, 30 minutes a day. The Markdown in `docs/` is published to https://faiyaz-svg.github.io/InvestingAndTradingFromTheGroundUp/ and also read directly in VS Code.

## Rules to follow

- Writing: `STYLE.md`. Every page must follow it, including the list of AI-writing patterns to avoid. Em dashes are the most common slip.
- Lesson structure, chart fences, figures and number checks: `LESSON_TEMPLATE.md`.
- Site look: `DESIGN.md`.
- Price charts use made-up data only (real price data is licensed). No buy or sell calls on real securities.
- Don't make decisions the reader hasn't agreed to. Ask first when a change goes beyond what was requested.

## Layout

- `docs/00-start-here`, then `docs/01-how-markets-work` to `docs/22-careers-interviews-and-ai`: the book, in reading order. Lesson files are `NN-slug.md`, numbered by position in `tools/lessons.yml`.
- `docs/practice`: chart drills, paper trading, the trade journal. `docs/reference`: glossary, formulas, calendars, specs, common mistakes.
- `docs/assets/charts/<folder>/*.json`: synthetic price data, made by `tools/make_charts.py` from `tools/charts_src/<folder>.yml`.
- `docs/assets/figures/<folder>/*-{dark,light}.svg`: figures drawn by `tools/figures/<folder>/*.py` with `tools/figures/figstyle.py`.
- `docs/assets/drills/<set>.json`: chart drills, built by `tools/build_drills.py` from `tools/drills_src/<set>.yml`.
- `docs/assets/data/*.csv`: sample data for the In code snippets.
- `docs/assets/vendor/lightweight-charts/`: TradingView Lightweight Charts 5.2.1 (Apache-2.0), unchanged, with its licence and notice.
- `mkdocs.yml` holds the site config; its `nav` block is generated.

## Commands (Windows, Git Bash)

```bash
py -3.14 -m venv .venv
.venv/Scripts/python -m pip install -r requirements-dev.txt
.venv/Scripts/zensical serve
.venv/Scripts/zensical build --clean
.venv/Scripts/python tools/build_nav.py          # nav, progress page, home watchlist, part lesson lists
.venv/Scripts/python tools/link_planned.py       # turn <!-- link: ... --> comments into links once targets exist
.venv/Scripts/python tools/build_reference.py    # glossary and common mistakes from the lessons
.venv/Scripts/python tools/make_charts.py <folder> [--preview]
.venv/Scripts/python tools/build_drills.py
.venv/Scripts/python tools/lint.py <file or folder>
.venv/Scripts/python tools/checks/run.py [NN]
.venv/Scripts/python tools/check_code.py <file or folder>
node --test tools/test_drills.mjs
```

## Before committing a page

1. `tools/lint.py` is clean.
2. `tools/checks/run.py` passes for the part, and `tools/check_code.py` passes for the page.
3. `zensical build --clean` reports no issues.

## Git

- Work on `main`. Short, plain commit messages. A hard cap of 100 commits for this repo.
- No Co-Authored-By or any other attribution lines in commits. No force pushes.
