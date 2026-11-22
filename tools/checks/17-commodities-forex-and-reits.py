"""Number checks for part 17, Commodities, forex and REITs."""
import json
import sys

from _lib import ROOT, lesson, has, usd, pct

F = "17-commodities-forex-and-reits"
CH = ROOT / "docs" / "assets" / "charts" / F


def bars(name):
    return json.loads((CH / f"{name}.json").read_text(encoding="utf-8"))["bars"]


def close_on(b, d):
    return next(x for x in b if x[0] == d)


# ---- Lesson 1 ----
t = lesson(F, 1)
phys = 100_000 * 60.00
fut = 100_000 * (70.00 - 60.00)
assert phys == 6_000_000 and fut == 1_000_000 and (phys + fut) / 100_000 == 70.0
has(t, usd(6_000_000, 0), usd(1_000_000, 0), usd(7_000_000, 0), "US$70.00 per barrel", "US$7.0 million", "US$6.0 million")
assert 100_000 * 80 - 100_000 * 10 == 7_000_000
has(t, "US$8,000,000")
g = (72.00 - 65.50) * 50_000
assert g == 325_000 and 65.50 * 50_000 == 3_275_000 and (g + 3_275_000) == 3_600_000 and 3_600_000 / 50_000 == 72.0
has(t, usd(325_000, 0), usd(3_275_000, 0), usd(3_600_000, 0))
assert (80 - 74) * 1000 * 20 == 120_000
has(t, usd(120_000, 0))

# ---- Lesson 2 ----
t = lesson(F, 2)
o = bars("oil-daily")
sep1, sep2 = close_on(o, "2026-09-01"), close_on(o, "2026-09-02")
assert sep1[4] == 70.75 and sep2[1] == 73.93 and pct(sep2[1] / sep1[4] - 1) == "4.5%"
assert max(x[2] for x in o[:22]) == 71.28 and max(x[2] for x in o) == 78.19
has(t, "US$70.75", "US$73.93", "4.5%", "71.28", "78.19")
sur = 3.2 - (-1.5)
assert round(sur, 1) == 4.7
d = 73.11 - 74.00
assert round(d, 2) == -0.89 and pct(d / 74.00) == "-1.2%" and round(0.89 * 1000) == 890
has(t, "4.7 million", "US$0.89", "-1.2%", "US$890", "US$74.00", "US$73.11")
assert 78 - 70 == 8 and pct(8 / 70) == "11.4%" and 73 - 72 == 1 and pct(1 / 72) == "1.4%"
assert 70 - 72 == -2 and 78 - 73 == 5
has(t, "+US$8.00, +11.4%", "+US$1.00, +1.4%", "-US$2.00", "+US$5.00")
assert 0.015 * 2400 == 36 and 0.025 * 2400 == 60
has(t, "US$36 a year", "US$60 a year")
assert 2400 * 1.35 == 3240 and 2400 * 1.40 == 3360 and pct(3360 / 3240 - 1) == "3.7%"
has(t, "C$3,240", "C$3,360", "3.7%")
assert round(-2.3 - 0.5, 1) == -2.8
has(t, "-2.8 million")
assert round(72.52 - 74.00, 2) == -1.48 and pct(-1.48 / 74) == "-2.0%" and round(1.48 * 1000 * 5) == 7400
has(t, "-US$1.48", "-2.0%", "US$7,400")
assert round(0.02 * 2400) == 48 and 48 - 36 == 12
has(t, "US$48", "US$12 per ounce")

