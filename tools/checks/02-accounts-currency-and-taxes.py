"""Number checks for part 2, Accounts, currency and taxes."""
import math
from datetime import date, timedelta

from _lib import lesson, has

F = "02-accounts-currency-and-taxes"

# Lesson 1: TFSA room
t = lesson(F, 1)
tfsa = {2009: 5000, 2010: 5000, 2011: 5000, 2012: 5000, 2013: 5500, 2014: 5500, 2015: 10000, 2016: 5500, 2017: 5500,
        2018: 5500, 2019: 6000, 2020: 6000, 2021: 6000, 2022: 6000, 2023: 6500, 2024: 7000, 2025: 7000, 2026: 7000}
assert sum(tfsa.values()) == 109_000
r14_25 = sum(v for y, v in tfsa.items() if 2014 <= y <= 2025)
assert r14_25 == 76_500 and r14_25 + 7000 == 83_500
has(t, "$109,000", "$76,500", "$83,500", "7,000 + 4,000 = $11,000", "$16,000")

# Lesson 2: cost model
t = lesson(F, 2)


def yearly(n, c, f, v, fixed):
    return n * (c + 2 * f * v) + fixed


assert round(yearly(40, 0, .015, 8000, 0)) == 9600
assert round(yearly(40, 5, .005, 8000, 120)) == 3520
assert round(yearly(20, 0, .015, 10000, 0)) == 6000
assert round(yearly(20, 5, .005, 10000, 120)) == 2220
assert 300_000 + 200_000 == 500_000
has(t, "C$9,600", "C$3,520", "C$6,000", "C$2,220", "C$500,000")

# Lesson 3
t = lesson(F, 3)
r = 1.38
buy = 10000 * r * 1.015
sell = 10000 * r * 0.985
assert round(buy, 2) == 14007.00 and round(sell, 2) == 13593.00 and round(buy - sell, 2) == 414.00
assert round((buy - sell) / buy * 100, 2) == 2.96
b2 = 10000 * r * 1.01
s2 = 10000 * r * 0.99
assert round(b2, 2) == 13938.00 and round(s2, 2) == 13662.00 and round(b2 - s2, 2) == 276.00
assert round((b2 - s2) / b2 * 100, 2) == 1.98 and round(414 - 276) == 138
eff = 14000 / 9950
assert round(eff, 4) == 1.4070 and round((round(eff, 4) - 1.38) / 1.38 * 100, 2) == 1.96
q1 = (5000 * 1.4 * 1.015, 5000 * 1.4 * 0.985)
assert round(q1[0], 2) == 7105.00 and round(q1[1], 2) == 6895.00 and round(q1[0] - q1[1], 2) == 210.00
rate = 1.35 * 1.005
assert round(rate, 5) == 1.35675 and round(30000 / rate, 2) == 22111.66, 30000 / rate
assert round((1.41 - 1.39) / 1.39 * 100, 2) == 1.44
has(t, "C$14,007.00", "C$13,593.00", "C$414.00", "2.96%", "C$13,938.00", "C$13,662.00", "C$276.00", "1.98%",
    "C$138", "1.4070", "1.96%", "C$7,105.00", "C$6,895.00", "C$210.00", "1.35675", "US$22,111.66", "1.44%")

# Lesson 4


def gambit(amount, ask=13.81, bid=9.99, rate=1.38, fees=30):
    sh = math.floor(amount / ask)
    cost = sh * ask
    us = sh * bid
    back = us * rate
    return sh, cost, us, back, cost - back, cost - back + fees


