# Indicators in pandas

<span class="tag tag-code">Code</span> <span class="tag tag-part">QUANT</span>

After this lesson you can compute SMA, EMA, RSI and ATR in pandas so that they match the book's charts bar for bar, and say exactly where the common ways of writing them differ.

Before this: [Moving averages](../05-reading-charts/05-moving-averages.md), [Momentum indicators: RSI, MACD and stochastics](../05-reading-charts/06-momentum-indicators.md), [Volatility indicators](../05-reading-charts/07-volatility-indicators.md), [Python and pandas for prices](01-python-and-pandas-for-prices.md). You need: Python with pandas.

## The idea

Two tools can draw "a 20-day EMA" and show different numbers. Neither is wrong. Each starts the calculation in a different place, and a recursive average never fully forgets its start. When you test a rule, you want the numbers your chart shows, so you need to know which convention is which.

The book's charts are drawn by `docs/javascripts/charts.js`. This lesson writes the same four indicators in pandas, and the checks for this part run the JavaScript and the pandas code on the same bars and compare the results.

## How it works

The SMA is a rolling mean, as in lesson 5 of part 5:

\[ \text{SMA}_t = \frac{1}{N}\sum_{i=0}^{N-1} C_{t-i} \]

In pandas it is `close.rolling(N).mean()`. The first \(N-1\) bars are empty (NaN) because the window is not full.

The EMA is \(\text{EMA}_t = k\,C_t + (1-k)\,\text{EMA}_{t-1}\) with \(k = 2/(N+1)\). It needs a first value, and two choices are common:

- **Seeded with the SMA** (the charting convention, and what charts.js does): the first EMA, at bar \(N\), is the SMA of the first \(N\) closes. Bars before that are empty.
- **Seeded with the first close** (what pandas does with `ewm(span=N, adjust=False)`): the first EMA is the first close, and every bar has a value.

The word `adjust=False` matters. With the default `adjust=True`, pandas divides by a sum of weights and the result is a different, weighted average that does not follow the recursion above.

<div class="example" markdown>

### Worked example: the two seeds on five closes

Closes: 10, 11, 12, 11, 13. Take \(N = 3\), so \(k = 2/4 = 0.5\).

1. SMA seed: the SMA of the first three closes is (10 + 11 + 12) / 3 = 11.00. The EMA at bar 3 is 11.00.
2. Bar 4: 0.5 x 11 + 0.5 x 11.00 = 11.00. Bar 5: 0.5 x 13 + 0.5 x 11.00 = 12.00.
3. First-close seed: bar 1 is 10.00, bar 2 is 0.5 x 11 + 0.5 x 10 = 10.50, bar 3 is 0.5 x 12 + 0.5 x 10.50 = 11.25, bar 4 is 0.5 x 11 + 0.5 x 11.25 = 11.125, bar 5 is 0.5 x 13 + 0.5 x 11.125 = 12.0625.

At bar 5 the two EMAs are 12.00 and 12.06. The gap was 0.25 at bar 3 and halves each bar, because each bar multiplies the old gap by \(1 - k = 0.5\).

</div>

The same thing happens on price data. Use [stock-a-daily-h1.csv](../assets/data/stock-a-daily-h1.csv) (made up), the data behind lesson 5's chart in part 5.

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

bars = pd.read_csv("stock-a-daily-h1.csv", parse_dates=["date"], index_col="date")
close = bars["close"]
n = 20

sma = close.rolling(n).mean()

seed = close.copy()
seed.iloc[: n - 1] = float("nan")
seed.iloc[n - 1] = close.iloc[:n].mean()            # start from the SMA of the first n closes
ema_seeded = seed.ewm(alpha=2 / (n + 1), adjust=False).mean()
ema_first = close.ewm(span=n, adjust=False).mean()  # start from the first close

out = pd.DataFrame({"close": close, "sma": sma, "ema_seeded": ema_seeded, "ema_first": ema_first})
print(out.iloc[[19, 29, 59, 124]].round(2))
print((ema_seeded - ema_first).abs().iloc[[19, 59, 124]].round(4).tolist())
```

On bar 20 (January 30, 2026) the close is 43.60, the SMA 20 is 41.53, the seeded EMA is 41.53 and the first-close EMA is 41.84. The first-close EMA is 0.3086 higher. By bar 60 (March 27) they are 47.92 and 47.92, with a gap of 0.0056, and by the last bar (June 26) both are 55.69. Lesson 5 of part 5 quotes the same last-bar values: an SMA 20 of 55.46 and an EMA 20 of 55.69.

</details>

The trick in the snippet is to blank out the first \(N-1\) values and put the SMA at bar \(N\); `ewm(adjust=False)` then starts the recursion from the first value it sees.

### RSI and ATR

RSI and ATR use **Wilder smoothing**, the average that J. Welles Wilder defined in 1978: \(\bar{x}_t = (\bar{x}_{t-1}(N-1) + x_t)/N\). It is an EMA with \(k = 1/N\) instead of \(2/(N+1)\), so it is slower. The first value is the plain average of the first \(N\) inputs, as in the EMA seeded with the SMA.

RSI uses the average gain and the average loss of the closes:

\[ \text{RSI} = 100 - \frac{100}{1 + \bar{G}/\bar{L}} \]

- \(\bar{G}\) is the Wilder average of the up-moves (a close-to-close gain, or 0 on a down day) and \(\bar{L}\) the same for the down-moves, both in US$ per bar.
- RSI runs from 0 to 100, and charts.js gives 100 when the average loss is 0.

ATR is the Wilder average of the true range, which is the larger of the high minus the low, the high minus the previous close, and the previous close minus the low. The first true range has no previous close, so it is the high minus the low.

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

bars = pd.read_csv("stock-a-daily-h1.csv", parse_dates=["date"], index_col="date")
close = bars["close"]

def wilder(x, n, start):
    s = x.copy()
    first = start + n - 1
    s.iloc[:first] = float("nan")
    s.iloc[first] = x.iloc[start:first + 1].mean()
    return s.ewm(alpha=1 / n, adjust=False).mean()

change = close.diff()
gain = change.clip(lower=0).fillna(0)
loss = (-change).clip(lower=0).fillna(0)
rsi = 100 - 100 / (1 + wilder(gain, 14, 1) / wilder(loss, 14, 1))

prev = close.shift()
tr = pd.concat([bars["high"] - bars["low"], (bars["high"] - prev).abs(), (bars["low"] - prev).abs()], axis=1).max(axis=1)
atr = wilder(tr, 14, 0)
print(rsi.iloc[[14, 15, 124]].round(2).tolist(), atr.iloc[[13, 124]].round(3).tolist())
```

