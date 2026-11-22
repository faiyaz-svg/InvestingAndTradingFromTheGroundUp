# How day trading differs

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">DAY</span>

After this lesson you can say what changes when every trade is opened and closed the same day: the stop distance, the position size, the costs in R and the shape of the trading day.

Before this: [Market hours and the opening and closing auctions](../01-how-markets-work/03-market-hours-and-auctions.md), [Position sizing with fixed fractional risk](../03-risk-and-position-sizing/04-fixed-fractional-sizing.md) and [Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md). You need: a calculator.

## The idea

**Day trading** means opening and closing each position within one trading day, so you hold nothing overnight. The chart you read is **intraday**: 1-minute, 5-minute or 15-minute bars instead of daily bars. Everything from Part 3 still applies: risk a fixed fraction, set the stop first, count results in R. What changes is the scale.

Take a US$25,000 account that risks 1% (US$250) per trade. Stock A trades at US$50, and a round trip costs US$0.05 per share in spread, commission and slippage (a made-up figure, see lesson 8).

| | Swing trade | Day trade |
|---|---|---|
| Stop distance | US$2.00 (4%) | US$0.60 (1.2%) |
| Shares for US$250 risk | 125 | 416 |
| Position value | US$6,250 | US$20,800 |
| Cost in R (0.05 / stop distance) | 0.025R | 0.083R |

A tighter stop gives a bigger position, and the same cost per share is a bigger part of 1R. A day trader has two new limits to watch: how much money the position needs, and how much of each R the costs eat.

## How it works

### What you give up and what you get

You avoid the overnight gap from Part 3 ([Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md)). A position held at 4:00 p.m. ET can open the next morning far from its close, and a day trade never faces that. You still face gaps inside the day: a news release, a halt, or a thin moment when a stop fills far from its price (lessons 6 and 7).

You also gain many more decisions per week and give up time. A day trade needs your attention while it is open. The busy part of the day is the first two hours after 9:30 a.m. ET, which is 9:30 a.m. in Toronto too. If you cannot sit at a screen then, swing trading fits a 30-minute day better (see [What swing trading is](../07-swing-trading/01-what-swing-trading-is.md)).

### The rhythm of the day

Volume and movement are not spread evenly. Look at the volume panel in the chart: tall bars in the first hour, short bars in the middle, taller bars again late.

```chart
data: 08-day-trading/day-rhythm.json
title: Stock A, 5-minute: the shape of a trading day
show: volume
level: 52.07 | High of the day
level: 49.71 | Low of the day
range: 2026-09-15 09:30 to 2026-09-15 15:55
caption: The first 30 minutes hold 14.5% of the day's volume, 12:00 to 12:30 holds 5.1%, and the last 30 minutes hold 12.6%.
```