# ---- Lesson 3 ----
t = lesson(F, 3)
n = 10_000_000 / (80 * 1000)
assert n == 125
has(t, "125 contracts")
assert round(80 * 1.0075, 2) == 80.60 and round(1 / 1.0075, 5) == 0.99256 and pct(1 - 1 / 1.0075, 2) == "0.74%"
has(t, "80.60", "0.99256", "0.74%")
roll = (1 / 1.0075) ** 12
assert round(roll, 4) == 0.9142
v_flat = 10_000_000 * roll
v_up = 10_000_000 * 1.05 * roll
assert round(v_flat, -3) == 9_142_000 and pct(v_flat / 1e7 - 1) == "-8.6%"
assert round(v_up, -3) == 9_600_000 and pct(v_up / 1e7 - 1) == "-4.0%"
has(t, "0.9142", usd(9_142_000, 0), "8.6%", usd(9_600_000, 0), "4.0%", "US$84.00")
assert round((1 / 0.9925) ** 12, 4) == 1.0945 and pct((1 / 0.9925) ** 12 - 1) == "9.5%"
has(t, "1.0945", "9.5%", "9.4%")
assert round(0.40 / 80, 4) == 0.005 and 0.40 * 1000 * 200 == 80_000
has(t, "0.5%", usd(80_000, 0))
r2 = (1 / 1.005) ** 12
assert round(r2, 4) == 0.9419 and round(10_000 * r2) == 9419 and pct(r2 - 1) == "-5.8%"
has(t, "0.9419", usd(9419, 0), "5.8%")
assert pct(1 / roll - 1) == "9.4%" and round(1 / roll - 1, 4) == 0.0938
has(t, "0.0938")
has(t, "-US$37.63", "April 20, 2020")
sys.path.insert(0, str(ROOT / "tools" / "figures" / F))
import roll_yield  # noqa: E402

m, spot, fund = roll_yield.series(80.0)
assert round(fund[12]) == 91
m, spot, fund = roll_yield.series(84.0)
assert round(fund[12], 1) == 96.0

# ---- Lesson 4 ----
t = lesson(F, 4)
assert round(1 / 1.3650, 4) == 0.7326
has(t, "0.7326")
assert pct(0.0100 / 1.3650, 2) == "0.73%"
has(t, "0.73%")
assert 100_000 * 0.0001 == 10 and round(10 / 1.3650, 2) == 7.33
has(t, "C$10 per pip", "US$7.33")
u = 20_000
pips = round((1.3691 - 1.3652) * 10_000)
assert pips == 39 and u * 0.0001 == 2.0 and 39 * 2.0 == 78.0 and round(u * (1.3691 - 1.3652), 2) == 78.0
assert round(78 / 1.3691, 2) == 56.97 and 2 * 2.0 == 4.0 and round(u * 1.3652) == 27_304 and pct(78 / 27_304, 2) == "0.29%"
has(t, "C$78.00", "US$56.97", "C$4.00", "C$27,304", "0.29%", "39 pips")
u2 = bars("usdcad-daily")
c928, o929 = close_on(u2, "2026-09-28"), close_on(u2, "2026-09-29")
assert c928[4] == 1.3702 and o929[1] == 1.3619 and round((c928[4] - o929[1]) * 10_000) == 83
c1016 = close_on(u2, "2026-10-16")
assert c1016[4] == 1.3480 and min(x[3] for x in u2) == 1.3437 and c1016[3] == 1.3437
assert round((1.3702 - 1.3480) * 10_000) == 222 and round((1.3650 - 1.3437) * 10_000) == 213
assert u2[-1][0] == "2026-11-13" and u2[-1][4] == 1.3650
has(t, "1.3702", "1.3619", "1.3437", "1.3650", "83 pips", "222 pips", "213 pips", "1.3480")
assert round((1.3651 - 1.3648) * 10_000) == 3 and round(100_000 * 1.3651) == 136_510
has(t, "3 pips", "C$136,510")
assert round((1.3600 - 1.3562) * 10_000) == 38 and 50_000 * 0.0001 == 5 and 38 * 5 == 190
has(t, "38 pips", "C$190.00")
assert round(1.00 / 1.3500, 2) == 0.74
has(t, "US$0.74")
assert round(1 / 1.0800, 4) == 0.9259
has(t, "0.9259")

# ---- Lesson 5 ----
t = lesson(F, 5)
S = 1.3650
f = S * 1.025 / 1.04
assert round(f, 4) == 1.3453 and round(S - 1.3453, 4) == 0.0197
has(t, "1.3453", "0.0197")
usd0 = 100_000 / S
usd1 = usd0 * 1.04
assert round(usd0, 2) == 73260.07 and round(usd1, 2) == 76190.48
has(t, "US$73,260.07", "US$76,190.48")
assert round(usd1 * 1.3650, 2) == 104000.00 and round(100_000 * 1.025, 2) == 102_500
has(t, "C$104,000.00", "C$102,500", "C$1,500")
assert abs(usd1 * 1.3453 - 102_500) < 5
assert round(usd1 * 1.3200, 2) == 100571.43 and round(102_500 - 100571.43, 2) == 1928.57
has(t, "C$100,571.43", "C$1,928.57")
fe = 1.0800 * 1.04 / 1.03
assert round(fe, 4) == 1.0905
has(t, "1.0905")
assert round((S - 1.3453) * 10_000) == 197
has(t, "197 pips")
u50 = 50_000 / S * 1.04
assert round(u50, 2) == 38095.24 and round(u50 * 1.34, 2) == 51047.62 and round(50_000 * 1.025, 2) == 51_250
assert round(u50 * 1.34 - 51_250, 2) == -202.38
has(t, "US$38,095.24", "C$51,047.62", "C$51,250.00", "-C$202.38")

