# R-multiples

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">RISK</span>

After this lesson you can write any trade's result in R, the unit of risk, and compare trades that had different prices, sizes and stops.

Before this: [Risk first: the math of losses](01-risk-first.md), [Order types](../01-how-markets-work/05-order-types.md). You need: a calculator.

## The idea

Trade 1 makes US$180. Trade 2 makes US$95. Which one went better?

You cannot tell from the dollars. Trade 1 may have risked US$900 and Trade 2 only US$50. A US$180 gain on US$900 at risk is a modest result. A US$95 gain on US$50 at risk is nearly double the risk.

Traders solve this by measuring every result against the amount they put at risk. That amount is **R**: the money you lose if the trade hits its stop. A trade that makes twice its risk is +2R. A trade stopped out at the planned level is -1R. A trade that loses half the planned risk is -0.5R.

The result of a trade in R is its **R-multiple**. The name R comes from "risk". Using R turns a pile of trades at different prices into one list of comparable numbers.

## How it works

For a long trade, you need three prices: the entry \(E\), the stop \(S\) and the exit \(X\).

\[ \text{risk per share} = E - S \qquad R = N \times (E - S) \qquad r = \frac{X - E}{E - S} \]

- \(E\) is the entry price, \(S\) the stop price (below \(E\) for a long), and \(X\) the exit price, all in US$ per share.
- \(N\) is the number of shares.
- \(R\) is the initial risk in US$, the loss if the stop fills at \(S\).
- \(r\) is the R-multiple. The share count cancels, so it depends only on the three prices.

For a short trade the stop is above the entry, so the risk per share is \(S - E\) and the result is \(r = (E - X) / (S - E)\). Lesson 8 of Part 1 covers shorting ([Short selling](../01-how-markets-work/08-short-selling.md)).

<div class="example" markdown>

### Worked example: one trade in R

Stock A (made-up) pulled back and then turned up. You buy 166 shares at US$48.20 on February 25, 2026. Your stop is US$46.70. Lesson 5 explains where that stop comes from, and lesson 4 explains the 166 shares.

1. Risk per share = 48.20 - 46.70 = US$1.50.
2. R = 166 x 1.50 = US$249.00.
3. The price rises. You sell at US$51.20 on March 5. Result per share = 51.20 - 48.20 = US$3.00.
4. r = 3.00 / 1.50 = +2.0R.
5. Profit = 166 x 3.00 = US$498.00, which is 2 x US$249.00.

The chart marks the entry, the stop and the levels that are 1R and 2R above the entry. The high on March 5 was 51.33, so a sell order at 51.20 (2R) would have filled that day.

</div>

```chart
data: 03-risk-and-position-sizing/stock-a-pullback.json
title: Stock A, daily: a long trade measured in R
level: 48.20 | Entry
level: 46.70 | Stop (-1R)
level: 49.70 | +1R
level: 51.20 | +2R
marker: 2026-02-25 | below | Entry 48.20
marker: 2026-03-05 | above | Exit 51.20
range: 2026-02-05 to 2026-03-17
caption: Entry at 48.20 with a stop at 46.70 gives 1R = 1.50 per share. The +2R level at 51.20 traded on March 5.
```

### A list of trades in R

Here are six trades from a made-up journal. Each row gives the prices and the result in R.

| Trade | Side | Entry | Stop | Exit | Result in R |
|---|---|---|---|---|---|
| 1 | Long | 48.20 | 46.70 | 51.20 | +2.0R |
| 2 | Long | 20.00 | 19.00 | 19.00 | -1.0R |
| 3 | Long | 75.50 | 73.50 | 74.50 | -0.5R |
| 4 | Long | 31.00 | 30.00 | 31.30 | +0.3R |
| 5 | Long | 60.00 | 58.00 | 66.20 | +3.1R |
| 6 | Short | 40.00 | 41.00 | 38.60 | +1.4R |

The total is +5.3R over six trades, an average of 0.88R per trade. If each trade risked US$250, the total is 5.3 x 250 = US$1,325. The next lesson uses averages like this to measure an edge ([Win rate, payoff and expectancy](03-win-rate-payoff-and-expectancy.md)).

R has a catch. A stop is a plan, not a promise. If a stop order fills below its price, the loss is more than 1R. Lesson 6 measures that in R ([Slippage, gaps and costs](06-slippage-gaps-and-costs.md)).

## In code

Computing R-multiples for a list of trades in pandas.

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

trades = pd.DataFrame(
    {
        "entry": [48.20, 20.00, 75.50, 31.00, 60.00, 40.00],
        "stop": [46.70, 19.00, 73.50, 30.00, 58.00, 41.00],
        "exit": [51.20, 19.00, 74.50, 31.30, 66.20, 38.60],
    }
)
trades["r"] = (trades["exit"] - trades["entry"]) / (trades["entry"] - trades["stop"])
print(trades["r"].round(1).tolist())
print(round(trades["r"].sum(), 1), round(trades["r"].mean(), 2))
```

The formula works for the short because the signs flip together: (38.60 - 40.00) / (40.00 - 41.00) = +1.4. The code prints the six results, then a total of 5.3 and an average of 0.88.

</details>

## Common mistakes

- Calling a trade "+2R" when the stop was moved after entry. R is fixed at entry from the first stop. A later, wider stop does not change it.
- Measuring risk from the price you wish you had paid. Use the price you actually got.
- Treating R as a fixed dollar amount across the account's life. R is whatever you risked on that trade (lesson 4 sets it as a percent of the account).

## Try it

1\. You buy Stock B at US$32.00 with a stop at US$30.40 and sell at US$35.20. What is the result in R?

<details class="solution" markdown>
<summary>Answer</summary>

Risk per share = 32.00 - 30.40 = 1.60. Gain per share = 35.20 - 32.00 = 3.20. r = 3.20 / 1.60 = +2.0R.

</details>

2\. You buy Stock B at US$32.00 with a stop at US$30.40, and you sell at US$31.20. What is the result in R?

<details class="solution" markdown>
<summary>Answer</summary>

(31.20 - 32.00) / 1.60 = -0.80 / 1.60 = -0.5R.

</details>

3\. You short Stock A at US$50.00 with a stop at US$52.00 and cover at US$46.00. What is the result in R?

<details class="solution" markdown>
<summary>Answer</summary>

Risk per share = 52.00 - 50.00 = 2.00. Gain per share = 50.00 - 46.00 = 4.00. r = 4.00 / 2.00 = +2.0R.

</details>

4\. You risked US$300 (1R) and the trade made US$465. What is the result in R? What if it had lost US$330?

<details class="solution" markdown>
<summary>Answer</summary>

465 / 300 = +1.55R. A loss of US$330 is -330 / 300 = -1.1R, which is 0.1R worse than the plan.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Pick three recent trades from your broker's history. For each, write the stop you had in mind and compute the result in R. If you had no stop, write "none" and note that you cannot compute R. Record them in the [trade journal](../practice/trade-journal.md) if you keep one. |
| 3 | Use [chart drills](../practice/chart-drills.md) and, for two charts, pick an entry and a stop below a recent low, then read off where +1R and +2R sit. |
| 2 | Write the average of your three results in R. |

</div>

## Key terms

- **R**: the money lost if a trade hits its stop, used as the unit of risk.
- **R-multiple**: a trade's result divided by its initial risk, written as +2R or -1R.
- **Initial risk**: the loss at the planned stop, fixed at entry.

Next: [Win rate, payoff and expectancy](03-win-rate-payoff-and-expectancy.md)
