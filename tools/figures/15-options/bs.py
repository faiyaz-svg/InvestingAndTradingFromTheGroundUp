"""Black-Scholes price and Greeks for European calls and puts, with a dividend yield.

Used by the checks, the figures and the In code boxes of part 15. Standard library only.

    from bs import price, greeks, implied_vol

    price(50, 50, 0.25, 0.04, 0.30)                 # call, no dividends
    price(50, 50, 0.25, 0.04, 0.30, kind="put")
    greeks(50, 50, 0.25, 0.04, 0.30)                # dict: delta, gamma, theta, vega, rho
    implied_vol(3.20, 50, 50, 0.25, 0.04)           # solve for sigma by bisection

Arguments, everywhere:
    S      stock price (US$)
    K      strike (US$)
    T      time to expiry in years (days / 365)
    r      risk-free rate, continuously compounded, as a decimal (0.04 = 4%)
    sigma  volatility per year, as a decimal (0.30 = 30%)
    q      continuous dividend yield, as a decimal (default 0)
    kind   "call" or "put"
"""
from __future__ import annotations

import math


def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def norm_pdf(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def d1_d2(S, K, T, r, sigma, q=0.0):
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    return d1, d1 - sigma * math.sqrt(T)


def price(S, K, T, r, sigma, q=0.0, kind="call"):
    """Black-Scholes value of a European option. At T <= 0 returns the intrinsic value."""
    if T <= 0:
        return max(S - K, 0.0) if kind == "call" else max(K - S, 0.0)
    d1, d2 = d1_d2(S, K, T, r, sigma, q)
    if kind == "call":
        return S * math.exp(-q * T) * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)
    return K * math.exp(-r * T) * norm_cdf(-d2) - S * math.exp(-q * T) * norm_cdf(-d1)


def greeks(S, K, T, r, sigma, q=0.0, kind="call"):
    """Dict with delta, gamma, theta (US$ per share per calendar day), vega (US$ per share per
    1 volatility point, i.e. sigma up by 0.01) and rho (US$ per share per 1 percentage point of r)."""
    d1, d2 = d1_d2(S, K, T, r, sigma, q)
    pdf = norm_pdf(d1)
    eq, er = math.exp(-q * T), math.exp(-r * T)
    gamma = eq * pdf / (S * sigma * math.sqrt(T))
    vega = S * eq * pdf * math.sqrt(T) / 100
    if kind == "call":
        delta = eq * norm_cdf(d1)
        theta = (-S * eq * pdf * sigma / (2 * math.sqrt(T)) - r * K * er * norm_cdf(d2) + q * S * eq * norm_cdf(d1)) / 365
        rho = K * T * er * norm_cdf(d2) / 100
    else:
        delta = eq * (norm_cdf(d1) - 1)
        theta = (-S * eq * pdf * sigma / (2 * math.sqrt(T)) + r * K * er * norm_cdf(-d2) - q * S * eq * norm_cdf(-d1)) / 365
        rho = -K * T * er * norm_cdf(-d2) / 100
    return {"delta": delta, "gamma": gamma, "theta": theta, "vega": vega, "rho": rho}


def implied_vol(mkt_price, S, K, T, r, q=0.0, kind="call", lo=1e-4, hi=5.0, tol=1e-10):
    """Volatility that makes price(...) equal mkt_price, found by bisection.
    Raises ValueError if the price is outside what any volatility in [lo, hi] can give."""
    f_lo = price(S, K, T, r, lo, q, kind) - mkt_price
    f_hi = price(S, K, T, r, hi, q, kind) - mkt_price
    if f_lo > 0 or f_hi < 0:
        raise ValueError("price outside the range reachable with this volatility range")
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if price(S, K, T, r, mid, q, kind) < mkt_price:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return 0.5 * (lo + hi)


def one_step_tree(S, K, u, d, r, T, kind="call"):
    """One-step binomial tree. Stock goes to S*u or S*d after time T. Returns
    (option value now, risk-neutral probability of the up move, shares of stock in the hedge = delta)."""
    p = (math.exp(r * T) - d) / (u - d)
    up = max(S * u - K, 0.0) if kind == "call" else max(K - S * u, 0.0)
    dn = max(S * d - K, 0.0) if kind == "call" else max(K - S * d, 0.0)
    value = math.exp(-r * T) * (p * up + (1 - p) * dn)
    delta = (up - dn) / (S * u - S * d)
    return value, p, delta
