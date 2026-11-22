# Bid, ask and the order book

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">MKT</span>

After this lesson you can read a quote and a book of orders, work out the spread and the average price a large order will get, and say why a thin book costs more to trade.

Before this: [Market hours and the opening and closing auctions](03-market-hours-and-auctions.md). You need: a calculator.

## The idea

You want to buy 1,000 shares of Stock A. The screen says US$49.99. If you send a market order, do you pay US$49.99 a share? Not quite, and the reason is that no one is offering to sell at US$49.99.

Two prices exist at any moment. The **bid** is the highest price a buyer is currently willing to pay. The **ask** (also called the offer) is the lowest price a seller is currently willing to accept. The bid is always below the ask, otherwise the two orders would already have traded. The difference is the **spread**.

Each price comes with a size, the number of shares offered at that price. A list of every waiting order, sorted by price, is the **order book**.

Here is the book for Stock A. Each row is one price level.

| Side | Price (US$) | Shares at this price | Shares up to this price |
|---|---|---|---|
| Ask | 50.03 | 1,000 | 2,700 |
| Ask | 50.02 | 700 | 1,700 |
| Ask | 50.01 | 600 | 1,000 |
| Ask | 50.00 | 400 | 400 |
| Bid | 49.98 | 300 | 300 |
| Bid | 49.97 | 500 | 800 |
| Bid | 49.96 | 800 | 1,600 |
| Bid | 49.95 | 1,200 | 2,800 |

The best bid is US$49.98 (300 shares) and the best ask is US$50.00 (400 shares). Together they are the quote, written 49.98 x 50.00. The "49.99" on your screen was the midpoint between them, or the last trade, and neither is a price you can trade at in size.

## How it works

The spread in dollars and as a share of the price:

\[ \text{Spread} = A - B \qquad \text{Spread \%} = \frac{A - B}{(A + B)/2} \]

- \(A\) is the best ask and \(B\) the best bid, both in US$.
- \((A+B)/2\) is the **midpoint**, the price halfway between them.

A trader who buys at the ask and sells at the bid pays the spread on a round trip. That is a real cost on every trade, whether or not the broker charges a commission.

A **market order** takes the best price on the other side first. If it is bigger than the size shown there, it takes the next price level, and then the next. This is called walking the book.

<div class="example" markdown>

### Worked example: buying 1,000 and selling 1,500

Spread: 50.00 - 49.98 = US$0.02. The midpoint is (50.00 + 49.98) / 2 = US$49.99, so the spread is 0.02 / 49.99 = 0.04%.

Buying 1,000 shares with a market order:

1. Take 400 at 50.00: 400 x 50.00 = US$20,000.00.
2. Take 600 at 50.01: 600 x 50.01 = US$30,006.00.
3. Total cost US$50,006.00, so the average price is 50,006 / 1,000 = US$50.006.
4. Compared with the midpoint of 49.99, you paid 50.006 - 49.99 = US$0.016 a share, or US$16.00 in all.

Selling 1,500 shares with a market order:

1. Take 300 at 49.98: US$14,994.00.
2. Take 500 at 49.97: US$24,985.00.
3. Take 700 at 49.96: US$34,972.00.
4. Total proceeds US$74,951.00, an average of 74,951 / 1,500 = US$49.967 (rounded to three decimals).

A round trip of 1,000 shares in and out costs more than the two-cent spread suggests, because the average price you get moves against you as the size grows.

</div>

The picture adds up the sizes. Look at how the green bids stack to the left and the red asks to the right, with the gap in the middle being the spread.

