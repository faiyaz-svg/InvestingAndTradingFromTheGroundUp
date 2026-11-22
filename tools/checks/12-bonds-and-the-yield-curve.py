"""Number checks for part 12, Bonds and the yield curve."""
import csv
from math import erf, sqrt

from _lib import ROOT, lesson, has, usd, num, pct

F = "12-bonds-and-the-yield-curve"
FIG = ROOT / "tools" / "figures" / F


def price(face, c, y, years):
    i = y / 2
    n = round(2 * years)
    cpn = face * c / 2
    return sum(cpn / (1 + i) ** k for k in range(1, n + 1)) + face / (1 + i) ** n


def measures(face, c, y, years):
    i = y / 2
    n = round(2 * years)
    p = price(face, c, y, years)
    cfs = [(k, face * c / 2 + (face if k == n else 0)) for k in range(1, n + 1)]
    dmac = sum(k / 2 * cf / (1 + i) ** k for k, cf in cfs) / p
    conv = sum(cf * k * (k + 1) / 4 / (1 + i) ** (k + 2) for k, cf in cfs) / p
    return p, dmac, dmac / (1 + i), conv


def ytm(p, face, c, years):
    lo, hi = 0.0, 0.5
    for _ in range(100):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if price(face, c, mid, years) > p else (lo, mid)
    return mid


def phi(z):
    return 0.5 * (1 + erf(z / sqrt(2)))


def signed(x, d=2):
    """Format a percentage change the way the lessons print it."""
    s = f"{100 * x:.{d}f}%"
    return "+" + s if x > 0 else s


# ---- Lesson 1 ----
t = lesson(F, 1)
pv_c = 20 * (1 - 1.025 ** -20) / 0.025
pv_f = 1000 / 1.025 ** 20
p5 = price(1000, 0.04, 0.05, 10)
assert abs(pv_c + pv_f - p5) < 1e-9
has(t, usd(pv_c), usd(pv_f), usd(p5), "92.205")
rows = {0.03: (1085.84, "+8.6%", "3.68%"), 0.04: (1000.00, "0.0%", "4.00%"), 0.05: (922.05, "-7.8%", "4.34%"), 0.06: (851.23, "-14.9%", "4.70%")}
for y, (p, chg, cy) in rows.items():
    pp = price(1000, 0.04, y, 10)
    assert round(pp, 2) == p
    if chg != "0.0%":
        assert signed(pp / 1000 - 1, 1) == chg
    assert pct(40 / pp, 2) == cy
    has(t, num(p), chg, cy)
assert pct(ytm(950, 1000, 0.04, 10), 2) == "4.63%" and pct(40 / 950, 2) == "4.21%"
has(t, "4.63%", "4.21%")
p492 = price(1000, 0.04, 0.0492, 10)
assert round(p492, 2) == 928.02 and pct(1 - p492 / 1000) == "7.2%"
has(t, usd(p492), "7.2%", "4.92%")
acc = 20 * 60 / 182
assert round(acc, 2) == 6.59 and round(922.05 + acc, 2) == 928.64
has(t, usd(acc), usd(922.05 + acc))
p_e1 = price(1000, 0.03, 0.04, 5)
assert round(15 * (1 - 1.02 ** -10) / 0.02, 2) == 134.74 and round(1000 / 1.02 ** 10, 2) == 820.35
assert round(p_e1, 2) == 955.09 and pct(30 / p_e1, 2) == "3.14%"
has(t, usd(134.74), usd(820.35), usd(p_e1), "3.14%")
assert 20 * 91 / 182 == 10.0
has(t, "US$10.00", "US$1,010.00", "0.0246")

# ---- Lesson 2 ----
t = lesson(F, 2)
P = 10000 * (1 - 0.04 * 182 / 360)
assert round(P, 2) == 9797.78 and round(10000 - P, 2) == 202.22
bey = (10000 - P) / P * 365 / 182
assert abs(bey - 365 * 0.04 / (360 - 0.04 * 182)) < 1e-12 and pct(bey, 2) == "4.14%"
has(t, usd(P), usd(10000 - P), "4.14%")
P2 = 10000 * (1 - 0.042 * 91 / 360)
assert round(P2, 2) == 9893.83 and round(10000 - P2, 2) == 106.17
assert pct(365 * 0.042 / (360 - 0.042 * 91), 2) == "4.30%"
has(t, usd(P2), usd(10000 - P2), "4.30%")
assert 1000 * 1.03 == 1030 and round(0.015 * 1030, 2) == 15.45 and round(0.015 * 1030 / 2, 3) == 7.725
assert 1000 * 0.98 == 980
has(t, usd(1030), usd(15.45), "US$7.725", usd(980), usd(1000))
assert pct(1.04 / 1.018 - 1, 2) == "2.16%"
has(t, "2.16%", "2.20%")
assert 5000 * 1.045 == 5225 and 0.02 * 5225 == 104.5
has(t, usd(5225), usd(104.5))
assert pct(1.038 / 1.016 - 1, 2) == "2.17%"
has(t, "2.17%")
assert pct(1.018 * 1.03 - 1, 2) == "4.85%"
has(t, "4.85%")

