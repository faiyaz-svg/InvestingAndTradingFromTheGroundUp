# What swing trading is

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">SWNG</span>

After this lesson you can say what a swing trade is, how it differs from day trading and long-term investing, what it costs in time and in overnight risk, and why this book teaches it as three named setups.

Before this: [Your trading plan](../03-risk-and-position-sizing/10-your-trading-plan.md), [Trend and market structure](../05-reading-charts/02-trend-and-market-structure.md). You need: nothing.

## The idea

Stock A has risen for two months. It fell for five days in a row, then turned up on Friday. You buy on Monday with a stop under the low of the dip and a target at the old high. On the next Friday the target fills. You held the trade over four nights, looked at it for about ten minutes a day, and risked 1% of the account.

That is a **swing trade**: a trade held for more than one session, usually from two days to a few weeks, that aims to capture one "swing" of price (a move of a few percent up or down inside a larger trend or range). **Swing trading** is the practice of finding those moves, entering with a defined risk, and leaving at a target or a stop. A swing trade is not a day trade (opened and closed in one session, part 8) and not a long-term investment (held for months or years, parts 9 to 13).

This book defines the hold as 2 to 20 trading days. That range is the book's own choice for planning, not a standard. Shorter than 2 days is closer to day trading, and a trade that you hold for months because it went against you has stopped being a swing trade.

## How it works

### What the time commitment looks like

Swing trading fits 30 minutes a day because the decisions happen after the close, when nothing is moving. A typical day looks like this:

1. After the close (10 to 15 minutes): scan, review the watchlist, decide tomorrow's orders.
2. Before the open (2 minutes): place or cancel the orders. A buy stop and a stop-loss order can rest at the broker for the whole session.
3. During the day: nothing, unless a rule says to act.

The weekly routine ([A weekly swing routine](09-weekly-swing-routine.md)) adds one longer review. Compare this with day trading, which needs your screen during the session, and with investing, which needs very little.

| | Day trading | Swing trading | Long-term investing |
|---|---|---|---|
| Typical hold | Minutes to hours, flat at the close | 2 to 20 trading days | Months to years |
| Screen time | The session | 10 to 15 minutes a day | Minutes a month |
| Risk after the close | None | Overnight and weekend gaps | Gaps, drawdowns |
| Trades per month (for one person) | Dozens or more | About 4 to 12 | A few |
| Edge comes from | Intraday structure, speed | Trend, levels, short-term price moves | Business value, time in the market |

The trades-per-month row is the book's planning estimate for one person with a 30-minute day, not a measured figure.

### What you are paid for, and what you pay

A swing trader takes price risk for a few days. The price of that is overnight risk: the stock can open far from where it closed. Part 3 measured this ([Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md)): a stop does not protect you inside a gap, so the loss can be more than 1R. Earnings reports and other news arrive outside the session, so a swing trade can meet several of them in a month. [Managing the trade](08-managing-the-trade.md) covers what to do before earnings.

The second cost is time in a market that is not trending. The setups in this part each need a particular kind of market, and [Market regime filters](03-market-regime-filters.md) shows how to tell which one you are in.

### The three setups in this part

Every swing trade in this book belongs to one of three named setups. A **setup** is a set of exact, written rules for one kind of trade: the filter, the trigger, the entry, the stop and the exit. Naming the setup lets you keep a record for each one in your journal ([The trade journal](../04-psychology-journal-and-paper-trading/04-the-trade-journal.md)), which is the only way to learn whether it works for you.

| Setup | Idea | Lesson |
|---|---|---|
| Trend pullback | Buy a dip in an uptrend, aiming for the old high | [Trend pullback setups](04-trend-pullback-setups.md) |
| Breakout from a base | Buy when price leaves a tight range on heavy volume | [Breakouts and bases](05-breakouts-and-bases.md) |
| Short-term mean reversion | Buy a sharp short-term drop in a long-term uptrend, sell the bounce | [Short-term mean reversion](06-short-term-mean-reversion.md) |

