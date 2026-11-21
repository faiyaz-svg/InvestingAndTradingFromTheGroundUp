# Order types

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">MKT</span>

After this lesson you can pick the right order type for a goal, say what each one guarantees and what it does not, and work out what a stop order costs you when the price gaps.

Before this: [Bid, ask and the order book](04-bid-ask-and-the-order-book.md). You need: a calculator.

## The idea

An order tells the market three things: which stock, how many shares, and how to trade them. The "how" is the order type. Each type trades off two things you can't have together: certainty that the order trades, and certainty about the price.

Stock A last closed at US$50.30. You want 100 shares, but you might want them at a lower price, or only if the price proves itself by rising. Each wish has its own order.

## How it works

### The four basic orders

A **market order** trades now at the best available price. It almost always fills, and it has no price limit, so it walks the book (lesson 4) when it is large and can fill far from the last price in a fast or thin market.

A **limit order** trades only at your price or better. A buy limit at US$49.50 fills at 49.50 or lower; a sell limit fills at its price or higher. It guarantees the price, not the fill: if the market never reaches your price, nothing happens. A limit order that is not yet filled waits in the order book, adding to the sizes other traders see.

A **stop order** (also called a stop-loss when used to exit) is a dormant order with a trigger price, the **stop price**. When the stock trades at or through that price, the stop becomes a market order. A sell stop sits below the market and exits a long position. A buy stop sits above the market and can enter on a rise, or close a short position (lesson 8). It guarantees the exit happens (almost always), and not the price.

A **stop-limit order** has a stop price and a limit price. When triggered it becomes a limit order, not a market order. It caps the price you accept, and it may not fill at all.

| Order | Guarantees | Does not guarantee |
|---|---|---|
| Market | A fill | The price |
| Limit | The price (or better) | A fill |
| Stop | A fill once triggered | The price |
| Stop-limit | A price cap once triggered | A fill |

A **marketable limit order** is a limit order priced at or through the other side of the book, so it fills at once up to your cap. A buy limit at US$50.05 when the best ask is US$50.00 takes shares at the ask and never pays more than 50.05. Many traders use it instead of a market order, especially in extended hours, because it caps the damage if the price jumps.

### Time in force

**Time in force** says how long an order lives. A **day** order expires at the close of the regular session. A **good-till-cancelled** (GTC) order stays until it fills or you cancel it, up to a maximum your broker sets. A **market-on-close** order trades only in the closing auction (lesson 3). Orders can fill in parts: a **partial fill** is a fill of fewer shares than you asked for, with the rest still waiting.

### Orders that link

A **trailing stop** for a long position moves its stop price up as the stock rises, keeping a fixed distance behind it, and never moves down. A **bracket order** attaches an exit above and an exit below to an entry, and an **OCO** (one cancels the other) order pairs a target and a stop so that when one fills, the other is cancelled. Which of these your broker offers varies, so check the order ticket.

The chart marks three orders against Stock A's last close of US$50.30.

```chart
data: 01-how-markets-work/order-types.json
title: Stock A, daily: where three orders would rest
level: 51.00 | Buy stop 51.00
level: 49.50 | Buy limit 49.50
level: 48.50 | Sell stop 48.50
range: 2026-10-01 to 2026-11-04
caption: A buy limit rests below the market, a buy stop above it, and a sell stop below a long position.
```

<div class="example" markdown>

### Worked example: a stop in a gap

You hold 100 shares of Stock A, bought at US$50.30, with a sell stop at US$48.50. You expect to lose at most (50.30 - 48.50) x 100 = US$180.

Overnight, bad news arrives and the stock opens at US$47.20. Your stop price was passed, so it triggers at the open and becomes a market order.

1. Market stop: fills near 47.20. Loss = (50.30 - 47.20) x 100 = US$310, which is US$130 more than planned.
2. Stop-limit with stop 48.50 and limit 48.30: it triggers, but 47.20 is below the 48.30 limit, so it does not fill. You still hold 100 shares, now worth US$4,720, and the loss on paper is the same US$310 until you act.

