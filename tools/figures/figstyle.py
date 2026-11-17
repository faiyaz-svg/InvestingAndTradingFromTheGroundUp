"""Shared look for the static figures in docs/assets/figures/.

Every figure is drawn twice, once for the dark theme (the terminal screen) and
once for the light theme (paper), from one drawing function:

    from figstyle import save_pair

    def draw(fig, ax, c):              # c is the palette for this theme
        ax.plot(x, y, color=c["accent"])
        ax.set_xlabel("Stock price at expiry (US$)")

    save_pair(draw, "15-options", "long-call-payoff")

This writes long-call-payoff-dark.svg and long-call-payoff-light.svg. A lesson
shows the right one for the reader's theme:

    ![Payoff of a long call ...](../assets/figures/15-options/long-call-payoff-dark.svg#only-dark)
    ![Payoff of a long call ...](../assets/figures/15-options/long-call-payoff-light.svg#only-light)

The colours match the site's --tw-* tokens in docs/stylesheets/site.css.
Text is IBM Plex Sans (tools/fonts, OFL), saved as paths so every browser
shows the same thing. Each lesson's script lives in tools/figures/<folder>/
and is run from the repo root:

    .venv/Scripts/python tools/figures/15-options/payoffs.py
"""

from __future__ import annotations

import re
from pathlib import Path

import matplotlib

matplotlib.use("svg")

import matplotlib.pyplot as plt  # noqa: E402
from cycler import cycler  # noqa: E402
from matplotlib import font_manager  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "docs" / "assets" / "figures"
FONTS = ROOT / "tools" / "fonts"

for ttf in FONTS.glob("*.ttf"):
    font_manager.fontManager.addfont(str(ttf))

# Keep these in step with the --tw-* tokens in docs/stylesheets/site.css.
PALETTES = {
    "dark": {
        "bg": "#0e1116",
        "fg": "#c9d1d9",
        "muted": "#8b949e",
        "grid": "#222a33",
        "accent": "#f0a020",
        "up": "#2fbf71",
        "down": "#e5534b",
        "blue": "#58a6ff",
        "teal": "#3cc4b4",
        "orange": "#ff9e7a",
        "zone": "#f0a02033",
    },
    "light": {
        "bg": "#fbfaf6",
        "fg": "#1f2328",
        "muted": "#5d6670",
        "grid": "#e4e1d8",
        "accent": "#a8620a",
        "up": "#187a47",
        "down": "#c0392b",
        "blue": "#1f63c6",
        "teal": "#0f7f75",
        "orange": "#c4552a",
        "zone": "#a8620a26",
    },
}


def _style(c: dict) -> dict:
    return {
        "font.family": "IBM Plex Sans",
        "mathtext.fontset": "custom",
        "mathtext.rm": "IBM Plex Sans",
        "mathtext.it": "IBM Plex Sans:italic",
        "font.size": 11,
        "text.color": c["fg"],
        "axes.edgecolor": c["muted"],
        "axes.labelcolor": c["fg"],
        "axes.linewidth": 1.0,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.prop_cycle": cycler(color=[c["accent"], c["blue"], c["teal"], c["up"], c["down"], c["orange"]]),
        "axes.grid": True,
        "xtick.color": c["muted"],
        "ytick.color": c["muted"],
        "xtick.labelcolor": c["fg"],
        "ytick.labelcolor": c["fg"],
        "grid.color": c["grid"],
        "grid.linewidth": 0.7,
        "lines.linewidth": 2.0,
        "lines.markersize": 6,
        "legend.frameon": False,
        "figure.facecolor": c["bg"],
        "axes.facecolor": c["bg"],
        "savefig.facecolor": c["bg"],
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.12,
        "svg.fonttype": "path",
        "svg.hashsalt": "investing-and-trading-from-the-ground-up",
    }


def save_pair(draw, folder: str, name: str, width: float = 6.0, height: float = 3.6, axes: int = 1) -> list[Path]:
    """Draw the figure in both themes and write <name>-dark.svg and <name>-light.svg.

    draw(fig, ax, c) gets the axes (a list when axes > 1) and the palette.
    """
    paths = []
    for theme, c in PALETTES.items():
        with plt.rc_context(_style(c)):
            fig, ax = plt.subplots(1, axes, figsize=(width, height)) if axes > 1 else plt.subplots(figsize=(width, height))
            draw(fig, ax, c)
            path = OUT / folder / f"{name}-{theme}.svg"
            path.parent.mkdir(parents=True, exist_ok=True)
            fig.savefig(path, format="svg", metadata={"Date": None, "Creator": None})
            plt.close(fig)
        # Matplotlib writes CRLF on Windows; the repo stores LF.
        path.write_bytes(path.read_bytes().replace(b"\r\n", b"\n"))
        print("wrote", path.relative_to(ROOT).as_posix())
        paths.append(path)
    return paths


def preview(path: Path, out_dir: Path | None = None) -> Path:
    """Render an SVG to PNG with resvg, to check a figure by eye."""
    import resvg_py

    out_dir = out_dir or ROOT / "tools" / "charts_src" / "_preview"
    out_dir.mkdir(parents=True, exist_ok=True)
    png = out_dir / (path.stem + ".png")
    svg = path.read_text(encoding="utf-8")
    # resvg_py rejects sizes in pt (matplotlib's unit); give it pixels (1 pt = 4/3 px).
    svg = re.sub(
        r'width="([\d.]+)pt" height="([\d.]+)pt"',
        lambda m: f'width="{float(m.group(1)) * 4 / 3:.1f}" height="{float(m.group(2)) * 4 / 3:.1f}"',
        svg,
        count=1,
    )
    data = resvg_py.svg_to_bytes(svg_string=svg, zoom=1.5)
    png.write_bytes(bytes(data))
    return png