t = lesson(F, 4)
sh, cost, us, back, spread, total = gambit(50000)
assert sh == 3620 and round(cost, 2) == 49992.20 and round(us, 2) == 36163.80 and round(back, 2) == 49906.04
assert round(spread, 2) == 86.16 and round(total, 2) == 116.16 and round(total / cost * 100, 2) == 0.23
assert 50000 * .005 == 250 and round(250 - total) == 134
sh, cost, us, back, spread, total = gambit(5000)
assert sh == 362 and round(cost, 2) == 4999.22 and round(total, 2) == 38.62 and round(total / cost * 100, 2) == 0.77
sh, cost, us, back, spread, total = gambit(20000)
assert sh == 1448 and round(cost, 2) == 19996.88 and round(us, 2) == 14465.52 and round(back, 2) == 19962.42
assert round(spread, 2) == 34.46 and round(total, 2) == 64.46 and round(total / cost * 100, 2) == 0.32
assert round(1.10 * .95 - 1, 3) == 0.045
has(t, "3,620", "C$49,992.20", "US$36,163.80", "C$49,906.04", "C$86.16", "C$116.16", "0.23%", "C$250",
    "362 shares for C$4,999.22", "C$38.62", "0.77%", "1,448", "C$19,996.88", "US$14,465.52", "C$19,962.42",
    "C$34.46", "C$64.46", "0.32%", "C$200", "4.5%")

# Lesson 5
t = lesson(F, 5)
assert 100 * 50 * 1.4 == 7000 and round(100 * 55 * 1.33, 2) == 7315 and round(7315 - 7000) == 315
assert round(1.33 / 1.4 - 1, 3) == -0.05 and round(1.10 * .95 - 1, 3) == 0.045
rx = 1.4 / 1.36 - 1
assert round(rx * 100, 2) == 2.94 and round((1.10 * (1 + rx) - 1) * 100, 1) == 13.2
assert round(8000 * 1.36) == 10880 and round(8800 * 1.4) == 12320 and 12320 - 10880 == 1440
assert round((1.3 / 1.4 - 1) * 100, 1) == -7.1
assert round(20000 * 1.41 - 20000 * 1.40) == 200
has(t, "C$7,000", "C$7,315", "C$315", "4.5%", "-5.0%", "2.94%", "13.2%", "C$10,880", "C$12,320", "C$1,440", "-7.1%", "C$200")

# Lesson 6
t = lesson(F, 6)
gross = 200 * 0.5
assert gross == 100 and round(gross * 1.38, 2) == 138.00 and gross * .15 == 15 and round(85 * 1.38, 2) == 117.30
assert round(138 * .3, 2) == 41.40 and round(15 * 1.38, 2) == 20.70 and round(41.40 - 20.70, 2) == 20.70
assert 100 * 1.4 == 140 and round(140 * .25, 2) == 35.00 and round(15 * 1.4, 2) == 21.00 and round(35 - 21, 2) == 14.00
assert date(2026, 9, 30).year + 3 == 2029
has(t, "US$100.00", "C$138.00", "US$15.00", "US$85.00", "C$117.30", "C$41.40", "C$20.70", "US$30.00", "US$70.00",
    "C$140.00", "C$35.00", "C$21.00", "C$14.00", "December 31, 2029")

# Lesson 7
t = lesson(F, 7)
assert 10000 * .5 * .4 == 2000 and 10000 * .4 == 4000
assert 20000 * .5 * .35 == 3500 and 20000 * .35 == 7000
assert 6000 * .5 * .3 == 900 and 6000 * .3 == 1800
has(t, "C$5,000", "C$2,000", "C$4,000", "C$3,500", "C$7,000", "C$900", "C$1,800")

# Lesson 8
t = lesson(F, 8)
buys = [(100, 50.00, 1.36), (100, 60.00, 1.40), (50, 55.00, 1.30)]
costs = [round(n * p * r_, 2) for n, p, r_ in buys]
assert costs == [6800.00, 8400.00, 3575.00]
total = sum(costs)
sh = sum(n for n, _, _ in buys)
acb = total / sh
assert total == 18775.00 and sh == 250 and round(acb, 2) == 75.10
proceeds = 150 * 65 * 1.35
assert round(proceeds, 2) == 13162.50 and round(150 * acb, 2) == 11265.00
gain = proceeds - 150 * acb
assert round(gain, 2) == 1897.50 and round(gain / 2, 2) == 948.75 and round(100 * acb, 2) == 7510.00
usd_avg = (5000 + 6000 + 2750) / 250
assert usd_avg == 55.0 and 150 * (65 - 55) == 1500 and round(1500 * 1.35, 2) == 2025.00
c2 = 100 * 20 * 1.4 + 100 * 30 * 1.3
assert round(c2, 2) == 6700.00 and round(c2 / 200, 2) == 33.50
p2 = 80 * 35 * 1.35
assert round(p2, 2) == 3780.00 and round(80 * 33.5, 2) == 2680.00 and round(p2 - 2680, 2) == 1100.00
assert round(120 * 33.5, 2) == 4020.00
has(t, "6,800.00", "8,400.00", "3,575.00", "C$18,775.00", "C$75.10", "C$13,162.50", "C$11,265.00",
    "C$1,897.50", "C$948.75", "C$7,510.00", "US$1,500", "US$55.00", "C$2,025.00", "C$2,800.00", "C$3,900.00",
    "C$6,700.00", "C$33.50", "C$3,780.00", "C$2,680.00", "C$1,100.00", "C$4,020.00", "C$90,000")

