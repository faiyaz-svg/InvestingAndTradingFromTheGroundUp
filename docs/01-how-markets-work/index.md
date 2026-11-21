# Part 1: How markets work

What a share is, where orders go, who takes the other side, and how to read a quote.

Before this part: Nothing. This is the start of the book.

<!-- lessons:start -->
## Lessons

1. [What a stock is and why prices move](01-what-a-stock-is.md) (idea)
2. [Exchanges and where your order goes](02-exchanges-and-where-orders-go.md) (idea)
3. [Market hours and the opening and closing auctions](03-market-hours-and-auctions.md) (idea)
4. [Bid, ask and the order book](04-bid-ask-and-the-order-book.md) (idea)
5. [Order types](05-order-types.md) (skill)
6. [Who is on the other side of your trade](06-who-is-on-the-other-side.md) (idea)
7. [Settlement, cash accounts and margin](07-settlement-cash-and-margin.md) (idea)
8. [Short selling](08-short-selling.md) (skill)
9. [Dividends, splits and corporate actions](09-dividends-splits-and-corporate-actions.md) (idea)
10. [Indexes, sectors and market cap](10-indexes-sectors-and-market-cap.md) (idea)
11. [Reading a quote page](11-reading-a-quote-page.md) (skill, review)

<!-- lessons:end -->

## Cheat sheet

### Formulas

| Formula | Symbols | Use |
|---|---|---|
| \( \text{Market cap} = P \times N \) | \(P\) price (US$), \(N\) shares outstanding | Size of a company |
| \( r = (P_1 - P_0)/P_0 \) | \(P_0\) start, \(P_1\) end | Percentage change |
| \( \text{Spread} = A - B \) | \(A\) best ask, \(B\) best bid | Cost of crossing the market |
| \( \text{Spread \%} = (A-B)/((A+B)/2) \) | midpoint in the denominator | Spread against price |
| \( \text{Equity ratio} = (V-L)/V \) | \(V\) position value, \(L\) loan | Margin safety |
| Short profit \( = (P_0 - P_1) N - C \) | \(C\) borrow fee, dividends, commissions | Result of a short |
| \( y = D/P \) | \(D\) yearly dividend per share | Dividend yield |
| \( I = \sum P_i / d \) | \(d\) divisor | Price-weighted index |
| \( w_i = P_i N_i f_i / \sum_j P_j N_j f_j \) | \(f\) float fraction | Cap weight |
| \( \text{P/E} = P/\text{EPS} \) | EPS earnings per share | Price per dollar of profit |

### Order types

| Order | Guarantees | Does not guarantee |
|---|---|---|
| Market | A fill | The price |
| Limit | The price or better | A fill |
| Stop | A fill once triggered | The price |
| Stop-limit | A price cap once triggered | A fill |

### Times (ET) and dates

- Regular session 9:30 a.m. to 4:00 p.m. Extended hours and overnight vary by broker, so check yours.
- NYSE closing auction orders: enter by 3:50 p.m.
- Settlement: T+1 in the US and Canada since May 2024. A Friday trade settles Monday.
- Dividend: buy at least one business day before the ex-dividend date (ex-date and record date are the same under T+1).

### Checklists

Before a trade:

1. Spread small against the expected move?
2. Size at the bid and ask enough for the order?
3. Volume normal, or is there news?
4. Ex-dividend, earnings or split date coming?
5. Order type matches the goal (price or fill)?

Before a short:

1. Account allows shorting (non-registered margin only in Canada)?
2. Shares available to borrow, and what is the borrow fee?
3. Loss limit set, knowing a stop can gap?

### Rules to remember

- A price is the last trade, not a fair value.
- Stops can fill far from the stop price in a gap.
- A split changes shares and price, not value.
- A price-weighted index follows the highest-priced stock, a cap-weighted index the largest company.

