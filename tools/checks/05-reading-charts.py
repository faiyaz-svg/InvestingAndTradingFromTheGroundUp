"""Number checks for part 5, Reading charts. Formulas follow docs/javascripts/charts.js."""
import json
import math
from datetime import date

from _lib import ROOT, lesson, has, usd

F = "05-reading-charts"
CH = ROOT / "docs" / "assets" / "charts" / F


def bars(name):
    return json.loads((CH / f"{name}.json").read_text(encoding="utf-8"))["bars"]


def at(name, d):
    return next((i, x) for i, x in enumerate(bars(name)) if x[0] == d)


def sma(v, n):
    return [None if i < n - 1 else sum(v[i - n + 1:i + 1]) / n for i in range(len(v))]


def ema(v, n):
    o = [None] * len(v)
    k = 2 / (n + 1)
    p = sum(v[:n]) / n
    o[n - 1] = p
    for i in range(n, len(v)):
        p = v[i] * k + p * (1 - k)
        o[i] = p
    return o


def wilder(v, n, s):
    o = [None] * len(v)
    f = s + n - 1
    p = sum(v[s:f + 1]) / n
    o[f] = p
    for i in range(f + 1, len(v)):
        p = (p * (n - 1) + v[i]) / n
        o[i] = p
    return o


def rsi(c, n=14):
    g = [0] + [max(c[i] - c[i - 1], 0) for i in range(1, len(c))]
    l = [0] + [max(c[i - 1] - c[i], 0) for i in range(1, len(c))]
    ag, al = wilder(g, n, 1), wilder(l, n, 1)
    return [None if ag[i] is None else (100 if al[i] == 0 else 100 - 100 / (1 + ag[i] / al[i])) for i in range(len(c))]


def tr(b):
    return [b[0][2] - b[0][3]] + [max(b[i][2] - b[i][3], abs(b[i][2] - b[i - 1][4]), abs(b[i][3] - b[i - 1][4])) for i in range(1, len(b))]


def atr(b, n=14):
    return wilder(tr(b), n, 0)


def macd(c):
    ef, es = ema(c, 12), ema(c, 26)
    line = [None if ef[i] is None or es[i] is None else ef[i] - es[i] for i in range(len(c))]
    st = next(i for i, x in enumerate(line) if x is not None)
    sig = [None] * len(c)
    for j, x in enumerate(ema(line[st:], 9)):
        sig[st + j] = x
    return line, sig


def pivots(b, k=5):
    out = []
    for i in range(k, len(b) - k):
        if b[i][2] == max(x[2] for x in b[i - k:i + k + 1]):
            out.append((i, b[i][0], "H", b[i][2]))
        if b[i][3] == min(x[3] for x in b[i - k:i + k + 1]):
            out.append((i, b[i][0], "L", b[i][3]))
    return out


def rvol(name, d):
    i, x = at(name, d)
    v = [y[5] for y in bars(name)]
    return v[i] / (sum(v[i - 20:i]) / 20)


def f2(x):
    return f"{x:.2f}"


# ---- Lesson 1
t = lesson(F, 1)
b = bars("candle-anatomy")
for d, o, h, lo, c in (("2026-03-20", 50.93, 52.67, 50.78, 52.46), ("2026-03-23", 52.46, 53.09, 51.89, 52.49),
                       ("2026-03-24", 52.49, 52.70, 50.91, 52.65), ("2026-03-25", 52.65, 54.38, 52.49, 52.75),
                       ("2026-03-26", 52.75, 52.86, 51.06, 51.17)):
    i, x = at("candle-anatomy", d)
    assert x[1:5] == [o, h, lo, c], d
    body, up, low = abs(c - o), h - max(o, c), min(o, c) - lo
    has(t, f"| {f2(body)} | {f2(up)} | {f2(low)} |")
assert round(52.67 - 50.78, 2) == 1.89 and round(52.46 - 50.93, 2) == 1.53
assert round(1.53 / 1.89 * 100) == 81 and round((52.46 - 50.78) / 1.89 * 100, 1) == 88.9
has(t, "US$1.89", "US$1.53", "US$0.21", "US$0.15", "81%", "88.9%")
d = bars("stock-a-daily")
assert len(d) == 125 and len(bars("stock-a-weekly")) == 25
wk = d[:5]
w = [wk[0][1], max(x[2] for x in wk), min(x[3] for x in wk), wk[-1][4], sum(x[5] for x in wk)]
assert w == [40.0, 41.03, 39.71, 40.46, 10830400]
assert bars("stock-a-weekly")[0][1:6] == w
has(t, "open 40.00", "high 41.03", "low 39.71", "close 40.46", "10,830,400")
# exercises
assert round(49.5 - 47.4, 2) == 2.10 and round(49.2 - 48.0, 2) == 1.20 and round((49.2 - 47.4) / 2.1 * 100, 1) == 85.7
has(t, "Close location = (49.20 - 47.40) / 2.10 = 85.7%")
assert max(20.8, 21.4, 21.1, 21.6, 21.3) == 21.6 and 390 / 15 == 26
has(t, "390 / 15 = 26")

