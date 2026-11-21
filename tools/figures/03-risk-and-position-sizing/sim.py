"""Seeded Monte Carlo for lesson 8 (drawdowns and risk of ruin): one edge, three risk levels.

The edge: 45% winners that pay +2R, 55% losers that cost -1R (expectancy +0.35R).
Each path is 200 trades. The same random draws are used at every risk level.
"""
import numpy as np

P_WIN, WIN_R, LOSS_R = 0.45, 2.0, -1.0
TRADES, PATHS, SEED = 200, 10_000, 2026
LEVELS = (0.01, 0.02, 0.05)


def outcomes(paths=PATHS, trades=TRADES, seed=SEED, p=P_WIN):
    rng = np.random.default_rng(seed)
    return np.where(rng.random((paths, trades)) < p, WIN_R, LOSS_R)


def curves(r, f, start=10_000.0):
    """Equity after each trade for risk fraction f (rows are paths), starting at start."""
    eq = start * np.cumprod(1 + f * r, axis=1)
    return np.concatenate([np.full((r.shape[0], 1), start), eq], axis=1)


def max_drawdown(eq):
    peak = np.maximum.accumulate(eq, axis=1)
    return ((peak - eq) / peak).max(axis=1)


def stats(f):
    r = outcomes()
    eq = curves(r, f)
    dd = max_drawdown(eq)
    return {
        "median_final": float(np.median(eq[:, -1])),
        "median_maxdd": float(np.median(dd)),
        "p_dd30": float((dd >= 0.30).mean()),
        "p_half": float((eq.min(axis=1) <= 5_000).mean()),
        "p_below_start": float((eq[:, -1] < 10_000).mean()),
    }


if __name__ == "__main__":
    for f in LEVELS:
        print(f, stats(f))
