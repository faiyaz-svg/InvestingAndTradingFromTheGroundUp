# Trend pullback setups

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">SWNG</span>

After this lesson you can apply the book's trend pullback rules to a chart: find the filter, the trigger, the entry, the stop and the target, size the position, and say when the setup fails.

Before this: [Trend and market structure](../05-reading-charts/02-trend-and-market-structure.md), [Moving averages](../05-reading-charts/05-moving-averages.md), [Position sizing with fixed fractional risk](../03-risk-and-position-sizing/04-fixed-fractional-sizing.md), [Where to put the stop](../03-risk-and-position-sizing/05-where-to-put-the-stop.md). You need: a calculator.

## The idea

A stock in an uptrend runs, falls back for a few days, and runs again. The **trend pullback** setup buys the second run: it waits for the dip, then for the first sign that the dip is over, and buys with a stop under the dip's low.

The bet is that the trend continues. The risk is a reversal, so the stop sits under the low.

## How it works

Exact rules for a long trade on daily bars, evaluated after the close. The numbers (3 down closes, 0.25 ATR, 2R, 10 days) are the book's choices, not tested standards.

1. Filter: the close is above the 50-day SMA, and the 50-day SMA is higher than it was 10 bars ago.
2. Pullback: find the highest high of the last 20 bars; call it \(H\), the prior high. Since that bar, price has made at least 3 down closes, and the lowest low since then, \(L\), touched or went below the 20-day EMA. No close since \(H\) is below the 50-day SMA.
3. Trigger: the first bar after \(L\) that closes above the previous bar's high. Call it the **trigger bar**.
4. Entry: a buy stop one cent above the trigger bar's high, placed for the next session only. If it does not trigger the next day, cancel it.
5. Initial stop: \(S = L - 0.25 \times ATR\), where ATR is the 14-day average true range on the trigger bar (Wilder smoothing, as in the chart data; lesson 2's scanner used a plain mean), rounded down to the cent.
6. Target: \(H\). Skip the trade unless \(H - E \ge 2R\), where \(E\) is the entry and \(R = E - S\) is the risk per share.
7. Time stop: if neither the target nor the stop has been hit, sell at the close of the 10th trading day after the entry day.
8. Size: shares = floor(0.01 x account / \(R\)) ([Position sizing](../03-risk-and-position-sizing/04-fixed-fractional-sizing.md)).

The **prior high** in step 2 is resistance that sellers defended once already. Step 6 uses it as the target and the test for room: a stop 1.50 below the entry with the old high 2.00 above gives 1.3R, and the rule skips it ([Win rate, payoff and expectancy](../03-risk-and-position-sizing/03-win-rate-payoff-and-expectancy.md)).

<div class="example" markdown>

### Worked example: a winning pullback

Stock A (made-up data). Account US$25,000, risk 1%.

1. The prior high is US$56.80 on March 26, 2026. Five down closes follow, to 51.60 on April 2. The low that day is \(L\) = US$51.30, under the 20-day EMA of 53.05. The 50-day SMA is 50.62.
2. April 3 closes at 52.60, above the previous bar's high of 52.50. It is the trigger bar. Its high is 52.80, so the buy stop is US$52.81. ATR is 0.9758.
3. Stop = 51.30 - 0.25 x 0.9758 = 51.056, rounded down to US$51.05. Risk per share \(R\) = 52.81 - 51.05 = US$1.76.
4. Room: 56.80 - 52.81 = US$3.99, which is 2.27R. It passes the 2R test.
5. Size: 0.01 x 25,000 = US$250. 250 / 1.76 = 142.05, so 142 shares. Cost 142 x 52.81 = US$7,499.02. Risk = 142 x 1.76 = US$249.92.
6. April 6 opens at 52.70 and trades up through 52.81, so the order fills at US$52.81.
7. April 10 trades up to 56.90, through the target of 56.80. The limit sell fills at 56.80.
8. Result: (56.80 - 52.81) x 142 = US$566.58, which is 3.99 / 1.76 = +2.27R.

</div>

```chart
data: 07-swing-trading/stock-a-pullback-win.json
title: Stock A, daily: a trend pullback that reaches the prior high
show: volume, ema 20, sma 50
level: 56.80 | Prior high (target)
level: 52.81 | Entry
level: 51.05 | Stop
marker: 2026-04-03 | below | Trigger bar
marker: 2026-04-10 | above | Target hit
range: 2026-03-02 to 2026-04-17
caption: The pullback low touched the 20-day average. The target was hit four nights after the entry.
```

<div class="example" markdown>

### Worked example: a losing pullback

Stock B (made-up data). Same account and rules.

1. The prior high is US$38.54 on April 23, 2026. After five down closes, \(L\) = US$34.81 on April 30, under the 20-day EMA of 35.62. The 50-day SMA is 33.16.
2. May 1 is the trigger bar (close 35.69 above the previous high of 35.63). Its high is 35.83, so the entry is US$35.84. ATR is 0.7427.
3. Stop = 34.81 - 0.25 x 0.7427 = 34.624, rounded down to US$34.62. Risk per share = 35.84 - 34.62 = US$1.22. Room = 38.54 - 35.84 = 2.70, which is 2.21R. It passes.
4. Size: 250 / 1.22 = 204.9, so 204 shares.
5. May 4 fills at 35.84. The stock drifts down for two sessions, and on May 7 it opens at US$34.47 on made-up bad news, below the stop. The stop fills at the open, US$34.47.
6. Result: (34.47 - 35.84) x 204 = -US$279.48, which is -1.37 / 1.22 = -1.12R.

</div>

The loss is more than 1R because the open was under the stop ([Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md)). The rules were followed. This is the cost of holding overnight.

```chart
data: 07-swing-trading/stock-b-pullback-loss.json
title: Stock B, daily: a pullback that fails through the stop
show: volume, ema 20, sma 50
level: 38.54 | Prior high
level: 35.84 | Entry
level: 34.62 | Stop
marker: 2026-05-07 | below | Opens 34.47
range: 2026-04-06 to 2026-05-11
caption: The stock opened below the stop on May 7, so the exit filled at the open and not at 34.62.
```

## When it fails, and what tests found

The setup does badly when the trend is ending (a dip that becomes a lower low), in a range with no trend to resume, and around earnings, where one gap overrides the chart. The [regime filter](03-market-regime-filters.md) cuts some of the first kind.

The published evidence is about the idea underneath it. Moskowitz, Ooi and Pedersen (2012) found that an asset's own past 1 to 12 month return predicts its next return across 58 futures and forwards ([Journal of Financial Economics, 104(2), 228-250](https://doi.org/10.1016/j.jfineco.2011.11.003)). George and Hwang (2004) found that stocks near their 52-week high outperformed stocks far from it over the following 6 months ([Journal of Finance, 59(5), 2145-2176](https://doi.org/10.1111/j.1540-6261.2004.00695.x)). Both support the trend half of the setup. Neither tests a pullback entry with a stop and a target, and I found no peer-reviewed test of this rule. Treat it as a hypothesis and test it in paper trading ([Paper trading](../practice/paper-trading.md)).

## In code

The stop and size from the sample file. Download [stock-a-pullback-win.csv](../assets/data/stock-a-pullback-win.csv).

<details class="code" markdown>
<summary>In code</summary>

```python
import math
import pandas as pd

bars = pd.read_csv("stock-a-pullback-win.csv", parse_dates=["date"]).set_index("date")
prev_close = bars["close"].shift()
tr = pd.concat(
    [bars["high"] - bars["low"], (bars["high"] - prev_close).abs(), (bars["low"] - prev_close).abs()],
    axis=1,
).max(axis=1)
atr = tr.ewm(alpha=1 / 14, adjust=False).mean()

trigger = pd.Timestamp("2026-04-03")
entry = round(bars.loc[trigger, "high"] + 0.01, 2)
low = bars.loc["2026-03-27":"2026-04-03", "low"].min()
stop = math.floor((low - 0.25 * atr[trigger]) * 100) / 100
shares = math.floor(0.01 * 25_000 / (entry - stop))
print(entry, low, stop, shares)
```

The code prints 52.81 51.3 51.05 142. The ATR here uses an exponential weight, close to Wilder's but not identical.

</details>

## Common mistakes

- Buying the dip before the trigger bar.
- Skipping the room test because the chart looks good. Without it you take trades that pay about 1R and lose 1R.
- Moving the stop down. A wider stop is a bigger loss than the size allows.

## Try it

1\. Stock C: entry US$30.20, pullback low US$28.90, ATR 0.60, prior high US$33.50. Find the stop, risk per share, room in R, and whether it passes the 2R test.

<details class="solution" markdown>
<summary>Answer</summary>

Stop = 28.90 - 0.25 x 0.60 = 28.75. Risk per share = 30.20 - 28.75 = US$1.45. Room = 33.50 - 30.20 = 3.30, which is 3.30 / 1.45 = 2.28R. It passes.

</details>

2\. Account US$40,000, risk 0.5%, entry US$30.20 and stop US$28.75. How many shares?

<details class="solution" markdown>
<summary>Answer</summary>

Risk = 0.005 x 40,000 = US$200. 200 / 1.45 = 137.9, so 137 shares.

</details>

3\. Stock D: entry US$20.00, stop US$19.00, prior high US$21.50. Does it pass the room test?

<details class="solution" markdown>
<summary>Answer</summary>

Risk per share is 1.00 and room is 1.50, which is 1.5R. That is under 2R, so the rule skips it.

</details>

4\. A trade fills at US$52.81 with a stop at US$51.05 and 142 shares. The stop order fills at US$50.90 after a gap. What is the loss in dollars and in R?

<details class="solution" markdown>
<summary>Answer</summary>

Loss = (52.81 - 50.90) x 142 = US$271.22. Risk per share was 1.76, so R = 1.91 / 1.76 = -1.09R.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Do the [chart drills](../practice/chart-drills.md) set 07-swing-trading, questions on pullbacks. |
| 5 | On a daily chart of any stock, find a past pullback and apply steps 1 to 6. Write the entry, stop, target and R on a note. |

</div>

## Key terms

- **Trend pullback**: a setup that buys the resumption of an uptrend after a short dip.
- **Prior high**: the highest high of the last 20 bars before the pullback, used as the target.
- **Trigger bar**: the first bar after the pullback low that closes above the previous bar's high.
- **Pullback low**: the lowest low between the prior high and the trigger bar.
- **Time stop**: an exit at a set number of days when neither the target nor the stop has been hit.

Next: [Breakouts and bases](05-breakouts-and-bases.md)
