"""Number checks for part 7, Swing trading. The worked trades are recomputed from the chart data."""
import math

import pandas as pd

from _lib import ROOT, lesson, has, usd
from swng_lib import Bars, sma, atr
from swng_trades import pullback, breakout, rsi2_trade, floor2, r2

F = "07-swing-trading"


def approx(a, b, tol=0.005):
    assert abs(a - b) <= tol, (a, b)


# ---------------------------------------------------------------- lesson 1
t = lesson(F, 1)
a = pullback("stock-a-pullback-win", 64)
assert a["date_entry"] == "2026-04-06" and a["date_exit"] == "2026-04-10"
has(t, "52.81", "56.80", "US$3.99", "four nights", "5 trading days")
assert len(Bars("stock-a-pullback-win").t[65:70]) == 5
approx(a["exit"] - a["entry"], 3.99)

# ---------------------------------------------------------------- lesson 2
t = lesson(F, 2)
assert 1_500_000 * 50 == 75_000_000
assert 400_000 * 30 == 12_000_000
approx(1.20 / 80 * 100, 1.5)
b = Bars("stock-a-pullback-win")
close = b.c[64]
pc = [None] + b.c[:-1]
tr = [b.h[0] - b.l[0]] + [max(b.h[i] - b.l[i], abs(b.h[i] - b.c[i - 1]), abs(b.l[i] - b.c[i - 1])) for i in range(1, b.n)]
atr_plain = sum(tr[51:65]) / 14
avgvol = sum(b.v[15:65]) / 50
dv = sum(b.c[i] * b.v[i] for i in range(15, 65)) / 50
approx(atr_plain, 1.0479, 0.0001)
assert round(avgvol) == 1_470_018, avgvol
approx(dv / 1e6, 74.4, 0.05)
approx(atr_plain / close * 100, 1.99, 0.005)
has(t, "US$52.60", "1,470,018", "US$1.0479", "US$74.4 million", "1.0479 / 52.60 = 1.99%",
    "2026-04-03 52.6 1.05 1.99", "then 74.4", "1,500,000 x 50 = US$75 million",
    "US$12 million", "1.20 / 80.00 = 1.5%")
df = pd.read_csv(ROOT / "docs" / "assets" / "data" / "stock-a-pullback-win.csv")
assert df.loc[64, "date"] == "2026-04-03"

# ---------------------------------------------------------------- lesson 3
t = lesson(F, 3)
ix = Bars("index-x-regime")
s200 = ix.sma(200)
below = [i for i in range(199, ix.n) if ix.c[i] <= s200[i]]
first = below[0]
assert ix.t[first] == "2025-12-16"
back = next(i for i in range(first + 1, ix.n) if ix.c[i] > s200[i])
assert ix.t[back] == "2026-04-27" and back - first == 94
cross = [ix.t[i] for i in range(back + 1, ix.n) if (ix.c[i] > s200[i]) != (ix.c[i - 1] > s200[i - 1])]
assert cross == ["2026-05-01", "2026-05-04", "2026-05-06", "2026-05-07"], cross
assert ix.t[back + 4] == "2026-05-01" and all(ix.c[i] > s200[i] for i in range(back, back + 4))
pk = max(range(ix.n), key=lambda i: ix.c[i])
assert ix.t[pk] == "2025-11-20" and ix.c[pk] == 4759.80
mn = min(range(ix.n), key=lambda i: ix.c[i])
assert ix.t[mn] == "2026-01-23" and ix.c[mn] == 3347.24
approx(100 * (1 - ix.c[first] / ix.c[pk]), 12.3, 0.05)
approx(100 * (1 - ix.c[mn] / ix.c[pk]), 29.7, 0.05)
approx(s200[first], 4206.06, 0.006)
approx(s200[back], 4007.10, 0.006)
i7 = ix.i("2025-11-07")
approx(s200[i7], 4130.17, 0.006)
assert ix.c[i7] == 4515.79
approx(s200[first] - ix.c[first], 32.22, 0.01)
approx(100 * (s200[first] - ix.c[first]) / s200[first], 0.77, 0.005)
approx(ix.c[back] - s200[back], 7.21, 0.01)
approx(50 / 4150 * 100, 1.2, 0.005)
approx(84 / 200 * 100, 42, 0.001)
dfi = pd.read_csv(ROOT / "docs" / "assets" / "data" / "index-x-daily.csv", parse_dates=["date"])
dfi["sma200"] = dfi["close"].rolling(200).mean()
valid = dfi.dropna(subset=["sma200"])
fb = valid[valid["close"] <= valid["sma200"]].iloc[0]
ba_ = valid[(valid["date"] > fb["date"]) & (valid["close"] > valid["sma200"])].iloc[0]
code_line = f"{fb['date'].date()} {fb['close']} {round(fb['sma200'], 2)}"
code_line2 = f"{ba_['date'].date()} {ba_['close']} {round(ba_['sma200'], 2)}"
print(code_line, code_line2)
has(t, code_line, code_line2)
has(t, "4,759.80", "4,173.84", "4,206.06", "12.3%", "3,347.24", "29.7%", "4,014.31", "4,007.10", "94 sessions", "May 1, 4, 6 and 7",
    "4,515.79", "4,130.17", "32.22 points (0.77%)", "7.21 points", "1.2%", "84 / 200 = 42%")