# ---- Lesson 6 ----
t = lesson(F, 6)
assert 10_000 * 1.3650 == 13_650 and 10_000 * 1.3240 == 13_240 and 13_240 - 13_650 == -410 and pct(1.3240 / 1.3650 - 1) == "-3.0%"
has(t, "C$13,650", "C$13,240", "-C$410", "-3.0%")
pos = 20_000 * 1.3650
assert round(pos) == 27_300 and round(0.02 * pos, 2) == 546.0 and 1 / 0.02 == 50
assert 100 * 2.0 == 200 and pct(200 / 546) == "36.6%"
assert round(546 / 20_000, 4) == 0.0273 and pct(0.0273 / 1.3650) == "2.0%"
has(t, "C$27,300", "C$546.00", "36.6%", "0.0273", "273 pips", "2.0%", "C$200")
assert 50 * 2.0 == 100
has(t, "C$100")
assert 25_000 * 1.35 == 33_750 and 25_000 * 1.38 == 34_500 and pct(750 / 33_750) == "2.2%"
has(t, "C$33,750", "C$34,500", "+C$750", "+2.2%")
assert round(1 / 0.033, 1) == 30.3
has(t, "30.3")
assert round(0.02 * 13_650, 2) == 273.0 and 273 / 2 == 136.5
has(t, "C$273.00", "136.5 pips")
assert 150 / 2.0 == 75
has(t, "75 pips")

# ---- Lesson 7 ----
t = lesson(F, 7)
assert round(0.9 * 42.0, 1) == 37.8 and round(37.8 / 20, 2) == 1.89 and pct(1.89 / 31.50) == "6.0%"
has(t, "US$37.8 million", "US$1.89", "6.0%", "US$42.0 million", "US$31.50")
assert round(0.9 * 60.0, 1) == 54.0 and 54.0 / 30 == 1.80
has(t, "US$54.0 million", "US$1.80")
assert pct(2.70 / 45.00) == "6.0%"
has(t, "US$45.00", "US$2.70")

# ---- Lesson 8 ----
t = lesson(F, 8)
noi = 168.0 - 60.0
pre = noi - 12.0 - 42.0 - 36.0
ni = pre + 12.0
assert noi == 108.0 and pre == 18.0 and ni == 30.0
eps = ni / 20
assert eps == 1.50 and pct(1.89 / eps, 0) == "126%"
has(t, "108.0", "18.0", "30.0", "US$1.50", "126%")
ffo = ni + 42 - 12
affo = ffo - 14 - 4
assert ffo == 60 and affo == 42 and ffo / 20 == 3.00 and affo / 20 == 2.10
has(t, "US$60.0 million", "US$3.00", "US$42.0 million", "US$2.10")
assert pct(1.89 / 2.10) == "90.0%" and pct(1.89 / 3.00) == "63.0%" and 31.50 / 3.00 == 10.5 and pct(2.10 / 31.50, 2) == "6.67%"
assert round(2.10 - 1.89, 2) == 0.21
has(t, "90.0%", "63.0%", "10.5", "6.67%", "US$0.21")
value = 108.0 / 0.075
assert round(value, 1) == 1440.0 and round(36.0 / 0.05) == 720
nav = value - 720
assert nav == 720.0 and nav / 20 == 36.00 and pct(31.50 / 36.00 - 1) == "-12.5%"
assert 31.50 * 20 == 630.0 and 630 + 720 == 1350 and pct(108 / 1350) == "8.0%"
has(t, "US$1,440.0 million", "US$720.0 million", "US$36.00", "-12.5%", "US$630.0 million", "US$1,350.0 million", "8.0%")
assert 50.0 + 80.0 - 20.0 == 110.0
has(t, "US$110.0 million")
a2 = 95.0 / 40
assert a2 == 2.375 and pct(2.20 / a2) == "92.6%"
has(t, "US$2.375", "92.6%")
assert pct(4.2 / 60.0) == "7.0%"
has(t, "7.0%")
v4 = 90.0 / 0.06
assert round(v4, 1) == 1500.0 and (v4 - 500.0) / 25 == 40.0
has(t, "US$1,500.0 million", "US$1,000.0 million", "US$40.00")

