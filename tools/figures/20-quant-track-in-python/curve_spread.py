"""Lesson 5: 2-year to 10-year yield spread from the made-up Treasury file."""
import pandas as pd
from _common import DATA, FOLDER, fmt_dates
from figstyle import preview, save_pair


def draw(fig, ax, c):
    ty = pd.read_csv(DATA / "treasury-yields.csv", parse_dates=["Date"], date_format="%m/%d/%Y", index_col="Date").sort_index()
    s = ty["10 Yr"] - ty["2 Yr"]
    ax.plot(s.index, s, color=c["accent"])
    ax.axhline(0, color=c["muted"], lw=0.8)
    ax.fill_between(s.index, s, 0, where=s < 0, color=c["down"], alpha=0.3)
    ax.set_ylabel("10-year minus 2-year yield (percentage points)")
    fmt_dates(ax)


if __name__ == "__main__":
    for p in save_pair(draw, FOLDER, "curve-spread"):
        preview(p)
