# Forex basics

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">CMDTY</span>

After this lesson you can read a currency pair quote, say which currency is the base and which is the quote, work out the value of a pip for a position size, and compute the profit of a trade after the spread.

Before this: [Bid, ask and the order book](../01-how-markets-work/04-bid-ask-and-the-order-book.md), [Currency risk on US stocks](../02-accounts-currency-and-taxes/05-currency-risk-on-us-stocks.md). You need: a calculator.

## The idea

You have bought a US stock and paid for it with Canadian dollars. Without noticing, you also traded currencies: you sold Canadian dollars and bought US dollars. The price of that trade is the exchange rate, and it moves all day.

**Forex** (also FX, or the foreign exchange market) is the market where currencies trade against each other. It has no single exchange. Banks, dealers and brokers quote prices to each other and to clients, which is why it is called an over-the-counter market. A price in forex is always a pair, because you buy one currency by paying with another.

## How it works

### Pairs, base and quote

A **currency pair** is written as two codes: USD/CAD. The first is the **base currency**, the one being bought or sold. The second is the **quote currency**, the one the price is in. A quote of USD/CAD 1.3650 means one US dollar costs 1.3650 Canadian dollars. Buying the pair means buying the base (USD) and paying with the quote (CAD).

The inverse pair is CAD/USD. Its price is the reciprocal: 1 / 1.3650 = 0.7326, so one Canadian dollar buys 0.7326 US dollars. Each pair has one standard direction, so you will see USD/CAD and not CAD/USD on a quote page. EUR/USD works the same way: a made-up quote of 1.0800 means one euro costs US$1.0800.

When USD/CAD rises the US dollar is getting stronger against the Canadian dollar, so US dollar assets are worth more in CAD. Part 11 used this when it linked rates to the exchange rate ([The Bank of Canada and a macro week](../11-macro-and-economic-data/11-the-bank-of-canada-and-a-macro-week.md)).

### Bid, ask and the pip

Like a stock, a pair has a **bid** (the price a dealer pays for the base currency, the price you sell at) and an **ask** (the price the dealer sells it at, the price you buy at). The gap is the spread. A made-up USD/CAD quote is 1.3650 bid and 1.3652 ask, so the spread is 0.0002.

A **pip** is the standard small step of a quote: 0.0001 for most pairs, and 0.01 for pairs with the Japanese yen as the quote currency. The spread above is 2 pips. A move from 1.3650 to 1.3750 is 100 pips, which is 0.0100 / 1.3650 = 0.73% of the rate.

### Lots and pip value

Forex trades in units of the base currency. A **standard lot** is 100,000 units of the base currency, a **mini lot** is 10,000 and a **micro lot** is 1,000. These sizes are common conventions, and brokers set their own minimums. The money value of one pip depends on the size and is first in the quote currency:

\[ \text{pip value (quote currency)} = \text{units} \times \text{pip size} \]

- \(\text{units}\) is the position size in base currency units, a count.
- \(\text{pip size}\) is 0.0001 for USD/CAD.
- The result is in the quote currency, C$ for USD/CAD. To get US$, divide by the USD/CAD rate.

For one standard lot of USD/CAD: 100,000 x 0.0001 = C$10 per pip, which is 10 / 1.3650 = US$7.33. A mini lot is C$1 per pip.

<div class="example" markdown>

### Worked example: a USD/CAD trade

All prices are made up. You buy 20,000 units of USD/CAD (two mini lots) at the ask of 1.3652, and later sell at the bid of 1.3691.

1. Pip value: 20,000 x 0.0001 = C$2.00 per pip.
2. Pips gained: 1.3691 - 1.3652 = 0.0039, which is 39 pips.
3. Profit: 39 x 2.00 = C$78.00. Check: 20,000 x 0.0039 = C$78.00.
4. In US dollars at the exit rate: 78.00 / 1.3691 = US$56.97.
5. The spread cost you 2 pips at the start: 2 x 2.00 = C$4.00, and the trade needed a 2-pip rise to break even.

The position's size in US dollars was US$20,000, worth C$27,304 at entry (20,000 x 1.3652). A 39-pip gain on C$27,304 is 78 / 27,304 = 0.29%, so forex moves are small in percentage terms, which is why traders use leverage, which lesson 6 covers ([Trading forex from Canada](06-trading-forex-from-canada.md)).