RSI 14 first appears at bar 15 (index 14) with 75.12, then 80.13, and on the last bar it is 76.68. ATR 14 first appears at bar 14 with 0.581 and ends at 0.969. The RSI starts one bar later than the ATR because the first close has no change from a previous close, so the gains start at bar 2.

</details>

The chart below is drawn by charts.js from the same data. Compare its last values with the snippet: EMA 20 at 55.69, RSI 14 at 76.68 and ATR 14 at 0.97.

```chart
data: 05-reading-charts/stock-a-daily.json
title: Stock A, daily: EMA 20, RSI 14 and ATR 14
show: ema 20, rsi 14, atr 14
caption: At the last bar the EMA 20 is 55.69, the RSI 14 is 76.68 and the ATR 14 is 0.97.
```

Many libraries compute RSI with a plain `ewm(alpha=1/14, adjust=False)`, which starts from the first gain instead of the average of the first 14. That gives 75.49, 82.62 and 76.68 on the same three bars: different in the early bars, the same later. If you compare your numbers with a platform's, check the first 50 bars before you decide that one is wrong.

## What tests found

An indicator is only a formula; whether a rule built on it pays is a separate question. Part 5 gives the evidence for each: [Moving averages](../05-reading-charts/05-moving-averages.md) for crossover rules (Brock, Lakonishok and LeBaron, 1992, and the data-snooping re-test by Sullivan, Timmermann and White, 1999), and [Momentum indicators](../05-reading-charts/06-momentum-indicators.md) for RSI. The next lessons show why the data-snooping warning matters.

## Common mistakes

- Using `ewm(span=N)` without `adjust=False`. The default is a different average.
- Comparing the first 50 bars of two tools. The seed has not worn off yet, so small differences are expected there.
- Computing RSI from the raw close across a split. Use a split-adjusted series ([Python and pandas for prices](01-python-and-pandas-for-prices.md)).

## Try it

1\. Closes 10, 11, 12, 11, 13 with \(N = 3\). What is the SMA 3 at bar 5, and the EMA 3 at bar 5 when seeded with the SMA?

<details class="solution" markdown>
<summary>Answer</summary>

SMA 3 at bar 5 = (12 + 11 + 13) / 3 = 12.00. The SMA-seeded EMA at bar 5 is 12.00, from the worked example.

</details>

2\. For the same closes, what is the first-close EMA 3 at bar 5, and how far is it from the seeded one?

<details class="solution" markdown>
<summary>Answer</summary>

12.0625, which is 0.0625 above 12.00. The gap was 0.25 at bar 3 and is multiplied by 0.5 each bar: 0.25, 0.125, 0.0625.

</details>

3\. Wilder smoothing with \(N = 14\). The average gain is 0.50 and today's gain is 1.20. What is the new average gain?

<details class="solution" markdown>
<summary>Answer</summary>

(0.50 x 13 + 1.20) / 14 = (6.50 + 1.20) / 14 = 7.70 / 14 = 0.55.

</details>

4\. An average gain of 0.55 and an average loss of 0.25. What is the RSI?

<details class="solution" markdown>
<summary>Answer</summary>

0.55 / 0.25 = 2.2. RSI = 100 - 100 / (1 + 2.2) = 100 - 31.25 = 68.75.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Run the first snippet, then print the SMA 50 and the EMA 50 for the last bar and compare them with the same values on the chart (use the [chart drills](../practice/chart-drills.md) page to open a chart if you want another one). |
| 5 | Change `adjust=False` to `adjust=True` in the first-close EMA and write down how the last bar and the first bar change. |

</div>

## Key terms

- **Seed**: the starting value of a recursive average.
- **Wilder smoothing**: an EMA with \(k = 1/N\), seeded with the plain average of the first N inputs; used by RSI and ATR.
- **NaN**: the empty value pandas uses for a bar where an indicator cannot yet be computed.
- **Warm-up**: the first bars of an indicator, where the seed still has a visible effect.

Next: [Fundamentals from EDGAR](04-fundamentals-from-edgar.md)
