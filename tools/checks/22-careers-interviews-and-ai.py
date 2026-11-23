"""Number checks for part 22, Careers, interviews and AI."""
import itertools
import math
import statistics as st
from fractions import Fraction

from _lib import lesson, has, usd, pct

F = "22-careers-interviews-and-ai"

# Lesson 1
t = lesson(F, 1)
assert 5_000_000 * 0.02 == 100_000 and 8_000_000 * 0.015 == 120_000
assert round(0.005 * 8000) == 40 and round(0.005 * 6000) == 30
fee_m, fee_p = 0.02 * 500, 0.20 * (50 - 0.02 * 500)
assert fee_m == 10 and fee_p == 8 and (fee_m + fee_p) / 500 == 0.036
has(t, "US$100,000", "US$120,000", "US$40 million", "US$30 million", "US$10 million (25%)",
    "US$10 million. The performance fee", "US$8 million", "US$18 million, or 3.6% of assets")

# Lesson 2
t = lesson(F, 2)
assert round(4000 / 3) == 1333 and round(1333 / 52, 1) == 25.6
assert 1000 * 0.41 == 410 and round(410 * 0.45, 1) == 184.5 and round(184.5 * 0.52, 1) == 95.9
assert round(2000 * 0.41 * 0.45 * 0.52, 1) == 191.9
assert 35 * 48 == 1680 and round(4000 / 1680, 2) == 2.38
has(t, "1,333 hours a year", "25.6 hours a week", "410 pass", "184.5 pass", "95.9 pass", "9.6 in 100",
    "191.9", "1,680 hours a year", "2.38 years", "41%", "45%", "52%", "4,000 hours")

# Lesson 3
t = lesson(F, 3)
se = 1.20 / math.sqrt(40)
assert round(se, 2) == 0.19
lo, hi = 0.315 - 1.96 * 0.19, 0.315 + 1.96 * 0.19
assert round(lo, 2) == -0.06 and round(hi, 2) == 0.69
assert round(1.20 / math.sqrt(160), 3) == 0.095
has(t, "1.20 / 6.325 = 0.19R", "from -0.06R to +0.69R", "0.095R", "plus or minus 0.37")
se = 1.0 / 5
assert round(0.2 - 1.96 * se, 2) == -0.19 and round(0.2 + 1.96 * se, 2) == 0.59
assert round((1.2 / 0.10) ** 2) == 144
has(t, "-0.19R to +0.59R", "144 trades")
r = [1.8, -0.9, -0.9, 2.1, -1.0, 0.4, -0.9, 3.0, -0.9, 1.5]
m, s = st.mean(r), st.stdev(r) / len(r) ** 0.5
assert round(m, 2) == 0.42, m
print("lesson 3 code:", round(m, 2), round(s, 2), round(m - 1.96 * s, 2), round(m + 1.96 * s, 2))
assert round(s, 2) == 0.49 and round(m - 1.96 * s, 2) == -0.54 and round(m + 1.96 * s, 2) == 1.38
has(t, "+0.42R", "0.49R", "-0.54R to +1.38R")

# Lesson 4
t = lesson(F, 4)
ev = 0.25 * 28.75 + 0.5 * 39.42 + 0.25 * 53.24
assert round(ev, 2) == 40.21
assert round(ev / 50 - 1, 3) == -0.196 and round(28.75 / 50 - 1, 3) == -0.425 and round(53.24 / 50 - 1, 3) == 0.065
assert round(ev / 1.10, 2) == 36.55 and round(33.33 / 39.42 - 1, 3) == -0.154 and round(33.33 / 50 - 1, 3) == -0.333
ev2 = 0.30 * 28.75 + 0.5 * 39.42 + 0.20 * 53.24
assert round(ev2, 2) == 38.98
assert 150 * 1.5 == 225 and 250 / 150 * 60 == 100
has(t, "US$40.21", "-19.6%", "-42.5%", "+6.5%", "36.55", "15.4% below US$39.42", "33.3% below the US$50.00",
    "US$38.98", "225 words", "US$36.50", "19.4%", "US$28.75, US$39.42 and US$53.24")

# Lesson 5
t = lesson(F, 5)
ni = 10 * (1 - 0.25)
assert ni == 7.5 and -7.5 + 10 == 2.5 and 2.5 - 10 == -7.5
assert 20 * 0.75 == 15 and -15 + 20 == 5 and 5 - 20 == -15
eq = 4925 + 150
assert eq == 5075 and eq + 275 - 130 == 5220 and round(5220 / 270, 1) == 19.3 and round(50 / 1.61, 1) == 31.1
assert 3000 + 800 + 100 - 300 == 3600 and 3600 / 300 == 12
has(t, "US$7.5", "+US$2.5", "-US$7.5", "US$5,220 million", "19.3 times", "31.1 times", "US$1.61",
    "US$3,600 million", "12.0", "+US$5", "net income by US$15", "-15")

