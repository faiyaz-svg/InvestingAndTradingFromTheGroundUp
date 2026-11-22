"""Contango and backwardation: futures price against expiry month (lesson 5). Made-up numbers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview

MONTHS = ["Spot", "Sep", "Dec", "Mar", "Jun", "Sep"]
CONTANGO = [100.0, 100.8, 101.6, 102.3, 103.0, 103.6]
BACKW = [100.0, 99.2, 98.5, 97.9, 97.4, 97.0]


def draw(fig, ax, c):
    x = range(len(MONTHS))
    ax.plot(x, CONTANGO, color=c["up"], marker="o", label="Contango: later contracts cost more")
    ax.plot(x, BACKW, color=c["down"], marker="o", label="Backwardation: later contracts cost less")
    ax.axhline(100.0, color=c["muted"], linestyle="--", linewidth=1)
    ax.text(5.05, 100.2, "Spot", color=c["muted"], fontsize=9, ha="right", va="bottom")
    ax.set_xticks(list(x))
    ax.set_xticklabels(MONTHS)
    ax.set_xlabel("Expiry month of the contract")
    ax.set_ylabel("Price (made-up units)")
    ax.set_ylim(96, 105)
    ax.legend(loc="upper center", fontsize=9)


if __name__ == "__main__":
    for q in save_pair(draw, "14-futures", "contango-backwardation"):
        preview(q)