# ---------------------------------------------------------------- lesson 4
t = lesson(F, 4)
assert a["why"] == "target" and a["day"] == 69
assert (a["H"], a["L"], a["entry"], a["stop"], a["shares"]) == (56.8, 51.3, 52.81, 51.05, 142)
approx(a["atr"], 0.9758, 0.0001)
approx(a["e20_at_low"], 53.05, 0.006)
approx(a["s50"], 50.62, 0.006)
approx(a["stop_raw"], 51.056, 0.0005)
approx((a["H"] - a["entry"]) / a["risk"], 2.27, 0.005)
approx(a["cost"], 7499.02, 0.005)
approx(a["risk_usd"], 249.92, 0.005)
approx(a["pl"], 566.58, 0.005)
approx(a["R"], 2.27, 0.005)
has(t, "US$56.80", "51.30", "53.05", "50.62", "52.81", "0.9758", "51.056", "US$51.05", "US$1.76", "US$3.99", "2.27R",
    "142.05", "142 shares", usd(a["cost"]), usd(a["risk_usd"]), usd(a["pl"]), "52.50", "52.80")
bb = pullback("stock-b-pullback-loss", 64)
assert bb["why"] == "stop gap" and bb["exit"] == 34.47 and bb["shares"] == 204
assert (bb["entry"], bb["stop"], bb["H"], bb["L"]) == (35.84, 34.62, 38.54, 34.81)
approx(bb["atr"], 0.7427, 0.0001)
approx(bb["e20_at_low"], 35.62, 0.006)
approx(bb["s50"], 33.16, 0.006)
approx((bb["H"] - bb["entry"]) / bb["risk"], 2.21, 0.005)
approx(bb["pl"], -279.48, 0.005)
approx(bb["R"], -1.12, 0.005)
approx(250 / 1.22, 204.9, 0.05)
has(t, "US$38.54", "34.81", "35.62", "33.16", "US$35.84", "0.7427", "34.624", "US$34.62", "US$1.22", "2.21R", "204.9", "204 shares",
    "US$34.47", "-US$279.48", "-1.12R", "35.69", "35.63", "35.83")
