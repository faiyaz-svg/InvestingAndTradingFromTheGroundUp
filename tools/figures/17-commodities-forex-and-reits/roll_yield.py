"""A futures-based commodity fund in contango against the spot price (lesson 3). Made-up numbers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview

MONTHLY_CONTANGO = 0.0075  # next month's contract is 0.75% above the front month
SPOT_START = 80.0


def series(spot_end):
    months = list(range(13))
    spot = [SPOT_START * (spot_end / SPOT_START) ** (m / 12) for m in months]
    fund = [100 * (spot[m] / SPOT_START) * (1 / (1 + MONTHLY_CONTANGO)) ** m for m in months]
    return months, spot, fund


def draw(fig, ax, c):
    m, _, flat = series(80.0)
    _, _, up = series(84.0)
    ax.plot(m, [100] * 13, color=c["muted"], linestyle="--", linewidth=1)
    ax.plot(m, [100 * s / SPOT_START for s in [80.0] * 13], color=c["muted"], linewidth=0)
    ax.plot(m, [100 * (84.0 / 80.0) ** (k / 12) for k in m], color=c["blue"], label="Spot up 5% in the year")
    ax.plot(m, up, color=c["accent"], marker="o", markersize=3, label="Fund when spot is up 5%")
    ax.plot(m, flat, color=c["down"], marker="o", markersize=3, label="Fund when spot is flat")
    ax.text(12.1, 100.0, "Flat spot", color=c["muted"], fontsize=9, va="center")
    ax.set_xlabel("Months")
    ax.set_ylabel("Value (start = 100)")
    ax.set_xlim(0, 13.8)
    ax.legend(loc="lower left", fontsize=9)


if __name__ == "__main__":
    for q in save_pair(draw, "17-commodities-forex-and-reits", "roll-yield"):
        preview(q)
