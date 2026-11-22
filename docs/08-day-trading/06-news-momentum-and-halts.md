# News, momentum and halts

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">DAY</span>

After this lesson you can trade the first pullback after a news-driven surge with a written stop and size, work out the price bands that pause a stock, and say what the short sale restriction after a 10% fall changes for a short seller.

Before this: [Premarket prep](02-premarket-prep.md), [The opening range breakout](04-opening-range-breakout.md) and [Market hours and the opening and closing auctions](../01-how-markets-work/03-market-hours-and-auctions.md). You need: a calculator.

## The idea

When a company reports news that changes what its shares are worth, the price jumps and volume jumps with it. Stock A closed at US$12.00 on September 23, 2026 and opened the next morning at US$13.80, up 15.0%, on a deal announcement (made up). Over the first five minutes it ran to US$14.75, then fell back to US$13.98 before buyers returned.

**News momentum** trading looks for the continuation after the first rush: wait for a pullback, buy when the price takes out the high of the first surge, and put the stop under the pullback. The setup trades a stock in a state where the usual rules are stretched: spreads are wide, prices jump, and exchanges can stop trading in the name.

## How it works

### The first-pullback rules

1. The stock is in play with a catalyst you can name and relative volume of at least 5 in the first minutes (made up). Use 1-minute bars.
2. Mark the **first push**: the high of the first surge, which is 14.75 at 9:34 a.m.
3. Wait for a pullback from the first push that holds above the open. Mark its low, 13.98 at 9:40 a.m.
4. Entry: a buy stop one cent above the first push, 14.76.
5. Stop: two cents below the pullback low, 13.96.
6. Size: 1% of the account over the risk per share, rounded down.
7. Target: 2R. Skip the trade if the price is already at the target level before you can enter.

<div class="example" markdown>

### Worked example: the first pullback

Account US$25,000, 1R = US$250.

1. Risk per share = 14.76 - 13.96 = US$0.80.
2. Shares = 250 / 0.80 = 312.5, so 312. One R is 312 x 0.80 = US$249.60. Position = 312 x 14.76 = US$4,605.12.
3. The 9:44 a.m. bar trades up to 14.87, so the buy stop fills at 14.76. The target is 14.76 + 1.60 = US$16.36, reached in the 9:51 a.m. bar (high 16.53). The stop is never touched.
4. Gross gain = 312 x 1.60 = US$499.20. Fees at US$0.005 per share per side (made up) = 3.12. Net = US$496.08, which is +1.99R.
5. Costs are higher in stocks like this. If the entry and the exit each slip 0.05, the cost is 0.10 x 312 = US$31.20 more, and the net is 499.20 - 3.12 - 31.20 = US$464.88, which is +1.86R.

</div>

Look at the surge, the pullback with its low at 13.98, and the second push.

```chart
data: 08-day-trading/news-momentum.json
title: Stock A, 1-minute: a news surge and its first pullback
show: vwap, volume
level: 14.75 | First push 14.75
level: 13.98 | Pullback low 13.98
level: 16.36 | Target 16.36
marker: 2026-09-24 09:44 | below | Buy stop 14.76 fills
range: 2026-09-24 09:30 to 2026-09-24 10:29
caption: The stock opened at 13.80, ran to 14.75, pulled back to 13.98 and then broke the first high.
```

### Halts: LULD

Under the **limit up-limit down** plan (LULD), each stock has a price band around a reference price set from recent trading. When the stock trades at a band's edge and stays there for 15 seconds, trading is paused for five minutes, and the listing exchange can extend it by five more on a large buy and sell imbalance. For stocks priced above US$3.00 the band is 5% for Tier 1 (the S&P 500, the Russell 1000 and some exchange-traded products) and 10% for other stocks. From 3:35 to 4:00 p.m. ET the bands double for Tier 1 and for Tier 2 stocks at or below US$3.00 ([FINRA, guardrails for market volatility](https://www.finra.org/investors/insights/guardrails-market-volatility), as of 2026; see also the [Nasdaq LULD FAQ](https://m.nasdaqtrader.com/content/MarketRegulation/LULD_FAQ.pdf)). Exchanges can also halt a stock to let the market absorb important news, which is common in news momentum names.

Part 1 introduced the pause ([Market hours and the opening and closing auctions](../01-how-markets-work/03-market-hours-and-auctions.md)). The new point for a day trader is that **you cannot exit during a halt**, and a stop order does not fire while the stock is paused. When trading resumes, the first price can be far outside your stop.

<div class="example" markdown>

### Worked example: a band and a gap through a stop