![Order book depth for a made-up stock: bids stacked to the left of US$49.99, asks to the right, with a US$0.02 spread](../assets/figures/01-how-markets-work/order-book-depth-dark.svg#only-dark)
![Order book depth for a made-up stock: bids stacked to the left of US$49.99, asks to the right, with a US$0.02 spread](../assets/figures/01-how-markets-work/order-book-depth-light.svg#only-light)

The steeper a side is, the more shares sit close to the price and the less your order moves it. A flat, shallow side means a small order can jump several levels. A stock with a tight spread and deep sizes is **liquid**: you can trade a lot quickly near the quote. **Slippage** is the difference between the price you expected (the quote or midpoint) and the price you got, as in the US$16.00 above.

### Ticks and quote levels

The smallest price step a stock can quote is the **tick**. For US stocks priced at US$1 or more it is one cent today. The SEC adopted a half-cent tick for certain tightly quoted stocks in 2024, and moved the compliance date to November 2027 (see [SEC press release 2024-137](https://www.sec.gov/newsroom/press-releases/2024-137) and the [Morrison Foerster summary](https://www.mofo.com/pdf/resources/insights/260612-sec-proposes-landmark-rollback-of-core-regulation), as of 2026).

**Level 1** data shows the best bid, best ask, their sizes and the last trade. **Level 2** data shows several price levels of the book, like the table above. Part 8 uses it for trading ([Level 2 and time and sales](../08-day-trading/07-level-2-and-time-and-sales.md)).

<details class="code" markdown>
<summary>In code</summary>

The function walks a list of (price, shares) levels and returns the average price for a market order. It prints the two averages from the example.

```python
asks = [(50.00, 400), (50.01, 600), (50.02, 700), (50.03, 1000)]
bids = [(49.98, 300), (49.97, 500), (49.96, 800), (49.95, 1200)]

def average_fill(levels, shares):
    left, cost = shares, 0.0
    for price, size in levels:
        take = min(left, size)
        cost += take * price
        left -= take
        if left == 0:
            return cost / shares
    raise ValueError("not enough shares in the book")

print(round(average_fill(asks, 1000), 3))
print(round(average_fill(bids, 1500), 3))
```

</details>

## Common mistakes

- Trading off the "last price" and expecting it. The last trade can be on either side of the spread.
- Looking only at the spread. A one-cent spread with 100 shares at each price is cheap for 100 shares and expensive for 5,000.
- Treating displayed size as certain. Orders can be cancelled the moment before you trade.

## Try it

1\. A stock quotes 20.10 bid and 20.14 ask. What are the spread in dollars and as a percentage of the midpoint?

<details class="solution" markdown>
<summary>Answer</summary>

Spread = 20.14 - 20.10 = US$0.04. Midpoint = (20.14 + 20.10) / 2 = 20.12. Spread % = 0.04 / 20.12 = 0.20% (rounded to two decimals).

</details>

2\. In the Stock A book, what is the average price for a market order to buy 1,700 shares?

<details class="solution" markdown>
<summary>Answer</summary>

400 at 50.00 = 20,000.00; 600 at 50.01 = 30,006.00; 700 at 50.02 = 35,014.00. Total = US$85,020.00. Average = 85,020 / 1,700 = US$50.012 (rounded to three decimals).

</details>

3\. You sell 300 shares of Stock A with a market order. What price do you get, and what is the slippage against the midpoint?

<details class="solution" markdown>
<summary>Answer</summary>

All 300 fill at the best bid, US$49.98. Against the midpoint of 49.99, slippage is 0.01 a share, or US$3.00 in all.

</details>

4\. Stock B's book has 100 shares at each level, one cent apart, on both sides. Stock C's book has 1,000 shares at each level, also one cent apart. Which is cheaper to trade for 500 shares and why?

<details class="solution" markdown>
<summary>Answer</summary>

Stock C. Its first level has enough size for the whole order. Stock B's order would walk five levels, and the average price would be about 2 cents worse than the best price.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Open the quote for one liquid and one thinly traded stock on your broker or TradingView. Write each spread in dollars and as a percentage of the midpoint. |
| 3 | If your platform shows depth, write the size at the best bid and best ask for both stocks. |
| 2 | Write which stock you would find more costly to buy 500 shares of, and why. |

</div>

## Key terms

- **Bid**: the highest price a buyer is willing to pay now.
- **Ask**: the lowest price a seller is willing to accept now.
- **Spread**: the ask minus the bid.
- **Midpoint**: the price halfway between the bid and the ask.
- **Order book**: all waiting orders, sorted by price.
- **Market order walking the book**: an order taking each price level in turn until it is filled.
- **Liquid**: able to trade in size near the quote with little price move.
- **Slippage**: the difference between the expected price and the price you got.
- **Tick**: the smallest allowed price step.
- **Level 1 and Level 2**: the best quote only, and several levels of depth.

Next: [Order types](05-order-types.md)