</div>

The chart is a made-up USD/CAD series, quoted as real USD/CAD is: 1.3650 means C$1.3650 per US dollar, and one pip is 0.0001 on the axis.

```chart
data: 17-commodities-forex-and-reits/usdcad-daily.json
title: USD/CAD (made up), daily
level: 1.3702 | Sept 28 close
level: 1.3437 | October 16 low
marker: 2026-09-29 | below | Gap down
range: 2026-09-01 to 2026-11-13
caption: The rate closed at 1.3702 on September 28, opened at 1.3619 the next day, fell to a low of 1.3437 on October 16, and recovered to 1.3650 on November 13.
```

The September 28 close of C$1.3702 and the next open of C$1.3619 differ by 83 pips. From the September 28 close to the October 16 close of 1.3480 the rate fell 222 pips, and from the October 16 low to the November 13 close of 1.3650 it rose 213 pips. When you read a pair, say the direction in terms of the base: here the US dollar weakened, then recovered.

## In code

Pip arithmetic in Python on the sample file [usdcad-daily.csv](../assets/data/usdcad-daily.csv).

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

bars = pd.read_csv("usdcad-daily.csv", parse_dates=["date"])
rate = bars["close"]                          # C$ per US$1
pips = rate.diff() * 10_000                   # one pip is 0.0001
print(round(pips.abs().max(), 1))              # biggest daily move in pips
print(rate.iloc[-1])                          # last close
```

</details>

## Common mistakes

- Reading the pair backwards. In USD/CAD, a rise means the base (USD) is dearer, not the Canadian dollar.
- Using the wrong pip size for yen pairs. A pip there is 0.01, so the same units give a different pip value.
- Forgetting the spread. A buy fills at the ask and sells at the bid, so you start every trade a spread behind.

## Try it

1\. USD/CAD is quoted 1.3648 bid and 1.3651 ask. What is the spread in pips, and what does one standard lot cost to buy in CAD?

<details class="solution" markdown>
<summary>Answer</summary>

Spread = 1.3651 - 1.3648 = 0.0003, which is 3 pips. One standard lot is 100,000 units bought at 1.3651, which costs 100,000 x 1.3651 = C$136,510.

</details>

2\. You buy 50,000 units of USD/CAD at 1.3600 and sell at 1.3562. What is the loss in pips and in CAD?

<details class="solution" markdown>
<summary>Answer</summary>

1.3562 - 1.3600 = -0.0038, so 38 pips lost. Pip value = 50,000 x 0.0001 = C$5.00. Loss = 38 x 5.00 = C$190.00.

</details>

3\. What is the value of one pip for 10,000 units of USD/CAD in US dollars when the rate is 1.3500?

<details class="solution" markdown>
<summary>Answer</summary>

10,000 x 0.0001 = C$1.00. In US dollars: 1.00 / 1.3500 = US$0.74.

</details>

4\. A made-up EUR/USD quote is 1.0800. What is the price of one US dollar in euros?

<details class="solution" markdown>
<summary>Answer</summary>

1 / 1.0800 = 0.9259 euros per US dollar.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | On your broker or the Bank of Canada's exchange rate page, find the current USD/CAD rate. Write the base, the quote and the value of one pip for 10,000 units in CAD. |
| 4 | Open the chart in this lesson. Using the CSV, compute the largest one-day move in pips and the date it happened (see [chart drills](../practice/chart-drills.md) for how to mark it). |
| 2 | Write the bid and ask in a quote you see, and the spread in pips. |

</div>

## Key terms

- **Forex (FX)**: the market where currencies trade against each other.
- **Currency pair**: two currency codes that give the price of the first in the second.
- **Base currency**: the first currency in a pair, the one being bought or sold.
- **Quote currency**: the second currency in a pair, the one the price is in.
- **Pip**: the standard small step in a quote, 0.0001 for most pairs and 0.01 for yen pairs.
- **Lot**: a standard trade size: 100,000 units (standard), 10,000 (mini) or 1,000 (micro).
- **Over-the-counter market**: a market with no central exchange, where dealers quote prices directly.

Next: [What moves currencies](05-what-moves-currencies.md)
