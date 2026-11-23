"""Number checks for part 21, Crashes, scams and case studies."""
import math

import pandas as pd

from _lib import ROOT, lesson, has

F = "21-crashes-scams-and-case-studies"


def price(c, y, n=10, fv=100.0):
    i = y / 200
    return sum((c / 2) / (1 + i) ** k for k in range(1, 2 * n + 1)) + fv / (1 + i) ** (2 * n)


# ---- Lesson 1: 1929 and 1987
t = lesson(F, 1)
assert 10_000 * 0.95 - 9_000 == 500 and 500 / 1000 == 0.5
assert 10_000 * 0.90 - 9_000 == 0
has(t, "US$9,500", "US$500", "50% of it on a 5% fall", "US$0")
assert round(1 / (1 - 0.89) - 1, 2) == 8.09
has(t, "8.09", "809%")
assert round(1 - 41.22 / 381.17, 4) == 0.8919 and round(381.17 / 41.22 - 1, 2) == 8.25
has(t, "0.8919", "89.2%", "8.25", "825%")
assert 16_000 / 20_000 == 0.8
assert round(20_000 * 0.92 - 16_000) == 2_400 and 2_400 / 4_000 == 0.6
has(t, "US$18,400", "US$2,400", "60% of what you put in", "lost 40% on an 8% fall")
hold, d, cum, rows = 75.0, 0.10, 0.0, []
for r in range(1, 7):
    sold = 2 * d * hold
    hold *= 1 - d
    cum = d if r == 1 else 1 - (1 - cum) * (1 - d)
    rows.append((d, sold, cum))
    d = 0.004 * sold
assert round(rows[0][1], 1) == 15.0 and round(rows[1][0] * 100, 1) == 6.0
assert round(rows[1][1], 1) == 8.1 and round(rows[2][0] * 100, 2) == 3.24 and round(rows[2][1], 2) == 4.11
assert round(rows[5][2] * 100, 2) == 20.45
has(t, "US$15.0 billion", "6.0%", "US$8.1 billion", "3.24%", "US$4.11 billion", "20.45%")
assert 2 * 0.05 * 75 == 7.5 and 0.4 * 7.5 == 3.0 and 3.0 / 5 == 0.6
has(t, "US$7.5 billion", "3.0%", "0.6 of the first shock")

# ---- Lesson 2: LTCM and dot-com
t = lesson(F, 2)
assert 2000 / 100 == 20 and round(2000 * 10 * 0.0001, 6) == 2.0
assert round(2000 * 10 * 0.0020, 1) == 40.0 and round(2000 * 10 * 0.0015, 1) == 30.0
has(t, "20 to 1", "US$2.0 million", "US$40 million", "40% of its equity", "US$30 million", "30% of its equity")
assert round(100 / 2800 * 100, 2) == 3.57
has(t, "28% of equity", "3.57%")
assert 50 / 1000 == 0.05 and 1000 / 50 == 20
has(t, "5% removes the equity")
assert 2000 * 10 * 0.0008 == 16.0
has(t, "US$16 million")
assert round(1 / 0.10 - 1) == 9
has(t, "900%", "US$3.625 billion")
need = 5000 / 15
assert round(need, 1) == 333.3 and round(need / 0.2, 1) == 1666.7 and round(need / 0.2 / 100, 1) == 16.7
yrs = math.log(need / 0.2 / 100) / math.log(1.25)
assert round(yrs, 1) == 12.6
has(t, "US$333.3 million", "US$1,666.7 million", "16.7 times", "12.6 years")
yrs40 = math.log(need / 0.2 / 100) / math.log(1.40)
assert round(yrs40, 1) == 8.4
has(t, "8.4 years", "2.814", "0.3365")
assert round(math.log(16.67), 3) == 2.814 and round(math.log(1.40), 4) == 0.3365
assert 487.5 + 387.5 + 432.5 + 80 == 1387.5
has(t, "US$487.5 million", "US$387.5 million", "US$432.5 million", "US$80 million", "US$1.4 billion")
has(t, "50 times its sales")

# ---- Lesson 3: 2008
t = lesson(F, 3)
assets = 11.8 + 383.6
assert round(assets, 1) == 395.4 and round(assets / 11.8, 1) == 33.5 and round(11.8 / assets * 100, 2) == 2.98
has(t, "US$395.4 billion", "33.5 to 1", "2.98%", "1 / 40 = 2.5%")
assert 100 - 2 == 98 and 100 / 2 == 50 and 100 - 95 == 5
assert 2 / 0.05 == 40 and round(100 - 40) == 60
has(t, "US$98", "50 to 1", "US$95", "US$40 of bonds", "US$60", "60% of its portfolio")
assert 30 + 870 == 900 and 900 / 30 == 30 and round(30 / 900 * 100, 2) == 3.33
has(t, "US$900 billion", "30 to 1", "3.33%")
assert 8 / 0.04 == 200 and 8 / 0.08 == 100
has(t, "US$100 of bonds", "half of the portfolio")
assert round((1.00 - 0.97) * 10_000) == 300
has(t, "US$300")

