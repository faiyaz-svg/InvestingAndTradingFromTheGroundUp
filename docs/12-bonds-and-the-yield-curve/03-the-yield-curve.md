# The yield curve

<span class="tag tag-data">Data</span> <span class="tag tag-part">BOND</span>

After this lesson you can read a Treasury yield curve, compute the 10-year minus 2-year and 10-year minus 3-month spreads, say what an inversion has meant for recessions and where that signal fails, and check the Sahm rule on unemployment data.

Before this: [Bond prices and yields](01-bond-prices-and-yields.md), [Treasuries and TIPS](02-treasuries-and-tips.md). You need: a calculator.

## The idea

On November 20, 2026, the US Treasury's par yield was 4.32% for a 3-month bill, 4.63% for a 2-year note and 4.92% for a 10-year note ([US Treasury, daily par yield curve rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026)). Lending for longer paid more. On December 30, 2022 it was reversed: the 3-month yield was 4.42% and the 10-year yield 3.88%.

The **yield curve** is the line you get when you plot Treasury yields against time to maturity. Its slope reflects what the market expects from interest rates, inflation and growth. Three shapes matter.

A **normal** curve slopes upward: longer maturities yield more, because investors want extra for locking money up. A **flat** curve has about the same yield at every maturity. An **inverted** curve has short-term yields above long-term yields. That often follows a central bank raising rates to slow the economy, and it means the market expects short-term rates to fall.