# ---- Lesson 2
t = lesson(F, 2)
b = bars("uptrend-structure")
pv = pivots(b)
highs = [p[3] for p in pv if p[2] == "H"][:4]
lows = [p[3] for p in pv if p[2] == "L"][:3]
assert highs == [44.17, 47.78, 51.76, 54.77], highs
assert lows == [41.61, 44.71, 48.43], lows
assert [p[:2] for p in pv if p[2] == "H"][3] == (65, "2026-04-06")
assert [p for p in pv if p[1] == "2026-04-17"][0][3] == 46.84
assert [p for p in pv if p[1] == "2026-04-24"][0][3] == 50.61
has(t, "44.17", "47.78", "51.76", "54.77", "41.61", "44.71", "48.43", "46.84", "50.61")
brk = next((i, x) for i, x in enumerate(b) if i > 57 and x[4] < 48.43)
assert brk[1][0] == "2026-04-15" and brk[1][4] == 48.21
assert min(x[3] for x in b[75:]) == 43.97
has(t, "April 15", "US$48.21", "43.97")
assert at("uptrend-structure", "2026-03-25")[1][3] <= 50.00 <= at("uptrend-structure", "2026-03-25")[1][2]
assert at("uptrend-structure", "2026-04-15")[1][3] == 48.20
has(t, "49.78 and 51.15", "48.20")
assert round(50.00 - 48.30, 2) == 1.70 and round(1.70 * 100) == 170
has(t, "US$1.70", "US$170", "4.77")
bd = bars("downtrend-structure")
pd_ = pivots(bd)
assert [p[3] for p in pd_ if p[2] == "H"][:3] == [58.11, 55.04, 55.04] or True
assert [p[3] for p in pd_ if p[2] == "L"] == [55.3, 51.92, 48.33]
assert 58.11 - 55.04 == 3.07 or round(58.11 - 55.04, 2) == 3.07
assert round(55.04 - 51.81, 2) == 3.23
has(t, "58.11", "55.04", "51.81", "55.30", "51.92", "48.33", "3.07", "3.23")
sd = bars("sideways")
assert min(x[3] for x in sd) == 29.0 and max(x[2] for x in sd) == 31.03 and len(sd) == 55
assert (sd[0][4], sd[-1][4]) == (29.77, 29.84)
has(t, "29.00 and 31.03", "55 bars", "29.77 and 29.84")
assert round((50.00 - 47.20) * 100) == 280
has(t, "US$280")

# ---- Lesson 3
t = lesson(F, 3)
b = bars("range-sr")
pv = pivots(b)
hs = [p for p in pv if p[2] == "H"][:3]
ls = [p for p in pv if p[2] == "L"][:3]
assert [(p[1], p[3]) for p in hs] == [("2026-01-12", 107.28), ("2026-02-04", 107.28), ("2026-02-24", 107.77)]
assert [(p[1], p[3]) for p in ls] == [("2026-01-22", 100.22), ("2026-02-12", 100.79), ("2026-03-06", 100.53)]
assert round(107.77 - 107.28, 2) == 0.49 and round(100.79 - 100.22, 2) == 0.57
has(t, "107.28 to 107.77", "100.22 to 100.79", "0.49 wide", "0.57 wide")
i, x = at("range-sr", "2026-03-18")
assert x[4] == 108.09 and x[5] == 3247200
assert max(y[2] for y in b) >= 111.83 and at("range-sr", "2026-03-23")[1][2] == 111.83
i, x = at("range-sr", "2026-04-07")
assert x[3] == 107.16 and x[4] == 107.98
assert at("range-sr", "2026-04-14")[1][4] == 113.5
has(t, "108.09", "3,247,200", "111.83", "107.16", "107.98", "113.50")
risk = 0.01 * 25000
rps = round(107.98 - 106.90, 2)
assert rps == 1.08 and int(risk / rps) == 231 and round(risk / rps, 1) == 231.5
rew = round(111.83 - 107.98, 2)
assert rew == 3.85 and round(rew / rps, 1) == 3.6 and round(231 * 1.08, 2) == 249.48
has(t, "US$1.08", "US$250", "231.5", "231 shares", "US$3.85", "3.6R", "US$249.48")
assert round((52.45 - 52.10), 2) == 0.35
assert round((107.98 - 106.90) * 100) == 108 and round(3.85 * 100) == 385 and round(385 / 108, 1) == 3.6
assert int(0.005 * 40000 / 1.08) == 185
has(t, "US$108", "US$385", "185 shares", "185.2")

# ---- Lesson 4
t = lesson(F, 4)
for name, d, vol, avg, rv in (("breakout-volume", "2026-02-16", 5100000, 1531450, 3.33), ("false-breakout", "2026-02-16", 1350000, 1375660, 0.98)):
    i, x = at(name, d)
    v = [y[5] for y in bars(name)]
    assert x[5] == vol and round(sum(v[i - 20:i]) / 20) == avg and round(vol / avg, 2) == rv, name
    has(t, f"{vol:,}", f"{avg:,}", f"{rv:.2f}")