# ---- Lesson 3 ----
t = lesson(F, 3)
rows = {r["Date"]: r for r in csv.DictReader(open(FIG / "treasury_par_curves.csv", encoding="utf8"))}
exp = {
    "2000-12-29": ("5.89", "5.11", "5.12", "0.01", "-0.77"),
    "2019-12-31": ("1.55", "1.58", "1.92", "0.34", "0.37"),
    "2022-12-30": ("4.42", "4.41", "3.88", "-0.53", "-0.54"),
    "2026-11-20": ("4.32", "4.63", "4.92", "0.29", "0.60"),
}
for d, (m3, y2, y10, s210, s310) in exp.items():
    r = rows[d]
    assert (r["3 Mo"], r["2 Yr"], r["10 Yr"]) == (m3, y2, y10), d
    assert f"{float(y10) - float(y2):.2f}" == s210 and f"{float(y10) - float(m3):.2f}" == s310, d
    has(t, f"| {m3} | {y2} | {y10} | {s210} | {s310} |")
h = list(csv.DictReader(open(FIG / "treasury_2021_2026.csv", encoding="utf8")))


def longest_negative_run(key):
    best, cur = [], []
    for r in h:
        s = float(r["10 Yr"]) - float(r[key])
        if s < 0:
            cur.append((r["Date"], s))
        else:
            best = cur if len(cur) > len(best) else best
            cur = []
    return cur if len(cur) > len(best) else best


a, b = longest_negative_run("2 Yr"), longest_negative_run("3 Mo")
assert (a[0][0], a[-1][0], len(a), round(min(s for _, s in a), 2)) == ("2022-07-06", "2024-08-26", 537, -1.08)
assert (b[0][0], b[-1][0], len(b), round(min(s for _, s in b), 2)) == ("2022-10-25", "2024-12-12", 534, -1.89)
assert sum(1 for r in h if r["Date"].startswith("2025") and float(r["10 Yr"]) - float(r["3 Mo"]) < 0) == 86
has(t, "86 trading days in 2025")
has(t, "July 6, 2022 to August 26, 2024 (537 trading days)", "-1.08", "October 25, 2022 to December 12, 2024 (534 trading days)", "-1.89")
for s, e in [(0, 27.3), (-1, 55.3), (2, 1.9)]:
    assert round(100 * phi(-0.6045 - 0.7374 * s), 1) == e
has(t, "27.3%", "55.3%", "1.9%", "0.1329", "2.0793")
assert round(-0.6045 + 0.7374, 4) == 0.1329 and round(-0.6045 - 0.7374 * 2, 4) == -2.0793
assert round(100 * phi(-0.6045 + 0.7374 * 0.54), 1) == 41.8 and round(-0.6045 + 0.7374 * 0.54, 4) == -0.2063
has(t, "41.8%", "0.2063")
u = [3.9, 3.8, 3.7, 3.7, 3.6, 3.6, 3.7, 3.7, 3.8, 3.9, 4.0, 4.2, 4.3, 4.4, 4.5]
avg = {m: sum(u[m - 3:m]) / 3 for m in range(3, 16)}


def gap(m):
    return avg[m] - min(avg[k] for k in range(max(3, m - 12), m))


assert round(min(avg[k] for k in range(3, 13)), 2) == 3.63
assert round(avg[12], 2) == 4.03 and round(gap(12), 2) == 0.40
assert round(avg[13], 2) == 4.17 and round(gap(13), 2) == 0.53
assert [m for m in range(4, 16) if gap(m) >= 0.5][0] == 13
has(t, "3.63", "4.03", "gap of 0.40", "4.17", "gap of 0.53")
assert round((3.8 + 3.9 + 4.0) / 3 - 3.40, 2) == 0.50
has(t, "3.90", "0.50")
has(t, "-0.08", "-3.51", "0.00 percentage points for October 2026")

# ---- Lesson 4 ----
t = lesson(F, 4)
i = 0.025
pvs = [(20 + (1000 if k == 6 else 0)) / (1 + i) ** k for k in range(1, 7)]
Ptot = sum(pvs)
w = [x / Ptot for x in pvs]
wt = [wi * k / 2 for k, wi in zip(range(1, 7), w)]
p3, dmac3, dmod3, conv3 = measures(1000, 0.04, 0.05, 3)
assert abs(Ptot - p3) < 1e-9 and abs(sum(wt) - dmac3) < 1e-9
for x in pvs:
    has(t, f"| {x:,.2f} |")
for x in w + wt:
    has(t, f"{x:.4f}")
