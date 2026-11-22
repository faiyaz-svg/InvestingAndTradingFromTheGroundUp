"""Efficient frontier of three made-up assets, with the tangency portfolio (lesson 8)."""
import numpy as np
from _model import ns, save_pair, preview

F = "13-etfs-portfolios-and-factors"
MU, SD, COV, RF = ns["MU"], ns["SD"], ns["COV"], ns["RF"]


def draw(fig, ax, c):
    rng = np.random.default_rng(5)
    w = rng.dirichlet(np.ones(3), 4000)
    mu = w @ MU
    sd = np.sqrt(np.einsum("ij,jk,ik->i", w, COV, w))
    ax.scatter(100 * sd, 100 * mu, s=4, color=c["muted"], alpha=0.35, linewidths=0, label="Random long-only mixes")
    # frontier: for each target return, minimum-variance long-only mix by brute force on a fine grid
    g = np.linspace(0, 1, 201)
    best = {}
    for a in g:
        for b in g:
            if a + b <= 1:
                x = np.array([a, b, 1 - a - b])
                m, s = x @ MU, float(np.sqrt(x @ COV @ x))
                k = round(m, 4)
                if k not in best or s < best[k]:
                    best[k] = s
    ks = sorted(best)
    mvi = int(np.argmin([best[k] for k in ks]))
    up = [(best[k], k) for k in ks[mvi:]]
    ax.plot([100 * s for s, _ in up], [100 * k for _, k in up], color=c["accent"], label="Efficient frontier")
    t = ns["tangency"]()
    tm, ts = t @ MU, float(np.sqrt(t @ COV @ t))
    xs = np.linspace(0, 0.12, 20)
    ax.plot(100 * xs, 100 * (RF + (tm - RF) / ts * xs), color=c["blue"], linestyle="--", label="Capital allocation line")
    ax.plot([100 * ts], [100 * tm], "o", color=c["blue"])
    ax.annotate(f"Tangency: {100 * tm:.2f}% return,\n{100 * ts:.2f}% risk", (100 * ts, 100 * tm), textcoords="offset points", xytext=(10, -26), fontsize=8.5)
    for i, n in enumerate(["Asset A", "Asset B", "Asset C"]):
        ax.plot([100 * SD[i]], [100 * MU[i]], "s", color=c["teal"])
        ax.annotate(n, (100 * SD[i], 100 * MU[i]), textcoords="offset points", xytext=(6, 4), fontsize=8.5)
    ax.plot([0], [100 * RF], "o", color=c["fg"])
    ax.annotate("Risk-free 2%", (0, 100 * RF), textcoords="offset points", xytext=(6, -12), fontsize=8.5)
    ax.set_xlabel("Risk: standard deviation (% a year)")
    ax.set_ylabel("Expected return (% a year)")
    ax.set_xlim(0, 18)
    ax.set_ylim(1, 9)
    ax.legend(loc="lower right", fontsize=8)


if __name__ == "__main__":
    for p in save_pair(draw, F, "frontier", width=6.0, height=3.8):
        preview(p)
