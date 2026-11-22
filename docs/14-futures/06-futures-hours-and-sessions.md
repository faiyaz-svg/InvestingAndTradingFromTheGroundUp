# Futures hours and sessions

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">FUT</span>

After this lesson you can say when equity index futures trade in Eastern Time, which part overlaps the stock market, and what the daily break and the overnight session mean for your stops and your charts.

Before this: [Market hours and the opening and closing auctions](../01-how-markets-work/03-market-hours-and-auctions.md), [Index futures: ES, MES, NQ and MNQ](03-index-futures.md). You need: a calculator.

## The idea

At 8:30 a.m. ET on a jobs report morning, the US stock market is closed for another hour. A trader in Toronto who holds a stock cannot react. A trader who holds an index future can, because the future has been trading since 6 p.m. the evening before.

Futures trade on **Globex**, CME Group's electronic trading platform. Equity index futures trade nearly around the clock: from Sunday 6 p.m. ET to Friday 5 p.m. ET, with a **daily maintenance break** from 5 p.m. to 6 p.m. ET, Monday to Thursday (CME Group's trading hours page, as of 2026: [CME Group trading hours](https://www.cmegroup.com/trading-hours.html)). Wealthsimple's futures page gives the same window and a one-hour daily break ([Wealthsimple futures](https://www.wealthsimple.com/en-ca/trade/futures), as of 2026). Hours can differ by contract and on holidays, so check the page for the contract you trade.

CME quotes its hours in Central Time. Both Central and Eastern time change with daylight saving on the same dates, so the Eastern Time hours above stay the same through the year.

## The day, in one picture

The figure shows one Globex day against the stock market's regular session of 9:30 a.m. to 4 p.m. ET. Look at how much of the day lies outside the shaded session.

![A 24-hour bar from 6 p.m. to 6 p.m. ET showing the futures session, the one-hour break, and the stock market's regular session from 9:30 a.m. to 4 p.m.](../assets/figures/14-futures/day-clock-dark.svg#only-dark)
![A 24-hour bar from 6 p.m. to 6 p.m. ET showing the futures session, the one-hour break, and the stock market's regular session from 9:30 a.m. to 4 p.m.](../assets/figures/14-futures/day-clock-light.svg#only-light)

A week has 5 sessions of 23 hours: 115 hours of trading. The stock market's regular session is 5 x 6.5 = 32.5 hours, which is 28.3% of the futures week. The rest is the **overnight session** (also called extended or electronic trading hours). A futures trading day is labelled by the session that ends it: the session that opens Sunday at 6 p.m. is Monday's trading day on most platforms.

## What changes outside stock hours

Overnight, fewer traders take part, so the order book is thinner. Spreads are wider and a stop can fill further from its price ([Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md)). Three things in the overnight session matter for a Toronto trader.

1. Economic data comes out before the stock market opens. The jobs report and CPI are released at 8:30 a.m. ET, so the futures price moves first and stocks gap to match at 9:30 a.m. ([The jobs report](../11-macro-and-economic-data/05-the-jobs-report.md)).
2. News from Asia and Europe moves futures while stocks are shut.
3. The break itself closes the market. A stop does not work during the break, and the price can reopen at 6 p.m. away from where it closed.

A **session** is a window of the trading day with its own character. The regular session (9:30 a.m. to 4 p.m. ET), when stocks trade, has the most volume. Most day-trading rules in Part 8 were written for it ([How day trading differs](../08-day-trading/01-how-day-trading-differs.md)). If you trade micros overnight, treat it as a different market: smaller size, wider stops in ticks, and fewer entries.

## Hours on your chart

A daily bar of a future runs from 6 p.m. to 5 p.m. ET, not 9:30 a.m. to 4 p.m. ET. A daily chart of the same index future can therefore show different highs, lows and closes from a daily chart of the index. Intraday charts have a setting for the session: all hours, or regular hours only. VWAP resets at the start of the session you choose ([VWAP and anchored VWAP](../05-reading-charts/08-vwap-and-anchored-vwap.md)). Pick one setting and use it for every chart in the plan, or your levels will not match across charts. The 5-minute chart in lesson 3 is a regular-session chart, from 9:30 a.m. to 4 p.m. ET.

Holidays change the schedule: some days have early closes or no session, and CME Group posts them in its holiday calendar. Check it before you plan a trade near a holiday.

<div class="canada" markdown>

### For Canadians

The Montreal Exchange has its own hours for the S&P/TSX 60 futures, which differ from Globex. Check the exchange's trading hours page for the contract before you trade ([Futures in Canada](07-futures-in-canada.md)).

</div>

## Common mistakes

- Reading the 5 p.m. to 6 p.m. ET break as part of the next day. The market is closed, and a stop cannot fill.
- Using a stock-hours chart to place a stop that must hold overnight. The overnight range is not on the chart.
- Mixing "all hours" and "regular hours" charts in one plan.

## Try it

1\. How many hours does a Globex day trade, Monday to Thursday?

<details class="solution" markdown>
<summary>Answer</summary>

From 6 p.m. to 5 p.m. ET the next day is 23 hours, since the break is 1 hour.

</details>

2\. What share of a 115-hour trading week is the stock market's regular session of 32.5 hours?

<details class="solution" markdown>
<summary>Answer</summary>

32.5 / 115 = 0.283, so 28.3%.

</details>

3\. CPI is released at 8:30 a.m. ET. How long before the stock market opens can you trade the future on it?

<details class="solution" markdown>
<summary>Answer</summary>

The stock market opens at 9:30 a.m. ET, so one hour.

</details>

4\. Your stop is at 6,003.00 and the market is closed from 5 p.m. to 6 p.m. ET. At 6 p.m. the future reopens at 5,998.00. Where can the stop fill, and what is the extra loss per micro contract (US$5 per point)?

<details class="solution" markdown>
<summary>Answer</summary>

A stop order becomes a market order when the price trades at or through the stop, so it can fill near 5,998.00, about 5.00 points below. Extra loss = 5.00 x 5 = US$25.00 per contract, before any further slippage.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Open a 5-minute chart of a micro future with all hours on, then with regular hours only. Note the overnight high and low. |
| 5 | Write the break and the session times for your contract in your trading plan. |

</div>

## Key terms

- **Globex**: CME Group's electronic trading platform.
- **Daily maintenance break**: the one-hour pause in futures trading from 5 p.m. to 6 p.m. ET.
- **Overnight session**: futures trading outside the stock market's regular hours.
- **Session**: a window of the trading day, such as regular hours or the overnight session.
- **Regular session**: the stock market's 9:30 a.m. to 4 p.m. ET.

Next: [Futures in Canada](07-futures-in-canada.md)
