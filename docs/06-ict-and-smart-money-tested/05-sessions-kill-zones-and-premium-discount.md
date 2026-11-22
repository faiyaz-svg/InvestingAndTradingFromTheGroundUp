# Sessions, kill zones and premium and discount

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">ICT</span>

After this lesson you can give the ICT session windows in Toronto time, work out the equilibrium and the optimal trade entry zone of a swing, price a trade from that zone, and say what is known about time-of-day and retracement claims.

Before this: [Fair value gaps](03-fair-value-gaps.md) and [Market hours and the opening and closing auctions](../01-how-markets-work/03-market-hours-and-auctions.md). You need: a calculator.

## The idea

Price does not move at the same speed all day. Volume and volatility are high near the open and the close of a market and thinner in between ([Volume and relative volume](../05-reading-charts/04-volume-and-relative-volume.md)). ICT teachers build on that. They say that the best moves start inside a few **kill zones**, short windows when the large traders of a region are active, and that a day often begins with a range that is swept early in the active window.

A second idea concerns where in a swing you buy. After a rise from a swing low to a swing high, the teachers split the swing in half. The 50% level is the **equilibrium**. The upper half is **premium** (expensive) and the lower half is **discount** (cheap). In an uptrend they want to buy in discount and sell in premium. Inside the discount half, the **optimal trade entry** (OTE) is the zone from 62% to 79% of the retracement, often with 70.5% as the middle. The numbers come from Fibonacci retracement levels, which teachers use for the swing's pullbacks.

## How it works

### Sessions and times

The windows below are the ones teachers most often give, in Eastern Time (ET), which is Toronto's time zone. Teachers differ by up to an hour on the edges, so check yours.

| Window | Time (ET) |
|---|---|
| Asian range | about 8 p.m. to midnight |
| London kill zone | 2 a.m. to 5 a.m. |
| New York kill zone | 7 a.m. to 10 a.m. |
| London close | 10 a.m. to noon |

