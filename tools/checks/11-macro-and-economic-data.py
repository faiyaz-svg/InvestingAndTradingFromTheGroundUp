"""Number checks for part 11, Macro and economic data. Every worked example and answer is made up unless noted."""
import csv
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

from _lib import ROOT, lesson, has

F = "11-macro-and-economic-data"
L = {n: lesson(F, n) for n in range(1, 12)}

# ---- 1. measurement
t = L[1]
assert 190_000 - 150_000 == 40_000
assert (170_000 - 200_000) == -30_000 and 40_000 - 30_000 == 10_000
assert round(0.1 / 4.2 * 100, 1) == 2.4
a3, a5 = (1.003**12 - 1) * 100, (1.005**12 - 1) * 100
assert round(a3, 2) == 3.66 and round(a5, 2) == 6.17 and round(a5 - a3, 1) == 2.5
has(t, "+40,000", "-30,000", "+10,000", "3.66%", "6.17%", "2.4%")
assert round((1.004**12 - 1) * 100, 1) == 4.9
has(t, "4.9%", "-0.3 percentage points")

# ---- 2. the Fed and futures odds
t = L[2]
R0, D = 3.625, 0.25


def odds(price):
    return (R0 - (100 - price)) / D


assert abs(odds(96.50) - 0.50) < 1e-9 and abs(odds(96.55) - 0.70) < 1e-9
assert abs(odds(96.60) - 0.90) < 1e-9 and abs(odds(96.375)) < 1e-9
has(t, "50%", "70%", "90%", "96.375", "3.45%")
assert (date(2026, 10, 28) + timedelta(days=21)) == date(2026, 11, 18)
assert date(2026, 3, 17) + timedelta(days=22) == date(2026, 4, 8)  # minutes listed April 8
has(t, "November 18, 2026", "3.25% to 3.50%", "4.00% to 4.25%")


# ---- 3. present value
def pv(cfs, r):
    return sum(c / (1 + r) ** y for y, c in cfs)


A = [(y, 20) for y in range(1, 6)]
B = [(10, 100)]
t = L[3]
vals = {(n, r): pv(c, r) for n, c in (("A", A), ("B", B)) for r in (0.03, 0.06)}
for v in ("91.59", "84.25", "74.41", "55.84"):
    has(t, "US$" + v)
assert round(vals["A", 0.03], 2) == 91.59 and round(vals["A", 0.06], 2) == 84.25
assert round(vals["B", 0.03], 2) == 74.41 and round(vals["B", 0.06], 2) == 55.84
assert round((vals["A", 0.06] / vals["A", 0.03] - 1) * 100, 1) == -8.0
assert round((vals["B", 0.06] / vals["B", 0.03] - 1) * 100, 1) == -25.0
has(t, "-8.0%", "-25.0%")
p1, p2 = 100 / 1.04**5, 100 / 1.05**5
assert round(p1, 2) == 82.19 and round(p2, 2) == 78.35 and round((p2 / p1 - 1) * 100, 1) == -4.7
has(t, "US$82.19", "US$78.35", "-4.7%")
c = pv([(2, 50), (4, 50)], 0.05)
assert round(50 / 1.05**2, 2) == 45.35 and round(50 / 1.05**4, 2) == 41.14 and round(c, 2) == 86.49
has(t, "45.35", "41.14", "US$86.49")

# ---- 4. inflation
t = L[4]
assert round(0.8 * 0.4 + 0.2 * -0.2, 2) == 0.28
assert round((320.96 / 320 - 1) * 100, 2) == 0.30 and round((320.96 / 310 - 1) * 100, 1) == 3.5
has(t, "0.28%", "0.30%", "3.5%")
assert round(0.75 * 0.3 + 0.25 * 0.7, 3) == 0.40
assert round((250.75 / 250 - 1) * 100, 2) == 0.30 and round((250.75 / 240 - 1) * 100, 2) == 4.48
has(t, "0.40%", "4.48%", "4.5%", "0.225% + 0.175%")
# figure data: BLS peaks
sys.path.insert(0, str(ROOT / "tools" / "figures" / F))
from cpi_headline_core import yoy  # noqa: E402

d = yoy()
ph = max(d, key=lambda r: r[3])
pc = max(d, key=lambda r: r[4])
assert (ph[1], ph[2], round(ph[3], 1)) == (2022, 6, 9.1)
assert (pc[1], pc[2], round(pc[4], 1)) == (2022, 9, 6.6)
has(t, "9.1% in June 2022", "6.6% in September 2022", "November 21, 2026")
rows = list(csv.DictReader(open(ROOT / "tools" / "figures" / F / "bls_cpi.csv")))
assert [r for r in rows if r["cpi_all"] == "-"] == [r for r in rows if (r["year"], r["month"]) == ("2025", "10")]

