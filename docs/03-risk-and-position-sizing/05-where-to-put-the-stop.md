# Where to put the stop

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">RISK</span>

After this lesson you can place a stop from chart structure (below a swing low) and from volatility (a multiple of the average true range), compare the two, and size the trade from either.

Before this: [Position sizing with fixed fractional risk](04-fixed-fractional-sizing.md). You need: a calculator.

## The idea

The size of a trade comes from the stop (lesson 4), so the stop has to be chosen first and chosen for a reason. The reason is not "the loss I can stand". A stop belongs at the price where your reason for the trade is wrong.

Stock A rose from about 42 to about 50, pulled back, and bounced. You want to buy the bounce. If the price falls below the low of the pullback, the pullback was not a pause, and the idea has failed. That low is the place for the stop. This is a stop from **structure**: a level the chart itself marks.

The other common method uses the stock's normal daily range. If a stock moves 0.80 a day on average, a stop 0.30 below your entry will be hit by ordinary noise. A stop at a multiple of that range sits outside the noise. This is a stop from **volatility**.

## How it works

### A stop from structure

A **swing low** is a bar whose low is lower than the lows of the bars on each side of it. On February 19, 2026, Stock A's bar has a low of 46.90, below the neighbouring lows of 47.19 (the day before) and 47.93 (the day after).

1. Find the swing low that the trade depends on: 46.90.
2. Put the stop a small buffer below it, so that a price that only touches the low does not stop you out. Here the buffer is 0.20, which is a quarter of the average true range defined below (0.25 x 0.80 = 0.20).
3. Stop = 46.90 - 0.20 = 46.70.

```chart
data: 03-risk-and-position-sizing/stock-a-pullback.json
title: Stock A, daily: a stop below a swing low
level: 46.90 | Swing low 46.90
level: 46.70 | Stop 46.70
level: 48.20 | Entry 48.20
marker: 2026-02-19 | below | Swing low
marker: 2026-02-25 | above | Entry
range: 2026-01-26 to 2026-03-09
caption: The swing low on February 19 is 46.90. The stop sits 0.20 below it, and the entry on February 25 is 48.20.
```

### A stop from volatility

The **true range** of a bar is its full range including any gap from the day before:

\[ TR = \max\bigl(H - L,\ |H - C_{\text{prev}}|,\ |L - C_{\text{prev}}|\bigr) \]

- \(H\) and \(L\) are the bar's high and low, and \(C_{\text{prev}}\) is the previous bar's close, all in US$.
- The three terms are the bar's own range and the distance from the old close to each extreme. The largest wins, so a gap is counted.

The **average true range** (ATR) is the mean of the last 14 true ranges. This lesson uses the plain average; Part 5 teaches the smoothed version traders usually plot ([Volatility indicators](../05-reading-charts/07-volatility-indicators.md)). The stop is

\[ S = E - k \times ATR \]

- \(E\) is the entry price, \(ATR\) is in US$ per share, and \(k\) is a multiplier you choose (2 is a common starting point).

<div class="example" markdown>

### Worked example: both stops on the same trade

Stock A, entry US$48.20 on February 25, 2026.

1. ATR (14 bars) on February 25 = US$0.80 (0.7971 before rounding).
2. ATR stop with k = 2: 48.20 - 2 x 0.7971 = 48.20 - 1.594 = US$46.61 (rounded).
3. Structure stop: US$46.70.
4. Risk per share: structure 48.20 - 46.70 = US$1.50. ATR 48.20 - 46.61 = US$1.59.
5. Size at US$250 of risk: structure 250 / 1.50 = 166 shares. ATR 250 / 1.594 = 156 shares (rounded down).

The two stops are nine cents apart, because the swing low happens to sit about two ATRs below the entry. On other charts they can differ a lot.

</div>

The chart shows the ATR in its own panel under the price, with the ATR stop as a level.

```chart
data: 03-risk-and-position-sizing/stock-a-pullback.json
title: Stock A, daily: a stop from the average true range
show: atr 14
level: 46.61 | ATR stop 46.61
level: 48.20 | Entry 48.20
marker: 2026-02-25 | above | Entry
range: 2026-01-26 to 2026-03-09
caption: Fourteen-bar ATR was about 0.80 on February 25. Twice that below the entry gives a stop at 46.61.
```

### Choosing between them

