"""A stylised business cycle (lesson 9). An illustration, not data."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview


def draw(fig, ax, c):
    t = np.linspace(0, 1, 400)
    y = np.sin(2 * np.pi * t) * 1.0 + 0.9 * t
    ax.plot(t, y, color=c["accent"])
    ax.axhline(0.45, color=c["muted"], lw=1, ls="--")
    labels = [(0.06, "Early\nexpansion"), (0.24, "Late\nexpansion"), (0.5, "Contraction\n(recession)"), (0.85, "Trough and\nrecovery")]
    for x, s in labels:
        ax.text(x, -1.45, s, ha="center", va="top", fontsize=9)
    ax.axvline(0.25, color=c["grid"], lw=1)
    ax.axvline(0.75, color=c["grid"], lw=1)
    ax.text(0.25, 2.1, "Peak", ha="center", fontsize=9, color=c["muted"])
    ax.text(0.75, 2.1 - 3.4, "Trough", ha="center", fontsize=9, color=c["muted"])
    ax.set_ylim(-1.5, 2.3)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylabel("Level of economic activity")
    ax.set_xlabel("Time (a stylised cycle, not data)", labelpad=36)
    ax.grid(False)


if __name__ == "__main__":
    for p in save_pair(draw, "11-macro-and-economic-data", "business-cycle", height=3.4):
        preview(p)
