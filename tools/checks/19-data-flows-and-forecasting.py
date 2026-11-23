"""Number checks for part 19, Data, flows and forecasting."""
import csv
import math
from datetime import date

from _lib import ROOT, lesson, has

F = "19-data-flows-and-forecasting"

# Lesson 1
t = lesson(F, 1)
assert 500 / 10 == 50 and round(1 / 0.11, 2) == 9.09 and round(500 * 0.11) == 55
assert 2000 / 10 == 200 and 300 / 10 == 30
has(t, "500 / 10 = 50 seconds", "1 / 0.11 = 9.09", "500 x 0.11 = 55 seconds", "2,000 / 10 = 200 seconds", "3 minutes and 20 seconds")

# Lesson 2
t = lesson(F, 2)
assert 5000 * 20.00 == 100_000 and 30_000 * 22 == 660_000 and 4_000 * 22 == 88_000
assert round(30_000 / 430_000 * 100, 1) == 7.0
assert 12_000 * 18.50 == 222_000 and 6_000 * 40 == 240_000
assert date(2026, 11, 19).weekday() == 3 and date(2026, 11, 18).weekday() == 2 and date(2026, 11, 16).weekday() == 0
has(t, "US$100,000", "US$660,000", "US$88,000", "7.0%", "US$222,000", "US$240,000", "November 18, 2026", "Thursday, November 19, 2026")

# Lesson 3
t = lesson(F, 3)
assert (650_000 - 500_000) / 500_000 == 0.30
v = 650_000 * 48.00
assert v == 31_200_000 and round(v / 400e6 * 100, 1) == 7.8
assert (date(2026, 11, 16) - date(2026, 9, 30)).days == 47
assert date(2026, 6, 30).toordinal() + 45 == date(2026, 8, 14).toordinal()
assert date(2026, 12, 31).toordinal() + 45 == date(2027, 2, 14).toordinal() and date(2027, 2, 14).weekday() == 6
assert 2_000_000 * 30 / 500e6 == 0.12
has(t, "+30%", "US$31,200,000", "7.8%", "47 days", "February 16, 2027", "12.0%", "US$60,000,000")

# Lesson 4
t = lesson(F, 4)
assert 6.0 / 1.5 == 4.0 and 6.0 / 40 == 0.15 and round((7.2 - 6.0) / 6.0, 3) == 0.2 and 7.2 / 1.5 == 4.8
fee30 = 5000 * 0.25 * 30 / 365
assert round(fee30, 2) == 102.74 and round(5000 * 0.02 * 30 / 365, 2) == 8.22 and round(fee30 / 5000 * 100, 2) == 2.05
assert round(8000 * 0.12 * 45 / 365, 2) == 118.36
assert (date(2026, 11, 24) - date(2026, 11, 13)).days == 11 and (date(2026, 12, 24) - date(2026, 12, 15)).days == 9
assert 9.0 / 3.0 == 3.0 and 9.0 / 60 == 0.15
has(t, "6.0 / 1.5 = 4.0 days", "15.0%", "+20.0%", "4.8", "US$102.74", "US$8.22", "2.05%", "US$118.36", "11 days", "9 days", "3.0 days")

# Lesson 5
t = lesson(F, 5)
assert 120_000 - 180_000 == -60_000 and -60_000 / 1_000_000 == -0.06 and -60_000 - (-45_000) == -15_000
assert (-60_000 + 150_000) / 240_000 == 0.375
assert 250_000 - 310_000 == -60_000 and -60_000 / 1_200_000 == -0.05
assert (60_000 + 80_000) / 200_000 == 0.70
assert date(2026, 11, 17).weekday() == 1 and date(2026, 11, 20).weekday() == 4
has(t, "-60,000", "-6.0%", "-15,000", "37.5%", "-5.0%", "70.0%", "Tuesday, November 17, 2026", "Friday, November 20")

