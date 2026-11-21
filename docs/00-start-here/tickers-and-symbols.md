# Tickers and symbols

A **ticker** is the short code a market uses for a security. You type it into a platform to pull up a quote, and each platform has its own habits for writing it. This page shows the formats you will meet, so a symbol does not stop you at the search box.

## US stock tickers and share classes

US stocks have tickers of one to five letters, such as AAPL or MSFT. A company with more than one class of shares gets a ticker for each. Berkshire Hathaway's class B shares are the usual example, and platforms write the class differently: BRK.B on some, BRK-B on others, BRKB or BRK B on others. If a symbol returns nothing, try another separator or search by company name.

The book writes tickers in plain capitals with no $ sign. Trade examples use made-up stocks instead of real tickers (see [How to use this book](index.md)).

## Canadian listings

A stock listed on the Toronto Stock Exchange (TSX) can share a letter code with a US stock, so platforms mark the exchange. Two common ways:

- A prefix: TSX:RY (TradingView style).
- A suffix: RY.TO (Yahoo Finance style).

Some companies trade on both countries' exchanges under the same or different codes. Check the exchange and the currency on the quote before you buy. A Canadian listing is priced in CAD and the US listing in USD.

A Canadian depositary receipt (CDR) is a CAD-priced share that tracks a US stock, listed in Canada. It is covered in Norbert's gambit and CDRs<!-- link: ../02-accounts-currency-and-taxes/04-norberts-gambit-and-cdrs.md -->.

## Index symbols and the ETF that tracks them

An index is a number calculated from a basket of stocks. You cannot buy it directly. SPX is the symbol many platforms use for the S&P 500 index, and SPY is a different thing: an ETF that holds the stocks and trades like a share. Their prices differ, and the ETF has a fee and a tracking gap. Platforms differ in how they write an index (SPX, ^GSPC or $SPX), so check that the chart says "index" and not "ETF". See Indexes, sectors and market cap<!-- link: ../01-how-markets-work/10-indexes-sectors-and-market-cap.md -->.

## Option symbols

An option symbol follows the Options Symbology Initiative format, which has 21 characters:

| Part | Length | Meaning |
|---|---|---|
| Root | 6 | The underlying's symbol, padded with spaces on the right |
| Expiry | 6 | YYMMDD |
| Type | 1 | C for a call, P for a put |
| Strike | 8 | The strike price times 1,000, padded with zeros on the left |

The format is described on [IBKR's symbology page](https://ibkb.interactivebrokers.com/article/972). Take a made-up example with a made-up underlying, ABC:

`ABC   261218C00050000`

The root is ABC plus three spaces. The expiry is 261218, which is December 18, 2026. The C means a call. The strike is 00050000, which is 50,000 divided by 1,000, so US$50.00. Many platforms drop the spaces and show ABC261218C00050000. A strike of US$12.50 would be 00012500.

Options are taught in part 15, starting with The options chain and moneyness<!-- link: ../15-options/03-the-chain-and-moneyness.md -->.

## Futures symbols

A futures symbol is the product code, then a month letter, then a year digit. The month letters are:

| Letter | F | G | H | J | K | M | N | Q | U | V | X | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |

ESZ6 is the ES product (the E-mini S&P 500 future), expiring in December (Z), in a year ending in 6 (2026 if you read it in 2026). Some platforms write two year digits: ESZ26. The roll between expiry months is in Expiry and rolling<!-- link: ../14-futures/04-expiry-and-rolling.md -->, and the main index futures are in Index futures: ES, MES, NQ and MNQ<!-- link: ../14-futures/03-index-futures.md -->.

## Crypto pairs and currency pairs

A crypto pair names the coin and the currency it is priced in: BTC-USD is the price of one bitcoin in US dollars. Some platforms write BTC/USD or BTCUSD. Crypto is covered in What bitcoin is<!-- link: ../18-crypto/01-what-bitcoin-is.md -->.

A currency pair is written base/quote. USD/CAD tells you how many Canadian dollars one US dollar costs. If USD/CAD is 1.40 (a made-up number), then US$1 buys C$1.40, and C$1 buys 1/1.40 = US$0.714. When USD/CAD rises, the US dollar gets stronger against the Canadian dollar. See Forex basics<!-- link: ../17-commodities-forex-and-reits/04-forex-basics.md -->.

## Abbreviations the book uses

| Short form | Meaning |
|---|---|
| ATR | Average true range, a measure of typical price movement |
| CDR | Canadian depositary receipt |
| EMA | Exponential moving average |
| EPS | Earnings per share |
| ETF | Exchange-traded fund |
| IV | Implied volatility, the volatility an option's price implies |
| OHLC | Open, high, low, close: the four prices of a bar |
| P/E | Price-to-earnings ratio |
| RSI | Relative strength index |
| SMA | Simple moving average |
| VWAP | Volume-weighted average price |
| ET | Eastern Time, Toronto's time zone |

Each one is defined in full in the lesson that first uses it, and the reference pages list them all.