# ---- Lesson 4: flash crash and COVID
t = lesson(F, 4)
assert round(75_000 / 0.09) == 833_333 and round(833_333 / 20) == 41_667
assert 0.09 * 10_000 == 900 and round(0.09 * 41_667) == 3_750 and round(3_750 / 900, 1) == 4.2
has(t, "833,333", "41,667", "900 a minute", "3,750 a minute", "4.2 times")
assert 100 * 40.00 == 4_000 and 100 * 0.01 == 1.0 and 4_000 - 1 == 3_999
has(t, "US$4,000", "US$1.00", "US$3,999")
assert round(3_000 * 0.93, 2) == 2_790 and round(3_000 * 0.87, 2) == 2_610 and round(3_000 * 0.80, 2) == 2_400
has(t, "2,790.00", "2,610.00", "2,400.00")
assert round(30_000 / 0.09) == 333_333
has(t, "333,333")
assert 250 * 25.0 == 6_250 and 250 * 0.01 == 2.5 and 6_250 - 2.5 == 6_247.5
has(t, "US$6,250", "US$2.50", "US$6,247.50")
assert round(4_000 * 0.93, 2) == 3_720 and round(4_000 * 0.87, 2) == 3_480 and round(4_000 * 0.8, 2) == 3_200
has(t, "3,720.00", "3,480.00", "3,200.00")
assert 500 + 200 == 700
has(t, "US$700 billion")

# ---- Lesson 5: GameStop
t = lesson(F, 5)
assert (30 - 20) * 1000 == 10_000 and 20 * 1000 == 20_000
assert 20_000 * 0.25 == 5_000 and round(5_000 / 365, 2) == 13.70
assert (348 - 20) * 1000 == 328_000 and round(348 / 20, 1) == 17.4 and 328_000 / 10_000 == 32.8
has(t, "US$20,000", "US$5,000 a year", "US$13.70 a day", "US$10,000", "US$328,000", "17.4 times", "32.8 times")
assert 0.5 * 500 * 40 == 10_000 and 40 + 10_000 / 500 == 60
has(t, "US$60.00")
assert round(1.2297 * 50, 3) == 61.485
has(t, "61.485 million")
assert round(347.51 / 17, 2) == 20.44
has(t, "US$20.44")
assert round(2.1 + 4.8, 1) == 6.9
has(t, "US$6.9 billion", "US$25.5 billion", "US$2.1 billion", "US$4.8 billion")

# ---- Lesson 6: Archegos and SVB
t = lesson(F, 6)
assert round(160 / 36, 1) == 4.4 and 36 / 160 == 0.225
has(t, "160 / 36 = 4.4 to 1", "36 / 160 = 22.5%")
assert 100 * 0.2 == 20 and 90 * 0.2 == 18 and 18 - 10 == 8
has(t, "US$18 million", "US$8 million")
d = pd.read_csv(ROOT / "tools/figures/12-bonds-and-the-yield-curve/treasury_2021_2026.csv", parse_dates=["Date"]).set_index("Date")
y0, y1 = d.loc["2021-12-31", "10 Yr"], d.loc["2022-12-30", "10 Yr"]
assert (y0, y1) == (1.52, 3.88) and round(y1 - y0, 2) == 2.36
loss = 6.2 * 2.36
assert round(loss, 1) == 14.6 and round(60 * loss / 100, 2) == 8.78
assert round(6 / (60 * 6.2 / 100), 2) == 1.61
has(t, "1.52%", "3.88%", "2.36 percentage points", "14.6%", "US$8.78", "1.61 percentage points")
assert 30 / 5 == 6 and round(5 / 30 * 100, 1) == 16.7
has(t, "6 to 1", "16.7%")
assert 50 * 0.9 == 45 and 45 * 0.2 == 9 and 10 - 5 == 5 and 9 - 5 == 4
has(t, "US$45 million", "US$9 million", "US$4 million")
assert 80 * 5 / 100 == 4.0 and 4 / 4.0 == 1.0
has(t, "6.2%", "1.0 percentage point")

