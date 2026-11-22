"""True range when a bar gaps (lesson 7): Stock A, 2026-02-23 and 2026-02-24."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from matplotlib.patches import Rectangle
from figstyle import save_pair, preview


def candle(ax, x, o, h, lo, c, col):
    ax.plot([x, x], [lo, h], color=col, lw=2, solid_capstyle="butt")
    ax.add_patch(Rectangle((x - 0.2, min(o, c)), 0.4, abs(c - o), facecolor=col, edgecolor=col))


def draw(fig, ax, cc):
    ax.grid(False)
    candle(ax, 1, 50.92, 51.37, 50.9, 51.34, cc["up"])
    candle(ax, 2, 53.91, 55.19, 53.60, 54.83, cc["up"])
    ax.annotate("", xy=(2.45, 51.34), xytext=(2.45, 55.19), arrowprops=dict(arrowstyle="<->", color=cc["accent"], lw=1.6))
    ax.text(2.55, 53.3, "True range 3.85\n(high minus previous close)", color=cc["accent"], fontsize=9, va="center")
    ax.annotate("", xy=(1.6, 53.60), xytext=(1.6, 55.19), arrowprops=dict(arrowstyle="<->", color=cc["muted"], lw=1.2))
    ax.text(1.55, 54.4, "High minus low\n1.59", color=cc["muted"], fontsize=9, va="center", ha="right")
    ax.axhline(51.34, color=cc["muted"], lw=0.8, ls="--")
    ax.text(0.55, 51.45, "Previous close 51.34", color=cc["muted"], fontsize=9)
    ax.set_xlim(0.4, 4.4)
    ax.set_ylim(50.5, 55.8)
    ax.set_xticks([1, 2])
    ax.set_xticklabels(["Feb 23", "Feb 24"])
    ax.set_ylabel("Stock A price (US$)")


if __name__ == "__main__":
    for q in save_pair(draw, "05-reading-charts", "true-range", width=6.0, height=3.4):
        preview(q)
