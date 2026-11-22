"""US Treasury par yield curve on four dates (lesson 3). Source: US Treasury."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pandas as pd
from figstyle import save_pair, preview

D = pd.read_csv(Path(__file__).with_name("treasury_par_curves.csv"))
COLS = ["3 Mo", "6 Mo", "1 Yr", "2 Yr", "3 Yr", "5 Yr", "7 Yr", "10 Yr", "20 Yr", "30 Yr"]
LABELS = ["3m", "6m", "1y", "2y", "3y", "5y", "7y", "10y", "20y", "30y"]


def draw(fig, ax, c):
    colors = [c["muted"], c["down"], c["blue"], c["accent"]]
    for (_, row), col in zip(D.iterrows(), colors):
        ax.plot(range(len(COLS)), [row[k] for k in COLS], color=col, marker="o", markersize=3.5, label=row["Date"])
    ax.set_xticks(range(len(COLS)))
    ax.set_xticklabels(LABELS)
    ax.set_xlabel("Time to maturity")
    ax.set_ylabel("Par yield (%)")
    ax.legend(loc="upper left", fontsize=9, ncol=2)
    ax.set_ylim(0, 7)


if __name__ == "__main__":
    for p in save_pair(draw, "12-bonds-and-the-yield-curve", "par-curves", width=6.0, height=3.6):
        preview(p)
