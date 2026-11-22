"""A made-up oil futures curve before and after a supply shock (lesson 2)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview

MONTHS = ["M1", "M2", "M3", "M4", "M5", "M6"]
BEFORE = [70.00, 70.60, 71.10, 71.50, 71.80, 72.00]
AFTER = [78.00, 76.50, 75.20, 74.20, 73.50, 73.00]


def draw(fig, ax, c):
    x = range(6)
    ax.plot(x, BEFORE, color=c["up"], marker="o", label="Before: contango")
    ax.plot(x, AFTER, color=c["down"], marker="o", label="After the shock: backwardation")
    ax.set_xticks(list(x))
    ax.set_xticklabels(MONTHS)
    ax.set_xlabel("Contract month (M1 is the front month)")
    ax.set_ylabel("Price (US$ per barrel, made up)")
    ax.set_ylim(68, 80)
    ax.legend(loc="upper right", fontsize=9)


if __name__ == "__main__":
    for q in save_pair(draw, "17-commodities-forex-and-reits", "oil-curve-shift"):
        preview(q)
