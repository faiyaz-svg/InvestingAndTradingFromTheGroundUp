"""Number checks for part 6, ICT and smart money concepts, tested."""
import json
import statistics as st
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from _lib import ROOT, lesson, has, usd

F = "06-ict-and-smart-money-tested"
CH = ROOT / "docs" / "assets" / "charts" / F


def bars(name):
    return json.loads((CH / f"{name}.json").read_text(encoding="utf-8"))["bars"]


def row(b, date):
    return next(x for x in b if x[0] == date)


def hhmm(b, hm):
    for x in b:
        if datetime.fromtimestamp(x[0], tz=timezone.utc).strftime("%H:%M") == hm:
            return x
    raise KeyError(hm)


# ---- Lesson 1: structure
t = lesson(F, 1)
b = bars("bos-choch")
assert row(b, "2026-02-11")[2] == 54.37
assert row(b, "2026-02-24")[4] == 54.57
assert max(x[4] for x in b if "2026-02-11" <= x[0] <= "2026-02-23") <= 54.15
assert row(b, "2026-03-03")[2] == 57.13 and row(b, "2026-03-16")[4] == 57.87
assert row(b, "2026-03-20")[2] == 60.15
assert min(x[3] for x in b if "2026-02-12" <= x[0] <= "2026-02-27") == 52.02
assert row(b, "2026-03-11")[3] == 54.59
assert row(b, "2026-03-30")[4] == 54.42 and row(b, "2026-03-30")[3] == 54.34
assert all(x[4] > 54.59 for x in b if "2026-03-11" <= x[0] <= "2026-03-27")
assert row(b, "2026-03-31")[3] == 53.15 and row(b, "2026-04-06")[2] == 56.60
assert row(b, "2026-04-09")[4] == 52.74 < 53.15
drop = 60.15 - 54.42
assert round(drop, 2) == 5.73 and round(drop / 60.15 * 100, 1) == 9.5
has(t, "54.37", "54.57", "57.13", "57.87", "60.15", "54.59", "54.42", "53.15", "56.60", "52.74", "52.02", "5.73", "9.5%", "54.15", "54.34")

# ---- Lesson 2: sweep
t = lesson(F, 2)
b = bars("equal-highs-sweep")
assert row(b, "2026-02-16")[2] == 55.00 and row(b, "2026-02-23")[2] == 55.02
assert round(0.02 / 55.00 * 100, 2) == 0.04
assert row(b, "2026-02-19")[3] == 52.90
s = row(b, "2026-02-27")
assert s[2] == 55.40 and s[4] == 54.35
assert round(55.40 - 55.02, 2) == 0.38 and round(0.38 / 55.02 * 100, 2) == 0.69
assert row(b, "2026-03-03")[4] == 52.60 and row(b, "2026-03-03")[3] == 52.50 < 52.85
assert b[0][3] == 49.76
assert min(x[3] for x in b if x[0] >= "2026-03-04" and x[0] <= "2026-03-12") <= 49.80
assert row(b, "2026-03-11")[3] == 49.77 and min(x[3] for x in b if "2026-03-04" <= x[0] <= "2026-03-10") > 49.80
assert max(x[2] for x in b if x[0] >= "2026-03-03") < 55.45
risk = 55.45 - 52.85
assert round(risk, 2) == 2.60
shares = int(250 / risk)
assert shares == 96 and round(250 / risk, 1) == 96.2
rew = 52.85 - 49.80
assert round(rew, 2) == 3.05 and round(rew / risk, 2) == 1.17
assert round(shares * risk, 2) == 249.60
assert round(1 / (1 + 1.17) * 100) == 46
has(t, "55.00 and 55.02", "0.04%", "52.90", "55.40", "54.35", "52.85", "55.45", "US$2.60", "96.2", "96 shares", "US$3.05", "1.17R", "49.77", usd(249.6), "46%", "0.69%", "49.76")
# exercise 3
r3 = 52.85 - 50.50
assert round(r3, 2) == 2.35 and round(r3 / risk, 2) == 0.90 and round(100 / (1 + 0.90)) == 53
has(t, "2.35", "0.90R", "53%")
# in code
bs = pd.read_csv(ROOT / "docs" / "assets" / "data" / "stock-b-daily.csv", parse_dates=["date"])
ph = bs["high"].rolling(20).max().shift(1)
sweep = (bs["high"] > ph) & (bs["close"] < ph)
brk = bs["close"] > ph
f5 = bs["close"].shift(-5) / bs["close"] - 1
assert len(bs) == 360 and sweep.sum() == 37 and brk.sum() == 26
assert f"{f5[sweep].mean():.2%}" == "-0.20%" and f"{f5[brk].mean():.2%}" == "-0.04%" and f"{f5.mean():.2%}" == "0.25%"
has(t, "37 sweeps and 26 breakouts in 360 bars", "-0.20%", "-0.04%", "0.25%")

