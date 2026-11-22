# VWAP and anchored VWAP

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">CHRT</span>

After this lesson you can compute VWAP by hand, tell a trend day from a chop day by where the price sits against it, and anchor a VWAP to a swing low.

Before this: [Volume and relative volume](04-volume-and-relative-volume.md) and [Moving averages](05-moving-averages.md). You need: a calculator.

## The idea

By 10 a.m. on a trading day, thousands of trades in Stock A have happened at different prices, in different sizes. What was the average price paid? A plain average of the bar prices treats a 5-minute bar with 50,000 shares the same as one with 500,000. The better answer weights each price by the shares that traded at it.

The **volume-weighted average price** (VWAP) is that average, from the open of the session to the current bar. Traders read it as the day's fair price: buyers above it paid more than the average buyer today, and buyers below it paid less. Institutions use it as a benchmark to judge how well they filled a large order, which is why many orders aim for it.

## How it works

For each bar, take the **typical price**, the average of its high, low and close. Weight it by the bar's volume and keep running totals from the open:

\[ \text{VWAP}_t = \frac{\sum_{i=1}^{t} TP_i \times V_i}{\sum_{i=1}^{t} V_i}, \qquad TP_i = \frac{H_i + L_i + C_i}{3} \]

- \(TP_i\) is the typical price of bar \(i\) in US$, and \(V_i\) is its volume in shares.
- Both sums start at the first bar of the session, so VWAP resets every morning.

<div class="example" markdown>

### Worked example: VWAP on the first three 5-minute bars

Stock A on March 2, 2026 (9:30, 9:35 and 9:40 a.m. ET):

| Bar | High | Low | Close | Typical price | Volume | Price x volume |
|---|---|---|---|---|---|---|
| 9:30 | 80.06 | 79.98 | 80.02 | 80.02 | 130,000 | 10,402,600 |
| 9:35 | 80.08 | 79.94 | 79.99 | 80.0033 | 80,200 | 6,416,267 |
| 9:40 | 80.11 | 79.96 | 80.05 | 80.04 | 93,500 | 7,483,740 |

1. After bar 1: 10,402,600 / 130,000 = 80.02.
2. After bar 2: (10,402,600 + 6,416,267) / (130,000 + 80,200) = 16,818,867 / 210,200 = 80.01.
3. After bar 3: 24,302,607 / 303,700 = 80.02.

The first bar had the most volume, so it pulls the VWAP toward its own price.

</div>

### Trend day and chop day

The price's position against VWAP says what kind of day it is. On a trend day the buyers keep paying more, and the price stays above VWAP with pullbacks that stop near it. On a chop day the price moves across VWAP again and again.

Look at the price staying above the VWAP line on the first chart.

```chart
data: 05-reading-charts/vwap-trend-day.json
title: Stock A, 5-minute: a trend day above VWAP
show: vwap
marker: 2026-03-02 12:00 | below | Pullback holds above VWAP
caption: The close is above VWAP on 76 of 78 bars, and the day ends at 82.40 against a VWAP of 81.24.
```

On March 2 the close is above VWAP on 76 of the 78 five-minute bars. The pullback at noon (12:00 p.m. ET) has a low 0.09 above VWAP, and the day closes at 82.40, with a VWAP of 81.24. The line works as a support level for the day.

The next day the price moves back and forth.

```chart
data: 05-reading-charts/vwap-chop-day.json
title: Stock A, 5-minute: a chop day around VWAP
show: vwap
caption: The close is above VWAP on 45 of 78 bars and crosses it 23 times, in a range of 79.64 to 80.42.
```

On March 3 the close is above VWAP on 45 of 78 bars and crosses it 23 times. Rules that buy "above VWAP" and sell "below" would trade 23 times here for small gains and losses, the same whipsaw as a moving-average cross in a range ([Moving averages](05-moving-averages.md)).

Two cautions. VWAP at 9:35 a.m. rests on a few bars, so it jumps around early and settles later. And VWAP is a running average of the day, so it lags more as the day goes on.

### Anchored VWAP

An **anchored VWAP** (AVWAP) starts the running sums at a bar you choose, such as a swing low, a gap or an earnings day, and continues for days or weeks. It shows the average price paid by everyone who bought since the anchor. If the price is above it, the average buyer since then is ahead.

In the chart, the anchor is the swing low of February 6, 2026 (a low of 45.68). Look at the first pullback.

