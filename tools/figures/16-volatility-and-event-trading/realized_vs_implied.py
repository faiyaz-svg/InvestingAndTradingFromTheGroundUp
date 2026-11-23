"""Realized and implied volatility of a made-up stock over one year (lesson 1)."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import numpy as np
from figstyle import save_pair, preview
import vol_data


def draw(fig, ax, c):
    d = vol_data.stock_year()
    x = np.arange(len(d["iv"]))
    ax.plot(x, d["iv"], color=c["accent"], label="Implied volatility (made up)")
    ax.plot(x, d["rv"], color=c["blue"], label="Realized volatility, 21 days")
    ax.set_xlabel("Trading day")
    ax.set_ylabel("Volatility (% per year)")
    ax.set_xlim(21, len(x) - 1)
    ax.legend(loc="upper left")


if __name__ == "__main__":
    for q in save_pair(draw, "16-volatility-and-event-trading", "realized-vs-implied"):
        preview(q)
    print(vol_data.stats())