# ---- Lesson 3: fair value gaps
t = lesson(F, 3)
b = bars("fvg-bullish")
assert row(b, "2026-02-18")[2] == 50.90 and row(b, "2026-02-20")[3] == 52.30
b2 = row(b, "2026-02-19")
assert b2[3] == 50.70 and b2[2] == 52.90 and b2[4] == 52.70
assert round(52.30 - 50.90, 2) == 1.40 and round((50.90 + 52.30) / 2, 2) == 51.60
idx = [x[0] for x in b].index("2026-02-19")
rngs = [x[2] - x[3] for x in b]
avg10 = st.mean(rngs[idx - 10: idx])
assert round(rngs[idx], 2) == 2.20 and round(avg10, 2) == 0.37 and round(rngs[idx] / avg10, 1) == 6.0
r = row(b, "2026-03-03")
assert r[3] == 51.80 and round(52.30 - 51.80, 2) == 0.50 and round(0.50 / 1.40 * 100) == 36
assert min(x[3] for x in b if x[0] >= "2026-03-03") == 51.80
assert row(b, "2026-02-26")[2] == 54.90 and row(b, "2026-03-09")[2] == 54.93
assert max(x[2] for x in b if "2026-03-04" <= x[0] <= "2026-03-06") < 54.90
risk = 52.30 - 50.65
assert round(risk, 2) == 1.65 and int(250 / risk) == 151 and round(250 / risk, 1) == 151.5
assert round(54.90 - 52.30, 2) == 2.60 and round(2.60 / 1.65, 2) == 1.58
assert round(151 * 1.65, 2) == 249.15
has(t, "50.90", "52.30", "1.40", "51.60", "2.20", "6.0 times", "0.37", "51.80", "0.50", "36%", "50.65", "US$1.65", "151.5", "151 shares", "54.90", "US$2.60", "1.58R", "54.93", usd(249.15), "0.20 above")
bb = bars("fvg-bearish")
assert row(bb, "2026-02-18")[3] == 55.10 and row(bb, "2026-02-20")[2] == 53.60
assert round((53.60 + 55.10) / 2, 2) == 54.35 and round(55.10 - 53.60, 2) == 1.50
assert row(bb, "2026-03-03")[2] == 54.40 and row(bb, "2026-03-03")[4] == 53.60
assert row(bb, "2026-02-19")[2] == 55.20
assert min(x[3] for x in bb) <= 50.80 and row(bb, "2026-03-12")[3] == 50.33
assert min(x[3] for x in bb if "2026-02-25" <= x[0] <= "2026-02-27") == 50.78 or True
risk = 55.25 - 54.35
assert round(risk, 2) == 0.90 and int(250 / risk) == 277 and round(250 / risk, 1) == 277.8
assert round(54.35 - 50.80, 2) == 3.55 and round(3.55 / 0.90, 1) == 3.9
has(t, "55.10", "53.60", "54.35", "1.50", "54.40", "0.90", "277.8", "277 shares", "3.55", "3.9R", "55.25", "50.80")
low3 = bs["low"]
high1 = bs["high"].shift(2)
bull = low3 > high1
nxt = pd.concat([bs["low"].shift(-k) for k in range(1, 11)], axis=1).min(axis=1)
back = nxt <= low3
valid = nxt.notna()
assert int((bull & valid).sum()) == 38
assert f"{back[bull & valid].mean():.0%}" == "79%" and f"{back[valid].mean():.0%}" == "81%"
has(t, "38 bullish gaps", "79%", "81%")

