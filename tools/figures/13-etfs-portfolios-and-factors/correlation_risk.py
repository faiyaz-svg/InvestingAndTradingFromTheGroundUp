"""Volatility of a stock-bond mix against the stock weight, for three correlations (lesson 6)."""
import numpy as np
from _model import ns, save_pair, preview

F = "13-etfs-portfolios-and-factors"


def draw(fig, ax, c):
    w = np.linspace(0, 1, 101)
    for rho, col in [(1.0, c["down"]), (0.2, c["accent"]), (-0.3, c["teal"])]:
        sd = [100 * ns["port_sd"](x, 0.16, 0.06, rho) for x in w]
        ax.plot(100 * w, sd, color=col, label=f"Correlation {rho:+.1f}")
    v = 100 * ns["port_sd"](0.6, 0.16, 0.06, 0.2)
    ax.plot([60], [v], "o", color=c["fg"])
    ax.annotate(f"60/40, correlation 0.2: {v:.2f}%", (60, v), textcoords="offset points", xytext=(-14, 14), ha="right", fontsize=8.5)
    ax.set_xlabel("Weight in stocks (%)")
    ax.set_ylabel("Portfolio volatility (% a year)")
    ax.legend(loc="upper left", fontsize=8.5)
    ax.set_xlim(0, 100)


if __name__ == "__main__":
    for p in save_pair(draw, F, "correlation-risk", width=6.0, height=3.6):
        preview(p)
