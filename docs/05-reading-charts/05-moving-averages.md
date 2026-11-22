# Moving averages

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">CHRT</span>

After this lesson you can compute a simple and an exponential moving average by hand, read a crossover rule off a chart, and say what tests found about moving-average trading rules.

Before this: [Trend and market structure](02-trend-and-market-structure.md), and the [mean](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/08-statistics/01-descriptive-statistics-and-study-design/) in the math book. You need: a calculator.

## The idea

A daily price chart is jagged. A smoother line shows which way the price is heading. The simplest smoother is the average of the last 20 closes, recomputed every day as the window moves forward. That is a **moving average** (MA).

Stock A closes at 61.10 on one day and 60.71 on the next. Is it falling? One day cannot say. The average of the last 20 closes moves slowly, and when it turns, the trend of the last month has turned. The cost is **lag**: the average reports a trend after it has started.

## How it works

Two averages are in common use.

The **simple moving average** (SMA) of length \(N\) is the plain average of the last \(N\) closes:

\[ \text{SMA}_t = \frac{1}{N} \sum_{i=0}^{N-1} C_{t-i} \]

- \(C_{t-i}\) is the close \(i\) bars before bar \(t\), in US$.
- \(N\) is the window length in bars (20 for about a month, 50 for about 2.5 months, 200 for about 10 months of daily bars).

The **exponential moving average** (EMA) weights recent closes more. It updates from yesterday's value:

\[ \text{EMA}_t = k\,C_t + (1 - k)\,\text{EMA}_{t-1}, \qquad k = \frac{2}{N + 1} \]

- \(k\) is the weight on today's close (no unit). For \(N = 20\), \(k = 2/21 = 0.0952\).
- \(\text{EMA}_{t-1}\) is yesterday's EMA. The first EMA is set to the SMA of the first \(N\) closes, which is the convention the charts in this book use.

Every old close still counts in an EMA, with a weight that shrinks by \(1 - k\) each day, so the EMA follows turns sooner than an SMA of the same \(N\).

<div class="example" markdown>

### Worked example: SMA 5 and EMA 5 by hand

The first seven closes of a made-up stock are 61.87, 61.84, 61.07, 60.91, 61.10, 60.71 and 60.96. Take \(N = 5\), so \(k = 2/6 = 1/3\).

1. SMA at bar 5 = (61.87 + 61.84 + 61.07 + 60.91 + 61.10) / 5 = 306.79 / 5 = 61.36 (rounded). This is also the first EMA.
2. SMA at bar 6 = (61.84 + 61.07 + 60.91 + 61.10 + 60.71) / 5 = 305.63 / 5 = 61.13.
3. EMA at bar 6 = (1/3) x 60.71 + (2/3) x 61.358 = 20.237 + 40.905 = 61.14.

The new close of 60.71 is below the average, so both averages fall. The two are close here (61.13 and 61.14) and differ more in a fast move.

</div>

The next chart shows a sharp turn in Stock A. The price peaks with a close of 62.00 on March 6. Look at when each average stops rising.

```chart
data: 05-reading-charts/sma-vs-ema.json
title: Stock A, daily: SMA 20 and EMA 20 after a peak
show: sma 20, ema 20
marker: 2026-03-13 | below | EMA stops rising
marker: 2026-03-18 | below | SMA stops rising
range: 2026-02-02 to 2026-04-14
caption: The EMA 20 peaks at 59.24 on March 13, the SMA 20 at 59.65 on March 18.
```

The EMA 20 peaked five trading days after the price did, and the SMA 20 eight days after. In a trend the lag is about the same, and the EMA is closer to the price.

### Using averages

Traders use an average as a trend filter ("only look for longs while the close is above the 50-day SMA") or as a crossover, a short average crossing a long one. A **golden cross** is the 50-day SMA crossing above the 200-day, and a **death cross** is the reverse. The chart below uses 20 and 50 days, which fit a shorter chart.

```chart
data: 05-reading-charts/ma-cross.json
title: Stock A, daily: SMA 20 and SMA 50 crossovers
show: sma 20, sma 50
marker: 2025-12-04 | below | 20 crosses above 50
marker: 2026-04-01 | above | 20 crosses below 50
caption: Two crossovers in 185 bars: a buy signal at 52.89 and a sell signal at 62.81.
```

The 20-day SMA crosses above the 50-day on December 4, 2025, with a close of 52.89 (SMA 20 is 53.77 and SMA 50 is 53.70). The price then rises to a close of 70.00 on February 20, 2026. The 20 crosses back below the 50 on April 1 at a close of 62.81 (66.40 and 66.43).

<div class="example" markdown>

### Worked example: trading the crossover

Rule: buy at the close when the 20-day SMA crosses above the 50-day, sell at the close when it crosses below.

1. Buy at 52.89 on December 4, 2025.
2. Sell at 62.81 on April 1, 2026.
3. Gain per share = 62.81 - 52.89 = US$9.92, which is 9.92 / 52.89 = 18.8%.

The rule gave back 7.19 from the peak close of 70.00 to the exit at 62.81 (about 10%), because the signal comes late. Holding to the last close in the chart (55.00 on May 15) would have gained only 2.11.

</div>

The same chart shows the weak case. From October 20 to December 12 the price moved sideways in a range, and its close crossed the 20-day SMA 10 times. A price-crosses-average rule would have traded ten times for small gains and losses. This is a **whipsaw**: a signal that reverses soon after it appears. An average works in a trend and loses in a range.