| Time (ET) | What usually happens | What it means for you |
|---|---|---|
| 9:30 to 10:30 a.m. | The open: the most volume, the widest bars, news reacts | Most setups in this part happen here (lessons 4 to 6) |
| 10:30 a.m. to 11:30 a.m. | Moves settle into a trend or a range | Reclaims and fades appear (lesson 5) |
| 11:30 a.m. to 2:00 p.m. | Midday: low volume, narrow ranges | Fewer clean setups, wider relative costs |
| 2:00 p.m. to 3:30 p.m. | Volume returns | Trends can resume or break |
| 3:30 p.m. to 4:00 p.m. | The close: orders for the closing auction arrive | NYSE closing-auction orders are due by 3:50 p.m. ([NYSE auctions](https://www.nyse.com/trade/auctions), as of 2026) |

In the chart, the first six bars average 194,583 shares each, and the six bars from 12:00 to 12:25 average 67,967. That is 2.9 times as many shares per bar at the open. The same volume pattern appears in the opening gap chart of Part 1 ([Market hours and the opening and closing auctions](../01-how-markets-work/03-market-hours-and-auctions.md)).

### What tests found about the intraday pattern

Gao, Han, Li and Zhou studied high-frequency data on the S&P 500 ETF from 1993 to 2013 and found that the return in the first half-hour of the day, measured from the previous close, predicts the return in the last half-hour. The effect was stronger on days of high volatility and high volume (*Market intraday momentum*, Journal of Financial Economics, 2018, volume 129, pages 394 to 414; [record on EconPapers](https://econpapers.repec.org/RePEc:eee:jfinec:v:129:y:2018:i:2:p:394-414)). The abstract does not give the size of the effect. Read it as an average tilt over thousands of days, not a rule for one day. The result is about an index fund, so it does not say your stock will follow its first half-hour.

<div class="example" markdown>

### Worked example: the same risk, two holding times

The account is US$25,000 and the risk is 1%, so 1R is US$250.

1. Swing: stop 2.00 below the entry. Shares = 250 / 2.00 = 125. Position = 125 x 50 = US$6,250. Cost = 0.05 / 2.00 = 0.025R.
2. Day: stop 0.60 below the entry. Shares = 250 / 0.60 = 416.7, so 416 shares (round down). Position = 416 x 50 = US$20,800. Cost = 0.05 / 0.60 = 0.083R.
3. The day trade needs US$20,800 of buying power against US$25,000 of cash. With a stop of 0.40 the position would be 625 x 50 = US$31,250, more than the cash in the account.

When the risk-based size is larger than your buying power, the buying power sets the size, and your actual risk is below 1R. Lesson 9 turns this into a rule.

</div>

<div class="canada" markdown>

### For Canadians

Two Canadian points matter before you start. First, the CRA treats frequent, short-term trading as a fact-based question of capital gains or business income, and day trading points toward business income ([Capital gains or business income](../02-accounts-currency-and-taxes/07-capital-gains-vs-business-income.md)). Talk to an accountant before you day trade in volume. Second, the US pattern day trader rule and its 2026 replacement are explained in [Settlement, cash accounts and margin](../01-how-markets-work/07-settlement-cash-and-margin.md). Canadian brokers follow CIRO margin rules, covered in [Margin rules in Canada](../02-accounts-currency-and-taxes/10-margin-rules-in-canada.md) (see its day trading section). Read your broker's day-trading page.

</div>

## Common mistakes

- Using the swing stop size on an intraday chart. A 4% stop is too wide for a trade you plan to close in two hours, and the position it allows is too small to matter.
- Sizing from risk and forgetting buying power. The order may be rejected, or you may end the day with less risk than planned.
- Trading the midday hours because the screen is open. Fewer setups appear then, and each costs the same fees.

## Try it

1\. Stock A trades at US$30, your account is US$20,000, and you risk 1%. The stop is US$0.50 away. How many shares, and what is the position value?

<details class="solution" markdown>
<summary>Answer</summary>

Risk = US$200. Shares = 200 / 0.50 = 400. Position = 400 x 30 = US$12,000.

</details>

2\. A round trip costs US$0.04 per share. What is the cost in R for a stop 0.40 away, and for a stop 2.00 away?

<details class="solution" markdown>
<summary>Answer</summary>

0.04 / 0.40 = 0.10R. 0.04 / 2.00 = 0.02R.

</details>

3\. From the chart, the first 30 minutes hold 14.5% of the day's volume and the last 30 minutes hold 12.6%. How many times the share of a fair even split (30 / 390 of the day) is the first 30 minutes?

<details class="solution" markdown>
<summary>Answer</summary>

An even split gives 30 / 390 = 7.7%. 14.5 / 7.7 = 1.9 times.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Open a 5-minute chart of any stock and mark the 9:30, 12:00 and 3:30 p.m. volume bars. Write the ratio of the first to the second. |
| 3 | Write the position value for a day trade in your account with a stop of 1% of the price. Compare it with your buying power. |
| 2 | Look at [chart drills](../practice/chart-drills.md) and note which time of day the intraday charts start. |

</div>

## Key terms

- **Day trading**: opening and closing every position within one trading day.
- **Intraday**: within a single trading day, usually 1-minute to 15-minute bars.
- **The open**: the first hour of the regular session, from 9:30 a.m. ET, with the most volume.
- **Midday**: the quiet part of the session, roughly 11:30 a.m. to 2:00 p.m. ET.
- **The close**: the last half-hour before the 4:00 p.m. ET closing auction.
- **Buying power**: the amount of stock your broker lets you hold, set by your cash and margin.

Next: [Premarket prep](02-premarket-prep.md)
