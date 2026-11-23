# Slippage, gaps and costs

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">RISK</span>

After this lesson you can measure a stop that filled worse than planned, a gap through a stop, and trading costs, all in R, and say how they change your size and your expectancy.

Before this: [Position sizing with fixed fractional risk](04-fixed-fractional-sizing.md), [Order types](../01-how-markets-work/05-order-types.md). You need: a calculator.

## The idea

Lesson 4 sized 166 shares of Stock A so that a stop-out at US$46.70 would cost US$249, which is 1R. That is the loss if the stop fills at its price. A stop order is not a price guarantee: Part 1 showed that it becomes a market order once triggered ([Order types](../01-how-markets-work/05-order-types.md)). The fill can land below the stop.

Three things make the real loss differ from the plan. **Slippage** is the difference between the price you expected and the price you got (Part 1 introduced it with the order book: [Bid, ask and the order book](../01-how-markets-work/04-bid-ask-and-the-order-book.md)). A **gap** is a jump between one close and the next open, with no trades in between, so a stop inside the gap fills at the open. **Costs** are what you pay to trade: commission, the spread and currency conversion. All three are easiest to compare in R.

## How it works

### Slippage and gaps in R

\[ r_{\text{stop}} = -\frac{E - F}{E - S} \]

- \(E\) is the entry and \(S\) the stop, in US$ per share.
- \(F\) is the price at which the stop order actually filled.
- If \(F = S\) the result is -1R. If \(F\) is below \(S\) the loss is more than 1R.

<div class="example" markdown>

### Worked example: slippage and a gap on 166 shares

You hold 166 shares of Stock A bought at US$48.20 with a stop at US$46.70. One R is 166 x 1.50 = US$249.00.

1. Slippage. The market is fast and the stop fills at US$46.55. Loss = (48.20 - 46.55) x 166 = US$273.90. In R: 1.65 / 1.50 = -1.10R.
2. Gap. The stock closes at 48.20 on April 15, 2026, then opens at US$45.10 on April 16. The stop at 46.70 is inside the gap, so it triggers at the open and fills near 45.10. Loss = (48.20 - 45.10) x 166 = US$514.60. In R: 3.10 / 1.50 = -2.07R.
3. On a US$25,000 account, the planned loss was 1.0% and the gap loss is 2.06%.

</div>

The chart shows the gap. No trade happened between 46.70 and 45.10 on that morning, so no order resting in that range could fill.

```chart
data: 03-risk-and-position-sizing/stock-a-gap-down.json
title: Stock A, daily: a gap down through a stop
level: 48.20 | Entry 48.20
level: 46.70 | Stop 46.70
marker: 2026-04-16 | below | Opens at 45.10
range: 2026-03-23 to 2026-04-28
caption: The close on April 15 was 48.20 and the open on April 16 was 45.10, which is 3.10 below the entry and 1.60 below the stop.
```

A gap does not have to come from news, but news is the usual cause: an earnings report after the close, a rate decision, a lawsuit. If you hold through one, 1R is not your worst case. Part 16 covers trading around earnings ([Earnings trades and IV crush](../16-volatility-and-event-trading/04-earnings-trades-and-iv-crush.md)).

To control gap risk, decide the loss you would take if a gap hit the stop, as well as the loss at the stop. If you think a stock can gap 2R through your stop, then risking 1% of the account can cost 2%. Risking 0.5% makes the gap loss 1%.

### Costs in R

A cost per share \(c\) (in US$) costs \(c / (E - S)\) in R. Because the stop distance is in the denominator, the same cost hurts a tight stop more than a wide one.