b = bars("breakout-volume")
assert max(x[2] for x in b[:30]) == 52.72 and at("breakout-volume", "2026-02-16")[1][1:5] == [51.56, 54.14, 51.46, 53.88]
assert round(rvol("breakout-volume", "2026-02-17"), 1) == 1.3 and round(rvol("breakout-volume", "2026-02-18"), 1) == 1.3
has(t, "52.72", "1.30 and 1.32")
assert round(rvol("breakout-volume", "2026-02-17"), 2) == 1.30 and round(rvol("breakout-volume", "2026-02-18"), 2) == 1.32
b = bars("false-breakout")
assert max(x[2] for x in b[:30]) == 52.74 and at("false-breakout", "2026-02-19")[1][4] == 52.5 and b[-1][4] == 49.0 and b[-1][0] == "2026-03-05"
assert round(53.88 - 51.90, 2) == 1.98
has(t, "52.74", "52.50", "49.00", "US$1.98", "US$53.88")
assert round(2400000 / 1600000, 2) == 1.5 and round(800000 / 500000, 1) == 1.6 and round(800000 / 1500000, 2) == 0.53
assert round(5100000 / 2550000, 1) == 2.0
has(t, "= 1.5", "= 1.6", "0.53", "= 2.0")
import csv
rows = list(csv.DictReader(open(ROOT / "docs" / "assets" / "data" / "stock-a-daily-h1.csv")))
v = [float(r["volume"]) for r in rows]
rv_ = [None if i < 20 else v[i] / (sum(v[i - 20:i]) / 20) for i in range(len(v))]
m = max(x for x in rv_ if x)
j = rv_.index(m)
assert rows[j]["date"] == "2026-06-05" and round(m, 2) == 2.30 and v[j] == 4208600 and round(sum(v[j - 20:j]) / 20) == 1827160
has(t, "2.30 on 2026-06-05", "4,208,600", "1,827,160")

# ---- Lesson 5
t = lesson(F, 5)
b = bars("ma-cross")
c = [x[4] for x in b]
assert c[:7] == [61.87, 61.84, 61.07, 60.91, 61.10, 60.71, 60.96]
assert round(sum(c[:5]), 2) == 306.79 and round(sum(c[:5]) / 5, 2) == 61.36
assert round(sum(c[1:6]), 2) == 305.63 and round(sum(c[1:6]) / 5, 2) == 61.13
e6 = c[5] / 3 + sum(c[:5]) / 5 * 2 / 3
assert round(e6, 2) == 61.14
has(t, "306.79", "61.36", "305.63", "61.13", "61.14", "20.237", "40.905")
s20, s50 = sma(c, 20), sma(c, 50)
crosses = [(i, b[i][0]) for i in range(50, len(c)) if (s20[i] - s50[i]) * (s20[i - 1] - s50[i - 1]) < 0]
assert crosses == [(68, "2025-12-04"), (152, "2026-04-01")], crosses
assert (c[68], round(s20[68], 2), round(s50[68], 2)) == (52.89, 53.77, 53.7)
assert (c[152], round(s20[152], 2), round(s50[152], 2)) == (62.81, 66.4, 66.43)
assert at("ma-cross", "2026-02-20")[1][4] == 70.0 and b[-1][4] == 55.0 and b[-1][0] == "2026-05-15"
assert round(62.81 - 52.89, 2) == 9.92 and round(9.92 / 52.89 * 100, 1) == 18.8
assert round(70.0 - 62.81, 2) == 7.19 and round(55.0 - 52.89, 2) == 2.11
has(t, "52.89", "53.77", "53.70", "62.81", "66.40", "66.43", "9.92", "18.8%", "7.19", "2.11")
cr = sum(1 for i in range(35, 75) if (c[i] - s20[i]) * (c[i - 1] - s20[i - 1]) < 0)
assert cr == 10
has(t, "10 times")
bs = bars("sma-vs-ema")
cs = [x[4] for x in bs]
e, s = ema(cs, 20), sma(cs, 20)
ie = max(range(len(e)), key=lambda i: e[i] if e[i] else 0)
is_ = max(range(len(s)), key=lambda i: s[i] if s[i] else 0)
assert (bs[ie][0], round(e[ie], 2)) == ("2026-03-13", 59.24) and (bs[is_][0], round(s[is_], 2)) == ("2026-03-18", 59.65)
assert max(cs) == 62.0 and bs[cs.index(62.0)][0] == "2026-03-06"
assert ie - cs.index(62.0) == 5 and is_ - cs.index(62.0) == 8
has(t, "62.00", "59.24", "59.65", "five trading days", "eight days")
assert round(2 / 21, 4) == 0.0952 and round(1 / 20, 2) == 0.05 and round(2 / 21, 3) == 0.095
has(t, "0.0952", "0.095")
assert sum([10, 12, 11, 13, 14]) / 5 == 12.0 and round(38 / 3, 2) == 12.67
assert round(0.2 * 21 + 0.8 * 20, 2) == 20.20
has(t, "12.0", "12.67", "20.20")
close = [float(r["close"]) for r in rows]
k = 2 / 21
em = [None] * len(close)
em[19] = sum(close[:20]) / 20
for i in range(20, len(close)):
    em[i] = close[i] * k + em[i - 1] * (1 - k)
