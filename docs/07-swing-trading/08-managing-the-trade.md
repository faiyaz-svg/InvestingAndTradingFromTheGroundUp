# Managing the trade

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">SWNG</span>

After this lesson you can compare three exit methods on one trade, move a stop only in the direction the plan allows, and decide what to do with an open trade before an earnings report or a weekend.

Before this: [Entries, stops and targets](07-entries-stops-and-targets.md), [Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md). You need: a calculator.

## The idea

After the order fills you have two tasks: do not damage the plan, and decide what happens if the trade runs past the target. The first has one rule: the stop only moves in the direction of profit. Widening a stop turns the 1% you chose to risk into a larger loss.

The second task has several answers. A fixed target takes a known profit. A trailing stop follows the price up and gives back some profit when the move ends. An indicator exit uses a rule such as a close under the 20-day average. Each gives a different result on the same chart.

## How it works

### Three exits on one trade

Take the pullback trade from lesson 4: Stock A, bought at US$52.81 on April 6, 2026, stop 51.05, 142 shares, one R = US$1.76. After the target at 56.80 fills on April 10, the price keeps rising to a high of 59.60 on April 16 and then falls back. Three exit rules, applied to the same bars:

1. Fixed target: the prior high, 56.80.
2. Trailing stop: after each close, set the stop to the highest close since entry minus 2 ATR (14-day), never lower than before. A fill happens when the price trades through it.
3. Indicator exit: sell at the next open after the first close below the 20-day EMA.

<div class="example" markdown>

### Worked example: three exits, one trade

1. Fixed target. The sell limit fills at 56.80 on April 10. Profit (56.80 - 52.81) x 142 = US$566.58, which is +2.27R.
2. Trailing stop. The highest close is 59.30 on April 16, and it holds through April 20. After April 20 the stop is 59.30 - 2 x ATR, which is US$57.24. On April 21 the stock opens at 57.50 and trades down to 56.40, so the stop fills at 57.24. Profit (57.24 - 52.81) x 142 = US$629.06, which is +2.52R.
3. Indicator exit. April 22 closes at 55.60, below the 20-day EMA of 55.92. The sell goes in for the next open, April 23, at 55.50. Profit (55.50 - 52.81) x 142 = US$381.98, which is +1.53R.

The trail earned the most here and the indicator exit the least. A different chart can reverse that order. One trade does not show which rule is better.

</div>

Look at the three exits on the same chart: the target on April 10, the trailing stop on April 21 and the indicator exit on April 23.

```chart
data: 07-swing-trading/stock-a-pullback-win.json
title: Stock A, daily: three ways to exit the same trade
show: ema 20
level: 56.80 | Fixed target 56.80
level: 57.24 | Trailing stop 57.24
marker: 2026-04-10 | above | Target 56.80, +2.27R
marker: 2026-04-21 | above | Trail 57.24, +2.52R
marker: 2026-04-23 | below | EMA exit 55.50, +1.53R
range: 2026-03-30 to 2026-04-23
caption: The same entry on April 6. The three rules exit on three different days at three different prices.
```

