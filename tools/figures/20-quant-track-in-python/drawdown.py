"""Lesson 10: the drawdown curve of stock-04."""
from _common import FOLDER, load, fmt_dates
from figstyle import preview, save_pair


def draw(fig, ax, c):
    r = load("stock-04").pct_change().dropna()
    eq = (1 + r).cumprod()
    dd = (eq / eq.cummax() - 1) * 100
    ax.fill_between(dd.index, dd, 0, color=c["down"], alpha=0.35)
    ax.plot(dd.index, dd, color=c["down"], lw=1.2)
    ax.annotate(f"Maximum drawdown {dd.min():.1f}%", (dd.idxmin(), dd.min()), xytext=(25, -4),
                textcoords="offset points", color=c["fg"], fontsize=9)
    ax.set_ylabel("Drawdown from the previous peak (%)")
    fmt_dates(ax)


if __name__ == "__main__":
    for p in save_pair(draw, FOLDER, "drawdown"):
        preview(p)