# exercises
approx(28.90 - 0.25 * 0.60, 28.75)
approx(30.20 - 28.75, 1.45)
approx((33.50 - 30.20) / 1.45, 2.28, 0.005)
approx(0.005 * 40_000 / 1.45, 137.9, 0.05)
approx((52.81 - 50.90) * 142, 271.22, 0.005)
approx((52.81 - 50.90) / 1.76, 1.09, 0.005)
has(t, "US$1.45", "2.28R", "137.9", "137 shares", "US$271.22", "-1.09R", "1.5R")
p = pd.read_csv(ROOT / "docs" / "assets" / "data" / "stock-a-pullback-win.csv", parse_dates=["date"]).set_index("date")
pcl = p["close"].shift()
trr = pd.concat([p["high"] - p["low"], (p["high"] - pcl).abs(), (p["low"] - pcl).abs()], axis=1).max(axis=1)
atr_e = trr.ewm(alpha=1 / 14, adjust=False).mean()
trig = pd.Timestamp("2026-04-03")
ent = round(p.loc[trig, "high"] + 0.01, 2)
lw = p.loc["2026-03-27":"2026-04-03", "low"].min()
st = math.floor((lw - 0.25 * atr_e[trig]) * 100) / 100
sh = math.floor(0.01 * 25_000 / (ent - st))
assert (ent, round(lw, 2), st, sh) == (52.81, 51.3, 51.05, 142), (ent, lw, st, sh)
has(t, "52.81 51.3 51.05 142")

# ---------------------------------------------------------------- lesson 5
t = lesson(F, 5)
ba = breakout("stock-a-base-breakout", 104, 73)
assert ba["why"] == "target" and ba["date_exit"] == "2026-04-08"
assert (ba["pivot"], ba["entry"], ba["stop"], ba["target"], ba["shares"], ba["nbase"]) == (40.69, 41.59, 40.06, 46.18, 163, 31)
approx(ba["depth"] * 100, 10.1, 0.05)
approx(ba["relvol"], 3.58, 0.005)
approx(ba["atr"], 0.6248, 0.0001)
assert round(ba["avgvol"]) == 1_090_605
approx(ba["pivot"] + 2 * ba["atr"], 41.94, 0.006)
approx(ba["cost"], 6779.17, 0.005)
approx(ba["risk_usd"], 249.39, 0.005)
approx(ba["pl"], 748.17, 0.005)
approx(ba["R"], 3.0, 0.005)
approx(250 / 1.53, 163.4, 0.05)
bar_ = ba["bars"]
assert bar_.t[105] == "2026-03-30" and bar_.o[112] == 45.49 and bar_.h[112] == 46.47
has(t, "US$40.69", "31 bars", "36.57", "10.1%", "41.46", "40.61", "41.75", "3.9 million", "1,090,605", "3.58 times", "0.6248",
    "US$41.59", "41.94", "40.065", "US$40.06", "US$1.53", "US$46.18", "163.4", "163 shares", usd(ba["cost"]), usd(ba["risk_usd"]),
    "45.49", "46.47", usd(ba["pl"]), "+3.0R", "31 40.69 3.58")
bf = breakout("stock-b-breakout-fail", 104, 74)
assert bf["why"] == "rule at open" and bf["date_exit"] == "2026-04-16"
assert (bf["pivot"], bf["entry"], bf["stop"], bf["target"], bf["shares"], bf["exit"], bf["nbase"]) == (31.13, 31.94, 30.68, 35.72, 198, 30.91, 30)
approx(bf["depth"] * 100, 8.0, 0.05)
approx(bf["relvol"], 2.62, 0.005)
approx(bf["atr"], 0.4468, 0.0001)
approx(bf["pl"], -203.94, 0.005)
approx(bf["R"], -0.82, 0.005)
b2 = bf["bars"]
assert b2.c[107] < 31.13 and b2.l[107] > 30.68 and b2.t[107] == "2026-04-15" and b2.c[107] == 31.01 and b2.l[107] == 30.94
assert b2.l[108] < 30.68  # the stop would have filled on April 16 instead, at -1R
has(t, "US$31.13", "28.63", "8.0%", "31.75", "2.62", "0.4468", "30.683", "US$30.68", "US$35.72", "198.4", "198 shares", "31.01", "30.94",
    "US$30.91", "-US$203.94", "-0.82R", "0.18R")
