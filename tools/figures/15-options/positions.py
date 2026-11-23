"""Multi-leg positions on Stock A's made-up chain (lessons 9 to 14 of part 15).

Pure math, no plotting. Buys fill at the ask, sells at the bid. Per-share prices; a contract is 100 shares.

    from positions import Position, STOCK
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bs
import chain

S0, T0, R0 = chain.S, chain.T, chain.R
FEE = 0.65  # made-up commission, US$ per contract per leg, charged on opening and again on closing
CALLS = {r["K"]: r for r in chain.rows("call")}
PUTS = {r["K"]: r for r in chain.rows("put")}


class Leg:
    """qty > 0 buys at the ask, qty < 0 sells at the bid. T is the years to this leg's expiry."""

    def __init__(self, qty, kind, K, T=T0, price=None, iv=None):
        row = (CALLS if kind == "call" else PUTS).get(K)
        self.qty, self.kind, self.K, self.T = qty, kind, K, T
        if price is None:
            price = row["ask"] if qty > 0 else row["bid"]
        if iv is None:
            iv = row["iv"]
        self.price, self.iv = price, iv

    def payoff(self, S):
        return max(S - self.K, 0.0) if self.kind == "call" else max(self.K - S, 0.0)

    def value(self, S, T):
        return bs.price(S, self.K, T, R0, self.iv, kind=self.kind)


class Position:
    def __init__(self, legs, stock=0):
        self.legs, self.stock = legs, stock  # stock: shares held per 100-share lot (0 or 1 lot)

    @property
    def net(self):
        """Net debit per share (negative means a credit). Stock is bought at S0."""
        return sum(l.qty * l.price for l in self.legs) + self.stock * S0

    @property
    def contracts(self):
        return sum(abs(l.qty) for l in self.legs)

    def fees(self, rounds=2):
        return FEE * self.contracts * rounds

    def expiry(self, S):
        """Profit per share when every leg expires at stock price S."""
        return self.stock * S + sum(l.qty * l.payoff(S) for l in self.legs) - self.net

    def before(self, S, T):
        """Profit per share if the stock is at S now and every leg has T years left."""
        return self.stock * S + sum(l.qty * l.value(S, T) for l in self.legs) - self.net

    def greeks(self, S=S0):
        g = dict(delta=self.stock, gamma=0.0, theta=0.0, vega=0.0, rho=0.0)
        for l in self.legs:
            x = bs.greeks(S, l.K, l.T, R0, l.iv, kind=l.kind)
            for k in g:
                g[k] += l.qty * x[k]
        return g  # per share; multiply by 100 for a contract


def breakevens(f, lo=20.0, hi=90.0, n=70001):
    out, prev = [], None
    step = (hi - lo) / (n - 1)
    for i in range(n):
        s = lo + i * step
        v = f(s)
        if prev is not None and (prev < 0 <= v or prev > 0 >= v) and not (prev == 0):
            out.append(round(s - step / 2, 2))
        prev = v
    return out


COVERED_CALL = Position([Leg(-1, "call", 52.5)], stock=1)
CASH_PUT = Position([Leg(-1, "put", 47.5)])
BULL_CALL = Position([Leg(1, "call", 50.0), Leg(-1, "call", 55.0)])
BULL_PUT = Position([Leg(-1, "put", 50.0), Leg(1, "put", 45.0)])
STRADDLE = Position([Leg(1, "call", 50.0), Leg(1, "put", 50.0)])
STRANGLE = Position([Leg(1, "call", 52.5), Leg(1, "put", 47.5)])
CONDOR = Position([Leg(1, "put", 45.0), Leg(-1, "put", 47.5), Leg(-1, "call", 52.5), Leg(1, "call", 55.0)])
BUTTERFLY = Position([Leg(1, "call", 47.5), Leg(-2, "call", 50.0), Leg(1, "call", 52.5)])

# Calendar and diagonal: the near expiry (January 15, 2027, 56 days out) is not in the chain,
# so its quotes are made up: model price at 31% volatility, 0.05 either side of it.
T_NEAR = 56 / 365
T_LEFT = T0 - T_NEAR  # far leg's time left when the near leg expires
def _near(K):
    mid = bs.price(S0, K, T_NEAR, R0, 0.31)
    return round(mid - 0.025, 2), round(mid + 0.025, 2)
NEAR50_BID, NEAR50_ASK = _near(50.0)
NEAR525_BID, NEAR525_ASK = _near(52.5)
CALENDAR = Position([Leg(-1, "call", 50.0, T=T_NEAR, price=NEAR50_BID, iv=0.31), Leg(1, "call", 50.0)])
DIAGONAL = Position([Leg(-1, "call", 52.5, T=T_NEAR, price=NEAR525_BID, iv=0.31), Leg(1, "call", 50.0)])


def calendar_at_near_expiry(pos, S):
    """Profit per share when the near leg expires: the near leg at intrinsic value, the far leg at its
    model value with T_LEFT years to go (same volatility as at entry)."""
    near, far = pos.legs
    return near.qty * near.payoff(S) + far.qty * far.value(S, T_LEFT) - pos.net
