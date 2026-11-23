"""Distribution of the sum of two dice, with a bid of 6 and an ask of 8 marked."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview


def draw(fig, ax, c):
    sums = list(range(2, 13))
    ways = [6 - abs(s - 7) for s in sums]
    ax.bar(sums, [w / 36 for w in ways], color=c["blue"], width=0.7)
    ax.axvline(7, color=c["accent"], linestyle="--", linewidth=1.2)
    ax.annotate("Fair value 7", (7, 0.17), xytext=(7.2, 0.176), fontsize=9, color=c["accent"])
    ax.annotate("Bid 6", (6, 0.14), xytext=(4.6, 0.185), fontsize=9, color=c["down"])
    ax.annotate("Ask 8", (8, 0.14), xytext=(8.3, 0.185), fontsize=9, color=c["up"])
    ax.axvline(6, color=c["down"], linewidth=1)
    ax.axvline(8, color=c["up"], linewidth=1)
    ax.set_xticks(sums)
    ax.set_xlabel("Sum of two dice")
    ax.set_ylabel("Probability")
    ax.set_ylim(0, 0.2)


if __name__ == "__main__":
    for q in save_pair(draw, "22-careers-interviews-and-ai", "two-dice"):
        preview(q)
