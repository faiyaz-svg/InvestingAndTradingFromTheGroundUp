"""Lesson 8: the same rule with and without lookahead, on the made-up index."""
from _common import FOLDER, load, fmt_dates
from figstyle import preview, save_pair


def draw(fig, ax, c):
    ret = load("index-x-3y").pct_change().fillna(0)
    sig = (ret > 0).astype(int)
    cheat = (1 + sig * ret).cumprod()
    honest = (1 + sig.shift(1).fillna(0) * ret).cumprod()
    ax.plot(cheat.index, cheat, color=c["down"], label="Position uses the same day's return (lookahead)")
    ax.plot(honest.index, honest, color=c["accent"], label="Position uses the previous day's signal")
    ax.set_yscale("log")
    ax.set_ylabel("Growth of 1 (log scale)")
    fmt_dates(ax)
    ax.legend(loc="upper left")


if __name__ == "__main__":
    for p in save_pair(draw, FOLDER, "lookahead"):
        preview(p)