![Three stylised yield curve shapes: normal rising from 3.4% to 4.9%, flat at 4.5%, and inverted falling from 5.4% to 4.2% at 10 years](../assets/figures/12-bonds-and-the-yield-curve/curve-shapes-dark.svg#only-dark)
![Three stylised yield curve shapes: normal rising from 3.4% to 4.9%, flat at 4.5%, and inverted falling from 5.4% to 4.2% at 10 years](../assets/figures/12-bonds-and-the-yield-curve/curve-shapes-light.svg#only-light)

The figure uses made-up numbers. The next one uses real par yields on four dates. The orange line (latest date) slopes up. The blue line (end of 2022) slopes down from the 6-month yield on.

![US Treasury par yield curves on four dates: December 29, 2000, December 31, 2019, December 30, 2022 and November 20, 2026](../assets/figures/12-bonds-and-the-yield-curve/par-curves-dark.svg#only-dark)
![US Treasury par yield curves on four dates: December 29, 2000, December 31, 2019, December 30, 2022 and November 20, 2026](../assets/figures/12-bonds-and-the-yield-curve/par-curves-light.svg#only-light)

Source: US Treasury, daily par yield curve rates, downloaded November 21, 2026 (US public domain). The December 29, 2000 and December 31, 2019 curves come from the same Treasury series for those years.

## How it works

### Two spreads

A **spread** is the difference between two yields. The two most used spreads subtract a short yield from the 10-year yield, in percentage points.

\[ S_{2s10s} = y_{10Y} - y_{2Y}, \qquad S_{3m10y} = y_{10Y} - y_{3M} \]

- \(y_{10Y}\), \(y_{2Y}\) and \(y_{3M}\) are the par yields (in %) at 10 years, 2 years and 3 months.
- A negative spread means the curve is inverted at that pair of maturities.

| Date | 3-month | 2-year | 10-year | 10Y minus 2Y | 10Y minus 3M |
|---|---|---|---|---|---|
| December 29, 2000 | 5.89 | 5.11 | 5.12 | 0.01 | -0.77 |
| December 31, 2019 | 1.55 | 1.58 | 1.92 | 0.34 | 0.37 |
| December 30, 2022 | 4.42 | 4.41 | 3.88 | -0.53 | -0.54 |
| November 20, 2026 | 4.32 | 4.63 | 4.92 | 0.29 | 0.60 |

The two spreads can disagree. On December 29, 2000 the 2-year spread was flat but the 3-month spread was inverted.

The next figure shows both spreads for every trading day from January 2021 to November 20, 2026. It covers the 2022 inversion only. The 2000 inversion in the table is not in this daily data.

![Daily 10-year minus 2-year and 10-year minus 3-month Treasury spreads from 2021 to 2026, both negative through 2023 and 2024](../assets/figures/12-bonds-and-the-yield-curve/spread-history-dark.svg#only-dark)
![Daily 10-year minus 2-year and 10-year minus 3-month Treasury spreads from 2021 to 2026, both negative through 2023 and 2024](../assets/figures/12-bonds-and-the-yield-curve/spread-history-light.svg#only-light)

Source: US Treasury, daily par yield curve rates, downloaded November 21, 2026 (US public domain).

From that data: the 10-year minus 2-year spread closed negative every trading day from July 6, 2022 to August 26, 2024 (537 trading days), with a low of -1.08. The 10-year minus 3-month spread did the same from October 25, 2022 to December 12, 2024 (534 trading days), with a low of -1.89. Both were back above zero by the end of 2024. The 3-month spread was below zero again on 86 trading days in 2025.

### Inversion as a recession signal

Why would the curve predict a recession? A central bank that tightens raises short rates, which flattens or inverts the curve, and tight policy slows the economy. Investors who expect a slowdown expect rate cuts, which pulls long yields down (see [Estrella and Trubin, 2006](https://www.newyorkfed.org/medialibrary/media/research/current_issues/ci12-5.pdf)).

The research behind the signal starts with Estrella and Mishkin (1998), "Predicting U.S. recessions: Financial variables as leading indicators", *Review of Economics and Statistics* 80(1), 45-61. They found that the yield curve slope predicts recessions better than other financial variables beyond a one-quarter horizon. Estrella and Trubin turn this into a model: a probit equation converts the 10-year minus 3-month spread into a probability of recession 12 months later:

\[ \Pr(\text{recession in month } t+12) = \Phi\left(\alpha + \beta \times S_t\right), \qquad \alpha = -0.6045,\ \beta = -0.7374 \]

- \(S_t\) is the 10-year minus 3-month spread in month \(t\), in percentage points.
- \(\Phi\) is the cumulative normal distribution function.
- \(\alpha\) and \(\beta\) were estimated on US data from January 1959 to December 2005.

<div class="example" markdown>

### Worked example: from spread to probability

Use the Estrella and Trubin constants.

1. Spread 0.00: \(\Phi(-0.6045)\) = 27.3%.
2. Spread -1.00: \(\Phi(-0.6045 + 0.7374)\) = \(\Phi(0.1329)\) = 55.3%.
3. Spread +2.00: \(\Phi(-0.6045 - 1.4748)\) = \(\Phi(-2.0793)\) = 1.9%.

Even a spread of zero maps to only a 27% chance.

</div>

The paper reports that all six NBER recessions since 1968 were preceded by at least three negative monthly average spreads in the 12 months before the recession, with no false signals on a monthly average basis. Its limits matter as much:

- It is a probability 12 months out, with no date and no size.
- The paper says daily or intraday inversions often prove false, and monthly averages are more reliable.
- The lowest monthly average spread before each recession ranged from -3.51 to -0.08.
- The sample is six recessions. The paper's data end in 2005, so it says nothing about 2022 to 2024.

Use the curve as one input among others. Check what followed the 2022 to 2024 inversion against the [NBER recession dates](https://www.nber.org/research/data/us-business-cycle-expansions-and-contractions).

### The Sahm rule

The **Sahm rule** is a different signal, built from unemployment. Claudia Sahm proposed it ([Sahm, 2019](https://www.hamiltonproject.org/publication/policy-proposal/direct-stimulus-payments-to-individuals/), Hamilton Project, where it was built as a payment trigger rather than a forecast), and FRED publishes it as [SAHMREALTIME](https://fred.stlouisfed.org/series/SAHMREALTIME). It signals the start of a recession when the three-month average of the unemployment rate rises 0.50 percentage points or more above the lowest three-month average of the previous 12 months.

\[ \text{Sahm gap}_t = \bar{u}_t - \min\left(\bar{u}_{t-12}, \dots, \bar{u}_{t-1}\right) \]

- \(\bar{u}_t\) is the average unemployment rate (%) over months \(t-2\), \(t-1\) and \(t\).
- The minimum runs over the three-month averages of the previous 12 months.

<div class="example" markdown>

### Worked example: a made-up unemployment series

Monthly rates (%): 3.9, 3.8, 3.7, 3.7, 3.6, 3.6, 3.7, 3.7, 3.8, 3.9, 4.0, 4.2, 4.3, 4.4, 4.5 (months 1 to 15).

1. The lowest three-month average is 3.63, in months 6 and 7 (for example, months 4 to 6: (3.7 + 3.6 + 3.6) / 3).
2. In month 12 the average is (3.9 + 4.0 + 4.2) / 3 = 4.03, a gap of 0.40. No signal.
3. In month 13 the average is (4.0 + 4.2 + 4.3) / 3 = 4.17, a gap of 0.53. The rule signals.

</div>

The rule reacts after unemployment has already risen, so it says a recession has probably begun. It is not a forecast. FRED's real-time series (SAHMREALTIME) showed 0.00 percentage points for October 2026 as of November 2026, well below the threshold.

## In code

Spreads, the probit probability, and a download of one year of Treasury data.

<details class="code" markdown>
<summary>In code</summary>

```python
from math import erf, sqrt

def phi(z):
    return 0.5 * (1 + erf(z / sqrt(2)))

y3m, y2y, y10y = 4.32, 4.63, 4.92
print(round(y10y - y2y, 2), round(y10y - y3m, 2))    # 0.29 0.6
for s in (0.0, -1.0, 2.0):
    print(s, round(100 * phi(-0.6045 - 0.7374 * s), 1))   # 27.3, 55.3, 1.9
```

```python
# needs internet
import pandas as pd

url = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/"
       "daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve"
       "&field_tdr_date_value=2026&page&_format=csv")
d = pd.read_csv(url, parse_dates=["Date"]).set_index("Date").sort_index()
d["s2s10s"] = d["10 Yr"] - d["2 Yr"]
d["s3m10y"] = d["10 Yr"] - d["3 Mo"]
print(d[["s2s10s", "s3m10y"]].tail())
print((d["s3m10y"] < 0).sum(), "days inverted this year")
```

</details>

## Common mistakes

- Calling a one-day dip below zero a signal. Use monthly averages.
- Treating the spread as a timer. It gives odds, not a date.
- Mixing spreads. The 2s10s and the 3m10y invert at different times, so say which one you mean.

## Try it

1\. On December 31, 2019, the 3-month yield was 1.55%, the 2-year 1.58% and the 10-year 1.92%. Compute both spreads. Is the curve inverted?

<details class="solution" markdown>
<summary>Answer</summary>

10Y minus 2Y = 1.92 - 1.58 = 0.34. 10Y minus 3M = 1.92 - 1.55 = 0.37. Both are positive, so it is not inverted.

</details>

2\. Using the Estrella and Trubin constants, what recession probability does a spread of -0.54 (December 30, 2022, 10-year minus 3-month) imply?

<details class="solution" markdown>
<summary>Answer</summary>

\(\Phi(-0.6045 + 0.7374 \times 0.54)\) = \(\Phi(-0.2063)\) = 41.8%. These are odds from 1959 to 2005 data, not a prediction.

</details>

3\. A monthly unemployment series has a lowest three-month average of 3.40% over the previous year, and the latest three months are 3.8, 3.9 and 4.0. Does the Sahm rule signal?

<details class="solution" markdown>
<summary>Answer</summary>

Latest average = (3.8 + 3.9 + 4.0) / 3 = 3.90. Gap = 3.90 - 3.40 = 0.50. The gap is 0.50 or more, so yes, it signals (exactly at the threshold).

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | On the Treasury's rates page, read the latest curve. Compute both spreads and say whether each is inverted. |
| 3 | For each NBER recession since 2000, check whether FRED series T10Y3M was negative in the year before it began. |
| 3 | Write two sentences in your [trade journal](../practice/trade-journal.md) on what the curve says about rate expectations today. |

</div>

## Key terms

- **Yield curve**: Treasury yields plotted against time to maturity.
- **Normal curve**: a curve where longer maturities yield more.
- **Flat curve**: a curve where yields are about equal at all maturities.
- **Inverted curve**: a curve where short-term yields are above long-term yields.
- **Spread**: the difference between two yields, in percentage points.
- **Par yield**: the coupon rate at which a new Treasury of that maturity would sell at face value.
- **Probit model**: a model that turns a number, such as a spread, into a probability with the normal distribution.
- **Sahm rule**: a recession signal that triggers when the three-month unemployment average is 0.50 points above its 12-month low.

Next: [Duration and convexity](04-duration-and-convexity.md)
