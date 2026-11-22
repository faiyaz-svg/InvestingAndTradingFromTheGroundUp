# Entries, stops and targets

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">SWNG</span>

After this lesson you can compare the entry orders, stop placements and target types a swing trade can use, work out what each does to your size and your R, and pick one set of choices and write it into your plan.

Before this: [Order types](../01-how-markets-work/05-order-types.md), [Where to put the stop](../03-risk-and-position-sizing/05-where-to-put-the-stop.md), [Trend pullback setups](04-trend-pullback-setups.md). You need: a calculator.

## The idea

The three setups in this part differ in their filters, and they share one structure: an entry, a stop and a target. Each can be done in more than one way, and each way has a cost. The entry order decides whether you get the trade and at what price. The stop decides your size, since size comes from the distance to it. The target decides your reward in R, which sets the win rate you need.

This lesson takes the trade from lesson 4, Stock A's pullback, and changes one choice at a time. The setup stays the same, so the differences show what each choice does.

## How it works

### The entry

Three ways to enter on the day after the trigger bar:

1. A buy stop above the trigger bar's high. The order fills only if the price rises through it, which confirms that buyers are still there. If the stock opens above it, you get the open.
2. A buy at the next open. It always fills, and there is no confirmation: you buy before you know whether the day goes up or down.
3. A buy limit below the market, at a pullback to a level such as the trigger bar's low or the 20-day average. It gets a better price and may not fill, so the winners you miss are the strong ones.

For Stock A on April 6, 2026 (the entry day), the trigger bar's high is 52.80, the open is 52.70, the low is 52.55 and the high is 53.60. Stop 51.05 and target 56.80 (the prior high). Account US$25,000, 1% risk.

| Entry | Fill | Risk per share | Shares | Reward to 56.80 |
|---|---|---|---|---|
| Buy stop at 52.81 | 52.81 | 1.76 | 142 | 2.27R |
| Next open | 52.70 | 1.65 | 151 | 2.48R |
| Limit at 52.00 | No fill: the low was 52.55 | none | none | none |

The next open was lower than the buy stop that day, so it gave a better price. On a day when the stock opens at 52.70 and then falls to 51.50, the buy stop would not have filled and the open would have lost. One day shows nothing about which is better. The buy stop costs a few cents and gives a filter. The limit order protects the price and loses the trade when it works. The book's setups use the buy stop for pullbacks and the next open for breakouts and mean reversion, where the trigger has already happened at the close.

### The stop

Part 3 gave two ways ([Where to put the stop](../03-risk-and-position-sizing/05-where-to-put-the-stop.md)): from structure (a buffer under the pullback low) and from volatility (a multiple of ATR under the entry).

| Stop | Level | Risk per share | Shares | Reward to 56.80 |
|---|---|---|---|---|
| Structure: 51.30 low minus 0.25 ATR | 51.05 | 1.76 | 142 | 2.27R |
| Volatility: 2 ATR under the entry | 50.85 | 1.96 | 127 | 2.04R |

The volatility stop is 0.20 lower, so you hold 15 fewer shares and the same target is worth fewer R. In this case the structure stop is better: it is tighter and sits under a low the trade should not break. Stops under obvious lows can be run before the move, a claim that part 6 tests in [Liquidity and stop runs](../06-ict-and-smart-money-tested/02-liquidity-and-stop-runs.md). A buffer such as 0.25 ATR is the book's compromise. A stop order at the broker protects you if you are away. A mental stop does not.

