"""Lesson 9: in-sample against out-of-sample Sharpe for 200 coin-flip rules."""
import numpy as np
import pandas as pd
from _common import FOLDER, load
from figstyle import preview, save_pair


def draw(fig, ax, c):
    ret = load("index-x-3y").pct_change().dropna()
    train, test = ret.iloc[:520], ret.iloc[520:]
    sh = lambda r: r.mean() / r.std() * np.sqrt(252)
    rng = np.random.default_rng(7)
    rules = pd.DataFrame(rng.choice([-1, 1], size=(200, len(ret))).T, index=ret.index)
    a = rules.iloc[:520].mul(train, axis=0).apply(sh)
    b = rules.iloc[520:].mul(test, axis=0).apply(sh)
    best = a.idxmax()
    ax.scatter(a, b, s=12, color=c["blue"], alpha=0.6)
    ax.scatter([a[best]], [b[best]], s=60, color=c["accent"], zorder=3)
    ax.annotate("best in-sample rule", (a[best], b[best]), xytext=(-110, 22), textcoords="offset points",
                color=c["accent"], fontsize=9, arrowprops=dict(arrowstyle="-", color=c["accent"]))
    ax.axhline(0, color=c["muted"], lw=0.8)
    ax.axvline(0, color=c["muted"], lw=0.8)
    ax.set_xlabel("Sharpe ratio in the first 520 days")
    ax.set_ylabel("Sharpe ratio in the last 261 days")


if __name__ == "__main__":
    for p in save_pair(draw, FOLDER, "best-of-many"):
        preview(p)
