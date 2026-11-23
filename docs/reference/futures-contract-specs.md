# Futures contract specs

The contract specs from [Index futures: ES, MES, NQ and MNQ](../14-futures/03-index-futures.md) and [Futures in Canada](../14-futures/07-futures-in-canada.md). A spec turns a quoted price into dollars. The multiplier is the dollar value of one index point, the tick size is the smallest price step, and the tick value is the tick size times the multiplier.

Specs and margins change, so check the exchange's contract page before you trade. The figures below are as of 2026.

## CME index futures

| | ES | MES | NQ | MNQ |
|---|---|---|---|---|
| Index | S&P 500 | S&P 500 | Nasdaq-100 | Nasdaq-100 |
| Size | E-mini | Micro E-mini | E-mini | Micro E-mini |
| Multiplier | US$50 | US$5 | US$20 | US$2 |
| Tick size | 0.25 | 0.25 | 0.25 | 0.25 |
| Tick value | US$12.50 | US$1.25 | US$5.00 | US$0.50 |
| Expiry months | Mar, Jun, Sep, Dec | same | same | same |
| Settlement | Cash | Cash | Cash | Cash |
| Hours (ET) | Sunday 6 p.m. to Friday 5 p.m., with a break from 5 p.m. to 6 p.m. Monday to Thursday | same | same | same |

Sources: CME Group's pages for [Micro E-mini S&P 500](https://www.cmegroup.com/markets/equities/sp/micro-e-mini-sandp-500.html), [E-mini S&P 500](https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.html), [E-mini Nasdaq-100](https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.html) and [Micro E-mini Nasdaq-100](https://www.cmegroup.com/markets/equities/nasdaq/micro-e-mini-nasdaq-100.html). Hours are from [CME Group trading hours](https://www.cmegroup.com/trading-hours.html) (as of 2026), as taught in [Futures hours and sessions](../14-futures/06-futures-hours-and-sessions.md). Hours can differ by contract and on holidays. CME quotes its hours in Central Time, and the Eastern Time hours stay the same through the year.

The expiry months are the quarterly cycle: March (H), June (M), September (U) and December (Z). [Expiry and rolling](../14-futures/04-expiry-and-rolling.md) covers the expiry rules, and [Tickers and symbols](../00-start-here/tickers-and-symbols.md) covers the month letters.

## Montreal Exchange index futures

| | SXF | SXM |
|---|---|---|
| Index | S&P/TSX 60 | S&P/TSX 60 |
| Size | Standard | Mini |
| Multiplier | C$200 per index point | C$50 per index point |
| Tick size | 0.10 index points (outright) | Not covered in the lesson |
| Tick value | C$20 (0.10 x C$200) | Not covered in the lesson |
| Expiry months | Mar, Jun, Sep, Dec | Not covered in the lesson |
| Settlement | Cash, through the Canadian Derivatives Clearing Corporation; final settlement on the third Friday of the contract month | Not covered in the lesson |
| Hours (ET) | Not covered in the lesson; they differ from Globex | Not covered in the lesson |

Sources: [Montreal Exchange, SXF](https://www.m-x.ca/en/markets/index-derivatives/sxf) and [Montreal Exchange, SXM](https://www.m-x.ca/envoi/produit/sxm_retail_en.html) (as of 2026). The lesson does not cover margin or the SXM tick size, so read the full specifications at [m-x.ca](https://www.m-x.ca) before you size a trade. Do not use a US multiplier for a Canadian contract: SXF is C$200, not US$.

## Value of a tick and a point

At an index level of 6,000 (a made-up level), one MES has a notional value of 6,000 x 5 = US$30,000, and one ES is 6,000 x 50 = US$300,000. Ten MES equal one ES in size. A move of \(x\) index points is \(x / 0.25\) ticks for the CME contracts. For the SXF, 5.0 points is 5.0 x C$200 = C$1,000 per contract, and for the SXM it is C$250.

## Margin

Margin is a deposit, not a loan. The exchange's clearinghouse sets a minimum for each product, CME Group publishes its margins on its website and changes them with volatility, and your broker can ask for more ([Margin, leverage and mark to market](../14-futures/02-margin-leverage-and-mark-to-market.md)). The book's lessons use made-up round numbers, so look up the current figure.

## Futures from Canada

Wealthsimple lists futures in micro, mini and standard sizes, with hours from Sunday 6 p.m. to Friday 5 p.m. ET and a one-hour break (as of 2026). The lesson does not say which accounts can hold futures, and does not state IBKR Canada's access, fees or margin. See [Futures in Canada](../14-futures/07-futures-in-canada.md) for the sources and the tax question to settle before your first trade.