```chart
data: 05-reading-charts/avwap-anchor.json
title: Stock A, daily: VWAP anchored to the February 6 low
show: avwap 2026-02-06
marker: 2026-03-10 | below | Dips under AVWAP
marker: 2026-03-13 | below | Back above
caption: The AVWAP rises slowly from 46.03, and the first pullback dips under it for two closes.
```

The AVWAP is 49.72 on March 10, when the close is 49.00 and the low 48.89. By March 12 the close is 49.73 against an AVWAP of 49.69, and on March 13 it is 50.80 against 49.73. The anchor gave a level that traders watching the same low might also watch. Later pullbacks stayed above it (the closest was a low of 52.51 against an AVWAP of 51.44 on April 9), which says the average buyer since the low stayed in profit.

## What tests found

VWAP is established as an execution benchmark: Berkowitz, Logue and Noser (1988) proposed measuring the cost of NYSE trades against the day's VWAP ([Journal of Finance, 43(1), 97-112](https://doi.org/10.1111/j.1540-6261.1988.tb02591.x)). That is about judging fills, not about predicting prices.

As a trading signal, this book knows of no peer-reviewed test of buying above VWAP or selling below it. A 2023 working paper by Zarattini and Aziz, not peer reviewed, reported results from trading the QQQ fund long above VWAP and short below it from January 2018 to September 2023 ([Concretum Group](https://concretumgroup.com/volume-weighted-average-price-vwap-the-holy-grail-for-day-trading-systems/)). It is one fund in one five-year period. Treat the evidence as thin. Intraday trading rules are also expensive: every cross costs the spread (lesson 4 of Part 1: [Bid, ask and the order book](../01-how-markets-work/04-bid-ask-and-the-order-book.md)).

## In code

VWAP for the trend day, from [stock-a-5m-trend-day.csv](../assets/data/stock-a-5m-trend-day.csv).

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

b = pd.read_csv("stock-a-5m-trend-day.csv", parse_dates=["datetime"], index_col="datetime")
tp = (b["high"] + b["low"] + b["close"]) / 3
vwap = (tp * b["volume"]).cumsum() / b["volume"].cumsum()
print(round(vwap.iloc[2], 2), round(vwap.iloc[-1], 2), int((b["close"] > vwap).sum()), len(b))
```

It prints 80.02 81.24 76 78: the VWAP after bar 3, the VWAP at the close, and the number of bars closing above VWAP out of 78.

</details>

## Common mistakes

- Using VWAP on a daily chart. A daily bar has one price, so the line means nothing. Use the intraday VWAP, or an anchored one.
- Treating the VWAP as a prediction. It is the average of what has already traded.
- Forgetting the early bars. In the first minutes the VWAP is the first few prints.

## Try it

1\. Two bars: typical price 50.00 with 1,000 shares, typical price 50.40 with 3,000 shares. What is VWAP, and what is the plain average of the two prices?

<details class="solution" markdown>
<summary>Answer</summary>

VWAP = (50.00 x 1,000 + 50.40 x 3,000) / 4,000 = 201,200 / 4,000 = 50.30. The plain average is 50.20. The heavier bar pulls VWAP toward 50.40.

</details>

2\. A bar has high 20.50, low 19.90 and close 20.30. What is its typical price?

<details class="solution" markdown>
<summary>Answer</summary>

(20.50 + 19.90 + 20.30) / 3 = 60.70 / 3 = 20.23.

</details>

3\. Stock B trades at 30.10 and its VWAP is 29.85 at 11 a.m. You bought 100 shares at 29.90 at the open. Did you pay more or less than the average buyer so far today, and what is your open profit?

<details class="solution" markdown>
<summary>Answer</summary>

You paid 29.90, which is 0.05 more than the VWAP of 29.85, so you paid more than the average buyer so far. Your open profit is (30.10 - 29.90) x 100 = US$20.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 3 | Run a set of [chart drills](../practice/chart-drills.md) with intraday charts. Say which side of VWAP the price is on. |
| 5 | Open a 5-minute chart of a stock you follow with VWAP on. Count the closes above and below VWAP and the number of crosses. Call the day trend or chop. |
| 2 | Anchor a VWAP to the last swing low on a daily chart and write where the price is against it. |

</div>

## Key terms

- **Volume-weighted average price (VWAP)**: the average price paid in a session, weighted by volume, from the open to now.
- **Typical price**: the average of a bar's high, low and close.
- **Anchored VWAP (AVWAP)**: a VWAP that starts at a bar you choose and continues.
- **Trend day**: a day when the price stays on one side of VWAP.
- **Chop day**: a day when the price crosses VWAP many times.

Next: [Chart patterns and the evidence](09-chart-patterns-and-the-evidence.md)
