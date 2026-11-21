# Reading a quote page

<span class="tag tag-skill">Skill</span> <span class="tag tag-review">Review</span> <span class="tag tag-part">MKT</span>

After this lesson you can read every field on a stock's quote page, work out what it says about price, cost and size, and use the page to check a trade before you place it.

Before this: [Indexes, sectors and market cap](10-indexes-sectors-and-market-cap.md), and the rest of Part 1. You need: a calculator.

## The idea

A quote page packs a dozen or more numbers into a screen. Each answers a question you ask before a trade: where is the price, what does it cost to trade, how busy is it, how big is the company, and what comes next. This lesson goes through a made-up page, then you find the same fields on a real one.

Here is a quote page for Stock A. Every number is made up.

| Field | Value |
|---|---|
| Last | US$50.30 |
| Change | +0.40 (+0.80%) |
| Previous close | US$49.90 |
| Bid x Ask | 50.29 x 50.31 (600 x 400 shares) |
| Open | US$50.00 |
| Day's range | 49.80 to 50.55 |
| 52-week range | 38.20 to 52.40 |
| Volume | 2,100,000 |
| Average volume | 1,500,000 |
| Market cap | US$5.03 billion |
| EPS (trailing 12 months) | US$2.50 |
| P/E | 20.1 |
| Dividend (yearly) and yield | US$2.00, 4.0% |
| Next ex-dividend date | December 3, 2026 |

## Price fields

The **last** price is the most recent trade (lesson 1). The **previous close** is the official close of the last session, set by the closing auction (lesson 3). The change is last minus previous close, shown in dollars and in percent:

\[ \text{Change \%} = \frac{\text{Last} - \text{Previous close}}{\text{Previous close}} \]

For Stock A: (50.30 - 49.90) / 49.90 = 0.80%. The **open** is the first regular-session trade, which comes from the opening auction. If the open is far from the previous close, there was a gap (lesson 1).

The **day's range** is the low and high of the session so far. The **52-week range** is the low and high of the past year. Where the last price sits in a range is

\[ \text{Position} = \frac{\text{Last} - \text{Low}}{\text{High} - \text{Low}} \]

In the 52-week range, (50.30 - 38.20) / (52.40 - 38.20) = 85.2%, so the price is near its yearly high.

## Cost and size fields

**Bid x Ask** is the best quote with sizes (lesson 4). The spread is 50.31 - 50.29 = US$0.02, which is 0.04% of the price. The sizes tell you how much you can trade near that price: 400 shares at the ask. A 1,000-share market buy would walk the book.

**Volume** is the number of shares traded so far today. **Average volume** is the usual daily volume over a period, often 30 or 90 days. Dividing them gives relative volume, a quick check of how busy today is.

\[ \text{Relative volume} = \frac{\text{Volume}}{\text{Average volume}} \]

For Stock A: 2,100,000 / 1,500,000 = 1.4, so 40% busier than usual. Part 5 uses this in detail (Volume and relative volume<!-- link: ../05-reading-charts/04-volume-and-relative-volume.md -->). Check the time of day too, since 1.4 times average at 10 a.m. is a busier day than 1.4 times at 4 p.m.

## Company fields

**Market cap** is price times shares outstanding (lesson 1): 50.30 x 100 million = US$5.03 billion. **EPS** (earnings per share) is the company's profit over the last twelve months divided by its shares outstanding. The **P/E ratio** (price-to-earnings) is the price divided by EPS:

\[ \text{P/E} = \frac{P}{\text{EPS}} = \frac{50.30}{2.50} = 20.1 \]

It tells you how many dollars the market pays for each dollar of yearly profit. Part 10 covers it in full (Price multiples<!-- link: ../10-valuation-and-research/01-multiples.md -->). Pages differ on whether EPS uses reported or adjusted profit.

The dividend shows the yearly dividend and the **dividend yield**: 2.00 / 50.30 = 4.0% (lesson 9). The **next ex-dividend date** tells you the last day to buy to receive it: for December 3, 2026 it is Wednesday, December 2.

### Fields to check before you trade

1. Is the market open, or is the page showing extended-hours prices? A page may show the after-hours last price next to the regular close.
2. Is the spread small compared with your expected move?
3. Is the size at the bid and ask enough for your order?
4. Is today's volume normal, or is there news?
5. Is there an ex-dividend date, earnings date or split coming?

<div class="canada" markdown>

### For Canadians

Check the currency on the quote page. A cross-listed company can have a USD quote and a CAD quote with different prices and volumes. The same page may show your holding in CAD or USD depending on the account. Look for the currency label next to each price.

</div>

## Common mistakes

- Reading a delayed quote as live. Free pages can run 15 minutes behind, so look for a "delayed" label.
- Ignoring the volume. A price move on very low volume says little.

## Try it

1\. Stock B has a last price of US$31.20 and a previous close of US$32.00. What is the change in dollars and percent?

<details class="solution" markdown>
<summary>Answer</summary>

