"""Number checks for part 18, Crypto."""
import hashlib
import json
import math

import pandas as pd

from _lib import ROOT, lesson, has, usd, cad, pct

F = "18-crypto"
CH = ROOT / "docs" / "assets" / "charts" / F

# Lesson 1
t = lesson(F, 1)
sub, tot = 50 * 10**8, 0
for _ in range(40):
    tot += 210_000 * sub
    sub //= 2
assert tot / 1e8 == 20_999_999.9769
four = 210_000 * (50 + 25 + 12.5 + 6.25)
assert four == 19_687_500
assert 24 * 6 == 144 and 144 * 3.125 == 450 and 450 * 365 == 164_250
assert round(164_250 / four * 100, 2) == 0.83
assert round(210_000 * 10 / 60 / 24 / 365, 1) == 4.0
assert 210_000 * (50 + 25 + 12.5) == 18_375_000 and 450 * 30 == 13_500 and 2**20 == 1_048_576
header, n = "coin-a-block-1|prev=0000|txs=3", 0
while int(hashlib.sha256(f"{header}|nonce={n}".encode()).hexdigest(), 16) >= 2 ** 240:
    n += 1
assert n == 38_624
has(t, "19,687,500", "20,999,999.9769", "3.125", "450 BTC", "164,250", "0.83%", "18,375,000", "13,500", "1,048,576", "38,624", "65,536")

# Lesson 2
t = lesson(F, 2)
assert 2048**12 == 2**132 and 24 * 11 == 264
sec = 2**128 / 1e12
yrs = sec / (365 * 24 * 3600)
assert f"{2**128:.1e}" == "3.4e+38" and f"{sec:.1e}" == "3.4e+26" and f"{yrs:.1e}" == "1.1e+19"
has(t, "2^132", "3.4 x 10^38", "3.4 x 10^26", "1.1 x 10^19", "264 bits", "2^128 times")

# Lesson 3
t = lesson(F, 3)
fee = 21_000 * 22
assert fee == 462_000 and fee / 1e9 == 0.000462 and round(fee / 1e9 * 3000, 3) == 1.386
assert 21_000 * 30 == 630_000
k = 100 * 2000
y2 = k / 90
assert round(y2, 2) == 2222.22 and round(y2 - 2000, 2) == 222.22 and round((y2 - 2000) / 10, 2) == 22.22
assert round(((y2 - 2000) / 10) / 20 - 1, 3) == 0.111 and round(y2 / 90, 2) == 24.69
y3 = k / 110
assert round(2000 - y3, 2) == 181.82 and round((2000 - y3) / 10, 2) == 18.18
assert round(10_000 / 0.8) == 12_500 and round(1 - 12_500 / 15_000, 3) == 0.167 and round(10_000 / 15_000 * 100, 1) == 66.7
assert 18_000 / 0.75 == 24_000 and (30_000 - 24_000) / 30_000 == 0.2 and 980 / 1000 == 0.98
has(t, "462,000", "0.000462", "US$1.386", "US$1.39", "0.00063 ETH", "2,222.22", "US$222.22", "US$22.22", "11.1%", "US$24.69",
    "US$181.82", "US$18.18", "US$12,500", "16.7%", "66.7%", "US$24,000", "20.0%", "US$0.98", "September 15, 2022")

# Lesson 4
t = lesson(F, 4)
net = 20_000 - 5_000
assert 30_000 - 20_000 == 10_000 and net == 15_000 and 30_000 - net == 15_000
assert 12_000 - 3_000 + 9_000 == 18_000 and 30_000 - 18_000 == 12_000
f1 = 0.009
a = 5000 * (1 - f1)
b = a * (1 - f1)
assert a == 4955 and abs(b - 4910.405) < 1e-6 and abs(5000 - b - 89.595) < 1e-6 and round(1 - 0.991**2, 3) == 0.018
c = 8000 * 0.993
d = c * 0.993
assert c == 7944 and round(d, 2) == 7888.39 and round(8000 - d, 2) == 111.61
has(t, "C$30,000", cad(10_000, 0), cad(15_000, 0), "33,000", "C$4,955", "C$4,910.41", "C$89.60", "1.8%", "C$18,000", "C$12,000", "7,888.39", "C$111.61", "1.4%", "0.5% fee")

# Lesson 5
t = lesson(F, 5)
assert round(10_000 * 0.996, 2) == 9960 and round(10_000 * 0.996**5, 2) == 9801.59
assert round(10_000 * 0.991**2, 2) == 9820.81
assert round(math.log(0.991**2) / math.log(0.996), 2) == 4.51
assert round(20_000 * 0.9975**3, 2) == 19_850.37 and round((40.30 - 40) / 40, 4) == 0.0075
has(t, "C$9,960.00", "C$9,801.59", "C$9,820.81", "4.51", "C$19,850.37", "0.75%", "February 18, 2021", "January 10, 2024", "July 23, 2024")

# Lesson 6
t = lesson(F, 6)
N = 1000 * 22.0
pays = [N * r for r in (0.0001, 0.0003, 0.0010)]
assert [round(p, 2) for p in pays] == [2.2, 6.6, 22.0] and round(sum(pays), 2) == 30.8
assert round(0.0001 * 3 * 365 * 100, 2) == 10.95 and round(0.0010 * 3 * 365 * 100, 1) == 109.5


def liq(e, L, m=0.005):
    return e * (1 - 1 / L) / (1 - m)


