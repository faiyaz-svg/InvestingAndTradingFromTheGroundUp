"""Made-up market-implied odds of a rate cut before and after a hot CPI print (lesson 8)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview

LOW, HIGH = 3.50, 3.75
EFFR = (LOW + HIGH) / 2


def odds(price):
    return (EFFR - (100 - price)) / 0.25


def draw(fig, ax, c):
    vals = [100 * odds(96.55), 100 * odds(96.45)]
    bars = ax.bar(["Before the CPI release\n(futures at 96.55)", "After the CPI release\n(futures at 96.45)"], vals, color=[c["blue"], c["down"]], width=0.5)
    for b in bars:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 2, f"{b.get_height():.0f}%", ha="center")
    ax.set_ylim(0, 100)
    ax.set_ylabel("Implied odds of a 25 bp cut (%)")
    ax.grid(axis="x", visible=False)


if __name__ == "__main__":
    for p in save_pair(draw, "11-macro-and-economic-data", "odds-before-after", height=3.2):
        preview(p)
