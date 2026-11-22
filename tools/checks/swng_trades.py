"""The three setups of part 7 as code, so the lessons' worked trades come from the chart data."""
import math

from swng_lib import Bars, run_long, buy_stop_fill

ACCOUNT = 25_000
RISK = 0.01


def r2(x):
    return round(x + 1e-9, 2)


def floor2(x):
    return math.floor(x * 100 + 1e-9) / 100


def finish(entry, stop, exit_price, target=None):
    risk = entry - stop
    shares = math.floor(ACCOUNT * RISK / risk)
    pl = (exit_price - entry) * shares
    return dict(entry=entry, stop=stop, target=target, risk=risk, shares=shares, risk_usd=risk * shares,
                exit=exit_price, pl=pl, R=(exit_price - entry) / risk, cost=entry * shares)


def pullback(name, trigger_day):
    """Trend pullback long. trigger_day is the bar index of the trigger bar."""
    b = Bars(name)
    s50, e20, at = b.sma(50), b.ema(20), b.atr(14)
    t = trigger_day
    # rule 1: filter
    assert b.c[t] > s50[t] and s50[t] > s50[t - 10]
    # rule 2: pullback from the highest high of the last 20 bars
    hi_day = max(range(t - 19, t + 1), key=lambda i: b.h[i])
    H = b.h[hi_day]
    low_day = min(range(hi_day + 1, t + 1), key=lambda i: b.l[i])
    L = b.l[low_day]
    downs = sum(1 for i in range(hi_day + 1, low_day + 1) if b.c[i] < b.c[i - 1])
    assert downs >= 3
    assert L <= e20[low_day] and min(b.c[hi_day + 1 : t + 1]) > s50[t]
    # rule 3: trigger bar closes above the previous bar's high (first such bar since the low)
    assert b.c[t] > b.h[t - 1]
    assert all(b.c[i] <= b.h[i - 1] for i in range(low_day + 1, t))
    entry = r2(b.h[t] + 0.01)
    stop = floor2(L - 0.25 * at[t])
    risk = entry - stop
    assert H - entry >= 2 * risk - 1e-9, (H, entry, stop)
    fill = buy_stop_fill(b, t + 1, entry)
    assert fill == entry
    day, px, why = run_long(b, t + 1, stop, target=H, max_days=10)
    out = finish(entry, stop, px, H)
    out.update(H=H, L=L, atr=at[t], day=day, why=why, hi_day=hi_day, low_day=low_day, trigger=t,
               date_signal=b.t[t], date_entry=b.t[t + 1], date_exit=b.t[day], e20_at_low=e20[low_day], s50=s50[t],
               trig_high=b.h[t], stop_raw=L - 0.25 * at[t], bars=b)
    return out


def breakout(name, signal_day, base_start):
    """Base breakout long. signal_day is the first close above the pivot."""
    b = Bars(name)
    at, vs = b.atr(14), b.vsma(20)
    t = signal_day
    base = range(base_start, t)
    pivot = max(b.h[i] for i in base)
    low = min(b.l[i] for i in base)
    depth = (pivot - low) / pivot
    assert len(base) >= 20 and depth <= 0.15
    assert all(b.c[i] <= pivot for i in base)
    relvol = b.v[t] / vs[t - 1]
    assert b.c[t] > pivot and relvol >= 1.5 and b.c[t] >= (b.h[t] + b.l[t]) / 2
    a = at[t]
    entry = b.o[t + 1]
    assert entry <= pivot + 2 * a
    stop = floor2(pivot - a)
    risk = entry - stop
    target = r2(entry + 3 * risk)

    def rule(day):
        return "next_open" if b.c[day] < pivot else None

    day, px, why = run_long(b, t + 1, stop, target=target, max_days=15, exit_rule=rule)
    out = finish(entry, stop, px, target)
    out.update(pivot=pivot, low=low, depth=depth, nbase=len(base), relvol=relvol, atr=a, day=day, why=why, signal=t,
               date_signal=b.t[t], date_entry=b.t[t + 1], date_exit=b.t[day], bars=b, avgvol=vs[t - 1])
    return out


def rsi2_trade(name, signal_day):
    """RSI(2) mean reversion long. Enter at the next open."""
    b = Bars(name)
    s200, s5, r, at = b.sma(200), b.sma(5), b.rsi(2), b.atr(14)
    t = signal_day
    assert b.c[t] > s200[t] and r[t] < 10
    assert r[t - 1] >= 10  # first day under 10
    entry = b.o[t + 1]
    stop = floor2(entry - 2 * at[t])

    def rule(day):
        return b.c[day] if b.c[day] > s5[day] else None

    day, px, why = run_long(b, t + 1, stop, max_days=5, exit_rule=rule)
    out = finish(entry, stop, px)
    out.update(rsi=r[t], atr=at[t], s200=s200[t], day=day, why=why, signal=t, date_signal=b.t[t], date_entry=b.t[t + 1],
               date_exit=b.t[day], bars=b)
    return out
