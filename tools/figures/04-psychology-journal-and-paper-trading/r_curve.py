"""R result of 20 made-up trades and their running total (lesson 5)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import numpy as np
from figstyle import save_pair, preview

from build_journal import TRADES  # noqa: E402


def draw(fig, ax, c):
    r = np.array([t[1] for t in TRADES])
    n = np.arange(1, len(r) + 1)
    ax.bar(n, r, color=[c["up"] if v > 0 else c["down"] for v in r], width=0.7)
    ax.plot(n, np.cumsum(r), color=c["accent"], marker="o", ms=3, label="Running total (R)")
    off = [i + 1 for i, t in enumerate(TRADES) if not t[2]]
    ax.plot(off, [-3.0] * len(off), "x", color=c["fg"], label="Broke the plan")
    ax.axhline(0, color=c["muted"], lw=1)
    ax.set_xticks(n)
    ax.set_xlabel("Trade number")
    ax.set_ylabel("Result (R)")
    ax.legend(loc="upper left")


if __name__ == "__main__":
    for q in save_pair(draw, "04-psychology-journal-and-paper-trading", "r-results", width=6.4, height=3.8):
        preview(q)