The stop-limit avoided selling at the bottom of the gap but left the risk open. Neither type removes gap risk. Part 3 sizes positions with it in mind ([Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md)).

</div>

## Choosing an order

1. If getting in or out matters more than a few cents, use a marketable limit with a cap you accept.
2. If price matters more than the fill, use a limit and accept that it may not fill.
3. If you must exit at some level and the exit matters more than the price, use a stop.
4. If a fill below your limit would be worse than staying in, use a stop-limit, and know that it may not fill.

<div class="canada" markdown>

### For Canadians

Order types, extended-hours rules and limit order requirements differ by broker and by account. Wealthsimple states its overnight orders may not be price protected ([Wealthsimple extended hours](https://www.wealthsimple.com/en-ca/legal/extended-hours), as of 2026), so a limit order is the safer choice there. Look at the order ticket in your TFSA, RRSP, FHSA or margin account and write down the types it offers, and check whether they differ by account.

</div>

## Common mistakes

- Using a market order on a thin stock or in extended hours. Use a marketable limit so you decide the worst price.
- Setting a stop at a round number a few cents below the market. Normal noise can trigger it, and the stop places no limit on the price.
- Forgetting that a day order dies at the close. A limit that did not fill is gone tomorrow.

## Try it

1\. Stock A is at US$50.30. You place a good-till-cancelled buy limit at US$49.50, and the stock opens the next day at US$48.90. At what price does the order fill, and why?

<details class="solution" markdown>
<summary>Answer</summary>

It fills at 48.90 (or better), not 49.50. A buy limit means "this price or lower", and 48.90 is lower, so the order fills at the available price.

</details>

2\. You own 200 shares bought at US$50.30 with a sell stop at US$48.50. What is the planned loss? What is the loss if the market order from the stop fills at US$48.10?

<details class="solution" markdown>
<summary>Answer</summary>

Planned loss = (50.30 - 48.50) x 200 = US$360. Actual loss = (50.30 - 48.10) x 200 = US$440, which is US$80 more.

</details>

3\. The best ask is US$50.00 with 400 shares. You send a buy limit for 1,000 shares at US$50.01. The book has 400 shares at 50.00 and 600 at 50.01. How much does it fill and at what total cost?

<details class="solution" markdown>
<summary>Answer</summary>

All 1,000 shares fill: 400 x 50.00 = US$20,000.00 and 600 x 50.01 = US$30,006.00, total US$50,006.00. Both levels are at or below the limit.

</details>

4\. Which order would you use to buy only if Stock A rises to US$51.00, and what happens if it opens at US$51.40?

<details class="solution" markdown>
<summary>Answer</summary>

A buy stop at 51.00. Opening at 51.40 is through the stop price, so it triggers and becomes a market order that fills near 51.40, not at 51.00.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Open the order ticket for a stock on your broker. List every order type and time in force it offers. |
| 3 | In a paper or practice account, if you have one, place a limit order well below the market and a stop above it. Write when each would fill. |
| 3 | Pick a recent gap on any chart (see [chart drills](../practice/chart-drills.md)) and compute what a stop 2% below the prior close would have cost. |

</div>

## Key terms

- **Market order**: an order to trade now at the best available price.
- **Limit order**: an order to trade only at a set price or better.
- **Stop order**: an order that becomes a market order when a trigger price trades.
- **Stop price**: the trigger price of a stop order.
- **Stop-limit order**: a stop that becomes a limit order when triggered.
- **Marketable limit order**: a limit order priced to fill at once, with a price cap.
- **Time in force**: how long an order stays active.
- **Day order**: an order that expires at the close of the regular session.
- **Good-till-cancelled (GTC)**: an order that stays until filled or cancelled.
- **Partial fill**: a fill of fewer shares than ordered.
- **Trailing stop**: a stop that follows the price at a fixed distance.
- **Bracket order and OCO**: orders linking an entry or exit so a fill cancels the other.

Next: [Who is on the other side of your trade](06-who-is-on-the-other-side.md)