# ---- 5. jobs
t = L[5]
l0, l1 = 160.0 + 6.9, 160.2 + 7.2
assert round(6.9 / l0 * 100, 2) == 4.13 and round(7.2 / l1 * 100, 2) == 4.30
assert round(36.18 / 36.00 * 100 - 100, 1) == 0.5
has(t, "166.9", "167.4", "4.13%", "4.30%", "0.5%")
assert round(6.0 / 156.0 * 100, 2) == 3.85
assert round((34.76 / 34.50 - 1) * 100, 2) == 0.75
has(t, "3.85%", "0.75%", "156.0 million")
assert date(2026, 11, 6).weekday() == 4 and date(2026, 12, 4).weekday() == 4

# ---- 6. growth
t = L[6]
assert 40 + 0.5 * 30 == 55 and 35 + 0.5 * 45 == 57.5
assert round((1.005**4 - 1) * 100, 2) == 2.02 and round((1.006**4 - 1) * 100, 1) == 2.4
has(t, "D = 40 + 0.5 x 30 = 55", "57.5", "2.02%", "2.4%")
assert round(2.0 - 0.6, 1) == 1.4 and round(2.0 + 0.6, 1) == 2.6 and round(1.8 - 0.6, 1) == 1.2 and round(1.8 + 0.6, 1) == 2.4
has(t, "1.4%", "2.6%", "1.2%")
assert date(2026, 4, 1).weekday() == 2  # Wednesday

# ---- 7. calendar
t = L[7]
assert date(2026, 12, 1).weekday() == 1 and date(2026, 12, 3).weekday() == 3
assert date(2026, 12, 4).weekday() == 4 and date(2026, 12, 9).weekday() == 2
fmt = "%H:%M"
m1 = (datetime.strptime("09:30", fmt) - datetime.strptime("08:30", fmt)).seconds // 60
m2 = (datetime.strptime("16:00", fmt) - datetime.strptime("14:00", fmt)).seconds // 60
assert (m1, m2) == (60, 120)
has(t, "60 minutes", "120 minutes", "Tuesday, December 1", "Friday, December 4", "Wednesday, December 9")

# ---- 8. reaction
t = L[8]
assert round(odds(96.55), 2) == 0.70 and round(odds(96.45), 2) == 0.30
assert round(3.92 - 3.80, 2) == 0.12
assert round(1.3800 * 1.005, 4) == 1.3869 and round((1.3868 / 1.38 - 1) * 100, 1) >= 0.5 - 0.1
assert round((4940 / 5000 - 1) * 100, 1) == -1.2
assert round((1.3568 / 1.3500 - 1) * 100, 2) == 0.50
has(t, "1.3869", "-1.2%", "+12 bp", "70%", "30%", "6.2%", "3.7%", "90%", "0.50%")

# ---- 9. cycle
t = L[9]
cyc = 64.2 + 10.3
assert round(cyc, 1) == 74.5 and round(cyc / 12, 1) == 6.2
assert round(64.2 / cyc * 100, 1) == 86.2 and round(10.3 / cyc * 100, 1) == 13.8
c2 = 41.4 + 17.0
assert round(c2, 1) == 58.4 and round(41.4 / c2 * 100, 1) == 70.9
has(t, "74.5 months", "86.2%", "13.8%", "58.4 months", "70.9%")

# ---- 10. balance sheet
t = L[10]
assert 6000 + 200 == 6200 and 3000 + 200 == 3200 and round(200 / 3000 * 100, 1) == 6.7
assert 6200 - 150 == 6050 and 3200 - 150 == 3050 and round(50 / 6000 * 100, 1) == 0.8
assert 5000 + 300 == 5300 and 300 / 5000 == 0.06 and 5300 - 100 == 5200
has(t, "US$6,200 billion", "US$3,200 billion", "6.7%", "US$6,050 billion", "US$3,050 billion", "0.8%", "5,300", "6.0%", "US$5,200 billion")

# ---- 11. BoC and the week
t = L[11]
e0, e1 = 3.625 - 0.25 * 0.70, 3.625 - 0.25 * 0.30
assert round(e0, 2) == 3.45 and round(e1, 2) == 3.55
assert round(e0 - 2.75, 2) == 0.70 and round(e1 - 2.75, 2) == 0.80
has(t, "3.45%", "3.55%", "0.70 percentage points", "0.80 percentage points")
assert 190_000 - 150_000 == 40_000
has(t, "+40,000", "+10,000")
boc = [date(2026, m, dd) for m, dd in [(1, 28), (3, 18), (4, 29), (6, 10), (7, 15), (9, 2), (10, 28), (12, 9)]]
fomc_end = [date(2026, m, dd) for m, dd in [(1, 28), (3, 18), (4, 29), (6, 17), (7, 29), (9, 16), (10, 28), (12, 9)]]
assert len([x for x in boc if x in fomc_end]) == 5
assert (datetime.strptime("09:45", fmt) - datetime.strptime("09:30", fmt)).seconds // 60 == 15
has(t, "15 minutes", "five Bank of Canada decision days")
