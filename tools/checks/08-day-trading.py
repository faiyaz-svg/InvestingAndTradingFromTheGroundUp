"""Number checks for part 8, Day trading."""
import csv
import json
from datetime import datetime, timezone

from _lib import ROOT, lesson, has, pct

F = "08-day-trading"
CH = ROOT / "docs" / "assets" / "charts" / F


def bars(name):
    return json.loads((CH / f"{name}.json").read_text(encoding="utf-8"))["bars"]


def hm(t):
    return datetime.fromtimestamp(t, tz=timezone.utc).strftime("%H:%M")


def approx(a, b, tol=0.005):
    assert abs(a - b) <= tol, (a, b)


def vwaps(b):
    pv = v = 0.0
    out = []
    for t, o, h, lo, c, vol in b:
        pv += (h + lo + c) / 3 * vol
        v += vol
        out.append(pv / v)
    return out


# ---- Lesson 1
t = lesson(F, 1)
for stop, shares, val, cost in ((2.00, 125, 6250, 0.025), (0.60, 416, 20800, 0.0833)):
    assert int(250 / stop) == shares and shares * 50 == val
    approx(0.05 / stop, cost, 0.0005)
has(t, "US$6,250", "US$20,800", "0.025R", "0.083R", "125", "416 shares")
assert 625 * 50 == 31250
has(t, "US$31,250")
b = bars("day-rhythm")
tot = sum(x[5] for x in b)
f6, l6 = sum(x[5] for x in b[:6]), sum(x[5] for x in b[-6:])
mid = sum(x[5] for x in b[30:36])
assert hm(b[30][0]) == "12:00" and hm(b[35][0]) == "12:25"
assert pct(f6 / tot) == "14.5%" and pct(l6 / tot) == "12.6%" and pct(mid / tot) == "5.1%"
approx(f6 / 6, 194583, 1)
approx(mid / 6, 67967, 1)
assert round(f6 / mid, 1) == 2.9
assert max(x[2] for x in b) == 52.07 and min(x[3] for x in b) == 49.71
has(t, "14.5%", "5.1%", "12.6%", "194,583", "67,967", "2.9 times", "52.07", "49.71")
assert 200 / 0.50 == 400 and 400 * 30 == 12000
assert round(0.04 / 0.40, 2) == 0.10 and round(0.04 / 2.00, 2) == 0.02
approx(30 / 390 * 100, 7.7, 0.05)
assert round(14.5 / 7.7, 1) == 1.9
has(t, "US$12,000", "0.10R", "0.02R", "7.7%", "1.9 times")

# ---- Lesson 2
t = lesson(F, 2)
d = bars("premarket-gapper")
d1, d2 = d[:78], d[78:]
v1, v2 = sum(x[5] for x in d1), sum(x[5] for x in d2)
assert (v1, v2) == (2740900, 15955800)
assert d1[-1][4] == 19.97 and d2[0][1] == 21.57
assert max(x[2] for x in d1) == 20.06 and min(x[3] for x in d1) == 19.77
assert d2[0][2:5] == [21.8, 21.45, 21.7]
assert pct((21.57 - 19.97) / 19.97) == "8.0%"
assert pct(685000 / 2740900) == "25.0%"
has(t, "2,740,900", "15,955,800", "19.97", "21.57", "8.0%", "25.0%", "20.06", "19.77", "21.45", "21.80")
risk = 21.81 - 21.43
assert round(risk, 2) == 0.38
approx((21.90 - 21.81) / risk, 0.24, 0.005)
assert round(21.81 + 2 * 0.38, 2) == 22.57
assert round(21.91 - 21.43, 2) == 0.48
has(t, "US$0.38", "0.24R", "US$22.57", "21.43", "risk 0.48")
assert pct((42.60 - 40) / 40) == "6.5%"
assert pct(450000 / 3000000) == "15.0%"
approx((23.20 - 21.91) / 0.48, 2.69, 0.005)
has(t, "6.5%", "15.0%", "2.69R")

