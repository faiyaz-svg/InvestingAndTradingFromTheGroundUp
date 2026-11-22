# Breakouts and bases

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">SWNG</span>

After this lesson you can recognise a base, mark its pivot, apply the book's breakout rules with a volume test, size the trade, and say when breakouts fail and what tests found.

Before this: [Support and resistance](../05-reading-charts/03-support-and-resistance.md), [Volume and relative volume](../05-reading-charts/04-volume-and-relative-volume.md), [Volatility indicators](../05-reading-charts/07-volatility-indicators.md). You need: a calculator.

## The idea

A stock rises to a high, then goes quiet. For six weeks it moves in a band, with smaller bars and falling volume. Then price closes above the high on heavy volume, the sellers at that level are gone and new buyers have arrived.

That quiet stretch is a **base**: a period of sideways trading after an advance, at least 20 bars long and no deeper than 15% from its high to its low. The top of the base is the **pivot**, the highest high in the base. A **breakout** is a close above the pivot. The setup buys it and leaves if price falls back into the base.

## How it works

Rules for a long trade on daily bars, evaluated after the close. The numbers (20 bars, 15%, 1.5 times volume, 2 ATR, 3R, 15 days) are the book's choices, not tested standards.

1. Base: since the highest high of the advance (the pivot \(P\)), at least 20 bars have passed, no close has been above \(P\), and the lowest low is no more than 15% below \(P\).
2. Trend: the 50-day SMA is rising.
3. Trigger: a bar closes above \(P\), the volume is at least 1.5 times the 20-day average volume before that bar, and the close is in the upper half of the bar's range.
4. Entry: buy at the next open. Skip the trade if the open is more than 2 ATR above \(P\) (the stock has run too far to buy with a tight stop).
5. Initial stop: \(S = P - ATR\), rounded down to the cent, where ATR is the 14-day average true range on the trigger bar. A fall to one ATR under the pivot means the breakout failed.
6. Target: \(E + 3R\), where \(E\) is the entry and \(R = E - S\).
7. Failed breakout exit: if any close is below \(P\) before the target, sell at the next open, even if the stop has not been hit.
8. Time stop: sell at the close of the 15th trading day after the entry day.
9. Size: shares = floor(0.01 x account / \(R\)).

Step 3 uses **relative volume**, a day's volume divided by its recent average ([Volume and relative volume](../05-reading-charts/04-volume-and-relative-volume.md)). The 3R target in step 6 is higher than the pullback's 2R because breakouts fail often and pay more when they work. A setup that pays 3R on a win and loses 1R otherwise has an expectancy of \(p \times 3 - (1 - p) \times 1\), where \(p\) is the win rate. That is zero at \(p = 0.25\), so the setup breaks even before costs at a 25% win rate and does better above it ([Win rate, payoff and expectancy](../03-risk-and-position-sizing/03-win-rate-payoff-and-expectancy.md)).

<div class="example" markdown>

### Worked example: a breakout that reaches 3R

Stock A (made-up data). Account US$25,000, risk 1%.

1. The advance peaks at US$40.69 on February 12, 2026. The base runs 31 bars to March 26, with a lowest low of 36.57 (10.1% under the pivot). Pivot \(P\) = 40.69.
2. March 27 closes at 41.46, above the pivot, in the upper half of its range (low 40.61, high 41.75). Volume is 3.9 million, against a prior 20-day average of 1,090,605, which is 3.58 times. The 14-day ATR is 0.6248.
3. March 30 opens at US$41.59, which is within 2 ATR of the pivot (the limit is 40.69 + 1.25 = 41.94). Entry \(E\) = 41.59.
4. Stop = 40.69 - 0.6248 = 40.065, rounded down to US$40.06. \(R\) = 41.59 - 40.06 = US$1.53.
5. Target = 41.59 + 3 x 1.53 = US$46.18.
6. Size: 250 / 1.53 = 163.4, so 163 shares. Cost 163 x 41.59 = US$6,779.17. Risk = 163 x 1.53 = US$249.39.
7. April 8 opens at 45.49 and trades to 46.47, through the target. The sell fills at 46.18.
8. Result: (46.18 - 41.59) x 163 = US$748.17, which is +3.0R.

</div>

The chart shows the base, then the volume spike on March 27.

```chart
data: 07-swing-trading/stock-a-base-breakout.json
title: Stock A, daily: a 31-day base and a breakout
show: volume, sma 50
level: 40.69 | Pivot
level: 40.06 | Stop
level: 46.18 | Target (3R)
marker: 2026-03-27 | above | Breakout, 3.58x volume
marker: 2026-04-08 | above | Target hit
range: 2026-01-12 to 2026-04-13
caption: The breakout bar had 3.58 times the average volume.
```

<div class="example" markdown>

### Worked example: a failed breakout

Stock B (made-up data). Same account and rules.