What tests found. Kaminski and Lo (2014) derived when stop-loss rules add value: under a random walk, a simple stop-loss rule always lowers expected return, and when returns have momentum or the market switches between regimes, a stop can add value ([Journal of Financial Markets, 18, 234-254](https://doi.org/10.1016/j.finmar.2013.07.001)). The first result says a stop is not free. The second says it pays when trends persist, which is the world the pullback setup assumes. Their analysis is about expected return. This book uses stops to cap the loss per trade at the size you chose.

### The target

| Target | Price | R | First hit |
|---|---|---|---|
| 2R | 56.33 | 2.00 | April 10 |
| Prior high | 56.80 | 2.27 | April 10 |
| 3R | 58.09 | 3.00 | April 14 |

The prices come from 52.81 + 2 x 1.76, 52.81 + 3 x 1.76 and the March 26 high. All three hit here. On Stock B's chart in lesson 4, none would have, since the stock gapped through the stop first. A farther target pays more and is hit less often. The break-even win rate for a reward of \(r\) times the risk, ignoring costs, is

\[ p_{\text{be}} = \frac{1}{1 + r} \]

- \(p_{\text{be}}\) is the win rate at which the expectancy is zero.
- \(r\) is the reward in R when the trade wins, with a loss of exactly 1R.

At \(r = 2\), \(p_{\text{be}}\) is 1 / 3 = 33.3%. At \(r = 3\) it is 25%. At \(r = 1\) it is 50%. A target is a bet on how often price travels that far, and only your journal shows how often. [Win rate, payoff and expectancy](../03-risk-and-position-sizing/03-win-rate-payoff-and-expectancy.md) works through the expectancy.

### Putting the orders in

Many brokers offer a bracket order, which attaches a stop and a target to an entry, so that when one exit fills the other is cancelled ([Order types](../01-how-markets-work/05-order-types.md)). If yours does not, place the entry, and place the stop as soon as the entry fills. Write the three prices in the journal before the order, as the journal page asks ([Trade journal](../practice/trade-journal.md)).

<div class="example" markdown>

### Worked example: choosing and writing the plan lines

You decide: pullback entries use a buy stop one cent above the trigger bar's high; the stop is the pullback low minus 0.25 ATR; the target is the prior high if it is at least 2R away.

1. Trigger bar high 52.80, so the buy stop is 52.81.
2. Low 51.30 and ATR 0.9758, so the stop is 51.30 - 0.244 = 51.056, rounded down to 51.05.
3. Risk per share 1.76 and room to the prior high 3.99, which is 2.27R, so the trade passes.
4. Shares = floor(250 / 1.76) = 142, for a risk of US$249.92.

The same four lines go in the plan for every pullback trade.

</div>

<div class="canada" markdown>

### For Canadians

The order types you can use depend on the broker and the account. Check whether your Wealthsimple or IBKR order ticket offers buy stop orders, stop orders and bracket orders for US stocks in your TFSA, RRSP, FHSA, cash and margin accounts, and whether orders can be left good-till-cancelled. Part 1 has the order types ([Order types](../01-how-markets-work/05-order-types.md)). A US stock bought in a CAD account may involve a currency conversion on entry and exit, which adds to your costs in R ([Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md)).

</div>

## Common mistakes

- Choosing the entry order after seeing the price. Decide it in the plan.
- Setting a target from what you hope for. Take it from a level on the chart, or from a fixed R multiple, and write it down.
- Placing the stop after the fill and being away from the screen. Use a bracket order, or place the stop in the same minute.

## Try it

1\. Trigger bar high US$24.60, pullback low US$23.20, ATR 0.50. Buy stop, stop, and risk per share?

<details class="solution" markdown>
<summary>Answer</summary>

Buy stop = 24.61. Stop = 23.20 - 0.25 x 0.50 = 23.075, rounded down to 23.07. Risk per share = 24.61 - 23.07 = US$1.54.

</details>

2\. For the trade in exercise 1, a 3R target is what price? Account US$30,000, 1% risk: how many shares?

<details class="solution" markdown>
<summary>Answer</summary>

Target = 24.61 + 3 x 1.54 = US$29.23. Shares = floor(300 / 1.54) = floor(194.8) = 194.

</details>

3\. What win rate do you need to break even with a 1.5R target and a 1R loss, before costs?

<details class="solution" markdown>
<summary>Answer</summary>

1 / (1 + 1.5) = 0.40, so 40%.

</details>

4\. Stock A's next open is US$53.40, above your buy stop of US$52.81. Where does the order fill, and what is the risk per share if the stop is 51.05?

<details class="solution" markdown>
<summary>Answer</summary>

It fills at the open, US$53.40, because the stop price was passed. Risk per share = 53.40 - 51.05 = US$2.35. Recompute the size: floor(250 / 2.35) = 106 shares, or skip the trade if the room to the target fails the 2R test (56.80 - 53.40 = 3.40, which is 1.45R, so skip).

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Write the plan lines for each of your setups: entry order, stop rule, target rule. |
| 3 | Take one past trade from your paper or live record. Recompute it with the other stop type and write the change in shares and R. |
| 3 | Check your broker's order ticket for a bracket order. Write how to place a stop and a target together. |

</div>

## Key terms

- **Buy stop entry**: a buy order that fills only if the price rises through a set level.
- **Structure stop**: a stop placed under a chart level, such as the pullback low, with a buffer.
- **Break-even win rate**: the win rate at which expectancy is zero, \(1 / (1 + r)\) for a reward of \(r\) R.
- **Bracket order**: an entry with a linked stop and target, where one exit fills and cancels the other.

Next: [Managing the trade](08-managing-the-trade.md)
