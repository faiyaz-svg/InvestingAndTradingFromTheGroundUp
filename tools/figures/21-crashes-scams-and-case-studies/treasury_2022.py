"""US Treasury yields through 2022 (lesson 7). Source: US Treasury daily par yield curve rates, home.treasury.gov."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pandas as pd
from figstyle import save_pair, preview

D = pd.read_csv(Path(__file__).parents[1] / "12-bonds-and-the-yield-curve" / "treasury_2021_2026.csv", parse_dates=["Date"])
D = D[(D["Date"] >= "2021-12-31") & (D["Date"] <= "2022-12-30")]


def draw(fig, ax, c):
    ax.plot(D["Date"], D["3 Mo"], color=c["muted"], linewidth=1.6, label="3-month")
    ax.plot(D["Date"], D["2 Yr"], color=c["accent"], linewidth=1.6, label="2-year")
    ax.plot(D["Date"], D["10 Yr"], color=c["blue"], linewidth=1.6, label="10-year")
    ax.set_ylabel("Yield (%)")
    ax.set_ylim(0, 5.2)
    ax.legend(loc="upper left", fontsize=9)
    import matplotlib.dates as mdates
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))


if __name__ == "__main__":
    for p in save_pair(draw, "21-crashes-scams-and-case-studies", "treasury-2022", width=6.0, height=3.4):
        preview(p)
