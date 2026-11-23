# Part 19: Data, flows and forecasting

Free data sources, insider and fund filings, short interest, COT, options flow, forecasting and prediction markets.

Before this part: Parts 9, 14 and 15.

<!-- lessons:start -->
## Lessons

1. [Free data sources and their licences](01-free-data-sources.md) (data)
2. [Insider trades and Form 4](02-insider-trades-form-4.md) (data)
3. [13F holdings](03-13f-holdings.md) (data)
4. [Short interest and borrow](04-short-interest-and-borrow.md) (data)
5. [The Commitments of Traders report](05-commitments-of-traders.md) (data)
6. [Options flow](06-options-flow.md) (data)
7. [Base rates, calibration and forecast logs](07-base-rates-calibration-and-forecast-logs.md) (skill)
8. [Prediction markets](08-prediction-markets.md) (idea, review)

<!-- lessons:end -->

## Cheat sheet

### Sources and what they ask

| Source | Key or header | Reuse (as of 2026) |
|---|---|---|
| SEC EDGAR APIs | User-Agent with your contact details, 10 requests per second | Filings are public documents |
| FRED | Free API key | Some series are copyrighted (S&P 500: ask S&P Dow Jones Indices) |
| BLS, BEA, Treasury Fiscal Data | BEA API: free UserID | Each agency states its terms: read them |
| CFTC | None | Check the CFTC notice before republishing |
| yfinance | None | Unofficial, and Yahoo's API is for personal use |

### Filings and reports, and their delay

| Data | Who | Timing | Shows | Does not show |
|---|---|---|---|---|
| Form 4 | Officers, directors, owners of more than 10% | Within 2 business days of the trade | Trades with a code (P, S, A, M, F, D, G) | Why, or anything before it was filed |
| 13F | Managers with US$100 million or more in 13(f) securities | Within 45 days after quarter end | Long US-listed positions at quarter end | Shorts, most derivatives, timing |
| Short interest | FINRA member firms | Twice a month, about 11 days from count to release | Shares sold short | Who, or covering since the count |
| COT | CFTC | Tuesday data, Friday 3:30 p.m. ET (twice weekly planned, announced October 27, 2026) | Positions by trader group | Purpose, entry prices |
| Options flow | Vendors, from the tape | Real time | Volume, price, size | Opening or closing, who, why |

### Formulas

| Name | Formula |
|---|---|
| Days to cover | short interest / average daily volume |
| Short percent of float | short interest / float |
| Borrow cost | value x annual rate x days / 365 |
| Net position (COT) | long - short |
| Option premium | contracts x price x 100 |
| Brier score | mean of (forecast - outcome)^2, lower is better, 0.25 for always 50% |
| Contract break-even | ask + fee |
| Contract EV | your probability - (ask + fee) |

### Form 4 codes

P purchase, S sale, A award, M option exercise, F tax or exercise paid in shares, D back to the company, G gift, J other (footnoted).

### Forecasting checklist

1. Find the base rate in a reference class.
2. Move it for reasons you can name, and write them down.
3. Write the probability and the date before the event.
4. Score with the Brier score after 50 or more forecasts, and check calibration in buckets.
5. Never edit a logged row.
