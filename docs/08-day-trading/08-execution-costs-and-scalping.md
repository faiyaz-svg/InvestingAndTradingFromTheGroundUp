# Execution costs and scalping

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">DAY</span>

After this lesson you can put the spread, the fees and the slippage of a day trade into R, find the win rate a trade needs to break even after costs, and say why scalping needs a very low cost per share.

Before this: [Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md), [Win rate, payoff and expectancy](../03-risk-and-position-sizing/03-win-rate-payoff-and-expectancy.md) and [Level 2 and time and sales](07-level-2-and-time-and-sales.md). You need: a calculator.

## The idea

A day trade with a stop 0.63 away and a cost of US$0.05 per share loses 0.08R to costs before the market does anything. A trade with a stop 0.10 away and the same cost loses 0.5R. The fixed cost per share is the same, and the stop sets how large it is next to your risk.

**Scalping** is day trading for very small gains: targets of a few cents to a dime, stops of similar size, and many trades. It looks attractive because small moves happen often. Its problem is arithmetic, and the arithmetic is cost.

## How it works

### The cost per share

For a round trip with market orders at both ends, the cost per share is:

\[ c = s + 2f + 2k \]

- \(s\) is the quoted spread, in US$ per share. A round trip pays it once: half on the way in, half on the way out.
- \(f\) is the commission per share per side, in US$.
- \(k\) is the extra slippage per share per side, in US$, beyond the half spread (Part 3, [Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md)).

In R, with \(r\) the stop distance in US$ per share:

\[ c_R = \frac{c}{r} \]

A win that reaches \(T\) times the risk nets \(T - c_R\) in R. A loss at the stop is \(-(1 + c_R)\). The win rate that makes the expectancy zero is:

\[ p^{*} = \frac{1 + c_R}{T + 1} \]

- \(T\) is the target distance divided by the stop distance, with no unit.
- With no costs, \(p^{*} = 1 / (T + 1)\), which is the break-even win rate of Part 3.

The fee schedule below is made up for the lesson, not any broker's: US$0.005 per share per side, with a spread of US$0.02 and extra slippage of US$0.01 per side. That gives \(c = 0.02 + 2 \times 0.005 + 2 \times 0.01 = 0.05\). Replace it with your broker's schedule and your measured slippage.

<div class="example" markdown>

### Worked example: the same cost at five stop sizes

The cost is US$0.05 per share and the target is 2R (\(T = 2\)).

| Stop (US$) | Cost in R | Break-even win rate |
|---|---|---|
| 0.10 | 0.50 | (1 + 0.50) / 3 = 50.0% |
| 0.20 | 0.25 | 41.7% |
| 0.40 | 0.125 | 37.5% |
| 0.63 | 0.079 | 36.0% |
| 1.00 | 0.05 | 35.0% |

With no costs the break-even rate is 1 / 3 = 33.3%. The 0.63 stop is the opening range trade of lesson 4. A stop of 0.10 needs half the trades to win at 2R, which is a hard bar for any setup.

</div>

The figure shows the same thing for three cost levels. The cost in R climbs steeply once the stop falls below about 0.20.