assert round(liq(20, 10), 2) == 18.09 and round((20 - liq(20, 10)) / 20, 3) == 0.095
assert round(liq(20, 2), 2) == 10.05 and round((20 - liq(20, 2)) / 20, 3) == 0.497
eq = 2000 + 1000 * (18.09 - 20)
assert round(eq) == 90 and round(0.005 * 18_090) == 90
assert round(liq(27.5, 10), 2) == 24.87 and round(liq(27.5, 5), 2) == 22.11
cas = json.loads((CH / "coin-a-cascade.json").read_text())["bars"]
by = {b[0]: b for b in cas}
b15, b16 = by["2026-04-15"], by["2026-04-16"]
assert b15[4] == 27.5 and b16[1] == 27.5 and b16[3] == 22.83 and b16[4] == 23.65
assert round((23.65 - 27.5) / 27.5, 3) == -0.14
avg_vol = sum(b[5] for b in cas[:30]) / 30
assert 3.5 < b16[5] / avg_vol < 4.5
assert 500 * 40 * 0.0002 == 4.0
assert round(liq(50, 4), 2) == 37.69 and round((50 - liq(50, 4)) / 50, 3) == 0.246
assert 10_000 * 0.0001 * 3 * 30 == 90.0
has(t, usd(2.2), usd(6.6), usd(22.0), usd(30.8), "10.95%", "109.5%", "US$18.09", "9.5%", "US$10.05", "49.7%", "US$24.87", "US$22.11",
    "27.50", "22.83", "23.65", "14.0%", "US$4.00", "US$37.69", "24.6%", "US$90.00", "0.9%")

# Lesson 7
t = lesson(F, 7)
mc = 1000 * 15
rc = 400 * 5 + 400 * 12 + 200 * 25
assert (mc, rc) == (15_000, 11_800) and round(mc / rc, 2) == 1.27 and round((15 - 25) / 25, 2) == -0.4
assert round(9_440 / 11_800, 2) == 0.80 and (3.125 - 6.25) / 6.25 == -0.5 and 1 / 0.25 - 1 == 3.0
assert round(3.182 / 1.96, 2) == 1.62
cyc = json.loads((CH / "coin-a-cycle.json").read_text())["bars"]
pk = max(cyc, key=lambda b: b[4])
assert pk[0] == "2024-06-24" and pk[4] == 32.35 and cyc[-1][4] == 6.8
assert round((6.8 - 32.35) / 32.35, 3) == -0.79 and round(32.35 / 6.8 - 1, 2) == 3.76
has(t, "US$15,000", "US$11,800", "1.27", "27%", "-40%", "32.35", "6.80", "-79.0%", "376%", "0.80", "-50%", "300%", "1.62", "3.18")

# Lesson 8
t = lesson(F, 8)
assert [1_000_000 / p for p in (10, 5, 2, 1)] == [100_000, 200_000, 500_000, 1_000_000]
assert 6_000 / 10_000 == 0.6 and 1_000_000 / 0.5 == 2_000_000
has(t, "100,000", "200,000", "500,000", "1,000,000", "60%", "2,000,000", "November 2, 2023", "March 28, 2024", "US$40 billion", "US$4.5 billion")

# Lesson 9
t = lesson(F, 9)
acb = (100 * 20 + 50 * 26) / 150
assert acb == 22.0
gain = 1800 - 60 * acb
assert gain == 480 and gain / 2 == 240 and gain / 2 * 0.4 == 96
rem_acb = 90 * acb
assert rem_acb == 1980
loss = 40 * acb - 40 * 15
assert loss == 280 and 40 * acb == 880
total = 50 * acb + 40 * 15.5 + loss
assert total == 2000 and round(total / 90, 2) == 22.22
df = pd.read_csv(ROOT / "docs" / "assets" / "data" / "coin-a-daily.csv")
prev = df["close"].shift()
tr = pd.concat([df["high"] - df["low"], (df["high"] - prev).abs(), (df["low"] - prev).abs()], axis=1).max(axis=1)
atr = tr.rolling(14).mean().iloc[-1]
e = df["close"].iloc[-1]
assert df["date"].iloc[-1] == "2026-06-02" and e == 22.17
assert round(atr, 4) == 1.2243 and round(atr / e, 3) == 0.055
s = e - 2 * atr
assert round(s, 2) == 19.72 and round(e - s, 4) == 2.4486 and round(e - s, 2) == 2.45
units = int(200 / (e - s))
assert units == 81 and round(81 * e, 2) == 1795.77 and round(81 * e / 20_000, 3) == 0.090
assert round(81 * (e - 18.0), 2) == 337.77 and round(81 * (e - 18) / 20_000, 3) == 0.017
assert 210_000 * 75 == 15_750_000 and round(liq(50, 5), 2) == 40.20
assert 10_000 + 15_000 - 4_000 == 21_000 and 30_000 - 21_000 == 9_000
assert round(10_000 * 0.995**2, 2) == 9900.25 and 20_000 * 0.0001 == 2.0
assert (3000 + 5000) / 200 == 40 and 50 * (60 - 40) == 1000
has(t, "C$22.00", "C$480", "C$240", "C$96", "1,980", "C$280", "C$2,000", "C$22.22", "C$19.72", "C$2.45", "81 coins", "C$1,795.77", "9.0%",
    "C$337.77", "1.7%", "15,750,000", "US$40.20", "C$9,000", "C$9,900.25", "US$2.00", "C$500", "1.2243", "5.5%")
assert 10_000 * 0.01 / 3 == 33.333333333333336 or int(100 / 3) == 33
has(t, "C$100", "33 coins")
print("part 18 ok")
