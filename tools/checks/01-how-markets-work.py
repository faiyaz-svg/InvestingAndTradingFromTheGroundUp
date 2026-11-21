"""Number checks for part 1, How markets work."""
import csv
import json
from datetime import date, datetime, timezone

from _lib import ROOT, lesson, has

F = "01-how-markets-work"
CH = ROOT / "docs" / "assets" / "charts" / F


def bars(name):
    return json.loads((CH / f"{name}.json").read_text(encoding="utf-8"))["bars"]


def auction(buys, sells):
    out = {}
    for p in sorted(set(buys) | set(sells)):
        dem = sum(s for q, s in buys.items() if q >= p)
        sup = sum(s for q, s in sells.items() if q <= p)
        out[p] = (dem, sup, min(dem, sup))
    best = max(out, key=lambda p: out[p][2])
    return out, best


def fill(levels, n):
    left, cost = n, 0.0
    for p, s in levels:
        k = min(left, s)
        cost += k * p
        left -= k
    assert left == 0
    return cost


# ---- Lesson 1
t = lesson(F, 1)
g = bars("earnings-gap")
assert g[19][0] == "2026-07-31" and g[19][4] == 49.40
assert g[20][0] == "2026-08-03" and g[20][1] == 53.35
assert date(2026, 7, 31).weekday() == 4 and date(2026, 8, 3).weekday() == 0
assert round((53.35 - 49.40) / 49.40, 4) == 0.0800
assert round(49.40 * 100, 2) == 4940 and round(53.35 * 100, 2) == 5335
has(t, "US$4.94 billion", "US$5.335 billion", "+8.0%", "US$395 million")
post = g[21:]
assert len(post) == 12 and min(b[3] for b in post) == 52.55 and max(b[2] for b in post) == 54.85
has(t, "between 52.55 and 54.85", "next 12 sessions")
assert 32.50 * 240 == 7800
has(t, "US$7.8 billion")
assert round((30.88 - 32.50) / 32.50, 3) == -0.050
assert round(30.88 * 240, 1) == 7411.2
has(t, "-5.0%", "US$7,411.2 million", "US$7.41 billion")
assert 250 / 100 == 2.5 and 50 / 2.5 == 20
has(t, "US$2.50", "20 dollars")

# ---- Lesson 2
t = lesson(F, 2)
assert round(200 * 50.00 - 200 * 49.995, 2) == 1.00 and round(200 * 49.995, 2) == 9999.00
has(t, "US$10,000.00", "US$9,999.00", "US$1.00")
assert round(500 * 20.02 - 500 * 20.015, 2) == 2.50 and round(500 * 20.02, 2) == 10010 and round(500 * 20.015, 2) == 10007.5
has(t, "US$10,010.00", "US$10,007.50", "US$2.50")

# ---- Lesson 3
t = lesson(F, 3)
m = bars("opening-gap-5m")
d1 = m[:78]
assert d1[-1][4] == 99.61 and m[78][1] == 101.60
assert round((101.60 - 99.61) / 99.61, 3) == 0.020
has(t, "US$99.61", "US$101.60", "+2.0%")
assert d1[0][5] == 215600
avg = sum(b[5] for b in d1[30:40]) / 10
assert round(avg, -2) == 49700
t30 = datetime.fromtimestamp(d1[30][0], timezone.utc)
t39 = datetime.fromtimestamp(d1[39][0], timezone.utc)
assert (t30.hour, t30.minute) == (12, 0) and (t39.hour, t39.minute) == (12, 45)
has(t, "215,600 shares", "49,700 shares", "12:00 to 12:45 p.m.")
assert date(2026, 3, 2).weekday() == 0 and date(2026, 11, 26).weekday() == 3
buys = {50.10: 500, 50.05: 400, 50.00: 300, 49.95: 200}
sells = {50.10: 600, 50.05: 500, 50.00: 400, 49.95: 300}
out, best = auction(buys, sells)
assert best == 50.05 and out[50.05] == (900, 1200, 900)
assert out[50.10] == (500, 1800, 500) and out[50.00] == (1200, 700, 700) and out[49.95] == (1400, 300, 300)
has(t, "| 50.10 | 500 | 1,800 | 500 |", "| 50.05 | 900 | 1,200 | 900 |", "| 50.00 | 1,200 | 700 | 700 |",
    "| 49.95 | 1,400 | 300 | 300 |", "US$50.05: 900 shares", "imbalance of 300 shares to sell")