approx(0.3 * 3 - 0.7, 0.2)
approx(0.25 * 3 - 0.75, 0.0)
# exercises
assert 60 + 2 * 1.2 == 62.4
approx(61.30 - 58.80, 2.5)
approx(61.30 + 3 * 2.5, 68.80)
approx(2.4 / 1.8, 1.33, 0.005)
has(t, "62.40", "US$2.50", "US$68.80", "80 shares", "1.33", "+0.20R")
c5 = pd.read_csv(ROOT / "docs" / "assets" / "data" / "stock-a-base-breakout.csv", parse_dates=["date"]).set_index("date")
bs = c5.loc["2026-02-12":"2026-03-26"]
tg = pd.Timestamp("2026-03-27")
rv = c5.loc[tg, "volume"] / c5["volume"].shift(1).rolling(20).mean()[tg]
assert (len(bs), bs["high"].max(), round(rv, 2)) == (31, 40.69, 3.58)

# ---------------------------------------------------------------- lesson 6
t = lesson(F, 6)
ra = rsi2_trade("stock-a-rsi2-win", 240)
assert ra["why"] == "rule at close" and ra["date_exit"] == "2026-03-05"
assert (ra["entry"], ra["stop"], ra["shares"], ra["exit"]) == (56.41, 54.52, 132, 58.48)
approx(ra["rsi"], 4.47, 0.005)
approx(ra["atr"], 0.9447, 0.0001)
approx(ra["s200"], 47.17, 0.006)
approx(ra["cost"], 7446.12, 0.005)
approx(ra["risk_usd"], 249.48, 0.005)
approx(ra["pl"], 273.24, 0.005)
approx(ra["R"], 1.10, 0.005)
rb = Bars("stock-a-rsi2-win")
r = rb.rsi(2)
approx(r[239], 10.32, 0.005)
s5 = rb.sma(5)
approx(s5[241], 57.84, 0.006)
approx(s5[242], 57.70, 0.006)
# the averages in the lesson
c = rb.c
ag_prev, al_prev = 0.0788, 0.6842
ag_new, al_new = ag_prev / 2, (al_prev + 1.00) / 2
approx(ag_new, 0.0394, 0.0001)
approx(al_new, 0.8421, 0.0001)
approx(ag_new / al_new, 0.0468, 0.0001)
approx(100 - 100 / (1 + 0.0394 / 0.8421), 4.47, 0.005)
approx(c[239] - c[238], -0.95, 0.005)
approx(c[240] - c[239], -1.00, 0.005)
has(t, "57.53", "-0.95", "10.32", "56.53", "0.0788", "0.6842", "0.0394", "0.8421", "0.0468", "4.47", "47.17", "US$56.41", "0.9447",
    "54.52", "US$1.89", "132.3", "132 shares", usd(ra["cost"]), usd(ra["risk_usd"]), "57.84", "58.48", "57.70", usd(ra["pl"]), "+1.10R",
    "The code prints 4.47 and 47.17")