# ---- Lesson 3
t = lesson(F, 3)
v = bars("vwap-1m")
assert len(v) == 120 and sum(x[5] for x in v) == 4054500
vw = vwaps(v)
approx(vw[-1], 80.6114, 0.00005)
assert v[-1][4] == 81.20 and round(81.20 - vw[-1], 2) == 0.59
V = sum(x[5] for x in v)
PV = vw[-1] * V
new = (PV + 81.5 * 20000) / (V + 20000)
approx(new, 80.6158, 0.00005)
approx(new - vw[-1], 0.0044, 0.00005)
approx(vw[29], 80.4996, 0.00005)
V30 = sum(x[5] for x in v[:30])
assert V30 == 1854500
early = 20000 * (81.5 - vw[29]) / (V30 + 20000)
approx(early, 0.0107, 0.00005)
has(t, "4,054,500", "80.6114", "80.6158", "0.0044", "1,854,500", "0.0107", "81.20", "80.61")
assert (50.00 * 1000 + 50.10 * 2000 + 50.20 * 1000) / 4000 == 50.10
approx((40 * 2e6 + 41 * 1e5) / 2.1e6, 40.0476, 0.00005)
has(t, "US$50.10", "40.0476")
rows = list(csv.DictReader(open(ROOT / "docs" / "assets" / "data" / "stock-a-1m.csv")))
assert len(rows) == 120

# ---- Lesson 4
t = lesson(F, 4)
w = bars("orb-win")
first = w[0]
assert first[1:5] == [42.40, 42.90, 42.30, 42.80]
trig, stop = round(42.90 + 0.01, 2), round(42.30 - 0.02, 2)
risk = round(trig - stop, 2)
assert (trig, stop, risk) == (42.91, 42.28, 0.63)
sh = int(250 / risk)
assert sh == 396
R1 = sh * risk
val = sh * trig
tgt = round(trig + 2 * risk, 2)
assert round(R1, 2) == 249.48 and round(val, 2) == 16992.36 and tgt == 44.17
ent = next(i for i, x in enumerate(w[1:], 1) if x[2] >= trig)
assert hm(w[ent][0]) == "09:55"
assert max(x[2] for x in w[1:ent]) < trig and min(x[3] for x in w[1:ent]) > stop
ex = next(i for i, x in enumerate(w[ent:], ent) if x[2] >= tgt)
assert hm(w[ex][0]) == "11:05"
assert min(x[3] for x in w[ent:ex + 1]) > stop
fees = 2 * sh * 0.005
gross = sh * (tgt - trig)
net = gross - fees
assert round(fees, 2) == 3.96 and round(gross, 2) == 498.96 and round(net, 2) == 495.00
approx(net / R1, 1.98, 0.005)
approx(gross / R1, 2.00, 0.005)
has(t, "42.91", "42.28", "US$0.63", "396", "US$249.48", "US$16,992.36", "US$44.17", "3.96", "US$498.96", "US$495.00", "+1.98R", "+2.00R", "9:55", "11:05")
f = bars("orb-fail")
assert f[0][1:5] == [30.60, 31.00, 30.55, 30.95]
trig, stop = 31.01, round(30.55 - 0.02, 2)
risk = round(trig - stop, 2)
assert (stop, risk) == (30.53, 0.48)
sh = int(250 / risk)
assert sh == 520
R2 = sh * risk
assert round(R2, 2) == 249.60
ent = next(i for i, x in enumerate(f[1:], 1) if x[2] >= trig)
assert hm(f[ent][0]) == "09:50" and f[ent][2] == 31.12 and f[ent][4] == 30.90
sx = next(i for i, x in enumerate(f[ent:], ent) if x[3] <= stop)
assert hm(f[sx][0]) == "10:15" and f[sx][3] == 30.37
loss = (trig - 30.50) * sh
assert round(loss, 2) == 265.20
tot = loss + 2 * sh * 0.005
assert round(tot, 2) == 270.40
approx(-tot / R2, -1.08, 0.005)
has(t, "30.53", "US$249.60", "US$265.20", "US$5.20", "US$270.40", "-1.08R", "520")
assert round(18.91 - 18.38, 2) == 0.53 and int(200 / 0.53) == 377 and round(18.91 + 1.06, 2) == 19.97
assert int(250 / 0.53) == 471 and round(25.09 - 1.06, 2) == 24.03 and round(25.60 + 0.02, 2) == 25.62
approx((31.01 - 30.45) * 520, 291.20, 0.005)
approx(291.20 / 249.60, 1.17, 0.005)
approx(498.96 / 249.48, 2.00, 0.005)
has(t, "377", "US$19.97", "471", "US$24.03", "25.62", "US$291.20", "-1.17R")