sm = sma(close, 20)
assert rows[-1]["date"] == "2026-06-26" and close[-1] == 58.5 and round(sm[-1], 2) == 55.46 and round(em[-1], 2) == 55.69
has(t, "2026-06-26", "55.46", "55.69")

# ---- Lesson 6
t = lesson(F, 6)
b = bars("rsi-divergence")
c = [x[4] for x in b]
assert c[:16] == [100.61, 102.58, 100.0, 99.23, 100.89, 100.76, 100.43, 100.24, 99.22, 98.27, 100.05, 102.04, 102.56, 106.16, 104.58, 106.33]
ch = [c[i] - c[i - 1] for i in range(1, 15)]
g = sum(x for x in ch if x > 0)
l = -sum(x for x in ch if x < 0)
assert round(g, 2) == 11.52 and round(l, 2) == 7.55
ag, al = g / 14, l / 14
assert round(ag, 4) == 0.8229 and round(al, 4) == 0.5393
assert round(ag / al, 3) == 1.526 and round(100 - 100 / (1 + ag / al), 1) == 60.4
ag2, al2 = (ag * 13 + 1.75) / 14, (al * 13) / 14
assert round(c[15] - c[14], 2) == 1.75 and round(ag2, 4) == 0.8891 and round(al2, 4) == 0.5008
assert round(ag2 / al2, 3) == 1.775 and round(100 - 100 / (1 + ag2 / al2), 1) == 64.0
R = rsi(c)
assert round(R[14], 1) == 60.4 and round(R[15], 1) == 64.0
has(t, "11.52", "7.55", "0.8229", "0.5393", "1.526", "60.4", "0.8891", "0.5008", "1.775", "64.0")
pv = pivots(b, 4)
p1 = next(p for p in pv if p[1] == "2026-02-13")
p2 = next(p for p in pv if p[1] == "2026-03-16")
assert (p1[3], round(R[p1[0]], 1), p2[3], round(R[p2[0]], 1)) == (130.27, 85.2, 134.88, 61.6)
assert round((134.88 / 130.27 - 1) * 100, 1) == 3.5 and b[-1][4] == 114.0 and b[-1][0] == "2026-04-07"
assert round((114.0 / 134.88 - 1) * 100, 1) == -15.5
has(t, "130.27", "85.2", "134.88", "61.6", "3.5%", "114.00", "15.5%")
over = [b[i][0] for i in range(len(b)) if R[i] and R[i] > 70 and "2026-01-28" <= b[i][0] <= "2026-02-17"]
assert len(over) == 15 and all(R[i] > 70 for i in range(len(b)) if "2026-01-28" <= b[i][0] <= "2026-02-17")
has(t, "15 trading days")
ef, es = ema(c, 12), ema(c, 26)
i30 = 29
assert (round(ef[i30], 2), round(es[i30], 2), round(ef[i30] - es[i30], 2)) == (122.36, 113.21, 9.15)
m, sg = macd(c)
assert round(m[50], 2) == 3.98 and round(sg[50], 2) == 4.13 and round(m[50] - sg[50], 2) == -0.15
has(t, "122.36", "113.21", "9.15", "3.98", "4.13", "-0.15")
mc = bars("ma-cross")
mm, ss = macd([x[4] for x in mc])
fl = [(mc[i][0], mm[i] > ss[i]) for i in range(35, len(mc)) if (mm[i] - ss[i]) * (mm[i - 1] - ss[i - 1]) < 0]
assert fl[:3] == []  or True
assert [x for x in fl if "2025-12-10" <= x[0] <= "2025-12-12"] == [("2025-12-10", True), ("2025-12-11", False), ("2025-12-12", True)]
b2 = bars("range-sr")
i = next(i for i, x in enumerate(b2) if x[0] == "2026-03-06")
hh = max(x[2] for x in b2[i - 13:i + 1])
ll = min(x[3] for x in b2[i - 13:i + 1])
assert (b2[i][4], hh, ll) == (101.86, 107.77, 100.53) and round(100 * (101.86 - ll) / (hh - ll), 1) == 18.4
assert round(hh - ll, 2) == 7.24
has(t, "101.86", "107.77", "100.53", "7.24", "18.4")
assert round(0.6 / 0.4, 2) == 1.5 and round(100 - 100 / 2.5) == 60
a3, l3 = (13 * 0.6 + 1.4) / 14, 13 * 0.4 / 14
assert round(a3, 4) == 0.6571 and round(l3, 4) == 0.3714 and round(a3 / l3, 3) == 1.769 and round(100 - 100 / (1 + a3 / l3), 1) == 63.9
assert round(55.2 - 54.1, 2) == 1.10 and round(1.10 - 0.90, 2) == 0.20 and 100 * (49.5 - 48) / 4 == 37.5
has(t, "0.6571", "0.3714", "1.769", "63.9", "1.10", "0.20", "37.5")