assert round(0.10 * 40, 2) == 4.00
has(t, "US$36.00 to US$44.00")
assert 6000 - 6000 * 0.07 == 5580
has(t, "6,000 - 420 = 5,580")

# ---- Lesson 4
t = lesson(F, 4)
asks = [(50.00, 400), (50.01, 600), (50.02, 700), (50.03, 1000)]
bids = [(49.98, 300), (49.97, 500), (49.96, 800), (49.95, 1200)]
assert round(50.00 - 49.98, 2) == 0.02 and round((50.00 + 49.98) / 2, 2) == 49.99
assert round(0.02 / 49.99 * 100, 2) == 0.04
c = fill(asks, 1000)
assert round(c, 2) == 50006.00 and round(c / 1000, 3) == 50.006
assert round(c - 49.99 * 1000, 2) == 16.00
has(t, "US$20,000.00", "US$30,006.00", "US$50,006.00", "US$50.006", "US$16.00", "0.04%")
c2 = fill(bids, 1500)
assert round(c2, 2) == 74951.00 and round(c2 / 1500, 3) == 49.967
has(t, "US$14,994.00", "US$24,985.00", "US$34,972.00", "US$74,951.00", "US$49.967")
has(t, "| Ask | 50.03 | 1,000 | 2,700 |", "| Bid | 49.95 | 1,200 | 2,800 |", "| Ask | 50.01 | 600 | 1,000 |", "| Bid | 49.96 | 800 | 1,600 |")
assert round(20.14 - 20.10, 2) == 0.04 and round(0.04 / 20.12 * 100, 2) == 0.20
has(t, "US$0.04", "0.20%")
c3 = fill(asks, 1700)
assert round(c3, 2) == 85020.00 and round(c3 / 1700, 3) == 50.012
has(t, "US$85,020.00", "US$50.012", "35,014.00")
assert round(300 * 0.01, 2) == 3.00
has(t, "US$3.00")

# ---- Lesson 5
t = lesson(F, 5)
assert round((50.30 - 48.50) * 100, 2) == 180.0 and round((50.30 - 47.20) * 100, 2) == 310.0 and 310 - 180 == 130
assert round(100 * 47.20, 2) == 4720
has(t, "US$180", "US$310", "US$130", "US$4,720")
assert round((50.30 - 48.50) * 200, 2) == 360 and round((50.30 - 48.10) * 200, 2) == 440
has(t, "US$360", "US$440", "US$80")
ot = bars("order-types")
assert ot[-1][4] == 50.30 and max(b[2] for b in ot) == 51.0
has(t, "US$50.30")
assert round(400 * 50.00 + 600 * 50.01, 2) == 50006.0
has(t, "US$50,006.00")

# ---- Lesson 6
t = lesson(F, 6)
assert round((50.00 - 49.98) * 1000, 2) == 20.00 and round((49.98 - 49.80) * 1000, 2) == 180.00 and 180 / 20 == 9
has(t, "US$20.00", "US$180.00", "9 complete round trips")
assert round((30.04 - 30.00) * 500, 2) == 20.00
assert round((30.00 - 29.70) * 500, 2) == 150.00 and 150 / 20 == 7.5
has(t, "US$150.00", "7.5")