31.20 - 32.00 = -US$0.80. -0.80 / 32.00 = -2.5%.

</details>

2\. Stock B's 52-week range is 24.00 to 36.00. Where is US$31.20 in that range?

<details class="solution" markdown>
<summary>Answer</summary>

(31.20 - 24.00) / (36.00 - 24.00) = 7.20 / 12.00 = 60.0%.

</details>

3\. Stock B has volume of 900,000 and average volume of 1,200,000. What is relative volume, and what does it say?

<details class="solution" markdown>
<summary>Answer</summary>

900,000 / 1,200,000 = 0.75. The stock is trading 25% below its usual volume, though check the time of day.

</details>

4\. Stock B earns US$1.60 per share and trades at US$31.20. What is the P/E?

<details class="solution" markdown>
<summary>Answer</summary>

31.20 / 1.60 = 19.5.

</details>

## Part check

1\. A stock trades at US$62.50 with 80 million shares outstanding. It falls to US$58.00. What is the new market cap and the percentage change?

<details class="solution" markdown>
<summary>Answer</summary>

New market cap = 58.00 x 80 million = US$4,640 million, or US$4.64 billion. Change = (58.00 - 62.50) / 62.50 = -7.2%.

</details>

2\. A price-weighted index has stocks at 120, 80 and 40 with a divisor of 3. The 120 stock falls 10%. What is the index change?

<details class="solution" markdown>
<summary>Answer</summary>

Before: 240 / 3 = 80. After: (108 + 80 + 40) / 3 = 76. Change = (76 - 80) / 80 = -5.0%.

</details>

3\. An opening book has buy limits for 300 at 10.02, 200 at 10.01 and 400 at 10.00, and sell limits for 200 at 10.00, 300 at 10.01 and 400 at 10.02. At what price does the auction open, and how many shares trade?

<details class="solution" markdown>
<summary>Answer</summary>

Demand (buyers at or above the price): 10.02 is 300, 10.01 is 500, 10.00 is 900. Supply (sellers at or below): 10.00 is 200, 10.01 is 500, 10.02 is 900. Matched: 300 at 10.02, 500 at 10.01, 200 at 10.00. The most trade at US$10.01: 500 shares.

</details>

4\. The asks are 300 at 20.01, 500 at 20.02 and 800 at 20.03. A market order buys 700 shares. What is the average price?

<details class="solution" markdown>
<summary>Answer</summary>

300 x 20.01 = 6,003.00 and 400 x 20.02 = 8,008.00. Total US$14,011.00 for 700 shares, an average of US$20.016 (rounded).

</details>

5\. You hold 100 shares bought at US$30.00 with a sell stop at US$28.50. The stock opens at US$27.00. What was the planned loss, and what is the loss on the stop's market order?

<details class="solution" markdown>
<summary>Answer</summary>

Planned loss = (30.00 - 28.50) x 100 = US$150. The stop triggers at the open and fills near 27.00, so the loss is (30.00 - 27.00) x 100 = US$300.

</details>

6\. A stock's ex-dividend date is Thursday, December 3, 2026. What is the last day to buy to receive the dividend, and when does that trade settle?

<details class="solution" markdown>
<summary>Answer</summary>

Wednesday, December 2, 2026. Under T+1 it settles Thursday, December 3, the ex-date and record date.

</details>

7\. You have US$8,000 and buy US$16,000 of stock using a margin loan of US$8,000. The stock falls 25%. What is your equity and what share of your cash did you lose?

<details class="solution" markdown>
<summary>Answer</summary>

The position is 16,000 x 0.75 = US$12,000. Equity = 12,000 - 8,000 = US$4,000. You lost 4,000 of 8,000, which is 50%.

</details>

8\. You short 100 shares at US$40.00 and cover at US$44.00. The borrow fee is US$5.00 and there is no dividend. What is the result?

<details class="solution" markdown>
<summary>Answer</summary>

(40.00 - 44.00) x 100 = -US$400.00, then the fee: -400.00 - 5.00 = -US$405.00.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 6 | Open a real quote page on your broker or TradingView for a US stock. Find each field in the table above and write down its value. For any field the page does not show, write "not shown". |
| 2 | Compute the spread in dollars and percent, and the position in the 52-week range. |
| 2 | Write the next ex-dividend date and earnings date if the page shows them, and whether the price is live or delayed. |

</div>

## Key terms

- **Last**: the price of the most recent trade.
- **Previous close**: the official closing price of the last session.
- **Open**: the first regular-session trade.
- **Day's range**: the low and high of the current session.
- **52-week range**: the low and high of the past year.
- **Volume**: shares traded so far in the session.
- **Average volume**: the usual daily volume over a set period.
- **Relative volume**: volume divided by average volume.
- **EPS**: earnings per share, profit divided by shares outstanding.
- **P/E ratio**: price divided by earnings per share.

Next: Account types for trading<!-- link: ../02-accounts-currency-and-taxes/01-account-types-for-trading.md -->
