# Order types

The order types and time-in-force options from [Order types](../01-how-markets-work/05-order-types.md). Each order trades off certainty that it trades against certainty about the price. Which orders your broker offers varies, so check the order ticket in each account.

## Order types

| Order | What it does | It guarantees | It does not guarantee | When to use it |
|---|---|---|---|---|
| Market | Trades now at the best available price | A fill (almost always) | The price; a large order walks the book | Avoid it on thin stocks and in extended hours; use a marketable limit instead |
| Limit | Trades only at your price or better | The price (or better) | A fill; if the market never reaches your price, nothing happens | When price matters more than the fill |
| Stop | Becomes a market order when the stop price trades | An exit once triggered (almost always) | The price; a gap can fill far past the stop | When you must exit at some level and the exit matters more than the price |
| Stop-limit | Becomes a limit order when the stop price trades | A price cap once triggered | A fill; in a gap past the limit you still hold the position | When a fill below your limit would be worse than staying in |
| Marketable limit | A limit priced at or through the other side of the book | A fill at once up to your cap | A fill if the price jumps past the cap | When getting in or out matters more than a few cents, especially in extended hours |

## Time in force

| Option | What it does | Note |
|---|---|---|
| Day | Expires at the close of the regular session | A limit that did not fill is gone tomorrow |
| Good-till-cancelled (GTC) | Stays until it fills or you cancel it | Up to a maximum your broker sets |
| Market-on-close | Trades only in the closing auction | See [Market hours and the opening and closing auctions](../01-how-markets-work/03-market-hours-and-auctions.md) |

An order can fill in parts. A partial fill is a fill of fewer shares than you asked for, with the rest still waiting.

## Orders that link

| Order | What it does | Note |
|---|---|---|
| Trailing stop | For a long position, moves the stop price up as the stock rises, at a fixed distance behind it, and never moves down | Same fill risk as any stop |
| Bracket | Attaches an exit above and an exit below to an entry | Offered differently by each broker |
| OCO (one cancels the other) | Pairs a target and a stop so that when one fills, the other is cancelled | Check the order ticket |

## Choosing an order

1. If getting in or out matters more than a few cents, use a marketable limit with a cap you accept.
2. If price matters more than the fill, use a limit and accept that it may not fill.
3. If you must exit at some level and the exit matters more than the price, use a stop.
4. If a fill below your limit would be worse than staying in, use a stop-limit, and know that it may not fill.

Neither a stop nor a stop-limit removes gap risk. [Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md) sizes positions with gaps in mind.

## Extended hours caution

Pre-market and after-hours sessions are together called extended hours. NYSE lists early sessions starting at 4:00 a.m. ET and late sessions from 4:00 to 8:00 p.m. ET (as of 2026, see [Market hours and the opening and closing auctions](../01-how-markets-work/03-market-hours-and-auctions.md)). Fewer participants means wider spreads and bigger price jumps on small orders, so use a limit order and not a market order.

Wealthsimple states that its overnight orders (8:00 p.m. to 4:00 a.m. ET) may not be price protected, and that trades after 8:00 p.m. count as the next business day for settlement ([Wealthsimple extended hours](https://www.wealthsimple.com/en-ca/legal/extended-hours), as of 2026). Check your own broker's sessions and which order types it allows in them.