## What tests found

Brock, Lakonishok and LeBaron (1992) tested moving-average rules and a trading-range breakout rule on the Dow Jones Industrial Average from 1897 to 1986. Buy signals were followed by higher returns than sell signals, returns after sell signals were negative, and four standard models of stock returns (a random walk, an AR(1) model and two GARCH models) did not reproduce the pattern ([Journal of Finance, 47(5), 1731-1764](https://doi.org/10.1111/j.1540-6261.1992.tb04681.x)).

Sullivan, Timmermann and White (1999) re-tested those rules on 100 years of daily Dow data with a much larger universe of rules, adjusting for data snooping: the bias that appears when many rules are tried on the same data and the best one is reported ([Journal of Finance, 54(5), 1647-1691](https://doi.org/10.1111/0022-1082.00163)). They found that the best rule still beat the benchmark over the period Brock and colleagues studied, but not in the following ten years of data. A rule's result counts only if the test accounts for every rule tried. See [multiple testing and p-hacking](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/08-statistics/07-multiple-testing-and-p-hacking/) in the math book.

Park and Irwin (2007) reviewed 95 modern studies: 56 found positive results for technical trading strategies, 20 negative and 19 mixed. They report profits at least until the early 1990s, and note that many studies have weaknesses such as data snooping and the treatment of risk and transaction costs ([Journal of Economic Surveys, 21(4), 786-826](https://doi.org/10.1111/j.1467-6419.2007.00519.x)).

Neely, Rapach, Tu and Zhou (2014) found that technical indicators, including moving-average rules, forecast the monthly US equity risk premium out of sample about as well as macroeconomic variables ([Management Science, 60(7), 1772-1791](https://doi.org/10.1287/mnsc.2013.1838)).

In short, the evidence for profit after costs is mixed, and older gains have not been shown to last. Treat an average as a way to define trend and risk, not as a signal that pays on its own.

## In code

The same SMA and EMA on all 125 bars of Stock A, with the EMA seeded from the first 20 closes as the charts do. Use [stock-a-daily-h1.csv](../assets/data/stock-a-daily-h1.csv).

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

bars = pd.read_csv("stock-a-daily-h1.csv", parse_dates=["date"], index_col="date")
close = bars["close"]
sma20 = close.rolling(20).mean()

k = 2 / (20 + 1)
ema20 = close * float("nan")
ema20.iloc[19] = close.iloc[:20].mean()
for i in range(20, len(close)):
    ema20.iloc[i] = close.iloc[i] * k + ema20.iloc[i - 1] * (1 - k)

print(close.index[-1].date(), close.iloc[-1], round(sma20.iloc[-1], 2), round(ema20.iloc[-1], 2))
```

The last bar (2026-06-26) closes at 58.5, with an SMA 20 of 55.46 and an EMA 20 of 55.69.

</details>

## Common mistakes

- Forgetting the lag. An average always signals late, so decide how much of a move you accept giving back before you choose a length.
- Trading crossovers in a range. The signal flips back and forth, and each flip costs spread and slippage ([Bid, ask and the order book](../01-how-markets-work/04-bid-ask-and-the-order-book.md)).
- Picking the length that fit the past best. That is the data-snooping problem above.

## Try it

1\. Closes of 10, 12, 11, 13 and 14. What is the SMA 5? What is the SMA 3 at the last bar?

<details class="solution" markdown>
<summary>Answer</summary>

SMA 5 = (10 + 12 + 11 + 13 + 14) / 5 = 60 / 5 = 12.0. SMA 3 at the last bar = (11 + 13 + 14) / 3 = 38 / 3 = 12.67.

</details>

2\. For \(N = 9\), what is \(k\)? If yesterday's EMA is 20.00 and today's close is 21.00, what is today's EMA?

<details class="solution" markdown>
<summary>Answer</summary>

\(k = 2 / (9 + 1) = 0.2\). EMA = 0.2 x 21.00 + 0.8 x 20.00 = 4.20 + 16.00 = 20.20.

</details>

3\. After a sharp one-day drop, which average falls more, the SMA 20 or the EMA 20?

<details class="solution" markdown>
<summary>Answer</summary>

The EMA. The new close has weight \(k = 2/21 = 0.095\) in the EMA and weight 1/20 = 0.05 in the SMA.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Run a set of [chart drills](../practice/chart-drills.md) that show a moving-average crossover and say what each cross means. |
| 4 | On a daily chart you follow, add the 20-day and 50-day averages. Write the last crossover date and whether the price is above both. |
| 2 | Note one range period on that chart and count how many times the price crossed the 20-day average. |

</div>

## Key terms

- **Moving average (MA)**: the average of the last N closes, recomputed each bar.
- **Lag**: the delay between a turn in price and the turn in an average of it.
- **Simple moving average (SMA)**: the plain average of the last N closes.
- **Exponential moving average (EMA)**: an average that weights recent closes more, updated with a factor k = 2/(N + 1).
- **Golden cross**: the 50-day SMA crossing above the 200-day SMA.
- **Death cross**: the 50-day SMA crossing below the 200-day SMA.
- **Whipsaw**: a signal that reverses soon after it appears.
- **Data snooping**: the bias from trying many rules on the same data and reporting the best.

Next: [Momentum indicators: RSI, MACD and stochastics](06-momentum-indicators.md)