# ---- Lesson 5
t = lesson(F, 5)
r = bars("vwap-reclaim")
vw = vwaps(r)
below = [i for i in range(1, 34) if r[i][4] < vw[i]]
assert below == list(range(1, 34))
assert r[34][4] > vw[34] and hm(r[34][0]) == "12:20"
assert hm(r[1][0]) == "09:35" and hm(r[33][0]) == "12:15"
assert r[34][1:5] == [58.79, 58.97, 58.78, 58.96] and round(vw[34], 2) == 58.92
base = min(x[3] for x in r[28:34])
assert hm(r[28][0]) == "11:50" and base == 58.18
trig, stop = round(58.97 + 0.01, 2), round(base - 0.02, 2)
risk = round(trig - stop, 2)
assert (trig, stop, risk) == (58.98, 58.16, 0.82)
sh = int(250 / risk)
assert sh == 304 and round(sh * risk, 2) == 249.28 and round(sh * trig, 2) == 17929.92
ent = next(i for i, x in enumerate(r[35:], 35) if x[2] >= trig)
assert hm(r[ent][0]) == "12:25" and r[ent][2] == 59.25
tgt = round(trig + 2 * risk, 2)
assert tgt == 60.62
ex = next(i for i, x in enumerate(r[ent:], ent) if x[2] >= tgt)
assert hm(r[ex][0]) == "13:30"
assert min(x[3] for x in r[ent:ex + 1]) > stop
gross = sh * 2 * risk
fees = 2 * sh * 0.005
net = gross - fees
assert round(gross, 2) == 498.56 and round(fees, 2) == 3.04 and round(net, 2) == 495.52
approx(net / (sh * risk), 1.99, 0.005)
approx((60.19 - 58.98) / 0.82, 1.48, 0.005)
assert max(x[2] for x in r[:12]) == 60.19
has(t, "58.98", "58.16", "US$0.82", "304", "US$249.28", "US$17,929.92", "60.62", "US$498.56", "US$3.04", "US$495.52", "+1.99R", "1.48R", "60.19", "33 straight")
g = bars("vwap-fade")
vg = vwaps(g)
assert g[6][1:5] == [26.30, 26.42, 26.15, 26.15] and hm(g[6][0]) == "10:00"
assert max(x[2] for x in g) == 26.42
approx(26.42 / vg[6] - 1, 0.030, 0.0005)
assert round(vg[6], 2) == 25.65
trig, stop = round(26.15 - 0.01, 2), round(26.42 + 0.02, 2)
risk = round(stop - trig, 2)
assert (trig, stop, risk) == (26.14, 26.44, 0.30)
sh = int(250 / risk)
assert sh == 833 and round(sh * risk, 2) == 249.90 and round(sh * trig, 2) == 21774.62
assert g[7][3] <= trig and hm(g[7][0]) == "10:05" and g[7][3] == 25.98
assert max(x[2] for x in g[7:14]) < stop
tg = round(vg[7] + 0.01, 2)
assert round(vg[7], 2) == 25.69 and tg == 25.70
ex = next(i for i, x in enumerate(g[8:], 8) if x[3] <= tg)
assert hm(g[ex][0]) == "10:25" and g[ex][3] == 25.69
gain = round(trig - tg, 2)
assert gain == 0.44
gross = sh * gain
fees = 2 * sh * 0.005
assert round(gross, 2) == 366.52 and round(fees, 2) == 8.33
net = gross - fees
assert round(net, 2) == 358.19
approx(net / (sh * risk), 1.43, 0.005)
approx(gain / risk, 1.47, 0.005)
approx(1 / (1 + 1.43), 0.412, 0.0005)
has(t, "26.14", "26.44", "833", "US$249.90", "US$21,774.62", "25.70", "US$366.52", "US$8.33", "US$358.19", "+1.43R", "1.47R", "41.2%", "3.0% above", "25.65", "25.69")
assert round(33.40 + 0.01, 2) == 33.41 and round(32.60 - 0.02, 2) == 32.58 and round(33.41 - 32.58, 2) == 0.83
assert int(200 / 0.83) == 240 and round(33.41 + 1.66, 2) == 35.07
assert round(52.10 - 0.01, 2) == 52.09 and round(52.60 + 0.02, 2) == 52.62 and round(52.62 - 52.09, 2) == 0.53
assert round(51.40 + 0.01, 2) == 51.41 and round(52.09 - 51.41, 2) == 0.68
approx(0.68 / 0.53, 1.28, 0.005)
approx(1 / (1 + 1.28), 0.439, 0.0005)
has(t, "33.41", "32.58", "240", "US$35.07", "52.09", "52.62", "51.41", "1.28", "43.9%")

