# Premarket prep

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">DAY</span>

After this lesson you can build a short watchlist before 9:30 a.m. ET: pick stocks that are in play, write their key levels, and write an if-then plan with the room to the first obstacle in R.

Before this: [Volume and relative volume](../05-reading-charts/04-volume-and-relative-volume.md), [Support and resistance](../05-reading-charts/03-support-and-resistance.md) and [Market hours and the opening and closing auctions](../01-how-markets-work/03-market-hours-and-auctions.md). You need: a calculator.

## The idea

Stock A closes Wednesday, September 16, 2026 at US$19.97 after a quiet day. Thursday morning it trades at US$21.57, which is 8.0% higher, and 15,955,800 shares trade that day, against 2,740,900 the day before. A trader who reads the news at 8:30 a.m. has an hour to decide what to do if the open goes one way or the other. A trader who first looks at 9:30 a.m. reacts to the busiest minutes of the day with no plan.

Premarket prep is that hour: find the few stocks that are **in play** (moving on unusual activity, usually news), write down the levels that matter, and decide in advance what you will do at each one.

## How it works

### Step 1: find the stocks in play

Five things to look for, each one a number you can read from a scanner or your broker.

1. A **gap**: the open differs from the prior close. Premarket, this is the indicated price against yesterday's close. The lesson on [Gaps](../05-reading-charts/10-gaps.md) covers how gaps behave.
2. A **catalyst**: a reason, such as an earnings report, a change in guidance, a regulatory decision, a contract, an analyst rating change or a share offering. No news and a big gap is a warning that the move has no known cause. You find company news in press releases and in filings ([Filings and EDGAR](../09-company-financials/01-filings-and-edgar.md)).
3. **Premarket volume**, compared with the stock's usual volume. Premarket volume is thin, so compare it with the average daily volume. For Stock A, take 685,000 premarket shares by 8:30 a.m. (a made-up input) and the prior day's 2,740,900 shares as its usual volume: 685,000 / 2,740,900 = 25.0% of a usual day, which is high.
4. **Relative volume** (Part 5, [Volume and relative volume](../05-reading-charts/04-volume-and-relative-volume.md)): how many times the usual volume the stock is trading.
5. **Float**: the shares available to trade (Part 1, [Indexes, sectors and market cap](../01-how-markets-work/10-indexes-sectors-and-market-cap.md)). A small float can move far on modest volume, and it can also fall as fast.

A screen for this book's examples, with made-up thresholds: price between US$5 and US$50, a gap of at least 4%, a catalyst, and premarket volume of at least 10% of the average day. Change the numbers to fit your plan, and write the reason down.

### Step 2: write the levels

Five levels go on every watchlist name:

- the prior day's high, low and close
- the premarket high and low

These are the levels that other traders see on the same screen. The chart shows Stock A's prior day with the high and low drawn, and the gap above them.

```chart
data: 08-day-trading/premarket-gapper.json
title: Stock A, 5-minute: a quiet day, then an 8% gap up
level: 20.06 | Prior day high 20.06
level: 19.77 | Prior day low 19.77
marker: 2026-09-17 09:30 | below | Opens at 21.57
range: 2026-09-16 09:30 to 2026-09-17 12:00
caption: The close on September 16 was 19.97, the open on September 17 was 21.57 (+8.0%), and the first 5-minute bar ran from 21.45 to 21.80.
```

### Step 3: write the plan

For each name, write the if-then in one line with prices: "If a 5-minute bar trades above X after the opening range forms, buy; stop at Y; size from Y." The setups are in lessons 4 to 6. Then measure the **room**: the distance from your entry to the nearest level above it, in R:

\[ \text{room} = \frac{L - E}{E - S} \]

- \(E\) is the entry, \(S\) the stop and \(L\) the nearest level above the entry (for a short, the nearest level below), all in US$ per share.
- Room has no unit. A room of 2 or more means a 2R target is not blocked by a level.

<div class="example" markdown>

### Worked example: one line of the watchlist

Stock A, with these premarket numbers (made up): catalyst, a raised sales forecast; premarket high US$21.90, premarket low US$20.95; float 18 million shares.

1. Gap: (21.57 - 19.97) / 19.97 = 8.0%.
2. The opening range is the first 5-minute bar, 21.45 to 21.80. A buy stop at 21.81 with a stop at 21.43 (the range low minus 0.02) risks 21.81 - 21.43 = US$0.38.
3. Room: the nearest level above 21.81 is the premarket high, 21.90. Room = (21.90 - 21.81) / 0.38 = 0.24R. A 2R target is 21.81 + 0.76 = US$22.57, past that level.
4. A buy above the premarket high instead: entry 21.91, stop 21.43, risk 0.48. The prior-day levels are far below, and there is no known level above 21.91 on the chart, so the plan is to trade a break of the premarket high, not of the range.

The plan is written in 3 minutes, before any price moves.

</div>

<div class="canada" markdown>

### For Canadians

Wealthsimple lists its pre-market session as 4:00 a.m. to 9:30 a.m. ET ([Wealthsimple extended hours](https://www.wealthsimple.com/en-ca/legal/extended-hours), as of 2026), and says overnight orders (8:00 p.m. to 4:00 a.m. ET) may not be price protected. Use limit orders in extended hours. Check your own broker's pre-market window and which orders it allows before you plan to trade the premarket. Many day traders only watch the premarket and place their first order at the open.

</div>

## Common mistakes

- Chasing a gap with no catalyst. A big move with no news has no stated reason to continue.
- Writing levels after the open. By then the price is moving and you pick the levels that fit the bar you want.
- Building a list of 20 names. You can watch two to five at the open, so cut the list to that.

## Try it

1\. Stock B closed at US$40.00 and indicates US$42.60 premarket. What is the gap in percent?

<details class="solution" markdown>
<summary>Answer</summary>

(42.60 - 40.00) / 40.00 = 6.5%.

</details>

2\. A stock with an average daily volume of 3,000,000 shares has traded 450,000 shares by 8:30 a.m. What share of an average day is that?

<details class="solution" markdown>
<summary>Answer</summary>

450,000 / 3,000,000 = 15.0%.

</details>

3\. Entry US$21.91, stop US$21.43, and the nearest level above is US$23.20. What is the room in R?

<details class="solution" markdown>
<summary>Answer</summary>

Risk = 21.91 - 21.43 = 0.48. Room = (23.20 - 21.91) / 0.48 = 1.29 / 0.48 = 2.69R.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 6 | Tomorrow morning, before 9:30 a.m. ET, pick two stocks from a scanner. For each, write the gap, the catalyst, the five levels and an if-then line. |
| 4 | Do three [chart drills](../practice/chart-drills.md) that ask you to click a prior-day high or low. |

</div>

## Key terms

- **In play**: moving on unusual volume, usually because of news.
- **Gap**: the difference between a stock's open and its prior close.
- **Catalyst**: the news or event that explains a move.
- **Premarket volume**: shares traded before 9:30 a.m. ET.
- **Room**: the distance from the entry to the nearest level in the trade's direction, in R.

Next: [Intraday charts and VWAP](03-intraday-charts-and-vwap.md)
