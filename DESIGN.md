# Design

All styles are in `docs/stylesheets/site.css` (the drill tool has its own `drills.css`). Part codes and header label come from `docs/javascripts/theme.js`.

## The idea

A trading terminal. Dark by default: a near-black screen, amber headings and tabs, light grey text. Light mode is paper: a warm off-white page, near-black text, dark amber accents. The header, tabs and footer are a dark bar in both schemes.

## Rules

- Flat and square. No shadows, gradients, rounded corners, glow, emoji or purple.
- Thin 1px rules. Amber marks structure (headings, links, active tab).
- Green and red mean gain and loss only (`--tw-up`, `--tw-down`). Never use them for decoration, warnings or success states.
- No brand look-alikes: no logos, brand names or copied keyboard styling.
- Phones: 16px side gutters, no horizontal page scroll. Wide tables scroll inside their own wrapper. The tabs bar scrolls sideways and shows a thin scrollbar.

## Tokens

Both schemes define the same names. Chart tokens must keep these exact values: `charts.js` and `tools/figures/figstyle.py` read them, and `charts.js` adds hex alpha to `--tw-up`, `--tw-down` and `--tw-chart-fg`, so those three stay 6-digit hex.

| Token | Dark | Light | Use |
|---|---|---|---|
| `--tw-bg` / `--tw-chart-bg` | `#0e1116` | `#fbfaf6` | page and chart background |
| `--tw-fg` / `--tw-chart-fg` | `#c9d1d9` | `#1f2328` | body text (12.3:1 / 15.1:1) |
| `--tw-muted` | `#8b949e` | `#5b5a52` | secondary text (6.2:1 / 6.6:1) |
| `--tw-rule` | `#2a323c` | `#d6d2c4` | 1px rules |
| `--tw-panel` | `#151a21` | `#f1eee5` | box and table header background |
| `--tw-accent-text` | `#f0a020` | `#8f5206` | headings, links (8.8:1 / 5.9:1) |
| `--tw-chart-grid` | `#222a33` | `#e4e1d8` | chart grid |
| `--tw-up` / `--tw-down` | `#2fbf71` / `#e5534b` | `#187a47` / `#c0392b` | gain and loss |
| `--tw-accent`, `--tw-s1` | `#f0a020` | `#a8620a` | chart accent, series 1 |
| `--tw-s2` | `#58a6ff` | `#1f63c6` | series 2 |
| `--tw-s3` | `#3cc4b4` | `#0f7f75` | series 3 |
| `--tw-s4` | `#7ee0c0` | `#187a47` | series 4 |
| `--tw-s5` | `#ff9e7a` | `#c4552a` | series 5 |
| `--tw-chart-zone` | `rgba(240,160,32,0.16)` | `rgba(168,98,10,0.15)` | shaded zones |
| `--tw-chart-font` | IBM Plex Mono | IBM Plex Mono | chart text |

Other tokens: `--tw-mark`, `--tw-blue-text`, `--tw-teal-text`, `--tw-coral-text` (tag and box colours checked for 4.5:1 on the page), `--tw-bar-*` (header, tabs, footer) and `--tw-code-*` (code panel, dark in both schemes). Material's `--md-*` variables are mapped to these at the top of the file.

## Type

IBM Plex Sans for text. IBM Plex Mono for the header, tabs, tags, table headers, box labels, code and the watchlist. Tables use `font-variant-numeric: tabular-nums`. H1 is amber. H2 is amber with a 1px amber rule. H3 has a mono `>` prefix.

## Components

Lessons follow `LESSON_TEMPLATE.md`. HTML for each part:

- Tags: `<span class="tag tag-skill">Skill</span>`. Kinds: `tag-idea tag-skill tag-strategy tag-data tag-canada tag-code tag-case tag-career tag-review`. `tag-part` is a filled amber label with the part code.
- Part code: `theme.js` adds `<span class="tw-fkey">RISK</span>` to the header on part pages (one span, updated on each page change).
- Boxes: `<div class="example" markdown>` (amber left rule), `note` (blue rule, "NOTE" label), `warning` (coral rule, "WATCH OUT" label), `canada` (teal rule, "CA" label in the corner, heading "For Canadians"), `practice` (amber outline, heading shown as a `$` command line).
- Answers: `<details class="solution" markdown><summary>Answer</summary>`. Code: `<details class="code" markdown><summary>In code</summary>`.
- Tables: thin rules, header row in mono caps.
- Watchlist (home page, written by `tools/build_nav.py`): `.tw-watch-wrap > table.tw-watch`, `tbody[data-group]`, `tr.tw-group`, `tr.tw-part` (`tw-started`, `tw-finished` set by `progress.js`), cells `tw-code tw-name tw-num tw-done`. The bar fill is green. On phones the summary and bar are hidden.
- Previous and next: `.mf-prevnext` with `.mf-prev` and `.mf-next`, top and bottom.
- Progress page: `.tw-progress-count`, `input.tw-progress-box`.
- Code blocks: dark panel in both schemes, syntax colours from the series tokens.

## Charts, figures and diagrams

- Price charts: `charts.js` replaces each `pre.chart` with `figure.tw-chart` (`.tw-chart-title`, `.tw-chart-area` with `.tw-chart-box` and `.tw-chart-legend`, `figcaption`, `.tw-chart-error`). The canvas reads the `--tw-chart-*`, `--tw-up`, `--tw-down`, `--tw-accent` and `--tw-s1` to `--tw-s5` tokens from `body` and re-colours when the scheme changes.
- Static figures: `tools/figures/figstyle.py` has the same values in `PALETTES`. Each figure is a dark and a light SVG; the CSS shows the one matching the scheme (`#only-dark`, `#only-light`). Images get a 1px rule border.
- Mermaid: colours come from the `--md-mermaid-*` variables in `site.css`, with IBM Plex Sans.

## Preview

`docs/style-sample.md` has one of every element. It is gitignored and not in the nav. Run `zensical serve` and open `/style-sample/`.
