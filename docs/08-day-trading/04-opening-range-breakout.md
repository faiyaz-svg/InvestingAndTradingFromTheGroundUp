# The opening range breakout

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">DAY</span>

After this lesson you can write the exact rules of a 5-minute opening range breakout, size one from the range, work out its result in R after costs, and say when it fails and what a published test found.

Before this: [Premarket prep](02-premarket-prep.md), [Intraday charts and VWAP](03-intraday-charts-and-vwap.md) and [Order types](../01-how-markets-work/05-order-types.md). You need: a calculator.

## The idea

At 9:30 a.m. ET the open absorbs the overnight news and orders (Part 1, [Market hours and the opening and closing auctions](../01-how-markets-work/03-market-hours-and-auctions.md)). The first few minutes set a high and a low. The **opening range** is the high and low of the first bars of the session. An **opening range breakout** (ORB) buys when price trades above the range, or sells short when it trades below, on the idea that a move out of the first range shows that one side has won the open.

## How it works

The rules below are this book's version. Every number marked "made up" is a starting value to test on paper, not a tested optimum.

1. **Pick a stock in play** (lesson 2): a gap, a catalyst and relative volume of at least 2 in the first five minutes (made up).
2. **The range** is the high and low of the first 5-minute bar, 9:30 to 9:35 a.m.
3. **The direction** follows that bar. If it closes above its open, look only for a long. If it closes below its open, look only for a short.
4. **The trigger**: a buy stop one cent above the range high (a sell stop one cent below the range low for a short). Place it after 9:35 a.m. Cancel it if it has not filled by 10:30 a.m. (made up).
5. **The stop**: two cents beyond the other side of the range, so below the range low for a long.
6. **The size**: risk 1% of the account. Risk per share is the trigger minus the stop. Shares = risk amount / risk per share, rounded down (Part 3, [Position sizing with fixed fractional risk](../03-risk-and-position-sizing/04-fixed-fractional-sizing.md)). The position value must fit your buying power.
7. **The target**: a limit order at 2R. Exit at 3:55 p.m. ET if neither the target nor the stop has filled.
8. **Skip** the trade if there is a level (the premarket high, the prior-day high) less than 2R away. Lesson 2 defines the room.

<div class="example" markdown>

### Worked example: a winning breakout

Stock A gapped up 6.0% on a raised forecast (prior close US$40.00, made up). The account is US$25,000, so 1R is US$250.

1. The first 5-minute bar on September 18, 2026: open 42.40, high 42.90, low 42.30, close 42.80. It closed above its open, so only a long is allowed. The range is 42.30 to 42.90.
2. Buy stop at 42.91. Stop at 42.30 - 0.02 = 42.28. Risk per share = 42.91 - 42.28 = US$0.63.
3. Shares = 250 / 0.63 = 396.8, so 396. One R is 396 x 0.63 = US$249.48. The position is 396 x 42.91 = US$16,992.36.
4. Target at 2R: 42.91 + 2 x 0.63 = US$44.17.
5. The 9:55 a.m. bar trades up to 43.40, so the buy stop fills at 42.91. The price reaches 44.17 in the 11:05 a.m. bar, and the stop at 42.28 is never touched.
6. Fees, with a made-up schedule of US$0.005 per share per side: 396 x 0.005 = 1.98 each way, 3.96 total.
7. Gross gain = 396 x 1.26 = US$498.96. Net = 498.96 - 3.96 = US$495.00. In R: 495.00 / 249.48 = +1.98R.

</div>

```chart
data: 08-day-trading/orb-win.json
title: Stock A, 5-minute: an opening range breakout that reaches 2R
show: volume
level: 42.90 | Range high 42.90
level: 42.30 | Range low 42.30
level: 42.28 | Stop 42.28
level: 44.17 | Target 44.17
marker: 2026-09-18 09:55 | below | Buy stop 42.91 fills
range: 2026-09-18 09:30 to 2026-09-18 15:55
caption: The range was 42.30 to 42.90. The entry filled in the 9:55 bar and the target at 44.17 was reached in the 11:05 bar.
```

<div class="example" markdown>

### Worked example: a failed breakout

Another day, another made-up stock. Stock B's first bar on September 21, 2026: open 30.60, high 31.00, low 30.55, close 30.95. The account is US$25,000.

1. Buy stop at 31.01, stop at 30.55 - 0.02 = 30.53. Risk per share = 0.48. Shares = 250 / 0.48 = 520.8, so 520. One R is 520 x 0.48 = US$249.60.
2. The 9:50 a.m. bar trades up to 31.12 and fills the entry, then closes at 30.90, below the entry.
3. The price drifts down. The 10:15 a.m. bar trades as low as 30.37, through the stop at 30.53. The stop order becomes a market order and fills at 30.50 (assumed, 3 cents of slippage).
4. Loss per share = 31.01 - 30.50 = 0.51. Loss = 520 x 0.51 = US$265.20. Fees = 2 x 520 x 0.005 = US$5.20. Total = US$270.40.
5. In R: -270.40 / 249.60 = -1.08R.

</div>

The 0.08R beyond the planned loss is the cost of the fill and the fees (Part 3, [Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md)).