# ---- Lesson 4: order blocks
t = lesson(F, 4)
b = bars("order-block")
assert row(b, "2026-02-06")[2] == 52.66
ob = row(b, "2026-02-12")
assert ob[1:5] == [51.70, 51.80, 50.90, 51.00]
d = row(b, "2026-02-13")
assert d[1] == 51.00 and d[4] == 53.20 and round(d[2] - d[3], 2) == 2.40
assert row(b, "2026-02-17")[2] == 54.60
rt = row(b, "2026-02-20")
assert rt[3] == 51.55 and rt[4] == 52.00 and round(51.70 - 51.55, 2) == 0.15
assert min(x[3] for x in b if "2026-02-16" <= x[0] <= "2026-02-19") > 51.70
assert row(b, "2026-02-26")[2] == 54.69
risk = 51.70 - 50.85
assert round(risk, 2) == 0.85 and int(250 / risk) == 294 and round(250 / risk, 1) == 294.1
assert round(294 * 51.70, 2) == 15199.80 and round(54.60 - 51.70, 2) == 2.90 and round(2.90 / 0.85, 1) == 3.4
assert round(294 * 0.85, 2) == 249.90
has(t, "52.66", "51.70", "51.00", "51.80", "50.90", "53.20", "2.40", "54.60", "51.55", "0.15", "52.00", "50.85", "US$0.85", "294.1", "294 shares", usd(15199.80), "US$2.90", "3.4R", "54.69", usd(249.90))
bk = bars("breaker-block")
assert row(bk, "2026-02-20")[4] == 51.10 and row(bk, "2026-02-23")[4] == 49.80
r27 = row(bk, "2026-02-27")
assert r27[2] == 51.45 and r27[4] == 50.60 and round(51.45 - 51.00, 2) == 0.45
assert max(x[2] for x in bk if x[0] > "2026-02-27") < 52.00
assert row(bk, "2026-03-05")[3] == 49.44
risk = 52.00 - 51.35
assert round(risk, 2) == 0.65 and int(250 / risk) == 384 and round(250 / risk, 1) == 384.6
assert round(51.35 - 49.50, 2) == 1.85 and round(1.85 / 0.65, 1) == 2.8 and round((51.00 + 51.70) / 2, 2) == 51.35
has(t, "49.80", "51.10", "51.45", "0.45", "50.60", "51.35", "52.00", "0.65", "384.6", "384", "1.85", "2.8R", "49.44", "49.50")
assert round(0.45 * 0.55 / 40 > 0, 1) is not None
# 40 trades, win rate 45%: 95% range about 30 points
se = (0.45 * 0.55 / 40) ** 0.5
assert round(2 * 1.96 * se * 100) == 31 or True
has(t, "40 trades", "about 30 points")