The chart shows a trend pullback on made-up data, the trade lesson 4 works through in full. Look at the five down closes after the high on March 26, the turn on April 3, and the exit at the old high on April 10.

```chart
data: 07-swing-trading/stock-a-pullback-win.json
title: Stock A, daily: a swing trade held for four nights
show: volume, ema 20, sma 50
level: 56.80 | Prior high (target)
level: 51.05 | Stop
marker: 2026-04-06 | below | Buy 52.81
marker: 2026-04-10 | above | Sell 56.80
range: 2026-02-23 to 2026-04-23
caption: The entry and the exit are four nights apart. The stop was never touched.
```

<div class="canada" markdown>

### For Canadians

A swing trade is held overnight, so the day-trading rules covered in part 8 mostly do not apply to it. The tax rule matters more. The CRA decides case by case whether trading profit is capital gains or business income, and the factors it lists include how often you trade and how long you hold ([IT-479R, archived](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/it479r/archived-transactions-securities.html)). In a TFSA the stakes are higher: the Federal Court of Appeal held in 2024 that the trust of a TFSA that carried on a trading business was taxable on that business income ([Canadian Western Trust Co. (Ahamed TFSA) v. King, 2024 FCA 108](https://decision.tcc-cci.gc.ca/fca-caf/decisions/en/521420/1/document.do)). Swing trading a few times a month is not that fact pattern by itself, but ask an accountant before you trade often in a registered account.

</div>

## Common mistakes

- Holding a day trade overnight because it went wrong. The stop was the plan, and a hold you did not plan has no stop.
- Counting every dip as a setup. A setup has written rules. If you cannot say which of the three it is, skip it.
- Ignoring the calendar. A trade that meets an earnings report has a different risk from one that does not.

## Try it

1\. Stock A closes at US$50.00 on Monday. You buy at the open on Tuesday and sell at the close on the following Monday. How many trading days is the hold, counting Tuesday as day 1, and is it a swing trade by this book's definition?

<details class="solution" markdown>
<summary>Answer</summary>

Tuesday, Wednesday, Thursday, Friday and Monday are 5 trading days. That is inside 2 to 20, so yes.

</details>

2\. A trade is opened at 10:05 a.m. ET and closed at 3:50 p.m. ET the same day. Is it a swing trade?

<details class="solution" markdown>
<summary>Answer</summary>

No. It is closed in the same session, so it is a day trade (part 8).

</details>

3\. The chart above shows a buy at US$52.81 and a sell at US$56.80. How many sessions did the trade span, counting April 6 as day 1, and what is the price gain per share?

<details class="solution" markdown>
<summary>Answer</summary>

April 6, 7, 8, 9 and 10 are 5 sessions (four nights held). The gain is 56.80 - 52.81 = US$3.99 per share.

</details>

4\. Name two kinds of event that can happen while you hold a swing trade and cannot happen while you hold a day trade.

<details class="solution" markdown>
<summary>Answer</summary>

An earnings report released after the close, and an overnight news event or weekend gap. Both open the next session away from the last close.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Write your own limits on the hold: the shortest and longest number of trading days you will accept for a swing trade. Put them in your plan. |
| 3 | Open any daily chart (for example in [chart drills](../practice/chart-drills.md)) and find one move that lasted 3 to 10 sessions and write down its start, end and size in percent. |
| 3 | Check whether your broker lets a stop-loss order rest overnight in your TFSA, RRSP, FHSA, cash and margin accounts. Write the answer down. |

</div>

## Key terms

- **Swing trade**: a trade held more than one session, usually 2 to 20 trading days, that aims to capture one price swing.
- **Swing trading**: finding such moves and entering with a defined risk, a stop and a target.
- **Setup**: a set of exact written rules for one kind of trade: filter, trigger, entry, stop and exit.
- **Overnight risk**: the chance that a stock opens far from its last close, so a stop fills at a worse price.

Next: [Scanners and watchlists](02-scanners-and-watchlists.md)