```chart
data: 08-day-trading/orb-fail.json
title: Stock B, 5-minute: a breakout that fails
level: 31.00 | Range high 31.00
level: 30.55 | Range low 30.55
level: 30.53 | Stop 30.53
marker: 2026-09-21 09:50 | above | Buy stop 31.01 fills
marker: 2026-09-21 10:15 | below | Stop is hit
range: 2026-09-21 09:30 to 2026-09-21 15:55
caption: The bar that broke the range closed back inside it, and the 10:15 bar fell through the stop.
```

### When it fails

A breakout fails when the range is a pause, not a decision. Signs: a wide first bar (the stop is far and the size small), a first bar on ordinary volume, a trigger bar that closes back inside the range, and a level close above the trigger. Lesson 9 limits the number of attempts per day.

### What tests found

Zarattini, Barbon and Aziz tested the 5-minute opening range breakout on more than 7,000 US stocks from 2016 to 2023 (*A Profitable Day Trading Strategy For The U.S. Equity Market*, Swiss Finance Institute Research Paper 24-98, February 2024; [SSRN 4729284](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4729284)). They found that restricting trades to "Stocks in Play", stocks with unusually high activity on the day (usually from company news), improved results after transaction costs. For a portfolio of the 20 most active names each day they report a Sharpe ratio of 2.81 and an annualized alpha of 36%. They also test 15, 30 and 60-minute ranges ([abstract on RePEc](https://ideas.repec.org/p/chf/rpseri/rp2498.html)).

Read this result with care. It is a working paper, only its abstract could be confirmed for this book, and it is one backtest of one rule set. Its stops, exits and sizing may differ from the rules above, so its numbers are not the expected result of this lesson. A backtest does not show how your own fills compare. Paper block 3 in lesson 9 tests that for you.

## In code

The code finds the opening range and the first breakout in the 5-minute file. Download [stock-a-orb-5m.csv](../assets/data/stock-a-orb-5m.csv).

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

bars = pd.read_csv("stock-a-orb-5m.csv", parse_dates=["datetime"]).set_index("datetime")
first = bars.iloc[0]
trigger = round(first["high"] + 0.01, 2)
stop = round(first["low"] - 0.02, 2)
risk = round(trigger - stop, 2)
shares = int(250 / risk)
hit = bars.iloc[1:][bars.iloc[1:]["high"] >= trigger].index[0]
print("range", first["low"], first["high"])
print("trigger", trigger, "stop", stop, "risk", risk, "shares", shares)
print("entry bar", hit.strftime("%H:%M"))
```

</details>

## Common mistakes

- Taking both directions. The first bar's colour picks the side, and a short on a green first bar is a different trade.
- Moving the stop to "give it room" after the entry. The size was computed from the stop, so a wider stop breaks the 1R.
- Entering on the first touch of a level in the first minute with no rule for the bar. Use the 5-minute bar and the buy stop.

## Try it

1\. The first 5-minute bar of a stock is open 18.50, high 18.90, low 18.40, close 18.85. Account US$20,000, risk 1%. Give the direction, trigger, stop, shares and 2R target.

<details class="solution" markdown>
<summary>Answer</summary>

The bar closed above its open, so long. Trigger 18.91. Stop 18.40 - 0.02 = 18.38. Risk = 0.53. Risk amount = US$200. Shares = 200 / 0.53 = 377.4, so 377. Target = 18.91 + 1.06 = US$19.97.

</details>

2\. The first bar is open 25.55, high 25.60, low 25.10, close 25.15. Account US$25,000. Give the direction, trigger, stop, shares and target.

<details class="solution" markdown>
<summary>Answer</summary>

The bar closed below its open, so short. Trigger (sell stop) 25.09. Stop 25.60 + 0.02 = 25.62. Risk = 0.53. Shares = 250 / 0.53 = 471.7, so 471. Target = 25.09 - 1.06 = US$24.03.

</details>

3\. In the failed trade above, the stop filled at 30.45 instead of 30.50. What is the loss in R before fees?

<details class="solution" markdown>
<summary>Answer</summary>

Loss = (31.01 - 30.45) x 520 = US$291.20. In R: 291.20 / 249.60 = -1.17R.

</details>

4\. The winning trade's costs were 3.96. How much better would the result in R be with no fees?

<details class="solution" markdown>
<summary>Answer</summary>

498.96 / 249.48 = +2.00R, against +1.98R with fees. The fees cost 0.02R here, because the stop was 0.63 away.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Do the opening-range items in [chart drills](../practice/chart-drills.md): click the range high and low, then name the stop. |
| 5 | On a 5-minute chart of any stock from this morning, mark the first bar's range and write the trigger, stop, size and target you would have used. |

</div>

## Key terms

- **Opening range**: the high and low of the first bar or bars of the session.
- **Opening range breakout (ORB)**: a trade that enters when price leaves the opening range.
- **Trigger**: the price at which an entry order activates.
- **Stocks in Play**: stocks with unusually high trading activity on the day, usually from news.

Next: [VWAP reclaims and fades](05-vwap-reclaims-and-fades.md)
