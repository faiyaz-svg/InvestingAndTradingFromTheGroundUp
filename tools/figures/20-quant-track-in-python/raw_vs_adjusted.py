"""Lesson 1: raw and adjusted close of the made-up stock with a 2-for-1 split."""
from _common import FOLDER, load, fmt_dates
from figstyle import preview, save_pair


def draw(fig, ax, c):
    df = load("stock-split-3y", None)
    day = df.index[df["split"] == 2][0]
    ax.plot(df.index, df["close"], color=c["down"], label="Close as traded (raw)")
    ax.plot(df.index, df["adj_close"], color=c["accent"], label="Adjusted close")
    ax.axvline(day, color=c["muted"], lw=0.8, ls="--")
    ax.text(day, df["close"].max() * 0.62, " 2-for-1 split, 2024-06-03", color=c["muted"], fontsize=9, va="top")
    ax.set_ylabel("Price (US$)")
    fmt_dates(ax)
    ax.legend(loc="upper right")


if __name__ == "__main__":
    for p in save_pair(draw, FOLDER, "raw-vs-adjusted"):
        preview(p)