What tests found. I did not find a peer-reviewed test that compares trailing-stop and fixed-target exits for swing trades on stocks. Kaminski and Lo (2014) derived when stop-loss rules add value, and found that a stop lowers expected return in a random walk and can raise it when returns have momentum ([Journal of Financial Markets, 18, 234-254](https://doi.org/10.1016/j.finmar.2013.07.001)). A trailing stop is a stop-loss rule, so it should do better when trends persist. Measure the choice in your paper trades.

### Moving the stop

Two common moves, and what each costs.

A break-even stop moves the stop to the entry price after the trade is up some amount, such as 1R. It removes the risk of a loss. It also gets hit by ordinary noise: a stock up 1R often comes back to the entry before it moves on, and the trade ends at zero.

A wider trail (3 ATR) gives the trade room and leaves more profit behind. A narrower trail (1 ATR) is hit often. Widening the initial stop is not allowed under the plan.

### Before earnings

An earnings report is the largest scheduled risk for a swing trade. Companies announce their dates ahead of time, and brokers list them. The gap can be large in either direction, and the stop fills at the open, not at its price ([Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md)).

<div class="example" markdown>

### Worked example: an earnings gap

You hold Stock A, 142 shares, bought at 52.81 with a stop at 51.05, and the stock closes at 55.00 the day before a report. The report is released overnight, and the stock opens at US$50.60, a drop of 8.0% from 55.00.

1. The stop at 51.05 is above the open, so it triggers and fills at 50.60.
2. Loss = (52.81 - 50.60) x 142 = US$313.82. In R: 2.21 / 1.76 = -1.26R.
3. Planned risk was US$249.92, so the gap added US$63.90.

Three choices before the report: sell, cut the position (a half position makes this loss US$156.91), or hold if you accept a loss of more than 1R. The book's setups exclude stocks with earnings inside the hold window, so the usual choice is to sell before the report.

</div>

For the options side of an earnings trade, see Earnings trades and IV crush<!-- link: ../16-volatility-and-event-trading/04-earnings-trades-and-iv-crush.md -->.

### Overnight and weekend holds

Every night held is an overnight gap risk. Lou, Polk and Skouras (2019) split returns into overnight (close to open) and intraday (open to close) parts, and reported that across 14 strategies the profits of reversal and several momentum strategies were earned overnight and those of others during the trading day ([Journal of Financial Economics, 134(1), 192-213](https://doi.org/10.1016/j.jfineco.2019.03.011)). So the timing of your entry and exit changes which part of the move you capture.

A weekend adds two days of news to one gap. The book has no rule for closing on Fridays. If you want one, write it down and test it in the journal.

### Open risk

Each open trade adds to your open risk. Part 3 gave the limit: add up the distance from each position's price to its stop, and stay under the heat cap in your plan ([Portfolio heat and correlation](../03-risk-and-position-sizing/07-portfolio-heat-and-correlation.md)). For example, with 1% risk per trade and a 5% heat cap, five open trades at full stop distance is the most.

## In code

The three exits from the sample file. Download [stock-a-pullback-win.csv](../assets/data/stock-a-pullback-win.csv).

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

bars = pd.read_csv("stock-a-pullback-win.csv", parse_dates=["date"]).set_index("date")
entry, risk, shares = 52.81, 1.76, 142
ema20 = bars["close"].ewm(span=20, adjust=False).mean()
day = pd.Timestamp("2026-04-22")
print(bars.loc[day, "close"], round(ema20[day], 2))
exit_price = bars["open"].shift(-1)[day]
print(exit_price, round((exit_price - entry) / risk, 2), round((exit_price - entry) * shares, 2))
```

The code prints 55.6 55.92 and then 55.5 1.53 381.98.

</details>

## Common mistakes

- Widening the stop because "it will come back". The size was set from the original stop.
- Moving to break-even too early. If you use it, set the trigger at 1.5R or more and measure the cost.
- Holding through earnings without deciding. Look at the calendar when you scan.

## Try it

1\. You bought at US$20.00 with a stop at US$19.00 and 250 shares. The stock closes at US$22.50. Where is a break-even stop, and what is the open profit in R?

<details class="solution" markdown>
<summary>Answer</summary>

The break-even stop is US$20.00. Open profit = 2.50 / 1.00 = 2.5R.

</details>

2\. The highest close since entry is US$30.00 and ATR is 0.80. Where is a 2 ATR trailing stop? Last night's stop was 28.20. What is tonight's?

<details class="solution" markdown>
<summary>Answer</summary>

30.00 - 2 x 0.80 = 28.40. It is higher than 28.20, so the stop moves up to 28.40.

</details>

3\. Tomorrow's stop is 28.40 and the stock opens at 27.90. What is the fill, and why?

<details class="solution" markdown>
<summary>Answer</summary>

Near 27.90. The price passed the stop level at the open, so the stop becomes a market order and fills at the open.

</details>

4\. You hold 200 shares bought at US$40.00 with a stop at US$38.00. A report is due tonight, and the stock closes at US$41.00. The stock opens at US$36.00. What is the loss in dollars and R?

<details class="solution" markdown>
<summary>Answer</summary>

Loss = (40.00 - 36.00) x 200 = US$800. One R is 2.00 x 200 = US$400, so the loss is -2.0R.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Take one trade from your paper record and recompute its result under a trailing stop and an indicator exit. Write which of the three was best. |
| 3 | Look up the next earnings date for each stock on your watchlist. Mark any inside 10 trading days. |
| 3 | Write your stop-moving rules in the plan: when it can move, and the one thing it may never do. |

</div>

## Key terms

- **Break-even stop**: a stop moved to the entry price once the trade is ahead by a set amount.
- **Trailing stop**: a stop that follows the price up at a set distance and never moves down. Here: the highest close minus 2 ATR.
- **Indicator exit**: an exit triggered by a rule on an indicator, such as a close under the 20-day EMA.
- **Earnings gap**: a jump at the open after a company reports results.

Next: [A weekly swing routine](09-weekly-swing-routine.md)