# Lesson 9
t = lesson(F, 9)
sale = date(2026, 3, 10)
assert sale - timedelta(30) == date(2026, 2, 8) and sale + timedelta(30) == date(2026, 4, 9)
assert 7000 - 5500 == 1500 and 1500 / 2 == 750 and 5600 + 1500 == 7100 and 7100 - 6800 == 300 and 300 / 2 == 150
assert 750 * .4 == 300
s2 = date(2026, 6, 15)
assert s2 - timedelta(30) == date(2026, 5, 16) and s2 + timedelta(30) == date(2026, 7, 15)
assert 3000 / 2 - 1000 / 2 == 1000 and 4000 + 900 == 4900
assert date(2026, 11, 20) + timedelta(30) == date(2026, 12, 20)
assert 30 + 1 + 30 == 61
has(t, "C$1,500", "C$750", "February 8, 2026", "April 9, 2026", "C$7,100", "C$300", "C$150",
    "May 16, 2026 to July 15, 2026", "C$1,000", "C$4,900", "61 days")

# Lesson 10
t = lesson(F, 10)
L, V0, m = 40000, 60000, 0.30
vc = L / (1 - m)
assert round(vc, 2) == 57142.86 and round((1 - vc / V0) * 100, 2) == 4.76 and round((V0 - L) / V0 * 100, 1) == 33.3
assert round(vc - L, 2) == 17142.86 and round(V0 - L - (vc - L), 2) == 2857.14 and round(2857.14 / 20000 * 100, 1) == 14.3
v = V0 * .98 * .97
assert round(v, 2) == 57036.00 and round((1 - .98 * .97) * 100, 2) == 4.94 and round((v - L) / v * 100, 1) == 29.9
assert round(L * .05 * 30 / 365, 2) == 164.38
assert round(18000 / .7, 2) == 25714.29 and round((1 - 18000 / .7 / 30000) * 100, 2) == 14.29
assert round(10000 * .06 * 45 / 365, 2) == 73.97
assert 60000 * 1.05 - 40000 == 23000 and (23000 - 20000) / 20000 == .15
assert round(10000 * 1.35 * 1.015, 2) == 13702.50 and round(10000 * 1.35 * .985, 2) == 13297.50
assert round(13702.5 - 13297.5, 2) == 405.00
rx = 1.36 / 1.40 - 1
assert round(rx * 100, 2) == -2.86 and round((1.06 * (1 + rx) - 1) * 100, 2) == 2.97
assert 400 * .15 == 60 and 400 - 60 == 340
acb = (4000 + 5000) / 200
assert acb == 45 and 50 * 60 - 50 * acb == 750
assert 8000 * .5 * .3 == 1200 and 8000 * .3 == 2400
has(t, "33.3%", "C$57,142.86", "4.76%", "C$17,142.86", "C$2,857.14", "14.3%", "C$57,036.00", "4.94%", "29.9%",
    "C$164.38", "C$25,714.29", "14.29%", "C$73.97", "C$23,000", "15%", "C$13,702.50", "C$13,297.50", "C$405.00",
    "2.86%", "2.97%", "US$60.00", "US$340.00", "C$45.00", "C$750.00", "December 20, 2026", "C$1,200", "C$2,400")
