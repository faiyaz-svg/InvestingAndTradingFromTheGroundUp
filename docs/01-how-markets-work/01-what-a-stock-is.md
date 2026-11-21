# What a stock is and why prices move

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">MKT</span>

After this lesson you can say what you own when you buy a share, work out a company's market capitalization and a percentage move, and name the three kinds of news that move a price.

Before this: nothing. For percentage changes, see [percent change](https://faiyaz-svg.github.io/MathFromTheGroundUp/02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications/) in the math book. You need: a calculator.

## The idea

Stock A closes on Friday, July 31, 2026 at US$49.40. After the close, the company reports its quarterly profit, and the number beats what analysts expected. On Monday, August 3, the first trade is at US$53.35, which is 8.0% above Friday's close. No regular-session trades happened in between, so the price jumped over the weekend.

Why did a profit report change what strangers will pay? To answer that, we need to say what a share is.

A **stock** is a slice of ownership in a company. One slice is a **share**, and the person who holds it is a **shareholder**. A share gives you a claim on the company's future profits. It also gives you a vote on some company decisions (usually one vote per share), and a right to a share of any **dividend**, which is cash the company chooses to pay out of its profits. If the company is wound up, shareholders are paid last, after lenders and suppliers.

Each listed company has a **ticker**, a short code such as AAPL, that identifies it when you place an order. This book uses made-up companies called Stock A and Stock B for any example with prices, and real tickers only for real facts.

### What a price is

The **price** of a stock is the price of the most recent trade: one buyer and one seller agreed on it. Nobody sets it. If buyers become more eager, they offer more, sellers see the higher offers and ask for more, and the price rises. If sellers become more eager, it falls. The process of buyers and sellers finding the price through their offers is called **price discovery**. Lesson 4 shows how it works one offer at a time ([Bid, ask and the order book](04-bid-ask-and-the-order-book.md)).

### Why prices move

A price is the market's current estimate of what a share is worth. It moves when that estimate changes. Three kinds of news do most of the work.

| Kind | Example | Why it matters |
|---|---|---|
| Company information | An earnings report (a company's profit for a quarter), a new product, a lawsuit | Changes the profit buyers expect |
| Interest rates and the economy | A rate cut, a jobs report | Changes how much future profit is worth today, and how much customers will spend |
| Buying and selling pressure | A fund selling a large position, an index adding the stock | Moves the price even when the company is unchanged |

The same event can raise one stock and lower another. What matters is whether the news is better or worse than what the market already expected. A good profit report that was fully expected can leave the price flat.

## How it works

Two numbers describe the size of a company in the market.

\[ \text{Market cap} = P \times N \]

- \(P\) is the price of one share, in US$ for a US-listed stock.
- \(N\) is the number of shares outstanding (shares held by investors), a count with no unit.
- Market cap, short for **market capitalization**, is the price the market puts on the whole company, in US$.

The size of a move is the percentage change:

\[ r = \frac{P_1 - P_0}{P_0} \]

- \(P_0\) is the starting price and \(P_1\) the ending price, both in US$.
- \(r\) is the return, a fraction; multiply by 100 for a percentage.

<div class="example" markdown>

### Worked example: the earnings gap

Stock A has 100 million shares outstanding.

1. Friday's close: market cap = 49.40 x 100 million = US$4.94 billion.
2. Monday's first trade: market cap = 53.35 x 100 million = US$5.335 billion.
3. The gap: (53.35 - 49.40) / 49.40 = 0.0800, so +8.0%.
4. The added value: 5.335 - 4.94 = US$0.395 billion, or US$395 million.

The company did not receive that US$395 million. Existing shareholders hold shares that the market now values higher. The company only receives money when it sells new shares itself.

</div>

The chart shows the gap. Look at the empty space between the last bar of July and the first bar of August: no regular-session trade happened at any price in that space.

```chart
data: 01-how-markets-work/earnings-gap.json
title: Stock A, daily: a gap up after an earnings report
marker: 2026-08-03 | below | Opens at 53.35
level: 49.40 | Friday close
range: 2026-07-06 to 2026-08-19
caption: Friday's close was 49.40, Monday opened at 53.35, and the price then stayed above the old range.
```

After the gap the price traded between 52.55 and 54.85 for the next 12 sessions. Here the news is absorbed in one jump, and then the market trades around the new level. The jump itself is a **gap**, which lesson 3 covers with the opening auction ([Market hours and the opening and closing auctions](03-market-hours-and-auctions.md)).

<div class="canada" markdown>

### For Canadians

A company can list its shares on a Canadian exchange (priced in CAD), a US exchange (priced in USD), or both. The shares are the same ownership, but you pay in the currency of the listing you trade. Part 2 covers how to pick a currency and what conversion costs ([USD or CAD, and currency conversion fees](../02-accounts-currency-and-taxes/03-usd-vs-cad-and-fx-fees.md)).

</div>

## Common mistakes

- Thinking the price is "fair" because it is the price. It is the last agreed trade, which can be wrong within minutes.
- Assuming good news means the price rises. The price already holds what the market expected, so only the surprise moves it.
- Reading market cap as money the company has. It is what shareholders' stakes are worth at the current price.

## Try it

1\. Stock B trades at US$32.50 and has 240 million shares outstanding. What is its market cap?

<details class="solution" markdown>
<summary>Answer</summary>

32.50 x 240 million = US$7,800 million, which is US$7.8 billion.

</details>

2\. Stock B falls from US$32.50 to US$30.88 after a weak report. What is the percentage change, and what is the new market cap?

<details class="solution" markdown>
<summary>Answer</summary>

(30.88 - 32.50) / 32.50 = -0.0498, so -5.0% (rounded to one decimal). New market cap = 30.88 x 240 million = US$7,411.2 million, about US$7.41 billion.

</details>

3\. A company earned US$250 million in a year and has 100 million shares outstanding. Its earnings per share (profit divided by shares outstanding) is what? If the stock trades at US$50, how many dollars is the market paying per dollar of earnings per share?

<details class="solution" markdown>
<summary>Answer</summary>

Earnings per share = 250 / 100 = US$2.50. The market pays 50 / 2.50 = 20 dollars for each dollar of yearly earnings per share. This ratio is the price-to-earnings ratio, covered in Part 10 (Price multiples<!-- link: ../10-valuation-and-research/01-multiples.md -->).

</details>

4\. Which of the three kinds of news is each? (a) The Federal Reserve cuts interest rates. (b) A company announces a recall. (c) A large fund sells 5% of its holding in Stock A for no reason about the company.

<details class="solution" markdown>
<summary>Answer</summary>

(a) Interest rates and the economy. (b) Company information. (c) Buying and selling pressure.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Open your broker app and pick three stocks you know. Write the price, then multiply by the shares outstanding (find it on the quote page) to get each market cap. |
| 4 | Find the last earnings date for one of them. Write the close before the report and the open after it, and compute the percentage gap. |
| 2 | Write one sentence on whether the move was bigger or smaller than you expected, and why. |

</div>

## Key terms

- **Stock**: a slice of ownership in a company.
- **Share**: one unit of that ownership.
- **Shareholder**: a person or firm that holds shares.
- **Dividend**: cash a company pays to shareholders out of its profits.
- **Ticker**: the short code that identifies a listed stock.
- **Price**: the price of the most recent trade.
- **Price discovery**: how buyers' and sellers' offers settle on a price.
- **Market capitalization (market cap)**: share price times shares outstanding.
- **Earnings report**: a company's published profit for a period.
- **Gap**: a price that opens away from the previous close with no trades between.

Next: [Exchanges and where your order goes](02-exchanges-and-where-orders-go.md)