Stock A (not in the S&P 500 or the Russell 1000, so Tier 2) is above US$3.00, with a reference price of US$14.00.

1. Band = 10% of 14.00 = 1.40, so the band runs from US$12.60 to US$15.40.
2. If the price sits at 15.40 for 15 seconds, trading pauses for five minutes.
3. You hold 312 shares from 14.76 with a stop at 13.96. The stock is paused at 14.40 and reopens at 13.40. Your stop becomes a market order and fills near 13.40.
4. Loss = (14.76 - 13.40) x 312 = US$424.32, which is 424.32 / 249.60 = -1.70R.

</div>

### Rule 201: the short sale restriction

**Rule 201** of Regulation SHO, the alternative uptick rule, is a short sale circuit breaker. A stock that falls 10% or more from the prior day's close triggers it. For the rest of that day and the whole next day, short sales may not be executed or displayed at or below the national best bid, so a short seller must sell above the bid, not into it. A short sale above the best bid is allowed, and some exceptions exist ([SEC Regulation SHO](https://www.sec.gov/investor/pubs/regsho.htm); rule text at [17 CFR 242.201](https://www.law.cornell.edu/cfr/text/17/242.201), as of 2026).

The effect is on your entry. Stock B closed at US$20.00, so the trigger is 20.00 x 0.90 = US$18.00. If it trades at 18.00 or below, the restriction starts. With the bid at 17.80 and the ask at 17.84, a short sale at 17.80 is not allowed, and one at 17.81 is. A short seller joins the offer and waits to be bought from, so a quick short at the bid is no longer possible.

### What tests found

No published test of the first-pullback rule itself was found for this book. The ORB paper in lesson 4 found that stocks with unusually high activity, usually news-driven, gave the better breakouts after costs. That supports watching these names, not this entry. Your paper block will test the rule.

<div class="canada" markdown>

### For Canadians

Rule 201 and LULD apply to US-listed stocks, which is what you trade from Wealthsimple and IBKR Canada. Canadian-listed stocks have their own rules under CIRO. Orders in Wealthsimple's overnight session may not be price protected ([Wealthsimple extended hours](https://www.wealthsimple.com/en-ca/legal/extended-hours), as of 2026), so use limit orders for a news open.

</div>

## Common mistakes

- Buying the first spike with a market order. The spread is widest and the price is least stable in the first minute.
- Sizing as if the stop would fill. A halt can move the open price through the stop.
- Shorting a stock that has already fallen 10% and expecting to hit the bid. Rule 201 removes that option.

## Try it

1\. A news stock has a first push at 8.40, a pullback low at 7.95. Account US$20,000, risk 1%. Give the trigger, stop, shares and 2R target.

<details class="solution" markdown>
<summary>Answer</summary>

Trigger 8.41. Stop 7.93. Risk = 0.48. Risk amount = US$200. Shares = 200 / 0.48 = 416.7, so 416. Target = 8.41 + 0.96 = US$9.37.

</details>

2\. A Tier 2 stock above US$3.00 has a reference price of US$8.00. What is the LULD band?

<details class="solution" markdown>
<summary>Answer</summary>

10% of 8.00 = 0.80, so the band runs from US$7.20 to US$8.80.

</details>

3\. A stock closed at US$32.50. At what price does the Rule 201 restriction start?

<details class="solution" markdown>
<summary>Answer</summary>

A 10% fall is 3.25, so the trigger is 32.50 - 3.25 = US$29.25.

</details>

4\. You are long 200 shares from 10.00 with a stop at 9.50. The stock halts and reopens at 9.10. What is the loss in R?

<details class="solution" markdown>
<summary>Answer</summary>

Loss = (10.00 - 9.10) x 200 = US$180. One R = 0.50 x 200 = US$100. Result = -1.80R.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Find a stock with a news gap today. Mark the first push and the first pullback low on a 1-minute chart and write the trigger, stop and size. |
| 3 | Find the LULD band for a stock you watch: its tier and its price band. |
| 2 | Write in your plan what you do if a stock you hold is halted. |

</div>

## Key terms

- **News momentum**: a trade that buys the continuation after the first surge on news.
- **First push**: the high of the first surge after a news open.
- **Limit up-limit down (LULD) band**: the price range around a reference price outside which a stock is paused.
- **Trading pause**: a five-minute stop in trading after a stock stays at a band edge for 15 seconds.
- **Rule 201**: the short sale restriction after a 10% fall from the prior close.

Next: [Level 2 and time and sales](07-level-2-and-time-and-sales.md)
