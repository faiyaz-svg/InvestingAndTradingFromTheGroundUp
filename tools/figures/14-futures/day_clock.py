"""One CME Globex trading day for equity index futures, in ET (lesson 6)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview

# Hours from 6 p.m. ET (0) to 6 p.m. ET the next day (24).
def h(hour, minute=0):
    return (hour - 18) % 24 + minute / 60


def draw(fig, ax, c):
    ax.barh(1, 23, left=0, color=c["blue"], height=0.45)
    ax.barh(1, 1, left=23, color=c["down"], height=0.45)
    ax.barh(0, 6.5, left=h(9, 30), color=c["accent"], height=0.45)
    ax.text(11.5, 1, "Globex session", ha="center", va="center", color=c["bg"], fontsize=9)
    ax.text(23.5, 1.4, "Break", ha="center", va="bottom", color=c["down"], fontsize=9)
    ax.text(h(9, 30) + 3.25, 0, "US stock regular session", ha="center", va="center", color=c["bg"], fontsize=8)
    ax.axvline(h(8, 30), color=c["muted"], linestyle="--", linewidth=1)
    ax.text(h(8, 30) - 0.1, -0.55, "8:30 a.m.\ndata", ha="right", va="top", color=c["muted"], fontsize=8)
    ticks = [0, 3, 6, 9, 12, 15, 18, 21, 24]
    ax.set_xticks(ticks)
    ax.set_xticklabels(["6 pm", "9 pm", "12 am", "3 am", "6 am", "9 am", "12 pm", "3 pm", "6 pm"], fontsize=9)
    ax.set_yticks([])
    ax.set_xlim(0, 24)
    ax.set_ylim(-1.1, 1.9)
    ax.grid(False)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("Eastern Time")


if __name__ == "__main__":
    for q in save_pair(draw, "14-futures", "day-clock", height=2.6):
        preview(q)