# ---- Lesson 9 ----
t = lesson(F, 9)
r = bars("reit-daily")
j26, j28 = close_on(r, "2026-06-26"), close_on(r, "2026-07-28")
assert j26[4] == 37.85 and j28[4] == 31.50 and pct(31.50 / 37.85 - 1) == "-16.8%"
aug = [x for x in r if x[0] >= "2026-07-29"]
assert max(x[2] for x in aug) == 32.12 and min(x[3] for x in r) == 31.23
has(t, "US$37.85", "US$31.50", "-16.8%", "31.23", "32.12")
v85 = 108.0 / 0.085
e85 = v85 - 720
assert round(v85, 1) == 1270.6 and pct(v85 / value - 1) == "-11.8%"
assert round(e85, 1) == 550.6 and round(e85 / 20, 2) == 27.53 and pct(e85 / 720 - 1) == "-23.5%"
v65 = 108.0 / 0.065
e65 = v65 - 720
assert round(v65, 1) == 1661.5 and pct(v65 / value - 1) == "15.4%" and round(e65, 1) == 941.5 and pct(e65 / 720 - 1) == "30.8%"
has(t, "US$1,270.6 million", "-11.8%", "US$550.6 million", "US$27.53", "-23.5%", "US$1,661.5 million", "+15.4%", "US$941.5 million", "+30.8%")
assert 200.0 * 0.025 == 5.0 and (60 - 5) / 20 == 2.75 and pct(2.75 / 3.00 - 1) == "-8.3%" and pct(1.89 / 2.75) == "68.7%"
has(t, "US$5.0 million", "US$2.75", "8.3%", "68.7%")
assert pct(2.10 / 31.50 - 0.04, 2) == "2.67%"
p2 = 2.10 / 0.0767
assert round(p2, 2) == 27.38 and pct(p2 / 31.50 - 1) == "-13.1%"
has(t, "2.67 points", "7.67%", "US$27.38", "13.1%")
assert 0.05 * 400_000 == 20_000 and 25_000 - 20_000 == 5_000 and pct(5_000 / 100_000) == "5.0%" and pct(25_000 / 500_000) == "5.0%"
assert 450_000 - 400_000 == 50_000
has(t, "C$20,000", "C$5,000", "C$50,000", "C$25,000", "5.0%")
a, b = 50.0 / 0.065, 50.0 / 0.075
assert round(a, 1) == 769.2 and round(b, 1) == 666.7 and pct(b / a - 1) == "-13.3%"
has(t, "US$769.2 million", "US$666.7 million", "-13.3%")
assert 1000 * 0.9 - 400 == 500 and pct(500 / 600 - 1) == "-16.7%"
has(t, "16.7%")
assert 72.00 * 40_000 == 2_880_000 and (72 - 68) * 40_000 == 160_000 and 2_880_000 - 160_000 == 2_720_000 and 2_720_000 / 40_000 == 68.0
has(t, usd(2_880_000, 0), "-US$160,000", usd(2_720_000, 0), "US$68.00")
assert round(-0.5 - (-2.0), 1) == 1.5
has(t, "+1.5 million")
r3 = (1 / 1.01) ** 12
assert round(r3, 4) == 0.8874 and pct(r3 - 1) == "-11.3%"
has(t, "0.8874", "11.3%")
assert round((1.3650 - 1.3620) * 10_000) == 30 and 30_000 * 0.0001 == 3.0 and 30 * 3.0 == 90.0
has(t, "C$3.00", "C$90.00")
f5 = 1.3400 * 1.02 / 1.035
assert round(f5, 4) == 1.3206
has(t, "1.3206")
assert 1 / 0.025 == 40 and 0.025 * 27_300 == 682.5
has(t, "C$682.50", "C$27,300")
ffo7 = 20.0 + 35.0 - 5.0
assert ffo7 == 50.0 and ffo7 / 25 == 2.00 and pct(1.60 / 2.00) == "80.0%"
has(t, "US$50.0 million", "US$2.00", "80.0%")