For the 166 shares above, one R is US$249.00. The spread and the commission are made up to show the arithmetic (this is not a real broker's schedule). The 1.5% conversion fee is Wealthsimple's, as of 2026 (see the box below). Check your own broker's schedule.

| Cost | Calculation | In R |
|---|---|---|
| Spread of US$0.04, crossed on the way in and the way out | 0.04 x 166 = US$6.64 | 0.03R |
| A commission of US$0.005 per share with a US$1.00 minimum | 166 x 0.005 = 0.83, so the US$1.00 minimum applies each way, US$2.00 | 0.01R |
| 1.5% currency conversion on the buy and on the sell | 120.02 + 127.49 = US$247.51 | 0.99R |

The spread and the commission together cost 0.03R per trade, small beside a 2R gain. The currency fee is large: bought in a CAD account that pays it both ways, the +2R trade from lesson 2 makes 498.00 - 247.51 = US$250.49, which is +1.01R. The fee is 1.5% of the position value on each side. It is the reason Part 2 asks whether to hold USD ([USD or CAD, and currency conversion fees](../02-accounts-currency-and-taxes/03-usd-vs-cad-and-fx-fees.md)).

Costs also come off expectancy. If a strategy has +0.315R per trade before costs (lesson 3) and costs 0.035R per trade, the net is 0.28R. A strategy with an expectancy of 0.05R before costs and 0.06R of costs loses money after them.

<div class="canada" markdown>

### For Canadians

Wealthsimple lists a US$0 commission on US and Canadian listed securities, and a 1.5% currency conversion fee on US-listed trades in a CAD account, as of 2026 ([Wealthsimple trade fees](https://www.wealthsimple.com/legal/fees/trade)). The page says the fee is built into the exchange rate on each filled order, so it applies on the buy and on the sell, and that there is no conversion fee when you trade US-listed securities from a USD account. Fees change, so check the current fee before you rely on the numbers. If you hold USD, you pay a conversion fee only when you move money between currencies, not on every trade.

</div>

## Common mistakes

- Treating -1R as the worst case. A stop can fill worse, and a gap can fill much worse.
- Ignoring costs on tight-stop, short-term trades. A cost of US$0.04 on a US$0.40 stop is 0.1R on every trade.
- Using the stop price in the journal when the fill was lower. Record the real fill, or the R-multiples will look better than they were.

## Try it

1\. A stop at US$46.70 fills at US$46.20 on a position bought at US$48.20 with 166 shares. What are the loss in dollars and the result in R?

<details class="solution" markdown>
<summary>Answer</summary>

Loss = (48.20 - 46.20) x 166 = US$332.00. In R: 2.00 / 1.50 = -1.33R.

</details>

2\. You buy Stock B at US$20.00 with a stop at US$19.00 and 250 shares. It gaps down and opens at US$17.60. What is the loss, in dollars and in R?

<details class="solution" markdown>
<summary>Answer</summary>

Loss = (20.00 - 17.60) x 250 = US$600.00. One R = 250 x 1.00 = US$250.00. In R: 2.40 / 1.00 = -2.40R.

</details>

3\. A trade has a stop 0.50 away and costs US$0.04 per share in spread and commission combined. What does it cost in R? What if the stop is 2.00 away?

<details class="solution" markdown>
<summary>Answer</summary>

0.04 / 0.50 = 0.08R. At a stop 2.00 away: 0.04 / 2.00 = 0.02R. The tight stop pays four times the cost in R.

</details>

4\. You expect a gap through the stop of up to 2.5R on an earnings day, and you will accept a worst-case loss of 1.5% of the account. What fraction of the account do you risk at the stop?

<details class="solution" markdown>
<summary>Answer</summary>

Risk at the stop = 1.5% / 2.5 = 0.6% of the account. A 2.5R gap then costs 0.6% x 2.5 = 1.5%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Find the last three fills of a stop order in your broker's history, or any three trades. For each, write the planned price and the real fill, and compute the slippage in R. Add the real fills to your [trade journal](../practice/trade-journal.md) if you keep one. |
| 3 | Look up your broker's fee page. Write the commission and the currency fee for your account, and compute the cost of one round trip of 100 shares in R. |
| 3 | Pick one chart from [chart drills](../practice/chart-drills.md) with a gap. Compute how many R a stop 2% below the prior close would have lost. |

</div>

## Key terms

- **Slippage**: the difference between the price you expected and the price you got.
- **Gap risk**: the chance that the price jumps through your stop, so the loss is more than 1R.
- **Cost in R**: a cost per share divided by the risk per share.
- **Round trip**: a buy and the sell that closes it, with the costs of both.

Next: [Portfolio heat and correlation](07-portfolio-heat-and-correlation.md)