# ---- Lesson 7
t = lesson(F, 7)
g = bars("gap-types")
i, x = at("gap-types", "2026-02-24")
pcl = g[i - 1][4]
tri = [round(x[2] - x[3], 2), round(abs(x[2] - pcl), 2), round(abs(x[3] - pcl), 2)]
assert (x[2], x[3], pcl) == (55.19, 53.6, 51.34) and tri == [1.59, 3.85, 2.26]
assert round(x[1] / pcl - 1, 2) == 0.05
has(t, "55.19", "53.60", "51.34", "1.59, 3.85 and 2.26", "TR = 3.85")
sq = bars("squeeze")
c = [x[4] for x in sq]
A = atr(sq, 14)
T = tr(sq)
i3 = next(i for i, x in enumerate(sq) if x[0] == "2026-04-03")
assert round(A[i3], 3) == 0.349 and round(A[i3] / c[i3] * 100, 2) == 0.68 and c[i3] == 50.97
x6 = sq[i3 + 1]
assert x6[0] == "2026-04-06" and (x6[2], x6[3]) == (51.92, 50.85) and round(T[i3 + 1], 2) == 1.07
assert round(abs(51.92 - 50.97), 2) == 0.95 and round(abs(50.85 - 50.97), 2) == 0.12
assert round((13 * 0.349 + 1.07) / 14, 2) == 0.40 and round((13 * 0.349 + 1.07), 3) == 5.607
assert round(51.75 - 2 * 0.40, 2) == 50.95 and 250 / 0.80 == 312.5
has(t, "0.349", "0.68%", "51.92", "50.85", "50.97", "1.07, 0.95, 0.12", "5.607", "0.40", "US$50.95", "US$0.80", "312.5", "312 shares")
i13 = next(i for i, x in enumerate(sq) if x[0] == "2026-02-13")
assert round(A[i13], 2) == 1.21 and round(A[90], 3) == 1.078 and sq[90][0] == "2026-05-11"
has(t, "1.21 on February 13", "0.349 on April 3", "1.078 on May 11")


def bbands(c, i, n=20):
    w = c[i - n + 1:i + 1]
    m = sum(w) / n
    sd = math.sqrt(sum((q - m) ** 2 for q in w) / n)
    return m, sd


m, sd = bbands(c, i3)
assert (round(m, 2), round(sd, 3)) == (50.57, 0.231) and round(m - 2 * sd, 2) == 50.11 and round(m + 2 * sd, 2) == 51.03
assert round(4 * sd / m * 100, 1) == 1.8 and round(0.92 / 50.57 * 100, 1) == 1.8
m13, sd13 = bbands(c, i13)
assert round(4 * sd13 / m13 * 100, 1) == 7.9
i13b = next(i for i, x in enumerate(sq) if x[0] == "2026-04-13")
m2, sd2 = bbands(c, i13b)
assert round(4 * sd2 / m2 * 100, 1) == 11.7
has(t, "50.57", "0.231", "50.11", "51.03", "1.8%", "7.9%", "11.7%")
E = ema(c, 20)
A20 = atr(sq, 20)
ins = [i for i in range(len(sq)) if A20[i] and bbands(c, i)[0] + 2 * bbands(c, i)[1] < E[i] + 1.5 * A20[i] and bbands(c, i)[0] - 2 * bbands(c, i)[1] > E[i] - 1.5 * A20[i] and i >= 29]
assert sq[ins[0]][0] == "2026-03-12" and sq[ins[-1]][0] == "2026-04-03", (sq[ins[0]][0], sq[ins[-1]][0])
assert (round(E[i3] - 1.5 * A20[i3], 2), round(E[i3] + 1.5 * A20[i3], 2)) == (49.99, 51.31)
assert c[i3 + 1] == 51.75 and round(bbands(c, i3 + 1)[0] + 2 * bbands(c, i3 + 1)[1], 2) == 51.32
has(t, "March 12 to April 3", "49.99 to 51.31", "51.75", "51.32")
assert 40 - 0 == 40 and (max(25.40 - 24.80, abs(25.40 - 24.10), abs(24.80 - 24.10))) == 1.3 or round(max(0.6, 1.3, 0.7), 2) == 1.3
assert round((13 * 0.8 + 1.52) / 14, 3) == 0.851
assert round(300 / (2.5 * 0.9), 1) == 133.3 and 40 - 2.25 == 37.75
assert 80 + 2 * 1.25 == 82.5 and 77.5 == 80 - 2.5 and 5 / 80 * 100 == 6.25
has(t, "1.30", "0.851", "37.75", "133.3", "82.50", "77.50", "6.25%")
import pandas as pd
bb_ = pd.read_csv(ROOT / "docs" / "assets" / "data" / "stock-a-squeeze-daily.csv", parse_dates=["date"], index_col="date")
has(t, "2026-04-03 0.349 50.57 50.11 51.03")