# ---- Lesson 7
t = lesson(F, 7)
assert date(2026, 11, 20).weekday() == 4 and date(2026, 11, 23).weekday() == 0
assert date(2026, 11, 25).weekday() == 2 and date(2026, 11, 27).weekday() == 4
has(t, "Monday, November 23, 2026", "Friday, November 27, 2026")
V, L = 400 * 50.0, 10000
assert V == 20000 and (V - L) / V == 0.5
V2 = 400 * 40.0
assert V2 == 16000 and V2 - L == 6000 and 6000 / 10000 - 1 == -0.4 and 6000 / 16000 == 0.375
P = L / (400 * 0.70)
assert round(P, 2) == 35.71 and round((50 - P) / 50 * 100, 1) == 28.6
V3 = 400 * P
assert round(V3, 2) == 14285.71 and round(V3 - L, 2) == 4285.71
assert round((10000 - (V3 - L)) / 10000 * 100, 1) == 57.1
assert round(10000 * 0.06 * 30 / 365, 2) == 49.32
has(t, "US$16,000", "US$6,000", "-40%", "37.5%", "US$35.71", "28.6%", "US$14,285.71", "US$4,285.71", "57.1%", "US$49.32")
assert round(10000 * 1.10 - 10000, 2) == 1000 and 1000 / 5000 == 0.20
assert 10000 * 0.75 == 7500 and 7500 - 5000 == 2500 and 2500 / 5000 == 0.5
has(t, "US$11,000", "20%", "US$7,500", "US$2,500", "50%")

# ---- Lesson 8
t = lesson(F, 8)
fee = 5000 * 0.03 * 30 / 365
assert round(fee, 2) == 12.33
C = round(fee, 2) + 50
assert round(C, 2) == 62.33
assert round(500 - C, 2) == 437.67 and round(-1000 - C, 2) == -1062.33
has(t, "US$5,000.00", "US$12.33", "US$50.00", "US$62.33", "US$437.67", "-US$1,062.33")
assert round((30.00 - 27.50) * 200, 2) == 500.00
has(t, "US$500.00")
assert round((50.00 - 75.00) * 100, 2) == -2500.00 and 2500 / 5000 == 0.5
has(t, "-US$2,500.00", "50% of the US$5,000 proceeds")
assert 2_000_000 / 500_000 == 4
has(t, "4 days")
fee2 = 5000 * 0.04 * 60 / 365
assert round(fee2, 2) == 32.88 and round(200 - fee2, 2) == 167.12
has(t, "US$32.88", "US$167.12")

# ---- Lesson 9
t = lesson(F, 9)
e = bars("ex-dividend")
assert e[14][0] == "2026-08-21" and e[14][4] == 49.95 and e[15][0] == "2026-08-24" and e[15][1] == 48.95
assert date(2026, 8, 21).weekday() == 4 and date(2026, 8, 24).weekday() == 0
assert round(49.95 - 48.95, 2) == 1.00
has(t, "49.95", "48.95", "Friday, August 21", "Monday, August 24")
assert 4 * 0.80 / 40.00 == 0.08
has(t, "US$3.20", "8.0%")
assert date(2026, 7, 8).weekday() == 2 and date(2026, 7, 7).weekday() == 1
has(t, "Tuesday, July 7, 2026")
s = bars("stock-a-split")
assert s[24][0] == "2026-10-12" and s[24][4] == 227.63 and s[25][0] == "2026-10-13" and s[25][1] == 113.82
assert date(2026, 10, 12).weekday() == 0 and date(2026, 10, 13).weekday() == 1
assert round(100 * 227.63, 2) == 22763.00 and 227.63 / 2 == 113.815 and round(200 * 113.815, 2) == 22763.00
has(t, "US$22,763.00", "US$113.815", "227.63", "113.82")
assert 1000 / 10 == 100 and 2.00 * 10 == 20.00
has(t, "1,000 / 10 = 100 shares")
assert 150 * 3 == 450 and round(80 / 3, 2) == 26.67 and round(450 * 80 / 3, 2) == 12000.00
has(t, "US$26.67", "US$12,000")
assert round((113.82 - 227.63) / 227.63, 4) == -0.5000
has(t, "-50.0%")
rows = list(csv.DictReader(open(ROOT / "docs" / "assets" / "data" / "stock-a-split-daily.csv")))
idx = [r["date"] for r in rows].index("2026-10-13")
raw_ret = float(rows[idx]["close"]) / float(rows[idx - 1]["close"]) - 1
adj_ret = float(rows[idx]["close"]) / (float(rows[idx - 1]["close"]) / 2) - 1
print("split-date raw return", round(raw_ret * 100, 2), "adjusted", round(adj_ret * 100, 2))
assert round(raw_ret * 100, 1) == -49.2, raw_ret
assert 0 < adj_ret < 0.03
has(t, "about -49.2%")