1. The pivot is US$31.13 (February 27, 2026). The base runs 30 bars, with a lowest low of 28.63 (8.0% under).
2. April 10 closes at 31.75, above the pivot, with relative volume of 2.62 and a close in the upper half. ATR is 0.4468.
3. April 13 opens at US$31.94, inside 2 ATR of the pivot. Entry = 31.94. Stop = 31.13 - 0.4468 = 30.683, rounded down to US$30.68. \(R\) = 1.26. Target = 31.94 + 3 x 1.26 = US$35.72.
4. Size: 250 / 1.26 = 198.4, so 198 shares.
5. The stock fades. On April 15 it closes at 31.01, below the pivot of 31.13. Its low that day was 30.94, still above the stop of 30.68, so the stop did not trigger.
6. Rule 7 applies. The sell order goes in at the next open, April 16, which is US$30.91.
7. Result: (30.91 - 31.94) x 198 = -US$203.94, which is -1.03 / 1.26 = -0.82R.

</div>

The failed breakout exit saved 0.18R against the stop here. It also exits trades that dip under the pivot and then continue up. Test it in your journal.

```chart
data: 07-swing-trading/stock-b-breakout-fail.json
title: Stock B, daily: a breakout that fell back into the base
show: volume, sma 50
level: 31.13 | Pivot
level: 30.68 | Stop
marker: 2026-04-10 | above | Breakout
marker: 2026-04-15 | above | Closes under the pivot
range: 2026-02-23 to 2026-04-17
caption: The close under the pivot on April 15 triggered the exit at the next open, April 16, at 30.91.
```

## When it fails, and what tests found

Breakouts fail when volume is weak, when the market is falling ([Market regime filters](03-market-regime-filters.md)), and when the stock gaps far above the pivot on news.

On evidence: George and Hwang (2004) found that nearness to the 52-week high predicted returns over the next 6 months better than a stock's return over the past 6 to 12 months, and that these profits did not reverse over the following years, unlike ordinary momentum ([Journal of Finance, 59(5), 2145-2176](https://doi.org/10.1111/j.1540-6261.2004.00695.x)). That supports buying strength near highs, over months. Brock, Lakonishok and LeBaron (1992) tested a trading-range breakout rule on the Dow Jones average from 1897 to 1986 and found that buy signals earned more than sell signals ([Journal of Finance, 47(5), 1731-1764](https://doi.org/10.1111/j.1540-6261.1992.tb04681.x)). That test is on an index with a different breakout definition, and part 5 covers data snooping ([Moving averages](../05-reading-charts/05-moving-averages.md)).

I found no peer-reviewed test of a base-and-volume breakout rule on individual stocks with a stop and a target. See [Chart patterns and the evidence](../05-reading-charts/09-chart-patterns-and-the-evidence.md) for what tests found on patterns in general.

## In code

Relative volume, ATR and the stop at the breakout. Download [stock-a-base-breakout.csv](../assets/data/stock-a-base-breakout.csv).

<details class="code" markdown>
<summary>In code</summary>

```python
import math
import pandas as pd

bars = pd.read_csv("stock-a-base-breakout.csv", parse_dates=["date"]).set_index("date")
base = bars.loc["2026-02-12":"2026-03-26"]
pivot = base["high"].max()
trigger = pd.Timestamp("2026-03-27")
avg_volume = bars["volume"].shift(1).rolling(20).mean()[trigger]
relative_volume = bars.loc[trigger, "volume"] / avg_volume
print(len(base), pivot, round(relative_volume, 2))
```

The code prints 31 40.69 3.58.

</details>

## Common mistakes

- Buying an intraday poke above the pivot. Many are above it at 11 a.m. and below it at 4 p.m. Wait for the close.
- Counting a flat patch as a base. A 6-bar pause is not one.
- Chasing a stock far past the pivot. The rule skips an open more than 2 ATR above it.

## Try it

1\. Stock E: pivot US$60.00, ATR 1.20, the next open is US$61.30. Entry, stop, risk per share and the 3R target? Does the open pass the 2 ATR test?

<details class="solution" markdown>
<summary>Answer</summary>

The limit is 60.00 + 2 x 1.20 = 62.40, and 61.30 is below it, so it passes. Stop = 60.00 - 1.20 = 58.80. Risk per share = 61.30 - 58.80 = US$2.50. Target = 61.30 + 3 x 2.50 = US$68.80.

</details>

2\. Account US$20,000, risk 1%, risk per share US$2.50. How many shares?

<details class="solution" markdown>
<summary>Answer</summary>

Risk = US$200. 200 / 2.50 = 80 shares.

</details>

3\. A breakout day has volume of 2.4 million shares. The prior 20-day average is 1.8 million. Does it pass the volume test?

<details class="solution" markdown>
<summary>Answer</summary>

2.4 / 1.8 = 1.33, which is below 1.5. It fails.

</details>

4\. A setup wins 30% of the time at +3R and loses 1R otherwise. What is the expectancy per trade, before costs?

<details class="solution" markdown>
<summary>Answer</summary>

0.30 x 3 - 0.70 x 1 = 0.90 - 0.70 = +0.20R.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Do the [chart drills](../practice/chart-drills.md) set 07-swing-trading, questions on breakouts. |
| 5 | Find a base on a daily chart. Mark its pivot, count its bars, and compute its depth in percent and the relative volume of the first close above the pivot. |

</div>

## Key terms

- **Base**: a period of sideways trading after an advance, at least 20 bars and no deeper than 15%.
- **Pivot**: the highest high of the base, the level a breakout must close above.
- **Breakout**: a close above the pivot.
- **Failed breakout**: a close back below the pivot after a breakout.

Next: [Short-term mean reversion](06-short-term-mean-reversion.md)