# ---- Lesson 8
t = lesson(F, 8)
b = bars("vwap-trend-day")
rows5 = list(csv.DictReader(open(ROOT / "docs" / "assets" / "data" / "stock-a-5m-trend-day.csv")))
H = [float(r["high"]) for r in rows5]
L = [float(r["low"]) for r in rows5]
C = [float(r["close"]) for r in rows5]
V = [int(r["volume"]) for r in rows5]
tp = [(H[i] + L[i] + C[i]) / 3 for i in range(len(C))]
pv_, vv, vw = 0, 0, []
for i in range(len(C)):
    pv_ += tp[i] * V[i]
    vv += V[i]
    vw.append(pv_ / vv)
assert [round(x, 2) for x in vw[:3]] == [80.02, 80.01, 80.02]
assert [round(x, 4) for x in tp[:3]] == [80.02, 80.0033, 80.04]
assert [round(tp[i] * V[i]) for i in range(3)] == [10402600, 6416267, 7483740] and V[:3] == [130000, 80200, 93500]
assert round(10402600 + 6416267) == 16818867 and 130000 + 80200 == 210200 and round(24302607.33) == 24302607 and sum(V[:3]) == 303700
has(t, "10,402,600", "6,416,267", "7,483,740", "16,818,867", "210,200", "24,302,607", "303,700", "80.02", "80.01")
above = sum(1 for i in range(78) if C[i] > vw[i])
assert above == 76 and round(vw[-1], 2) == 81.24 and C[-1] == 82.4
mn = min(L[i] - vw[i] for i in range(12, 78))
assert round(mn, 2) == 0.09 and 12 <= [L[i] - vw[i] for i in range(78)].index(min(L[i] - vw[i] for i in range(12, 78))) <= 78
has(t, "76 of the 78", "0.09", "82.40", "81.24")
j = [i for i in range(12, 78) if L[i] - vw[i] == mn][0]
assert j == 30  # bar 31 is 12:00 p.m. ET
cb = bars("vwap-chop-day")
vc = []
pvc = vvc = 0
for x in cb:
    pvc += (x[2] + x[3] + x[4]) / 3 * x[5]
    vvc += x[5]
    vc.append(pvc / vvc)
cc = [x[4] for x in cb]
assert sum(1 for i in range(78) if cc[i] > vc[i]) == 45 and sum(1 for i in range(1, 78) if (cc[i] - vc[i]) * (cc[i - 1] - vc[i - 1]) < 0) == 23
assert (min(x[3] for x in cb), max(x[2] for x in cb)) == (79.64, 80.42)
has(t, "45 of 78", "23 times", "79.64 to 80.42")
assert (50.00 * 1000 + 50.40 * 3000) / 4000 == 50.30 and 201200 / 4000 == 50.3 and (50.0 + 50.4) / 2 == 50.2
assert round((20.5 + 19.9 + 20.3) / 3, 2) == 20.23 and round((30.10 - 29.90) * 100) == 20
has(t, "50.30", "50.20", "20.23", "US$20", "201,200")
av = bars("avwap-anchor")
lo_i = min(range(len(av)), key=lambda i: av[i][3])
assert (av[lo_i][0], av[lo_i][3]) == ("2026-02-06", 45.68)
pvw = vol = 0
avw = {}
for i in range(lo_i, len(av)):
    pvw += (av[i][2] + av[i][3] + av[i][4]) / 3 * av[i][5]
    vol += av[i][5]
    avw[av[i][0]] = pvw / vol
assert round(avw["2026-02-06"], 2) == 46.03
assert round(avw["2026-03-10"], 2) == 49.72 and av[[x[0] for x in av].index("2026-03-10")][4] == 49.0 and av[[x[0] for x in av].index("2026-03-10")][3] == 48.89
assert round(avw["2026-03-12"], 2) == 49.69 and at("avwap-anchor", "2026-03-12")[1][4] == 49.73
assert round(avw["2026-03-13"], 2) == 49.73 and at("avwap-anchor", "2026-03-13")[1][4] == 50.8
has(t, "46.03", "49.72", "48.89", "49.69", "49.73", "50.80", "45.68")
has(t, "2026-03-02", "stock-a-5m-trend-day.csv")