# ---- Lesson 10
t = lesson(F, 10)
price, shares = [200, 50, 10], [10, 100, 300]
caps = [p * s for p, s in zip(price, shares)]
assert caps == [2000, 5000, 3000]
assert [round(p / sum(price) * 100, 1) for p in price] == [76.9, 19.2, 3.8]
assert [c / sum(caps) for c in caps] == [0.2, 0.5, 0.3]
assert sum(price) == 260 and 260 / 2.6 == 100
i1 = (220 + 50 + 10) / 2.6
assert round(i1, 2) == 107.69 and round(i1 / 100 - 1, 3) == 0.077
i2 = (200 + 50 + 11) / 2.6
assert round(i2, 2) == 100.38 and round(i2 / 100 - 1, 3) == 0.004
has(t, "107.69", "7.7%", "102.0", "100.38", "0.4%", "103.0", "3.0%", "260 / 2.6 = 100")
assert 100 + 50 + 10 == 160 and 160 / 100 == 1.6
has(t, "160 / 100 = 1.6")
assert round((84 + 24) / 100 - 1, 3) == 0.08
assert round(0.8 * 5 + 0.2 * 20, 1) == 8.0
has(t, "108", "8.0%")
assert 3000 * 0.6 == 1800 and round(1800 / (2000 + 5000 + 1800) * 100, 1) == 20.5
has(t, "1,800", "8,800", "20.5%")
assert (90 + 60 + 30) / 1.8 == 100 and (30 + 60 + 30) / 100 == 1.2
has(t, "1.2")

# ---- Lesson 11
t = lesson(F, 11)
assert round((50.30 - 49.90) / 49.90 * 100, 2) == 0.80
assert round(0.02 / 50.30 * 100, 2) == 0.04
assert round((50.30 - 38.20) / (52.40 - 38.20) * 100, 1) == 85.2
assert round(2_100_000 / 1_500_000, 1) == 1.4
assert round(50.30 * 100_000_000 / 1e9, 2) == 5.03
assert round(50.30 / 2.50, 1) == 20.1 and round(2.00 / 50.30 * 100, 1) == 4.0
assert date(2026, 12, 3).weekday() == 3 and date(2026, 12, 2).weekday() == 2
has(t, "0.80%", "85.2%", "1.4", "US$5.03 billion", "20.1", "4.0%", "Wednesday, December 2")
assert round(31.20 - 32.00, 2) == -0.80 and round(-0.80 / 32.00 * 100, 1) == -2.5
assert round((31.20 - 24.00) / (36.00 - 24.00) * 100, 1) == 60.0
assert 900_000 / 1_200_000 == 0.75 and round(31.20 / 1.60, 1) == 19.5
has(t, "-US$0.80", "-2.5%", "60.0%", "0.75", "19.5")
assert round(58.00 * 80, 2) == 4640 and round((58.00 - 62.50) / 62.50 * 100, 1) == -7.2
has(t, "US$4,640 million", "US$4.64 billion", "-7.2%")
assert (120 + 80 + 40) / 3 == 80 and (108 + 80 + 40) / 3 == 76 and round((76 - 80) / 80 * 100, 1) == -5.0
has(t, "-5.0%")
o, best = auction({10.02: 300, 10.01: 200, 10.00: 400}, {10.00: 200, 10.01: 300, 10.02: 400})
assert best == 10.01 and o[10.01] == (500, 500, 500) and o[10.02] == (300, 900, 300) and o[10.00] == (900, 200, 200)
has(t, "US$10.01: 500 shares")
c4 = 300 * 20.01 + 400 * 20.02
assert round(c4, 2) == 14011.00 and round(c4 / 700, 3) == 20.016
has(t, "6,003.00", "8,008.00", "US$14,011.00", "US$20.016")
assert round((30.00 - 28.50) * 100, 2) == 150 and round((30.00 - 27.00) * 100, 2) == 300
has(t, "US$150", "US$300")
assert 16000 * 0.75 == 12000 and 12000 - 8000 == 4000 and 4000 / 8000 == 0.5
has(t, "US$12,000", "US$4,000", "50%")
assert round((40.00 - 44.00) * 100 - 5.00, 2) == -405.00
has(t, "-US$405.00", "-US$400.00")
print("part 1 checks ok")
