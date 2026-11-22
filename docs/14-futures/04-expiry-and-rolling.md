# Expiry and rolling

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">FUT</span>

After this lesson you can find a contract's expiry, move a position to the next contract, shift your levels across the gap, and read a continuous chart.

Before this: [Index futures: ES, MES, NQ and MNQ](03-index-futures.md), [Gaps](../05-reading-charts/10-gaps.md). You need: a calculator.

## The idea

A stock has no end date. A futures contract does. Index futures trade in a **quarterly cycle**: March, June, September and December, with the month letters H, M, U and Z. At any time several contracts trade at once, each with its own price. The one that expires first is the **front month**, and the next is the second month.

Index futures are cash settled, and they stop trading on the third Friday of the contract month, with the final settlement based on the index's opening prices that morning (CME Group sets the exact rule in each contract's specs, as of 2026). For the September 2026 contract (MESU6 or ESU6) the third Friday is September 18, 2026.

If you want to keep a position past expiry, you cannot. You close the position in the expiring contract and open the same position in the next one. This is called **rolling**.

## The roll

Volume does not move on the expiry date. It moves to the next contract in the week before, and the expiring contract becomes thin, with wider spreads. A trader who rolls late trades in a poor market. Look at volume by contract on your platform and roll when the next contract has more.

There are two ways to roll.

1. Two separate trades: sell the old contract and buy the new one. Each leg pays a bid-ask spread and a fee.
2. A **calendar spread** order, one order that sells one month and buys another at a quoted price difference. The exchange lists these spreads as their own market, and they tend to cost less than two legs because the spread market is tight.

The new contract has a different price. The difference is not a profit or a loss. It is the carry priced into the later contract, which lesson 5 explains ([Contango, backwardation and basis](05-contango-backwardation-and-basis.md)). What the roll does cost is two sets of fees and the spread you cross.

<div class="example" markdown>

### Worked example: rolling 3 contracts

You bought 3 September contracts on the made-up MXF at 5,900.00. On Thursday, September 10, 2026, eight days before expiry, the September contract closes at 6,010.00. The December contract opens the next morning at 6,050.51, a gap of 40.51 points (0.67% of 6,010.00). The multiplier is US$5.

1. Close the old position: sell 3 September at 6,010.00. P&L = (6,010.00 - 5,900.00) x 5 x 3 = US$1,650.00. This is a real gain, realised on the close.
2. Open the new position: buy 3 December at 6,050.51. The December contract is priced 40.51 points higher, and you did not lose that.
3. Shift your levels. An old stop at 5,980.00 on September is the same distance below the new price: 5,980.00 + 40.51 = 6,020.51 on December.
4. Check the risk: from 6,050.51 to 6,020.51 is 30.00 points = 120 ticks, the same 30.00 points as 6,010.00 to 5,980.00.

If you copy a stop of 5,980.00 onto December unchanged, it is 70.51 points away, more than twice the intended distance.

</div>

## Continuous charts and back-adjustment

A chart of one contract ends at its expiry. A **continuous contract** chart joins the front month contracts into one long series. It stitches at each roll, and the stitch leaves a price gap. The chart shows the gap between the September close of 6,010.00 and the December open of 6,050.51.

```chart
data: 14-futures/mxf-roll-daily.json
title: MXF (made-up micro index future), daily: an unadjusted continuous chart
level: 6010.00 | September close, last day
marker: 2026-09-10 | above | Last September bar
marker: 2026-09-11 | below | First December bar
range: 2026-07-06 to 2026-09-24
caption: The roll on September 10 and 11 leaves a 40.51-point gap that no trade crossed.
```

That gap is not a move in the market. An unadjusted chart shows it as a jump, and indicators treat it as real: a gap shows in a 14-day average true range, in a percentage return, in a moving average. **Back-adjustment** removes the gap by changing the older prices.

- Difference method: add 40.51 to every price before the roll. The September 10 close of 6,010.00 becomes 6,050.51, and the chart is continuous. Older prices are no longer the prices that traded.
- Ratio method: multiply every older price by 6,050.51 / 6,010.00 = 1.00674. This keeps percentage moves right, which matters for returns and volatility. An old price of 5,900.00 becomes 5,939.77.

Both methods make the latest price real and change the history. A back-adjusted level drawn from last week will not match the price printed on that day. Never trade a level read off an adjusted chart without checking the live contract. Data vendors and platforms differ on method, so find the setting for your own platform.

<div class="canada" markdown>

### For Canadians

The Montreal Exchange's S&P/TSX 60 futures also roll on a quarterly cycle (March, June, September and December), with final settlement on the third Friday of the contract month, as of 2026 ([Montreal Exchange, SXF](https://www.m-x.ca/en/markets/index-derivatives/sxf)). The same steps apply. Lesson 7 covers the product ([Futures in Canada](07-futures-in-canada.md)).

</div>

## Common mistakes

- Holding to the last day. The expiring contract is thin and your broker may close it for you.
- Copying levels across the roll without the spread. A stop or target needs the gap added or removed.
- Reading a gap on a continuous chart as a trade signal. It is the stitch.

## Try it

1\. What is the third Friday of December 2026, the expiry of the December contract?

<details class="solution" markdown>
<summary>Answer</summary>

December 1, 2026 is a Tuesday. The Fridays are December 4, 11 and 18, so the third Friday is December 18, 2026.

</details>

2\. You hold 2 September contracts. The September price is 6,010.00 and December is 6,050.51. Your target on September is 6,040.00. What is the equivalent December target?

<details class="solution" markdown>
<summary>Answer</summary>

6,040.00 + (6,050.51 - 6,010.00) = 6,040.00 + 40.51 = 6,080.51.

</details>

3\. The roll spread is 40.51 points on a 6,010.00 price. What is the gap as a percentage?

<details class="solution" markdown>
<summary>Answer</summary>

40.51 / 6,010.00 = 0.00674, so 0.67% (rounded to two decimals).

</details>

4\. Using the ratio method, what does an old close of 5,950.00 become?

<details class="solution" markdown>
<summary>Answer</summary>

5,950.00 x 1.006741 = 5,990.11 (using the ratio 6,050.51 / 6,010.00 = 1.006741).

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | On your platform, open the next two index contracts (for example MES September and December). Write both prices and the spread, and which has more volume. |
| 5 | Find your platform's continuous contract setting. Write whether it back-adjusts and by which method. |

</div>

## Key terms

- **Quarterly cycle**: expiry months of March, June, September and December.
- **Front month**: the contract that expires first.
- **Roll**: closing a position in one contract and opening it in the next.
- **Calendar spread**: one order that buys one expiry month and sells another.
- **Continuous contract**: a chart that joins successive contracts into one series.
- **Back-adjustment**: changing older prices on a continuous chart to remove the gaps at rolls.

Next: [Contango, backwardation and basis](05-contango-backwardation-and-basis.md)