# Lesson 6
t = lesson(F, 6)
assert Fraction(sum(range(1, 7)), 6) == Fraction(7, 2)
v2 = Fraction(4 + 5 + 6, 6) + Fraction(3, 6) * Fraction(7, 2)
assert v2 == Fraction(17, 4)
v3 = Fraction(5 + 6, 6) + Fraction(4, 6) * v2
assert round(float(v3), 2) == 4.67
rolls = [x for x in itertools.product(range(1, 7), repeat=2) if 6 in x]
good = [x for x in rolls if sum(x) >= 10]
assert len(rolls) == 11 and len(good) == 5 and round(5 / 11, 3) == 0.455
p = 0.009 / (0.009 + 0.99 * 0.09)
assert round(0.99 * 0.09, 4) == 0.0891 and round(p, 3) == 0.092
p2 = 0.018 / (0.018 + 0.98 * 0.09)
assert round(0.98 * 0.09, 4) == 0.0882 and round(p2, 3) == 0.169
# expected flips: solve small Markov systems by value iteration
def flips(target):
    states = {"": 0.0, "H": 0.0}
    for _ in range(4000):
        new = {}
        for sname in states:
            tot = 0.0
            for c in "HT":
                nxt = sname + c
                if nxt == target:
                    tot += 0.5 * 1
                else:
                    nxt = "H" if nxt.endswith("H") else ""
                    tot += 0.5 * (1 + states[nxt])
            new[sname] = tot
        states = new
    return states[""]
assert round(flips("HH"), 3) == 6 and round(flips("HT"), 3) == 4
assert 8 - (5 + 3.5) == -0.5 and 6 + 3.5 == 9.5 and 9.5 - 8 == 1.5
assert 23 * 11 == 253 and 65 ** 2 == 4225 and 0.15 * 240 == 36 and 47 * 11 == 517 and 35 ** 2 == 1225
assert 0.15 * 84 == 12.6 and 99 * 37 == 3663 and 17 * 13 == 221 and round(math.log(2) / math.log(1.08), 2) == 9.01
has(t, "US$4.25", "5 / 11 = 45.5%", "0.009 / 0.0981 = 9.2%", "0.0891", "16.9%", "US$4.67", "-US$0.50", "9.5",
    "US$1.5", "517", "1,225", "12.6", "3,663", "221", "253", "4,225", "9 years", "6 rolls")

# Lesson 7
t = lesson(F, 7)
xs, ys = [1, 2, 3, 4], [2, 4, 5, 9]
xb, yb = 2.5, 5
sxy = sum((x - xb) * (y - yb) for x, y in zip(xs, ys))
sxx = sum((x - xb) ** 2 for x in xs)
slope = sxy / sxx
assert sxy == 11 and sxx == 5 and slope == 2.2 and yb - slope * xb == -0.5 and round(-0.5 + 2.2 * 5, 1) == 10.5
assert round(1 - 0.95 ** 20, 3) == 0.642 and round(0.95 ** 20, 4) == 0.3585
assert round(1 - 0.95 ** 10, 3) == 0.401 and round(0.95 ** 10, 4) == 0.5987
import numpy as np
assert sorted(np.linalg.eigvalsh(np.array([[2, 1], [1, 2]]))) == [1.0, 3.0]
def max_drawdown(values):
    peak, worst = values[0], 0.0
    for v in values:
        peak = max(peak, v)
        worst = max(worst, (peak - v) / peak)
    return worst
assert round(max_drawdown([100, 120, 90, 110, 80, 130]), 4) == 0.3333
doors = [n for n in range(1, 101) if sum(1 for k in range(1, n + 1) if n % k == 0) % 2 == 1]
assert doors == [k * k for k in range(1, 11)]
emax = sum(max(a, b) for a in range(1, 7) for b in range(1, 7)) / 36
assert round(emax, 2) == 4.47 and sum(max(a, b) for a in range(1, 7) for b in range(1, 7)) == 161
has(t, "Slope = 11 / 5 = 2.2", "-0.5", "10.5", "64.2%", "40.1%", "0.3333", "161 / 36 = 4.47", "lambda = 3", "which is 1 - 1/3 = 2/3")

# Lesson 8
t = lesson(F, 8)
assert round(1150 / 1000 - 1, 3) == 0.15 and round(235 / 1150, 3) == 0.204 and round(165 / 123 - 1, 3) == 0.341
assert 165 + 35 + 30 - 25 == 205 and 300 - 25 == 275 and round(483 / 1150, 3) == 0.42 and round(165 / 102.5, 2) == 1.61
se = 1.2 / 6
assert round(0.30 - 1.96 * se, 2) == -0.09 and round(0.30 + 1.96 * se, 2) == 0.69
ev = 0.25 * 30 + 0.5 * 40 + 0.25 * 55
assert ev == 41.25 and round(45 / 41.25 - 1, 3) == 0.091
assert round(1 - 0.95 ** 15, 3) == 0.537 and round(0.95 ** 15, 4) == 0.4633
has(t, "15.0%", "20.4%", "21.4%", "34.1%", "US$205 million", "275 remains", "US$1.61", "42.0%",
    "-0.09R to +0.69R", "US$41.25", "9.1%", "53.7%", "Four of seven")
print("part 22 checks ok")