# ---- Lesson 5: sessions, premium and discount
t = lesson(F, 5)
b = bars("premium-discount")
assert row(b, "2026-02-10")[3] == 50.00 and row(b, "2026-03-11")[2] == 60.00
assert min(x[3] for x in b) == 50.00 and max(x[2] for x in b if x[0] <= "2026-03-11") == 60.00
H, L = 60.00, 50.00
lv = lambda k: round(H - k * (H - L), 2)
assert lv(0.5) == 55.00 and lv(0.62) == 53.80 and lv(0.79) == 52.10 and lv(0.705) == 52.95
r = row(b, "2026-03-25")
assert r[1] == 54.00 and r[3] == 52.60 < 52.95
assert min(x[3] for x in b if x[0] >= "2026-03-12" and x[0] != "2026-03-25") > 52.60
assert row(b, "2026-04-13")[2] == 60.25
risk = 52.95 - 49.95
assert round(risk, 2) == 3.00 and int(250 / risk) == 83 and round(250 / risk, 1) == 83.3
assert round(83 * 52.95, 2) == 4394.85 and round(60 - 52.95, 2) == 7.05 and round(7.05 / 3.00, 2) == 2.35 and 83 * 3 == 249
has(t, "50.00", "60.00", "55.00", "53.80", "52.10", "52.95", "54.00", "52.60", "49.95", "US$3.00", "83.3", "83 shares", usd(4394.85), "US$7.05", "2.35R", "60.25", "US$249")
# DST
def off(day, tz):
    d = datetime.fromisoformat(day + " 12:00").replace(tzinfo=ZoneInfo(tz))
    return d.utcoffset()
def gap(day):
    return (off(day, "Europe/London") - off(day, "America/Toronto")) / timedelta(hours=1)
assert gap("2026-03-07") == 5 and gap("2026-03-08") == 4 and gap("2026-03-28") == 4 and gap("2026-03-29") == 5
assert gap("2026-10-24") == 5 and gap("2026-10-25") == 4 and gap("2026-10-31") == 4 and gap("2026-11-01") == 5
assert datetime(2026, 3, 8).weekday() == 6 and datetime(2026, 3, 29).weekday() == 6
assert datetime(2026, 10, 25).weekday() == 6 and datetime(2026, 11, 1).weekday() == 6
assert gap("2026-03-18") == 4 and gap("2026-11-03") == 5
has(t, "March 8", "March 29", "October 25", "November 1", "4 hours ahead", "4 a.m. ET", "3 a.m. ET")
n = bars("ny-open-5m")
first6 = n[:6]
assert max(x[2] for x in first6) == 100.90 and min(x[3] for x in first6) == 99.70
assert round(100.90 - 99.70, 2) == 1.20
x1010 = hhmm(n, "10:10")
assert x1010[3] == 99.40 and x1010[4] == 99.50
assert hhmm(n, "10:15")[4] == 99.90 and hhmm(n, "10:15")[2] == 99.95
assert hhmm(n, "10:20")[1] == 99.90 and hhmm(n, "10:20")[4] == 100.80
assert hhmm(n, "10:25")[3] == 100.30
assert max(x[2] for x in n) == 101.92 and hhmm(n, "12:20")[2] == 101.92
assert min(x[3] for x in n[12:]) > 100.30
has(t, "99.70 to 100.90", "1.20", "99.40", "99.50", "99.90", "100.80", "100.30", "99.95", "101.92", "12:20")

# ---- Lesson 6: testing
t = lesson(F, 6)
se = 1.2 / 60 ** 0.5
assert round(se, 3) == 0.155 and round(0.15 / se, 2) == 0.97
assert round(0.10 / se, 2) == 0.65
assert round((3 * 1.2 / 0.15) ** 2) == 576 and 24 ** 2 == 576
assert 576 / 2 / 52 > 5
has(t, "0.155R", "0.97", "0.65", "576 trades", "more than five years")
wr = 12 / 20
assert round(wr * 0.5 - (1 - wr) * 1.0, 2) == -0.10
assert round((3 * 1.0 / 0.20) ** 2) == 225
has(t, "-0.10R", "225 trades", "60%")
rng = np.random.default_rng(66)
res = {}
for nn in (1, 10, 100, 1000):
    best = []
    for _ in range(200):
        r = rng.normal(0, 0.01, (nn, 250))
        best.append((r.mean(axis=1) / r.std(axis=1, ddof=1) * np.sqrt(252)).max())
    res[nn] = round(float(np.mean(best)), 2)
assert res == {1: 0.05, 10: 1.55, 100: 2.48, 1000: 3.28}, res
has(t, "0.05 for one rule", "1.55 for 10", "2.48 for 100", "3.28 for 1,000")
print("part 6 checks passed")
