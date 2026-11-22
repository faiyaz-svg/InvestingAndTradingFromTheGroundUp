"""A trading day's scheduled releases in Eastern Time (lesson 7). Times from the agencies' schedules, as of 2026."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview

EVENTS = [
    (8.5, "8:30  CPI, PPI, payrolls, GDP,\nretail sales, jobless claims", 4),
    (9.5, "9:30  US stock market opens", 3),
    (9.75, "9:45  Bank of Canada decision", 2),
    (10.0, "10:00  ISM PMIs, JOLTS", 1),
    (14.0, "2:00 p.m.  FOMC statement", 1),
    (16.0, "4:00 p.m.  US stock market closes", 3),
]


def draw(fig, ax, c):
    ax.set_xlim(7.5, 17)
    ax.set_ylim(-0.6, 4.6)
    ax.axhline(0, color=c["muted"], lw=1.5)
    for t, label, lvl in EVENTS:
        y = 0.6 + lvl * 0.85
        col = c["accent"] if "9:30" not in label and "4:00" not in label else c["muted"]
        ax.plot([t, t], [0, y], color=col, lw=1.4)
        ax.plot(t, 0, "o", color=col)
        ax.text(t + 0.07, y, label, va="center", ha="left", fontsize=9, color=c["fg"])
    ticks = list(range(8, 17))
    ax.tick_params(axis='x', labelsize=8)
    ax.set_xticks(ticks, [f"{h if h <= 12 else h - 12}{' a.m.' if h < 12 else ' p.m.'}" for h in ticks])
    ax.set_yticks([])
    ax.grid(axis="y", visible=False)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("Eastern Time")


if __name__ == "__main__":
    for p in save_pair(draw, "11-macro-and-economic-data", "release-clock", width=6.5, height=3.4):
        preview(p)