# ---- Lesson 6
t = lesson(F, 6)
n = bars("news-momentum")
assert n[0][1] == 13.80 and pct((13.80 - 12.00) / 12.00) == "15.0%"
assert hm(n[4][0]) == "09:34" and n[4][2] == 14.75 and max(x[2] for x in n[:5]) == 14.75
assert hm(n[10][0]) == "09:40" and min(x[3] for x in n[5:11]) == 13.98
trig, stop = 14.76, round(13.98 - 0.02, 2)
risk = round(trig - stop, 2)
assert (stop, risk) == (13.96, 0.80)
sh = int(250 / risk)
assert sh == 312 and round(sh * risk, 2) == 249.60 and round(sh * trig, 2) == 4605.12
ent = next(i for i, x in enumerate(n[11:], 11) if x[2] >= trig)
assert hm(n[ent][0]) == "09:44" and n[ent][2] == 14.87
tgt = round(trig + 2 * risk, 2)
assert tgt == 16.36
ex = next(i for i, x in enumerate(n[ent:], ent) if x[2] >= tgt)
assert hm(n[ex][0]) == "09:51" and n[ex][2] == 16.53
assert min(x[3] for x in n[ent:]) > stop
assert min(x[3] for x in n[5:11]) > 13.80
gross = sh * 2 * risk
assert round(gross, 2) == 499.20 and round(2 * sh * 0.005, 2) == 3.12
net = gross - 2 * sh * 0.005
assert round(net, 2) == 496.08
approx(net / (sh * risk), 1.99, 0.005)
slip = 0.10 * sh
assert round(slip, 2) == 31.20
net2 = gross - 3.12 - slip
assert round(net2, 2) == 464.88
approx(net2 / (sh * risk), 1.86, 0.005)
has(t, "15.0%", "14.75", "13.98", "14.76", "13.96", "US$0.80", "312", "US$249.60", "US$4,605.12", "16.36", "US$499.20", "US$496.08", "+1.99R", "US$31.20", "US$464.88", "+1.86R", "9:44", "9:51")
assert round(0.10 * 14.00, 2) == 1.40 and round(14 - 1.4, 2) == 12.60 and round(14 + 1.4, 2) == 15.40
loss = (14.76 - 13.40) * sh
assert round(loss, 2) == 424.32
approx(loss / (sh * risk), 1.70, 0.005)
has(t, "US$12.60", "US$15.40", "US$424.32", "-1.70R")
assert round(20 * 0.9, 2) == 18.00
has(t, "US$18.00", "17.80", "17.81")
assert round(8.41 - 7.93, 2) == 0.48 and int(200 / 0.48) == 416 and round(8.41 + 0.96, 2) == 9.37
assert round(8 * 0.10, 2) == 0.80
assert round(32.50 * 0.9, 2) == 29.25
approx((10 - 9.10) * 200, 180)
approx(180 / 100, 1.80)
has(t, "US$9.37", "US$7.20", "US$8.80", "US$29.25", "-1.80R")

# ---- Lesson 7
t = lesson(F, 7)
assert round(600 * 25.01, 2) == 15006.00
c = round(600 * 25.01 + 900 * 25.02 + 500 * 25.03, 2)
assert c == 50039.00
approx(c / 2000, 25.0195, 0.00005)
approx((c / 2000 - 25.01) * 2000, 19.00, 0.005)
assert round((2000 - 1500) / 3500, 2) == 0.14 and round(1000 / 9000, 2) == 0.11
has(t, "US$50,039", "US$25.0195", "0.0095", "US$19.00", "+0.14", "+0.11", "12,515", "22,518", "15,006")
ask = 300 + 300 + 500 + 800
bid = 150 + 100
assert (ask, bid) == (1900, 250)
assert pct(ask / (ask + bid)) == "88.4%"
has(t, "1,900", "250", "88.4%")
c1 = round(600 * 25.01 + 900 * 25.02, 2)
assert c1 == 37524.00 and round(c1 / 1500, 3) == 25.016
assert pct(3400 / 4500) == "75.6%" and round((1800 - 600) / 2400, 2) == 0.50
has(t, "US$37,524", "US$25.016", "75.6%", "+0.50")