# Lesson 6
t = lesson(F, 6)
assert 4200 / 600 == 7.0 and round(4200 * 1.35 * 100) == 567_000 and round((56.35 - 50) / 50 * 100, 1) == 12.7 and 4500 - 600 == 3900
assert 1500 / 250 == 6.0 and round(800 * 2.20 * 100) == 176_000 and 1650 - 250 == 1400
has(t, "7.0", "US$567,000", "US$56.35", "12.7%", "3,900", "6.0", "US$176,000", "+1,400")

# Lesson 7
t = lesson(F, 7)
rows = list(csv.DictReader((ROOT / "docs" / "assets" / "data" / "forecast-log.csv").open(encoding="utf-8")))
n = len(rows)
f = [float(r["forecast"]) for r in rows]
o = [int(r["outcome"]) for r in rows]
assert n == 60 and sum(o) == 28
b = sum((a - c) ** 2 for a, c in zip(f, o)) / n
assert round(b, 4) == 0.2295
base = sum(o) / n
assert round(base * (1 - base), 4) == 0.2489 and round(1 - b / (base * (1 - base)), 3) == 0.078
assert round(18 / 40 * 100) == 45 and round(27 / 60 * 100) == 45
ex = ((0.8 - 1) ** 2 + 0.3 ** 2 + 0.9 ** 2) / 3
assert round(ex, 4) == 0.3133
assert round(((0.6 - 1) ** 2 + 0.6 ** 2) / 2, 2) == 0.26
for lo, hi, exp in [(0, 0.25, (14, 0.14, 0.14)), (0.25, 0.5, (11, 0.34, 0.36)), (0.5, 0.75, (17, 0.65, 0.65)), (0.75, 1.01, (18, 0.85, 0.61))]:
    sel = [(a, c) for a, c in zip(f, o) if lo <= a < hi]
    got = (len(sel), round(sum(a for a, _ in sel) / len(sel), 2), round(sum(c for _, c in sel) / len(sel), 2))
    assert got == exp, (got, exp)
assert sum(c for a, c in zip(f, o) if a >= 0.75) == 11
se = math.sqrt(11 / 18 * (7 / 18) / 18)
assert round(se, 2) == 0.11 and 1.9 < (0.85 - 11 / 18) / se < 2.3
assert round(math.sqrt(0.6 * 0.4 / 20), 2) == 0.11
has(t, "0.2295", "0.2489", "0.078", "0.3133", "= 0.26", "11 of 18", "about 0.11", "28 of the 60", "46.7%", "45.0%", "0.04", "0.09", "0.81")

# Lesson 8
t = lesson(F, 8)
assert (0.60 + 0.64) / 2 == 0.62 and round(0.64 + 0.02, 2) == 0.66
assert round(0.70 - 0.66, 2) == 0.04 and round(0.04 / 0.66 * 100, 1) == 6.1
assert round(0.65 - 0.66, 2) == -0.01 and round(0.66 - 0.60, 2) == 0.06 and round(0.06 / 0.66 * 100, 1) == 9.1
assert round((0.30 + 0.34) / 2, 2) == 0.32 and round(0.34 + 0.01, 2) == 0.35
assert round(0.45 - 0.42, 2) == 0.03 and round(0.03 / 0.42 * 100, 1) == 7.1
assert round(((0.7 - 1) ** 2 + 0.2 ** 2 + 0.5 ** 2) / 3, 4) == 0.1267
assert round(0.50 - 0.42, 2) == 0.08
assert 4 / 5 == 0.8 and 4 / 50 == 0.08
assert date(2026, 11, 18).toordinal() + 2 == date(2026, 11, 20).toordinal() and date(2026, 11, 20).weekday() == 4
has(t, "US$0.62", "US$0.66", "+US$0.04", "6.1%", "-US$0.01", "US$0.06", "9.1%", "US$0.32", "= 0.35", "+US$0.03", "7.1%", "0.1267", "+US$0.08", "80%", "8%", "November 20, 2026", "August 14, 2026", "30 seconds", "3.0 days")
print("part 19 checks passed")
