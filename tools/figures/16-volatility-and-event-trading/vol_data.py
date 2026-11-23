"""Made-up data and numbers shared by the part 16 figures and checks."""
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "15-options"))
import bs  # noqa: E402,F401


def stock_year(seed=1611, n=252):
    """A made-up stock year: daily returns with changing volatility, 30-day realized
    volatility, and a made-up implied volatility that sits a little above what follows.
    Returns dict of arrays (annualized volatility in percent)."""
    rng = np.random.default_rng(seed)
    log_sig = np.zeros(n + 21)
    mu = np.log(0.24)
    log_sig[0] = mu
    for t in range(1, n + 21):
        log_sig[t] = mu + 0.97 * (log_sig[t - 1] - mu) + 0.09 * rng.standard_normal()
    sig = np.exp(log_sig)  # annualized, decimal
    # a shock period in the middle of the year
    sig[120:150] *= np.linspace(1.0, 1.9, 30)
    sig[150:175] *= np.linspace(1.9, 1.0, 25)
    ret = sig / np.sqrt(252) * rng.standard_normal(n + 21)
    # realized: 21-day close-to-close, annualized, measured over the days ending at t
    rv = np.full(n, np.nan)
    for t in range(21, n):
        rv[t] = ret[t - 20:t + 1].std(ddof=1) * np.sqrt(252) * 100
    # implied: the market's guess at the next 21 days = 1.18 x a blend of today's level and the long run
    iv = 100 * 1.18 * (0.55 * sig[:n] + 0.45 * 0.24)
    iv = np.convolve(iv, np.ones(3) / 3, mode="same")
    fwd = np.full(n, np.nan)  # realized over the next 21 days
    for t in range(n - 21):
        fwd[t] = ret[t + 1:t + 22].std(ddof=1) * np.sqrt(252) * 100
    return {"ret": ret[:n], "rv": rv, "iv": iv, "fwd": fwd}


def stats():
    d = stock_year()
    ok = ~np.isnan(d["fwd"])
    return {
        "iv_mean": float(d["iv"][ok].mean()),
        "fwd_mean": float(d["fwd"][ok].mean()),
        "share_iv_above": float((d["iv"][ok] > d["fwd"][ok]).mean()),
    }


CONTANGO = {"spot": 14.5, "futures": [15.8, 16.7, 17.3, 17.8, 18.1, 18.4, 18.6]}
BACKWARDATION = {"spot": 31.0, "futures": [28.9, 27.2, 26.0, 25.1, 24.5, 24.0, 23.6]}