# ---- Lesson 8
t = lesson(F, 8)
cc = 0.02 + 2 * 0.005 + 2 * 0.01
approx(cc, 0.05, 1e-9)
rows8 = {0.10: "50.0%", 0.20: "41.7%", 0.40: "37.5%", 0.63: "36.0%", 1.00: "35.0%"}
for stop, p in rows8.items():
    cr = cc / stop
    assert pct((1 + cr) / 3) == p, (stop, (1 + cr) / 3)
has(t, "50.0%", "41.7%", "37.5%", "36.0%", "35.0%", "33.3%", "0.125", "0.079")
cr = 0.05 / 0.10
assert pct((1 + cr) / 2.5) == "60.0%" and pct(1 / 2.5) == "40.0%"
has(t, "60.0%", "40.0%", "20 percentage points")
fx = 16992.36 * 0.015
assert round(fx, 2) == 254.89 and round(2 * fx, 2) == 509.77
approx(2 * fx / 249.48, 2.04, 0.005)
has(t, "254.89", "US$509.77", "2.04R")
assert round(0.03 + 0.01 + 0.02, 2) == 0.06 and round(0.06 / 0.30, 2) == 0.20
assert pct(1.2 / 3) == "40.0%"
assert round(0.04 / 0.08, 2) == 0.5 and round(0.12 / 0.08, 2) == 1.5 and pct(1.5 / 2.5) == "60.0%"
assert 10000 * 0.015 == 150 and 2 * 150 == 300
has(t, "US$0.06", "0.20R", "US$150", "US$300", "3.0%")


def cost_in_r(spread, commission, slippage, stop):
    return (spread + 2 * commission + 2 * slippage) / stop


approx(cost_in_r(0.02, 0.005, 0.01, 0.63), 0.0794, 0.0001)

# ---- Lesson 9
t = lesson(F, 9)
assert 250 / 0.40 == 625 and 625 * 50 == 31250 and int(25000 / 50) == 500
assert round(500 * 0.40, 2) == 200.0 and round(200 / 250, 1) == 0.8
approx(-1.08 - 1.00, -2.08)
runs = []
s = 0
for x in (1.99, -1.00, -1.08, -1.00):
    s += x
    runs.append(round(s, 2))
assert runs == [1.99, 0.99, -0.09, -1.09]
has(t, "US$31,250", "= 500", "US$200", "0.8 of", "-2.08R", "-1.09R", "+1.99, +0.99, -0.09, -1.09", "US$500")
assert round(70.81 - 70.08, 2) == 0.73 and int(300 / 0.73) == 410 and round(70.81 + 1.46, 2) == 72.27
assert round(70.10 - 0.02, 2) == 70.08
assert pct((1 + 0.2) / 3) == "40.0%"
assert (10.00 * 1000 + 10.20 * 3000) / 4000 == 10.15
assert 100 * 0.05 == 5.0 and 50 - 5 == 45
assert round(1.05 + 0.98, 2) == 2.03 and 40000 * 0.01 * 2 == 800
assert pct(2400 / 3000) == "80.0%"
assert int(200 / 0.50) == 400 and 400 * 40 == 16000 and int(20000 / 40) == 500
has(t, "70.81", "70.08", "0.73", "410", "US$72.27", "40.0%", "US$10.15", "95.00 to 105.00", "US$45.00", "-2.03R", "US$800", "80.0%", "US$16,000")
assert 32000 * 0.01 == 320 and 2 * 320 == 640
assert 300 / 0.50 == 600 and 600 * 80 == 48000 and int(30000 / 80) == 375
assert round(375 * 0.50, 2) == 187.50 and 187.5 / 300 == 0.625
has(t, "US$320", "US$640", "US$48,000", "375", "US$187.50", "0.625")

print("part 8 checks passed")
