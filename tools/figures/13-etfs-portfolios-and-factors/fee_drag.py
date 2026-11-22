"""Growth of US$10,000 at three fee levels (lesson 2)."""
import numpy as np
from _model import ns, save_pair, preview

F = "13-etfs-portfolios-and-factors"


def draw(fig, ax, c):
    yrs = np.arange(0, 31)
    for fee, col in [(0.0, c["fg"]), (0.001, c["accent"]), (0.01, c["blue"]), (0.0225, c["down"])]:
        y = ns["fee_value"](10000, 0.07, fee, yrs)
        lab = "No fee" if fee == 0 else f"Fee {100 * fee:.2f}%"
        ax.plot(yrs, y, color=col, linewidth=1.6 if fee == 0 else 2.0, linestyle="--" if fee == 0 else "-")
        ax.plot([], [], color=col, linestyle="--" if fee == 0 else "-", label=lab + r": US\$" + f"{y[-1]:,.0f}")
    ax.set_xlabel("Years")
    ax.set_ylabel(r"Value of US\$10,000 (US\$)")
    ax.legend(loc="upper left", fontsize=8.5)
    ax.set_xlim(0, 30)


if __name__ == "__main__":
    for p in save_pair(draw, F, "fee-drag", width=6.0, height=3.6):
        preview(p)
