# FOMC, CPI and other data days

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">VOL</span>

After this lesson you can write a plan for a scheduled data release or an FOMC decision, choose between standing aside and trading the release, size a post-release trade with the wider spread and stop slippage in the numbers, and say what the research found about the hours before an FOMC statement.

Before this: [The economic calendar](../11-macro-and-economic-data/07-the-economic-calendar.md), [How markets react to data](../11-macro-and-economic-data/08-how-markets-react-to-data.md), [Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md), [Index futures](../14-futures/03-index-futures.md). You need: a calculator.

## The idea

At 1:55 p.m. ET on October 28, 2026 (a made-up day), Index X has traded in a 13-point range for four hours. Its average 5-minute bar over the morning was 3.1 points tall. At 2:00 p.m. the Federal Reserve's statement is due. The next 5-minute bar is 25.0 points tall, eight times the morning average, and the one after it is 34.1 points.

That is **scheduled event risk**: you know the minute the news arrives, but not its size or direction. Part 11 lists the release times ([The economic calendar](../11-macro-and-economic-data/07-the-economic-calendar.md)): BLS data such as CPI and the jobs report at 8:30 a.m. ET, and the FOMC statement at 2:00 p.m. ET (sources there, as of 2026). A plan fixes the decision before the minute.

## How it works

### What the chart shows

The chart is made-up Index X on 5-minute bars. Look at the 2:00 p.m. bar: it rises to 5,025.53, then the next bar reverses through the whole morning range and falls to 4,947.74 by the late afternoon.

```chart
data: 16-volatility-and-event-trading/index-x-fomc-5m.json
title: Index X, 5-minute: a spike and a reversal at the 2:00 p.m. statement
show: volume
marker: 2026-10-28 14:00 | above | Statement
level: 5000.51 | Low of the 2:00 p.m. bar
level: 5025.53 | High of the 2:00 p.m. bar
range: 2026-10-28 09:30 to 2026-10-28 15:55
caption: The 2:00 p.m. bar ran from 5,000.51 to 5,025.53 and closed at 5,022.53. The next bar fell to 4,991.39, and the index closed the day at 4,962.00.
```

The first move did not hold. This happens often enough that many traders let the first bar or two pass. Part 11 says the same: the first move can reverse as traders read the details ([How markets react to data](../11-macro-and-economic-data/08-how-markets-react-to-data.md)).

### Three plans

1. Stand aside. Close or shrink positions before the release and place no new trade until a fixed time, such as 15 minutes after it. The cost is the move you miss.
2. Hold through it. Keep your position and accept the gap risk. A stop does not protect you in a jump: it becomes a market order after the price passes it, and the fill can be far away.
3. Trade the break. Wait for the first bar after the release to close, then trade a break of its range with the other side of the bar as the stop.

Plan 3 needs numbers for the costs that matter on these days. Spreads widen, so you pay more to get in. Stops slip, so you lose more than planned. Both belong in the size ([Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md)).

<div class="example" markdown>

### Worked example: trading the break of the 2:00 p.m. bar

The instrument is a made-up Micro Index X future worth US$5 per index point (like the MES in part 14). The account is US$25,000 and 1R is US$250.

1. The 2:00 p.m. bar has a low of 5,000.51 and a high of 5,025.53. The plan: sell on a break below 5,000.50, with a stop above the bar's high at 5,026.00.
2. The 2:05 p.m. bar trades down through 5,000.50. We assume a fill 1.50 points worse, at 4,999.00.
3. Risk = (5,026.00 - 4,999.00) = 27.00 points x US$5 = US$135 per contract. 250 / 135 = 1.85, so 1 contract, with 1R = US$135.
4. The target is 1.5R: 4,999.00 - 1.5 x 27.00 = 4,958.50. The index trades through it by 2:35 p.m. (its low that bar is 4,949.95), so the exit fills there: profit = 40.50 x 5 = US$202.50, which is 1.5R.
5. The stop did not trigger, since no later bar went above 5,026.00. If it had triggered with 3 points of slippage, the fill would be 5,029.00 and the loss (5,029.00 - 4,999.00) x 5 = US$150, or 1.11R instead of 1R.