rl = rsi2_trade("stock-b-rsi2-loss", 240)
assert rl["why"] == "stop" and rl["date_exit"] == "2026-03-18"
assert (rl["entry"], rl["stop"], rl["shares"], rl["exit"]) == (53.55, 51.78, 141, 51.78)
approx(rl["rsi"], 5.8, 0.05)
approx(rl["atr"], 0.8826, 0.0001)
approx(rl["s200"], 42.52, 0.006)
approx(rl["pl"], -249.57, 0.005)
approx(rl["R"], -1.0, 0.005)
rlb = rl["bars"]
assert rlb.o[242] == 52.42 and rlb.l[242] == 51.01 and rlb.c[241] == 52.76
approx(250 / 1.77, 141.2, 0.05)
has(t, "53.83", "5.8", "42.52", "US$53.55", "0.8826", "51.78", "US$1.77", "141.2", "141 shares", "52.76", "52.42", "51.01", "-US$249.57", "-1.00R")
# exercises
approx(100 - 100 / (1 + (0.05 / 0.55)), 8.33, 0.005)
has(t, "8.33", "38.50", "US$1.50", "200 shares")
approx(40.00 - 2 * 0.75, 38.50)
assert math.floor(300 / 1.50) == 200
rr = pd.read_csv(ROOT / "docs" / "assets" / "data" / "stock-a-rsi2.csv", parse_dates=["date"]).set_index("date")
ch = rr["close"].diff()
g, l = ch.clip(lower=0), (-ch).clip(lower=0)
ag = g.iloc[1:].ewm(alpha=0.5, adjust=False).mean()
al = l.iloc[1:].ewm(alpha=0.5, adjust=False).mean()
rs2 = 100 - 100 / (1 + ag / al)
day = pd.Timestamp("2026-03-03")
assert (round(rs2[day], 2), round(rr["close"].rolling(200).mean()[day], 2)) == (4.47, 47.17)

# ---------------------------------------------------------------- lesson 7
t = lesson(F, 7)
risk = a["risk"]
assert round(risk, 2) == 1.76
# entries
op = b.o[65]
assert op == 52.70 and b.l[65] == 52.55 and b.h[65] == 53.60
risk_open = round(52.70 - 51.05, 2)
sh_open = math.floor(250 / risk_open)
assert (risk_open, sh_open) == (1.65, 151)
approx((56.80 - 52.70) / 1.65, 2.48, 0.005)
approx(a["bars"].l[65], 52.55)
assert a["bars"].l[65] > 52.00
# stops
atr64 = a["atr"]
st2 = floor2(52.81 - 2 * atr64)
assert st2 == 50.85
r2s = round(52.81 - st2, 2)
sh2 = math.floor(250 / r2s)
assert (r2s, sh2) == (1.96, 127)
approx(3.99 / 1.96, 2.04, 0.005)
# targets
t2, t3 = 52.81 + 2 * 1.76, 52.81 + 3 * 1.76
approx(t2, 56.33)
approx(t3, 58.09)
first_hit = lambda lvl: next(i for i in range(65, b.n) if b.h[i] >= lvl)
assert b.t[first_hit(t2)] == "2026-04-10" and b.t[first_hit(56.80)] == "2026-04-10" and b.t[first_hit(t3)] == "2026-04-14"
approx(1 / 3 * 100, 33.3, 0.05)
has(t, "52.70", "52.55", "53.60", "1.65", "151", "2.48R", "2.27R", "50.85", "1.96", "127", "2.04R", "15 fewer shares", "56.33", "58.09",
    "April 14", "33.3%", "25%", "50%", "51.056", "249.92")
# exercises
trig_high, low, atr_x = 24.60, 23.20, 0.50
assert round(trig_high + 0.01, 2) == 24.61
assert floor2(low - 0.25 * atr_x) == 23.07
approx(24.61 - 23.07, 1.54)
approx(24.61 + 3 * 1.54, 29.23)
assert math.floor(300 / 1.54) == 194
approx(1 / (1 + 1.5), 0.40)
approx(53.40 - 51.05, 2.35)
assert math.floor(250 / 2.35) == 106
approx((56.80 - 53.40) / 2.35, 1.45, 0.005)
has(t, "24.61", "23.075", "23.07", "US$1.54", "US$29.23", "194", "40%", "US$2.35", "106 shares", "1.45R")

# ---------------------------------------------------------------- lesson 8
t = lesson(F, 8)
ab = a["bars"]
at14 = ab.atr(14)
ema20 = ab.ema(20)
entry, stop_ = a["entry"], a["stop"]
trail = stop_
hc = ab.c[65]
trail_exit = None
for d in range(65, ab.n):
    hc = max(hc, ab.c[d])
    if d > 65 and ab.l[d] <= trail:
        trail_exit = (d, round(trail, 2))
        break
    trail = max(trail, hc - 2 * at14[d])