Use structure when the chart has a clear low or high that your idea depends on. Use ATR when it does not, or to check a structure stop: if the structure stop is less than one ATR away, ordinary noise will probably hit it, and if it is more than three ATRs away, the position will be small. In either case the stop sets the size. A wide stop means a small position and a tight stop means a large one, and the loss at the stop is the same.

Where stops fail: a stop at an obvious low can be hit when the price dips below it and then recovers, which is why the buffer exists. A volatility stop can sit in the middle of a chart with no meaning, so the price can hit it without saying anything about the idea. Neither method protects against a gap through the stop (lesson 6). The book does not claim that one rule beats the other: no published test of stop placement is cited here, so there is no evidence to report.

## In code

Computing the 14-bar ATR and the stop from the sample file. Download [stock-a-pullback-daily.csv](../assets/data/stock-a-pullback-daily.csv).

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

bars = pd.read_csv("stock-a-pullback-daily.csv", parse_dates=["date"])
prev_close = bars["close"].shift()
true_range = pd.concat(
    [
        bars["high"] - bars["low"],
        (bars["high"] - prev_close).abs(),
        (bars["low"] - prev_close).abs(),
    ],
    axis=1,
).max(axis=1)
bars["atr"] = true_range.rolling(14).mean()

entry_day = bars[bars["date"] == "2026-02-25"].iloc[0]
stop = entry_day["close"] - 2 * entry_day["atr"]
print(round(entry_day["atr"], 4), round(stop, 2))
```

The code prints 0.7971 and 46.61.

</details>

## Common mistakes

- Putting the stop exactly on the low. A price that touches the level and turns can stop you out. Leave a buffer.
- Widening the stop after entry to avoid being stopped. That changes the risk you agreed to (lesson 2 keeps R fixed at entry). If the idea is still right, you should have placed the stop there to begin with.
- Picking a stop from a round loss, such as "I will lose 2%". A percent of price has no link to the chart.

## Try it

1\. Stock B's last three bars have lows of 31.80, 31.10 and 31.60. The middle bar is a swing low. You buy at 32.50 with a buffer of 0.15 below the swing low. What are the stop and the risk per share?

<details class="solution" markdown>
<summary>Answer</summary>

Stop = 31.10 - 0.15 = US$30.95. Risk per share = 32.50 - 30.95 = US$1.55.

</details>

2\. Compute the true range of a bar with high 52.40, low 51.50, whose previous close was 50.80.

<details class="solution" markdown>
<summary>Answer</summary>

H - L = 0.90. |H - prev close| = 1.60. |L - prev close| = 0.70. The largest is 1.60, so TR = US$1.60. The gap above the old close is part of the range.

</details>

3\. ATR is US$1.20 and you buy at US$60.00 with k = 2. What is the stop, and how many shares for US$300 of risk?

<details class="solution" markdown>
<summary>Answer</summary>

Stop = 60.00 - 2 x 1.20 = US$57.60. Risk per share = 2.40. Shares = 300 / 2.40 = 125.

</details>

4\. The structure stop is US$2.10 away and the ATR is US$1.80. About how many ATRs away is it, and is that tight, normal or wide?

<details class="solution" markdown>
<summary>Answer</summary>

2.10 / 1.80 = 1.17 ATRs. That is above the one-ATR warning level but under the 2 ATRs of a common volatility stop, so it is on the tight side and ordinary noise could still hit it. Widen the buffer, accept the smaller position that goes with a wider stop, or skip the trade.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Open [chart drills](../practice/chart-drills.md). On three charts, mark the swing low you would use and write the stop with a buffer. |
| 3 | For each, write the risk per share and the shares for 1% of a US$25,000 account. |
| 2 | Write which of the three stops is under one ATR from the entry, by eye. |

</div>

## Key terms

- **Stop from structure**: a stop placed beyond a level the chart marks, such as a swing low.
- **Swing low**: a bar whose low is below the lows of the bars on each side.
- **Buffer**: the distance between the structure level and the stop.
- **True range**: the largest of a bar's range and the distances from the previous close to its high and low.
- **Average true range (ATR)**: the average of the last 14 true ranges.
- **Stop from volatility**: a stop placed a multiple of the ATR from the entry.

Next: [Slippage, gaps and costs](06-slippage-gaps-and-costs.md)
