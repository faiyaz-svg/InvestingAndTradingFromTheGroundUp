"""10-year minus 2-year and 10-year minus 3-month Treasury spreads, 2021 to 2026 (lesson 3). Source: US Treasury."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pandas as pd
from figstyle import save_pair, preview

D = pd.read_csv(Path(__file__).with_name("treasury_2021_2026.csv"), parse_dates=["Date"])
D["s210"] = D["10 Yr"] - D["2 Yr"]
D["s310"] = D["10 Yr"] - D["3 Mo"]


def draw(fig, ax, c):
    ax.plot(D["Date"], D["s210"], color=c["accent"], linewidth=1.4, label="10-year minus 2-year")
    ax.plot(D["Date"], D["s310"], color=c["blue"], linewidth=1.4, label="10-year minus 3-month")
    ax.axhline(0, color=c["fg"], linewidth=1)
    ax.fill_between(D["Date"], D["s310"], 0, where=D["s310"] < 0, color=c["down"], alpha=0.25)
    ax.set_ylabel("Spread (percentage points)")
    ax.legend(loc="upper left", fontsize=9)


if __name__ == "__main__":
    for p in save_pair(draw, "12-bonds-and-the-yield-curve", "spread-history", width=6.0, height=3.4):
        preview(p)