![The ICT session windows on a 24-hour Eastern Time clock, with the US regular session for comparison.](../assets/figures/06-ict-and-smart-money-tested/sessions-et-dark.svg#only-dark)
![The ICT session windows on a 24-hour Eastern Time clock, with the US regular session for comparison.](../assets/figures/06-ict-and-smart-money-tested/sessions-et-light.svg#only-light)

Daylight saving matters for the London times. London opens at 8 a.m. London time, which is 3 a.m. ET when both places are on standard time or both on summer time. The US and the UK change their clocks on different days. In 2026 the US moves its clocks forward on March 8 and the UK on March 29, so from March 8 to March 28 London is 4 hours ahead of Toronto, not 5. In autumn the UK moves back on October 25 and the US on November 1, so from October 25 to October 31 the gap is again 4 hours. Decide whether your rule is fixed in ET or tied to the London open.

Most of these windows are currency and futures hours. A US stock trades its regular session from 9:30 a.m. to 4 p.m. ET, with extended hours before and after it that vary by broker. Of the New York kill zone, only 9:30 to 10 a.m. falls in the regular session, and the hours before it are thin pre-market trading.

### Premium, discount and OTE

\[ \text{level}_k = H - k\,(H - L) \]

- \(H\) is the swing high and \(L\) is the swing low, in US$.
- \(k\) is the retracement fraction: 0.5 for equilibrium, 0.62 and 0.79 for the OTE zone.
- \(\text{level}_k\) is the price that has retraced \(k\) of the swing, measured down from the high. For a falling swing, mirror it: \(L + k\,(H - L)\).

The chart shows Stock A rising and pulling back.

```chart
data: 06-ict-and-smart-money-tested/premium-discount.json
title: Stock A, daily: premium, discount and the OTE zone
level: 60.00 | Swing high
level: 55.00 | Equilibrium (50%)
level: 50.00 | Swing low
zone: 52.10-53.80 | 2026-03-18 to 2026-04-13 | OTE (62% to 79%)
marker: 2026-03-25 | below | Pullback into OTE
show: volume
caption: Swing low 50.00 (February 10) to swing high 60.00 (March 11).
```

The swing low is 50.00 on February 10 and the swing high is 60.00 on March 11, so \(H - L\) = 10.00. Equilibrium is 60.00 - 0.5 x 10.00 = 55.00. The OTE zone runs from 60.00 - 0.62 x 10.00 = 53.80 down to 60.00 - 0.79 x 10.00 = 52.10, with 70.5% at 52.95.

<div class="example" markdown>

### Worked example: a long from the OTE zone

Account US$25,000, risk 1% per trade, Stock A.

1. Entry: a buy limit at 52.95 (the 70.5% level). On March 25 the bar opens at 54.00 and trades down to 52.60, so the order fills.
2. Stop: 49.95, five cents under the swing low.
3. Risk per share = 52.95 - 49.95 = US$3.00. Shares = 250 / 3.00 = 83.3, so 83 shares, costing 83 x 52.95 = US$4,394.85.
4. Target: the swing high, 60.00. Reward per share = 60.00 - 52.95 = US$7.05.
5. Reward to risk = 7.05 / 3.00 = 2.35R.

On April 13 the high is 60.25, so the target fills. A stop-out loses 83 x 3.00 = US$249.

</div>

The intraday chart shows a New York open in a 5-minute series.

```chart
data: 06-ict-and-smart-money-tested/ny-open-5m.json
title: Stock A, 5-minute: the opening range, a sweep and a gap
level: 100.90 | Opening range high
level: 99.70 | Opening range low
zone: 99.95-100.30 | 2026-03-02 10:15 to 2026-03-02 10:25 | Bullish FVG
marker: 2026-03-02 10:10 | below | Sweep of the range low
marker: 2026-03-02 10:20 | below | Displacement
show: vwap
caption: The first six bars set a range of 99.70 to 100.90; the 10:10 bar trades to 99.40.
```

The first six bars (9:30 to 9:55) set a range of 99.70 to 100.90, 1.20 wide. The 10:10 bar trades to 99.40 and closes at 99.50. The 10:15 bar closes back inside at 99.90, which confirms the sweep by the lesson 2 rule. The 10:20 bar rises from 99.90 to 100.80, and the 10:25 bar has a low of 100.30, so the gap runs from 99.95 to 100.30. The price never returns to it, and the high of the day is 101.92 at 12:20. A limit order at the gap would have missed the whole move. Window-based methods have the same problem as gap methods: the best moves leave without you.

<div class="canada" markdown>

### For Canadians

All times above are Eastern Time, the same as Toronto's, so you do not convert. Wealthsimple lists its pre-market session as 4:00 to 9:30 a.m. ET and overnight trading from 8 p.m. to 4 a.m. ET ([Wealthsimple extended hours](https://www.wealthsimple.com/en-ca/legal/extended-hours), as of 2026), so the London kill zone falls in its overnight window and the New York kill zone is mostly pre-market. Spreads are wider in those hours ([Bid, ask and the order book](../01-how-markets-work/04-bid-ask-and-the-order-book.md)), so use limit orders.

</div>

## What tests found

Time-of-day effects in volume and volatility are well documented. Andersen and Bollerslev (1998) studied five-minute deutsche mark-dollar returns and found strong intraday patterns and strong effects from scheduled macroeconomic announcements ([NBER working paper 5783](https://www.nber.org/papers/w5783); Journal of Finance 53(1), 219-265). That supports "some hours are more active". It does not show that price reverses or runs in a predictable direction at a kill zone. We found no peer-reviewed test of ICT's kill zones as a direction signal.

For premium, discount and the 62% to 79% zone we found no peer-reviewed test either. The retracement ratios come from Fibonacci numbers and have no known economic mechanism. A test is easy to state: take every swing of a size you define, measure how deep the next pullback goes, and check whether the pullback stops in the OTE zone more often than in an equally wide zone elsewhere, such as 30% to 47%.

## Common mistakes

- Forgetting the daylight saving gap. For three weeks in March and one in October, London is 4 hours ahead of Toronto, so a rule based on London time moves on your clock.
- Applying a 7 to 10 a.m. window to stocks without noticing that most of it is thin pre-market trading.
- Choosing the swing after seeing the pullback. The swing low and high must be fixed by a rule (lesson 1) before you draw the levels.

## Try it

1\. A swing runs from a low of 50.00 to a high of 60.00. Where is equilibrium, and which half is discount?

<details class="solution" markdown>
<summary>Answer</summary>

60.00 - 0.5 x 10.00 = 55.00. The half below 55.00 is discount.

</details>

2\. For the same swing, where does the OTE zone start and end?

<details class="solution" markdown>
<summary>Answer</summary>

62%: 60.00 - 6.20 = 53.80. 79%: 60.00 - 7.90 = 52.10. The zone is 52.10 to 53.80.

</details>

3\. Entry at 52.95, stop 49.95, target 60.00, risk US$250. How many shares and what reward to risk?

<details class="solution" markdown>
<summary>Answer</summary>

Risk per share 3.00, so 250 / 3.00 = 83 shares. Reward per share 7.05, so 7.05 / 3.00 = 2.35R.

</details>

4\. It is Wednesday, March 18, 2026. London opens at 8 a.m. London time. What is that in Toronto time?

<details class="solution" markdown>
<summary>Answer</summary>

The US changed its clocks on March 8 and the UK has not yet (March 29), so London is 4 hours ahead: 8 a.m. in London is 4 a.m. ET. In winter, with both on standard time, it is 3 a.m. ET.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | On a 5-minute chart of a stock you know, mark the opening range (9:30 to 10:00) for the last 5 days. Note whether price swept one side first and where the day's high and low came. |
| 3 | On a daily chart, mark a recent swing and compute its 50%, 62% and 79% levels. Did the next pullback stop in the zone? |
| 3 | Do the premium and discount drills in [chart drills](../practice/chart-drills.md). |

</div>

## Key terms

- **Kill zone**: a short window of the day, tied to a regional session, in which ICT teachers expect the best moves.
- **Equilibrium**: the 50% level of a swing.
- **Premium**: the half of a swing above equilibrium.
- **Discount**: the half of a swing below equilibrium.
- **Optimal trade entry (OTE)**: the zone from 62% to 79% of a retracement, often with 70.5% as its middle.

Next: [Testing smart money claims](06-testing-smc-claims.md)
