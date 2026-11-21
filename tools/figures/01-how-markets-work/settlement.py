"""T+1 settlement on a calendar strip (lesson 7)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview
from matplotlib.patches import FancyBboxPatch

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon"]


def draw(fig, ax, c):
    ax.set_xlim(-0.5, 7.5)
    ax.set_ylim(0, 3.4)
    ax.axis("off")
    ax.grid(False)
    for i, d in enumerate(DAYS):
        weekend = d in ("Sat", "Sun")
        ax.add_patch(FancyBboxPatch((i - 0.4, 2.3), 0.8, 0.7, boxstyle="round,pad=0.02", fc=c["grid"] if weekend else c["bg"], ec=c["muted"]))
        ax.text(i, 2.65, d, ha="center", va="center", color=c["muted"] if weekend else c["fg"])
    ax.text(2.6, 1.7, "Trade (T)", ha="center", color=c["accent"])
    ax.annotate("", xy=(4, 2.25), xytext=(3, 1.85), arrowprops=dict(arrowstyle="->", color=c["accent"]))
    ax.text(4.5, 1.7, "Settles (T+1)", ha="center", color=c["accent"])
    ax.text(4.5, 0.9, "Trade (T)", ha="center", color=c["blue"])
    ax.annotate("", xy=(7, 2.25), xytext=(4.9, 0.95), arrowprops=dict(arrowstyle="->", color=c["blue"], connectionstyle="arc3,rad=-0.25"))
    ax.text(7, 1.6, "Settles (T+1)", ha="center", color=c["blue"])
    ax.text(3.5, 0.2, "A Thursday trade settles Friday. A Friday trade settles the next Monday.", ha="center", color=c["fg"], fontsize=10)


if __name__ == "__main__":
    for p in save_pair(draw, "01-how-markets-work", "settlement-t1", width=7.0, height=2.8):
        preview(p)