# ---- Lesson 7: 2022 rate shock
t = lesson(F, 7)
assert (d.loc["2021-12-31", "3 Mo"], d.loc["2022-12-30", "3 Mo"]) == (0.06, 4.42)
assert (d.loc["2021-12-31", "2 Yr"], d.loc["2022-12-30", "2 Yr"]) == (0.73, 4.41)
x = d.loc["2022-01-01":"2022-12-31"]
assert x["10 Yr"].max() == 4.25 and str(x["10 Yr"].idxmax().date()) == "2022-10-24"
assert x["2 Yr"].max() == 4.72 and str(x["2 Yr"].idxmax().date()) == "2022-11-07"
has(t, "0.06%", "4.42%", "0.73%", "4.41%", "4.25% on October 24", "4.72% on November 7")
p0, p1 = price(1.52, 1.52), price(1.52, 3.88)
assert round(p0, 2) == 100.0 and round(p1, 2) == 80.59 and round((p1 / p0 - 1) * 100, 1) == -19.4
md = (price(1.52, 1.51) - price(1.52, 1.53)) / (2 * p0 * 0.0001)
cv = (price(1.52, 1.51) + price(1.52, 1.53) - 2 * p0) / (p0 * 0.0001**2)
dy = 0.0236
est = -md * dy
est2 = est + 0.5 * cv * dy**2
assert round(md, 2) == 9.24 and round(cv, 1) == 94.0
assert round(est * 100, 1) == -21.8 and round(0.5 * cv * dy**2 * 100, 1) == 2.6 and round(est2 * 100, 1) == -19.2
has(t, "US$80.59", "19.4%", "9.24 years", "94.0", "21.8%", "2.6%", "19.2%")
assert round(2 * 2.36, 1) == 4.7
has(t, "4.7%")
assert round(3 / 0.03) == 100 and round(3 / 0.05) == 60 and round(3 / 0.04) == 75
has(t, "US$100", "US$60", "40%", "US$75", "25%")
assert 6 * 1.5 == 9.0
assert round(-md * 0.01 * 100, 1) == -9.2 and round(0.5 * cv * 0.01**2 * 100, 2) == 0.47
assert round((-md * 0.01 + 0.5 * cv * 0.01**2) * 100, 1) == -8.8
has(t, "9%", "-9.2%", "0.47%", "-8.8%", "236 basis points")
assert round(p1 + 1.52 - 100, 1) == -17.9
has(t, "about 18%")

# ---- Lesson 8: pump and dumps
t = lesson(F, 8)
assert round(200_000 * 0.80) == 160_000 and round(200_000 * 2.10) == 420_000 and 420_000 - 160_000 == 260_000
assert round(200_000 / 300_000 * 100) == 67
assert round(100_000 * 2.20) == 220_000 and round(100_000 * 0.70) == 70_000 and 220_000 - 70_000 == 150_000 and round(150_000 / 220_000 * 100) == 68
has(t, "US$160,000", "US$420,000", "US$260,000", "67%", "US$220,000", "US$70,000", "US$150,000", "68%")
se = math.sqrt(0.8 * 0.2 / 20)
assert round(se, 4) == 0.0894 and round(80 - 1.96 * se * 100, 1) == 62.5 and round(80 + 1.96 * se * 100, 1) == 97.5
has(t, "0.0894", "8.9 points", "17.5 points", "62.5% to 97.5%")
assert round(0.8 * 0.5 - 0.2 * 3, 2) == -0.20
has(t, "-0.20R")
assert round(100_000 * 1.20 - 100_000 * 0.50) == 70_000
assert round(math.sqrt(0.9 * 0.1 / 10), 4) == 0.0949
has(t, "0.0949", "9.5 points")
assert round(0.7 * 1 - 0.3 * 3, 1) == -0.2
has(t, "-0.2R")
assert 150_000 / 500_000 == 0.3
has(t, "30%")

# ---- Lesson 9: prop firms and registration
t = lesson(F, 9)
assert 0.08 * 50_000 == 4_000 and 0.10 * 50_000 == 5_000 and 50_000 - 5_000 == 45_000 and 0.01 * 50_000 == 500
assert 5_000 / 500 == 10 and 53_000 - 5_000 == 48_000
has(t, "US$4,000", "US$5,000", "US$45,000", "US$500", "ten full losses", "US$48,000")
assert 150 / 0.25 == 600 and 150 / 0.20 == 750
has(t, "US$600", "US$750")
assert round(99 / (1 / 3)) == 297
has(t, "US$297")
assert 200 / 1_000 == 0.2
has(t, "20%")
assert 100_000 + 1_300_000 == 1_400_000
has(t, "C$1.4 million held, C$1 million covered")
assert 200 * (75 - 30) == 9_000
has(t, "US$9,000")
assert round(100 / 28, 2) == 3.57 and round(1 / 28 * 100, 1) == 3.6
has(t, "3.6%")
print("part 21 ok")
