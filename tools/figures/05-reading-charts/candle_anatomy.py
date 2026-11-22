"""The parts of an up candle and a down candle (lesson 1)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from matplotlib.patches import Rectangle
from figstyle import save_pair, preview


def candle(ax, x, o, h, lo, c, col):
    ax.plot([x, x], [lo, h], color=col, lw=2, solid_capstyle="butt")
    ax.add_patch(Rectangle((x - 0.25, min(o, c)), 0.5, abs(c - o), facecolor=col, edgecolor=col))


def draw(fig, ax, cc):
    ax.grid(False)
    candle(ax, 1, 50.93, 52.67, 50.78, 52.46, cc["up"])
    candle(ax, 3, 52.75, 52.86, 51.06, 51.17, cc["down"])
    ax.text(1, 53.1, "Up candle", ha="center", color=cc["fg"], fontsize=10)
    ax.text(3, 53.1, "Down candle", ha="center", color=cc["fg"], fontsize=10)
    for x, o, h, lo, c, side in ((1, 50.93, 52.67, 50.78, 52.46, -1), (3, 52.75, 52.86, 51.06, 51.17, 1)):
        pass
    kw = dict(color=cc["muted"], fontsize=9, va="center")
    ax.annotate("High 52.67", xy=(1, 52.67), xytext=(1.6, 52.9), arrowprops=dict(arrowstyle="->", color=cc["muted"]), **kw)
    ax.annotate("Close 52.46", xy=(1.25, 52.46), xytext=(1.6, 52.3), arrowprops=dict(arrowstyle="->", color=cc["muted"]), **kw)
    ax.annotate("Open 50.93", xy=(1.25, 50.93), xytext=(1.6, 51.2), arrowprops=dict(arrowstyle="->", color=cc["muted"]), **kw)
    ax.annotate("Low 50.78", xy=(1, 50.78), xytext=(1.6, 50.6), arrowprops=dict(arrowstyle="->", color=cc["muted"]), **kw)
    ax.annotate("Open 52.75", xy=(3.25, 52.75), xytext=(3.6, 52.9), arrowprops=dict(arrowstyle="->", color=cc["muted"]), **kw)
    ax.annotate("Close 51.17", xy=(3.25, 51.17), xytext=(3.6, 51.4), arrowprops=dict(arrowstyle="->", color=cc["muted"]), **kw)
    ax.text(3.2, 50.3, "Body: open to close\nWicks: the high and low", ha="center", color=cc["fg"], fontsize=9)
    ax.set_xlim(0.2, 4.6)
    ax.set_ylim(49.9, 53.5)
    ax.set_xticks([])
    ax.set_ylabel("Stock A price (US$)")


if __name__ == "__main__":
    for q in save_pair(draw, "05-reading-charts", "candle-anatomy", width=6.0, height=3.4):
        preview(q)