![Round-trip cost in R against stop distance for costs of US$0.02, 0.05 and 0.10 per share](../assets/figures/08-day-trading/cost-vs-stop-dark.svg#only-dark)
![Round-trip cost in R against stop distance for costs of US$0.02, 0.05 and 0.10 per share](../assets/figures/08-day-trading/cost-vs-stop-light.svg#only-light)

### Scalping, in numbers

A scalp has a stop of 0.10 and a target of 0.15, so \(T = 1.5\). The cost is 0.05, so \(c_R = 0.5\). The break-even win rate is (1 + 0.5) / (1.5 + 1) = 60.0%. With no cost it would be 1 / 2.5 = 40.0%. Costs add 20 percentage points to the win rate the scalp must achieve.

Three things reduce the burden:

1. **Use limit orders to enter.** A limit order at the bid earns the spread instead of paying it, but it fills mostly when the price is moving against you (Part 1, [Who is on the other side of your trade](../01-how-markets-work/06-who-is-on-the-other-side.md)).
2. **Trade liquid stocks**, where the spread is one cent.
3. **Choose a broker schedule by your volume.** A per-share fee scales with size; a flat fee does not.

### What tests found

No published test of retail scalping rules could be confirmed for this book, so the lesson makes no claim about whether any scalp works. The arithmetic is exact, though, and you can measure your own \(s\), \(f\) and \(k\). The paper block in lesson 9 asks you to record them per trade.

<div class="canada" markdown>

### For Canadians

Wealthsimple lists a US$0 commission on US-listed stocks, and a 1.5% currency conversion fee on US-listed trades made in a CAD account, with no conversion fee from a USD account ([Wealthsimple trade fees](https://www.wealthsimple.com/legal/fees/trade), as of 2026). On a day trade that fee is large. On the opening range trade of lesson 4 (position US$16,992.36), 1.5% on the buy and on the sell is 2 x 254.89 = US$509.77, which is 2.04R. Trading from a USD account avoids that fee, but moving cash between CAD and USD accounts has its own tiered conversion fee (1.5% under C$10,000, lower above), and the USD account has a monthly fee. Plan the conversions once, not per trade (Part 2, [USD or CAD, and currency conversion fees](../02-accounts-currency-and-taxes/03-usd-vs-cad-and-fx-fees.md)). Check your IBKR Canada commission schedule on its pricing page before you use per-share numbers.

</div>

## In code

The function puts a cost schedule into R and finds the break-even win rate. It is plain Python.

<details class="code" markdown>
<summary>In code</summary>

```python
def cost_in_r(spread, commission, slippage, stop):
    """Round-trip cost per share, as a multiple of the stop distance."""
    return (spread + 2 * commission + 2 * slippage) / stop

def break_even_win_rate(cost_r, target_r):
    return (1 + cost_r) / (target_r + 1)

for stop, target in [(0.63, 2.0), (0.10, 1.5)]:
    c = cost_in_r(0.02, 0.005, 0.01, stop)
    p = break_even_win_rate(c, target)
    print(f"stop {stop:.2f}: cost {c:.3f}R, break-even {p:.1%}")
```

</details>

## Common mistakes

- Using the quoted spread as the whole cost. Add slippage on the stop exit, which is a market order.
- Judging a scalper's win rate without costs. A 55% win rate can be a loss at 60% required.
- Paying a 1.5% currency fee on every trade from a CAD account.

## Try it

1\. The spread is 0.03, commission 0.005 per side and slippage 0.01 per side. What is the cost per share, and the cost in R for a stop of 0.30?

<details class="solution" markdown>
<summary>Answer</summary>

c = 0.03 + 2 x 0.005 + 2 x 0.01 = US$0.06. c_R = 0.06 / 0.30 = 0.20R.

</details>

2\. With a cost of 0.20R and a target of 2R, what win rate breaks even?

<details class="solution" markdown>
<summary>Answer</summary>

(1 + 0.20) / (2 + 1) = 1.20 / 3 = 40.0%.

</details>

3\. A scalp has a stop of 0.08, a target of 0.12 and a cost of 0.04 per share. What is the break-even win rate?

<details class="solution" markdown>
<summary>Answer</summary>

c_R = 0.04 / 0.08 = 0.5. T = 0.12 / 0.08 = 1.5. p* = 1.5 / 2.5 = 60.0%.

</details>

4\. A US$10,000 position is bought and sold in a CAD account with a 1.5% fee each way. What does the round trip cost?

<details class="solution" markdown>
<summary>Answer</summary>

1.5% of 10,000 = US$150 each way, so US$300, or 3.0% of the position.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Look up your broker's commission and the typical spread of a stock you trade. Write \(c\) for a round trip. |
| 3 | Compute \(c_R\) for your usual stop distance and the break-even win rate for a 2R target. |
| 3 | Add a cost column to your [trade journal](../practice/trade-journal.md) and fill it for your last trade. |

</div>

## Key terms

- **Scalping**: day trading for very small gains, with small stops and many trades.
- **Round-trip cost per share**: the spread, commissions and slippage paid to enter and exit one share.
- **Break-even win rate (after costs)**: the win rate at which the expectancy, net of costs, is zero.

Next: [A day trading routine and limits](09-day-trading-routine-and-limits.md)