assert trail_exit is not None and ab.t[trail_exit[0]] == "2026-04-21" and trail_exit[1] == 57.24
approx(ab.c[73], 59.30)
assert ab.h[73] == 59.6 and max(ab.c[65:76]) == 59.3
assert ab.o[76] == 57.5 and ab.l[76] == 56.4
pl_trail = (57.24 - entry) * 142
approx(pl_trail, 629.06, 0.005)
approx((57.24 - entry) / 1.76, 2.52, 0.005)
sig = next(d for d in range(65, ab.n) if ab.c[d] < ema20[d])
assert ab.t[sig] == "2026-04-22" and ab.c[sig] == 55.60
approx(ema20[sig], 55.92, 0.006)
assert ab.o[sig + 1] == 55.50 and ab.t[sig + 1] == "2026-04-23"
pl_ema = (55.50 - entry) * 142
approx(pl_ema, 381.98, 0.005)
approx((55.50 - entry) / 1.76, 1.53, 0.005)
loss_gap = (52.81 - 50.60) * 142
approx(loss_gap, 313.82, 0.005)
approx((52.81 - 50.60) / 1.76, 1.26, 0.005)
approx(loss_gap - 249.92, 63.90, 0.005)
approx((52.81 - 50.60) * 71, 156.91, 0.005)
approx(50.60 / 55.00, 0.92, 0.0005)
has(t, "US$566.58", "+2.27R", "59.30", "59.60", "57.24", "US$629.06", "+2.52R", "55.60", "55.92", "55.50", usd(pl_ema), "+1.53R",
    "US$50.60", "US$313.82", "-1.26R", "US$63.90", "US$156.91", "8.0%")
# in code
pe = pd.read_csv(ROOT / "docs" / "assets" / "data" / "stock-a-pullback-win.csv", parse_dates=["date"]).set_index("date")
ema_c = pe["close"].ewm(span=20, adjust=False).mean()
dd = pd.Timestamp("2026-04-22")
exit_p = pe["open"].shift(-1)[dd]
out1 = (pe.loc[dd, "close"], round(ema_c[dd], 2))
out2 = (exit_p, round((exit_p - 52.81) / 1.76, 2), round((exit_p - 52.81) * 142, 2))
has(t, f"The code prints {out1[0]} {out1[1]} and then {out2[0]} {out2[1]} {out2[2]}")
# exercises
approx(2.50 / 1.00, 2.5)
approx(30.00 - 2 * 0.80, 28.40)
approx((40.00 - 36.00) * 200, 800)
has(t, "US$20.00", "2.5R", "28.40", "27.90", "US$800", "-2.0R")

# ---------------------------------------------------------------- lesson 9
t = lesson(F, 9)
heat = (249.92 + 249.39 + 249.48)
approx(heat, 748.79, 0.005)
approx(heat / 25_000 * 100, 3.0, 0.01)
approx((heat + 250) / 25_000 * 100, 4.0, 0.01)
approx(670 / 30_000 * 100, 2.23, 0.005)
approx(970 / 30_000 * 100, 3.23, 0.005)
assert 5 * 15 + 30 == 105
assert 600_000 * 45 == 27_000_000
approx((4150 - 4100) / 4150 * 100, 1.2, 0.005)
assert math.floor(round(0.01 * 20_000 / round(25.50 - 24.70, 2), 6)) == 250
approx((28.00 - 25.50) / 0.80, 3.1, 0.05)
approx(50 + 2 * 1.0, 52.0)
approx(51.20 + 3 * 2.20, 57.80)
approx(1 / (1 + 3) * 100, 25)
has(t, "US$748.79", "3.0%", "(748.79 + 250) / 25,000 = 4.0%", "2.23%", "3.23%", "105 minutes", "US$27 million", "1.2%", "3.1R", "US$57.80", "25%",
    "US$249.92, US$249.39 and US$249.48")

# the chart drill sets exist and the lessons point to them
print("ok part 7")