has(t, usd(p3), "2.85 years", "2.854 / 1.025 = 2.78", "-2.78%")
p3b = price(1000, 0.04, 0.06, 3)
assert round(p3b, 2) == 945.83 and pct(p3b / p3 - 1, 2) == "-2.74%"
has(t, usd(p3b), "-2.74%")
pA, dmacA, dmodA, convA = measures(1000, 0.04, 0.04, 10)
assert round(dmodA, 2) == 8.18 and round(convA, 1) == 78.9
h_ = 1e-4
d1 = -(price(1000, .04, .04 + h_, 10) - price(1000, .04, .04 - h_, 10)) / (2 * h_) / pA
d2 = (price(1000, .04, .04 + h_, 10) - 2 * pA + price(1000, .04, .04 - h_, 10)) / h_ ** 2 / pA
assert abs(d1 - dmodA) < 1e-4 and abs(d2 - convA) < 0.05
for yrs, dm in [(2, "1.90"), (5, "4.49"), (10, "8.18"), (30, "17.38")]:
    assert f"{measures(1000, .04, .04, yrs)[2]:.2f}" == dm
    has(t, f"| {dm} |")
assert round(measures(1000, .04, .04, 30)[3]) == 421
has(t, "421", "79 for Bond A", "1.9%", "17.4%")
for dy in (0.01, -0.01, 0.02):
    act = price(1000, .04, .04 + dy, 10) / pA - 1
    dur_only = -dmodA * dy
    with_c = dur_only + 0.5 * convA * dy ** 2
    has(t, signed(dur_only), signed(with_c), signed(act))
assert round(100 * 0.5 * convA * 0.0001, 2) == 0.39
has(t, "+0.39%")
dv = dmodA * 1000 * 0.0001
assert round(dv, 2) == 0.82 and round(dmodA * 100000 * 0.0001, 2) == 81.76 and round(25 * 81.76) == 2044
has(t, usd(dv), usd(81.76), "US$2,044")
assert round(-6.0 * 0.005, 3) == -0.03
has(t, "-3.0%")
assert round(dmod3 * p3 * 0.0001, 2) == 0.27
has(t, "US$0.27")
dv250 = dmodA * 250000 * 0.0001
assert round(dv250, 2) == 204.39 and round(30 * dv250) == 6132 and round(100 * dmodA * 0.003, 2) == 2.45
has(t, usd(204.39), "US$6,132", "2.45%")

# ---- Lesson 5 ----
t = lesson(F, 5)
assert round(0.02 * 0.6, 4) == 0.012 and round(4.00 - 1.20, 2) == 2.80 and round(8.00 - 1.20, 2) == 6.80
assert round(0.002 * 0.6 * 100, 2) == 0.12 and round(1.00 - 0.12, 2) == 0.88
has(t, "1.20%", "2.80 percentage points", "6.80%", "0.12%", "0.88 percentage points", "US$400", "US$600")
assert round(7 * 0.005, 3) == 0.035
has(t, "3.5%")
assert round(6.30 - 4.10, 2) == 2.20
has(t, "220 basis points")
el = 0.015 * (1 - 0.35)
assert round(100 * el, 4) == 0.975 and round(2.80 - 100 * el, 3) == 1.825
has(t, "0.975%", "1.825 percentage points")
assert round(-5.5 * 0.012, 3) == -0.066 and round(-5.5 * 0.008, 3) == -0.044
has(t, "-6.6%", "-4.4%")
assert 4.00 + 0.12 + 0.88 == 5.00 and 4.00 + 1.20 + 2.80 == 8.00
has(t, "5.00%", "8.00%")

# ---- Lesson 6 ----
t = lesson(F, 6)
pr, yy, dd = 80.00, 0.045, 6.0
assert round(-dd * 0.01 * pr, 2) == -4.80 and round(pr - 4.80, 2) == 75.20 and round(yy * pr, 2) == 3.60
assert round(-4.80 + 3.60, 2) == -1.20 and round((-4.80 + 3.60) / pr * 100, 1) == -1.5
assert round(100 * yy / dd, 2) == 0.75 and round(6.0 + 4.5, 1) == 10.5
has(t, "-US$4.80", "US$75.20", "US$3.60", "-US$1.20", "-1.5%", "0.75 percentage points", "+10.5%")
assert pct(1 / 20, 2) == "5.00%" and pct(1 / 25, 2) == "4.00%"
has(t, "5.00%", "4.00%", "1.00 percentage point")
assert round(6.0 * 0.005, 3) == 0.03 and round(0.03 + 0.045, 3) == 0.075
has(t, "+3.0%", "+7.5%" if False else "about +7.5%")
assert round(3.00 - 0.015 * 0.6 * 100, 2) == 2.10 and round(0.015 * 0.6 * 100, 2) == 0.90
has(t, "0.90%", "2.10 percentage points", "300 basis points")
assert pct(1 / 16, 2) == "6.25%" and round(6.25 - 4.00, 2) == 2.25
has(t, "6.25%", "2.25 percentage points", "0.29 percentage points")
has(t, usd(922.05), usd(9797.78), "4.14%")