</div>

In this made-up day the break worked. On another day the first bar's range can be tiny and the break can run the other way, so the stop above is not decoration.

### The 8:30 a.m. releases

CPI, the jobs report and similar releases land at 8:30 a.m. ET, an hour before the stock market opens at 9:30. Futures trade then, and the stocks' first reaction shows at the open, with a gap. Check before the day whether your broker's stop orders work before 9:30 ([Market hours and the opening and closing auctions](../01-how-markets-work/03-market-hours-and-auctions.md)). If they do not, a position you hold through the release has no working stop until the open.

### Options on data days

Index options price the day's event like any other. The one-day move of one standard deviation is IV divided by \( \sqrt{252} \) (a straddle price is about 0.8 of that), so compare the actual index move on the day with that figure, as in the lesson on earnings ([Earnings trades and IV crush](04-earnings-trades-and-iv-crush.md)).

## What tests found

Lucca and Moench (Journal of Finance, 2015) studied scheduled FOMC announcements since 1994 and found a large and statistically significant excess return on US stocks earned in the hours before the announcement ([paper](https://econpapers.repec.org/RePEc:bla:jfinan:v:70:y:2015:i:1:p:329-371)). That is the **pre-FOMC announcement drift**. Kurov, Wolfe and Gilbert later reported (Finance Research Letters, 2021) that the drift essentially disappeared after 2015 ([paper](https://econpapers.repec.org/RePEc:eee:finlet:v:40:y:2021:i:c:s1544612320315956)). Neither paper tests the plans above, and this book found no published test of them, so it makes no claim that they pay.

<!-- lint-ok: significant (statistical sense) -->

## In code

Measure how large the 2:00 p.m. bar is against the morning, on [index-x-fomc-5m.csv](../assets/data/index-x-fomc-5m.csv).

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

b = pd.read_csv("index-x-fomc-5m.csv")
b["range"] = b["high"] - b["low"]
morning = b["range"].iloc[:54].mean()
print(round(morning, 2), round(b["range"].iloc[54], 2), round(b["range"].iloc[54] / morning, 1))
```

</details>

## Common mistakes

- Placing a market order in the first minute after a release. Spreads are widest then.
- Sizing a release trade as if the stop will fill exactly. Add the slippage you expect to the risk.
- Deciding what to do when the number prints. Decide the night before.

## Try it

1\. A micro future is worth US$5 a point. You sell at 4,999.00 with a stop at 5,026.00. What is the risk per contract, and how many contracts fit a US$250 1R?

<details class="solution" markdown>
<summary>Answer</summary>

27.00 points x 5 = US$135. 250 / 135 = 1.85, so 1 contract.

</details>

2\. In the same trade, the stop fills 3 points worse. What is the loss in R?

<details class="solution" markdown>
<summary>Answer</summary>

(5,029.00 - 4,999.00) x 5 = US$150. 150 / 135 = 1.11R.

</details>

3\. The morning bars average 3.06 points and the 2:00 p.m. bar is 25.02. How many times larger is it?

<details class="solution" markdown>
<summary>Answer</summary>

25.02 / 3.06 = 8.2 times.

</details>

4\. A release is at 8:30 a.m. ET and you hold a stock position with a stop that works only from 9:30. How long is the position without a working stop?

<details class="solution" markdown>
<summary>Answer</summary>

60 minutes, from 8:30 to 9:30 a.m.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | On the economic calendar, mark the next 8:30 a.m. release and the next FOMC statement. Write the time in ET. |
| 4 | For one of them, write your plan (stand aside, hold or trade the break) in three lines, with the size. |
| 2 | Open [chart drills](../practice/chart-drills.md) and answer the data release items. |

</div>

## Key terms

- **Scheduled event risk**: price risk from news whose time is known in advance, such as a data release or an FOMC statement.
- **Pre-FOMC announcement drift**: the excess stock return found in the hours before scheduled FOMC announcements.
- **Trading the break**: entering after a release when price breaks the range of the first bar, with the other end of the bar as the stop.

Next: [Opex, gamma and index rebalances](06-opex-gamma-and-index-rebalances.md)