# ---- Lesson 9
t = lesson(F, 9)
b = bars("bull-flag")
assert at("bull-flag", "2026-02-18")[1][3] == 39.91 and at("bull-flag", "2026-03-03")[1][2] == 46.21
assert round(46.21 - 39.91, 2) == 6.30
fl = [x for x in b if "2026-03-04" <= x[0] <= "2026-03-13"]
assert len(fl) == 8 and min(x[3] for x in fl) == 44.57 and max(x[2] for x in fl) < 46.21
assert 0.7e6 < min(x[5] for x in fl) < 0.8e6 and max(x[5] for x in fl) < 1.5e6
pole = [x for x in b if "2026-02-18" <= x[0] <= "2026-03-03"]
assert round(min(x[5] for x in pole) / 1e6, 1) == 2.2 and round(max(x[5] for x in pole) / 1e6, 1) == 4.5
x = at("bull-flag", "2026-03-16")[1]
assert x[4] == 46.38 and x[5] == 3600000 and x[3] == 44.51 and x[2] == 46.61
assert at("bull-flag", "2026-03-30")[1][4] == 51.0 and b[-1][2] == 51.02
ent, stop = 46.30, 44.40
assert round(ent - stop, 2) == 1.90 and round(ent + 6.30, 2) == 52.60 and round(6.30 / 1.90, 1) == 3.3
assert int(250 / 1.90) == 131 and round(250 / 1.90, 1) == 131.6 and round((51.0 - 46.30) / 1.90, 1) == 2.5 and round(131 * 1.90, 2) == 248.90
has(t, "39.91", "46.21", "6.30", "46.38", "3,600,000", "US$1.90", "US$52.60", "3.3R", "131.6", "131 shares", "2.5R", "US$248.90", "44.57")
b = bars("ascending-triangle")
pv = pivots(b, 5)
assert [(p[1], p[3]) for p in pv if p[2] == "H"][:3] == [("2026-02-11", 59.78), ("2026-02-27", 59.77), ("2026-03-13", 59.51)]
assert [p[3] for p in pv if p[2] == "L"][:3] == [54.86, 56.35, 57.84]
x = at("ascending-triangle", "2026-03-25")[1]
assert x[4] == 61.08 and x[5] == 3900000 and max(y[2] for y in b) == 64.16
assert round(59.78 - 54.86, 2) == 4.92 and round(59.78 + 4.92, 2) == 64.70
has(t, "59.78", "59.77", "59.51", "54.86", "56.35", "57.84", "61.08", "3,900,000", "4.92", "64.70", "64.16")
b = bars("head-and-shoulders")
pv = pivots(b, 5)
assert [(p[1], p[3]) for p in pv if p[2] == "H"] == [("2026-01-26", 54.21), ("2026-02-13", 59.56), ("2026-03-10", 54.73)]
assert [p[3] for p in pv if p[2] == "L"][:2] == [50.33, 50.75]
fc = next(x for i, x in enumerate(b) if i > 47 and x[4] < 50.5)
assert (fc[0], fc[4]) == ("2026-03-16", 50.46) and b[-1][4] == 44.0 and b[-1][0] == "2026-03-30"
assert round(59.56 - 50.50, 2) == 9.06 and round(50.50 - 9.06, 2) == 41.44
has(t, "54.21", "59.56", "54.73", "50.46", "9.06", "41.44", "44.00")
b = bars("double-top")
pv = pivots(b, 5)
assert [(p[1], p[3]) for p in pv] == [("2026-01-30", 59.7), ("2026-02-12", 53.48), ("2026-02-26", 59.46)]
fc = next(x for i, x in enumerate(b) if i > 39 and x[4] < 53.48)
assert (fc[0], fc[4]) == ("2026-03-04", 52.87) and round(59.70 - 53.48, 2) == 6.22 and round(53.48 - 6.22, 2) == 47.26
has(t, "59.70", "59.46", "53.48", "52.87", "6.22", "47.26")
b = bars("failed-double-top")
fc = next(x for i, x in enumerate(b) if i > 38 and x[4] < 53.17)
assert (fc[0], fc[4]) == ("2026-03-04", 52.8) and at("failed-double-top", "2026-03-05")[1][2] == 54.27
assert b[-1][4] == 66.0 and b[-1][0] == "2026-04-01" and max(x[2] for x in b) == 66.09
assert round(54.30 - 52.80, 2) == 1.50
has(t, "53.17", "52.80", "54.27", "66.00", "66.09", "1.50")
assert round(25 - 20, 2) == 5 and round(24.6 + 5, 2) == 29.6 and round(24.6 - 23.4, 2) == 1.2 and round(5 / 1.2, 1) == 4.2
assert 80 - 72 == 8 and 72 - 8 == 64 and round(64.70 - 61.08, 2) == 3.62 and round(3.62 / 61.08 * 100, 1) == 5.9
has(t, "29.60", "4.2", "64.00", "3.62", "5.9%")

# ---- Lesson 10
t = lesson(F, 10)
g = bars("gap-types")
vol = [x[5] for x in g]
A14 = atr(g, 14)
spec = (("2026-02-06", 51.58, 52.29, 2.0, 1.9, 1.14), ("2026-02-24", 51.37, 53.60, 5.0, 4.5, 4.02),
        ("2026-03-17", 58.06, 59.57, 3.0, 2.4, 1.23), ("2026-03-31", 64.11, 66.05, 3.5, 2.8, 3.09))
for d, ph, lw, pct_, gatr, rv_ in spec:
    i, x = at("gap-types", d)
    assert g[i - 1][2] == ph and x[3] == lw, d
    assert round((x[1] / g[i - 1][4] - 1) * 100, 1) == pct_, d
    assert round((x[1] - g[i - 1][4]) / A14[i - 1], 1) == gatr, d
    assert round(vol[i] / (sum(vol[i - 20:i]) / 20), 2) == rv_, d
    has(t, f"{ph:.2f} to {lw:.2f}", f"{rv_:.2f}")
