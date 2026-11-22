"""Indicators and a small trade simulator for the part 7 checks (the same maths as docs/javascripts/charts.js)."""
import json
import math

from _lib import ROOT

CH = ROOT / "docs" / "assets" / "charts" / "07-swing-trading"


class Bars:
    def __init__(self, name):
        rows = json.loads((CH / f"{name}.json").read_text(encoding="utf-8"))["bars"]
        self.t = [r[0] for r in rows]
        self.o = [r[1] for r in rows]
        self.h = [r[2] for r in rows]
        self.l = [r[3] for r in rows]
        self.c = [r[4] for r in rows]
        self.v = [r[5] for r in rows]
        self.n = len(rows)

    def i(self, date):
        return self.t.index(date)

    def sma(self, n):
        return sma(self.c, n)

    def ema(self, n):
        return ema(self.c, n)

    def rsi(self, n):
        return rsi(self.c, n)

    def atr(self, n=14):
        return atr(self.h, self.l, self.c, n)

    def vsma(self, n):
        return sma(self.v, n)


def sma(x, n):
    return [None if i < n - 1 else sum(x[i - n + 1 : i + 1]) / n for i in range(len(x))]


def ema(x, n):
    out = [None] * len(x)
    k = 2 / (n + 1)
    prev = sum(x[:n]) / n
    out[n - 1] = prev
    for i in range(n, len(x)):
        prev = x[i] * k + prev * (1 - k)
        out[i] = prev
    return out


def wilder(x, n, start):
    out = [None] * len(x)
    first = start + n - 1
    prev = sum(x[start : first + 1]) / n
    out[first] = prev
    for i in range(first + 1, len(x)):
        prev = (prev * (n - 1) + x[i]) / n
        out[i] = prev
    return out


def rsi(c, n):
    g = [0.0] + [max(c[i] - c[i - 1], 0) for i in range(1, len(c))]
    lo = [0.0] + [max(c[i - 1] - c[i], 0) for i in range(1, len(c))]
    ag, al = wilder(g, n, 1), wilder(lo, n, 1)
    out = []
    for a, b in zip(ag, al):
        if a is None:
            out.append(None)
        elif b == 0:
            out.append(50.0 if a == 0 else 100.0)
        else:
            out.append(100 - 100 / (1 + a / b))
    return out


def atr(h, lo, c, n=14):
    tr = [h[0] - lo[0]] + [max(h[i] - lo[i], abs(h[i] - c[i - 1]), abs(lo[i] - c[i - 1])) for i in range(1, len(c))]
    return wilder(tr, n, 0)


def buy_stop_fill(b, day, price):
    """A buy stop resting on `day`: the fill price, or None if it does not trigger."""
    if b.o[day] >= price:
        return b.o[day]
    if b.h[day] >= price:
        return price
    return None


def run_long(b, entry_day, stop, target=None, max_days=None, exit_rule=None):
    """Follow a long trade that filled on entry_day. In a bar that touches both stop and target the stop counts first.

    exit_rule(day) returns None, a price (exit at that close) or "next_open".
    Returns (day, price, reason).
    """
    day = entry_day
    pending = False
    while day < b.n:
        if pending:
            return day, b.o[day], "rule at open"
        if day > entry_day and b.o[day] <= stop:
            return day, b.o[day], "stop gap"
        if b.l[day] <= stop:
            return day, stop, "stop"
        if target is not None:
            if day > entry_day and b.o[day] >= target:
                return day, b.o[day], "target gap"
            if b.h[day] >= target:
                return day, target, "target"
        if max_days is not None and day - entry_day >= max_days:
            return day, b.c[day], "time"
        if exit_rule is not None:
            r = exit_rule(day)
            if r == "next_open":
                pending = True
            elif r is not None:
                return day, r, "rule at close"
        day += 1
    return b.n - 1, b.c[-1], "end of data"


def shares_for(account, risk_frac, entry, stop):
    return math.floor(account * risk_frac / (entry - stop))
