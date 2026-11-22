"""Sessions on a 24-hour Eastern Time clock (lesson 5)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview

ROWS = [
    ("Asian range (commonly 8 p.m. to midnight)", 20, 24, "blue"),
    ("London kill zone (2 to 5 a.m.)", 2, 5, "teal"),
    ("New York kill zone (7 to 10 a.m.)", 7, 10, "accent"),
    ("London close (10 a.m. to noon)", 10, 12, "orange"),
    ("US regular session (9:30 a.m. to 4 p.m.)", 9.5, 16, "up"),
]


def draw(fig, ax, cc):
    ax.grid(axis="x")
    for i, (label, a, b, col) in enumerate(ROWS):
        y = len(ROWS) - 1 - i
        ax.barh(y, b - a, left=a, height=0.3, color=cc[col])
        ax.text(0.2, y + 0.17, label, fontsize=9, color=cc["fg"], va="bottom")
    ax.set_xlim(0, 24)
    ax.set_ylim(-0.6, len(ROWS) - 0.1)
    ax.set_yticks([])
    ax.set_xticks(range(0, 25, 3))
    ax.set_xticklabels(["12a", "3a", "6a", "9a", "12p", "3p", "6p", "9p", "12a"])
    ax.set_xlabel("Hour of the day, Eastern Time (Toronto)")
    ax.spines["left"].set_visible(False)


if __name__ == "__main__":
    for q in save_pair(draw, "06-ict-and-smart-money-tested", "sessions-et", width=6.4, height=3.6):
        preview(q)