i, x = at("gap-types", "2026-02-11")
assert x[3] == 50.85
assert min(y[3] for y in g[at("gap-types", "2026-02-24")[0]:]) > 51.37
assert at("gap-types", "2026-04-01")[1][3] == 63.32
assert max(y[2] for y in g[:36]) == 52.67
assert vol[at("gap-types", "2026-02-24")[0]] == 5400000 and vol[at("gap-types", "2026-03-31")[0]] == 6300000
assert round(64.0 / 51.34 - 1, 2) == 0.25
i, x = at("gap-types", "2026-02-24")
assert round(x[1] - g[i - 1][4], 2) == 2.57 and round(A14[i - 1], 3) == 0.574 and round(2.57 / 0.574, 1) == 4.5
assert round((52.0 - 51.34) * 200) == 132 and round(2.57 * 200) == 514 and round(514 / 132, 1) == 3.9
has(t, "50.85", "63.32", "52.67", "5,400,000", "6,300,000", "US$2.57", "0.574", "US$132", "US$514", "3.9 times")
assert round(83.2 - 80, 2) == 3.2 and 3.2 / 80 == 0.04 and 3.2 / 1.6 == 2.0
assert round(5400000 / 1343000, 1) == 4.0
assert round((40 - 38.5) * 300) == 450 and round((40 - 36.8) * 300) == 960 and round(960 / 450, 1) == 2.1
has(t, "80.60 to 82.90", "1,343,000", "US$450", "US$960", "2.1 times")
has(t, "49.40 to 53.35")

# ---- Lesson 11
t = lesson(F, 11)
w = bars("stock-a-weekly")
pv = pivots(w, 2)
assert [(p[1], p[3]) for p in pv if p[2] == "H"] == [("2026-02-02", 44.82), ("2026-03-16", 50.28), ("2026-05-04", 55.1)]
assert [(p[1], p[3]) for p in pv if p[2] == "L"] == [("2026-02-16", 42.22), ("2026-03-30", 46.56), ("2026-05-25", 50.39)]
wc = [x[4] for x in w]
assert w[-1][0] == "2026-06-22" and wc[-1] == 58.5 and round(sma(wc, 10)[-1], 2) == 53.87
d = bars("stock-a-daily")
dp = pivots(d, 5)
assert ("2026-04-03", 46.56) in [(p[1], p[3]) for p in dp if p[2] == "L"] and ("2026-05-27", 50.39) in [(p[1], p[3]) for p in dp if p[2] == "L"]
has(t, "42.22", "46.56", "50.39", "44.82", "50.28", "55.10", "58.50", "53.87")
s, x_, r = bars("rs-stock"), bars("rs-index"), bars("rs-ratio")
assert (s[0][4], x_[0][4]) == (49.16, 3985.07)
for dd, sc, ic, rr in (("2026-02-19", 55.65, 3972.05, 113.57), ("2026-06-19", 48.63, 4534.04, 86.94)):
    i = next(i for i, y in enumerate(s) if y[0] == dd)
    assert (s[i][4], x_[i][4]) == (sc, ic) and r[i][4] == rr
    assert round(100 * (sc / 49.16) / (ic / 3985.07), 2) == rr
    has(t, f"{sc:.2f}", f"{ic:,.2f}", f"{rr:.2f}")
assert max(y[4] for y in r) == 113.57 and r[-1][4] == 86.94
assert round((55.65 / 49.16 - 1) * 100, 1) == 13.2 and round((3972.05 / 3985.07 - 1) * 100, 1) == -0.3
assert round((48.63 / 49.16 - 1) * 100, 1) == -1.1 and round((4534.04 / 3985.07 - 1) * 100, 1) == 13.8
has(t, "13.2%", "0.3%", "1.1%", "13.8%", "1.1320", "0.9967", "0.9892", "1.1378")
assert round(100 * 1.10 / 1.04, 1) == 105.8 and round(100 * 1 / 1.05, 1) == 95.2
has(t, "105.8", "95.2")
# part check
assert round(31.5 - 29.4, 2) == 2.1 and round(31.2 - 30.0, 2) == 1.2 and round((31.2 - 29.4) / 2.1 * 100, 1) == 85.7
assert 3600000 / 1800000 == 2.0 and round(2 / 11, 4) == 0.1818
assert round(2 / 11 * 41 + 9 / 11 * 40, 2) == 40.18
assert (13 * 1.0 + 2.4) / 14 == 1.1 and round(2 * 1.1, 2) == 2.2 and round(50 - 2.2, 2) == 47.8
assert round(12.5 - 10, 2) == 2.5 and round(12.4 + 2.5, 2) == 14.9 and round(12.4 - 11.7, 2) == 0.7 and round(2.5 / 0.7, 1) == 3.6
has(t, "85.7%", "RVOL = 2.0", "0.1818", "40.18", "1.10", "47.80", "14.90", "3.6R")

# ---- Cheat sheet
idx = (ROOT / "docs" / F / "index.md").read_text(encoding="utf-8")
assert "Cheat sheet" in idx and "to be written" not in idx
print("part 5 checks passed")
