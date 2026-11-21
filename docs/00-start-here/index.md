# How to use this book

This book is for one kind of reader: a computer science student or graduate in Canada who has traded a little and wants to understand markets properly. You may want to invest for the long term, swing trade or day trade, read company financials and economic data, try options, futures or crypto, or work in finance. You know programming and some statistics. You do not need to know finance terms: each one is explained when it first appears.

## How the book is organised

The book has 22 parts in six groups. Each part is a folder with an overview page (with a cheat sheet) and a set of short lessons. The parts run in reading order, but later groups can be read in different orders (see the paths below). The table on the [home page](../index.md) links each part.

| Code | Part | What it covers |
|---|---|---|
| **Foundations** | | |
| MKT | How markets work | What a share is, where orders go, who takes the other side, and how to read a quote. |
| ACCT | Accounts, currency and taxes | Trading US stocks from Canada: which account, USD or CAD, withholding tax, CRA rules and records. |
| RISK | Risk and position sizing | How much to risk, how many shares to buy, and how losses and drawdowns add up. |
| MIND | Psychology, the journal and paper trading | The habits that keep a plan working: rules, a trade journal, reviews and a paper account. |
| **Trading** | | |
| CHRT | Reading charts | Candles, trend, levels, volume and the common indicators, with what tests found about patterns. |
| ICT | ICT and smart money concepts, tested | Liquidity, fair value gaps, order blocks and sessions: what each idea says and what tests found. |
| SWNG | Swing trading | Trades held for days to weeks: finding setups, entries, stops, targets and a weekly routine. |
| DAY | Day trading | Trades opened and closed the same day: premarket prep, intraday setups, the tape and daily limits. |
| **Companies and economy** | | |
| FIN | Company financials | Reading 10-Ks and 10-Qs: the three statements, margins, returns, debt, dilution and earnings quality. |
| VAL | Valuation and research | Multiples, enterprise value, free cash flow, discount rates, DCFs and writing a stock pitch. |
| MACRO | Macro and economic data | The Fed, inflation, jobs and growth reports, the economic calendar and how markets react. |
| BOND | Bonds and the yield curve | Bond prices and yields, Treasuries, the yield curve, duration, credit and bond ETFs. |
| **Investing and derivatives** | | |
| ETF | ETFs, portfolios and factors | How ETFs work, which to hold from Canada, allocation, rebalancing, portfolio theory and factors. |
| FUT | Futures | Contracts, margin and leverage, index futures, rolling, contango and futures from Canada. |
| OPT | Options | Calls and puts, pricing, the Greeks, implied volatility, the main strategies and options in Canadian accounts. |
| VOL | Volatility and event trading | Realized and implied volatility, the VIX, regimes, earnings, data days, opex and rebalances. |
| **Markets, data and quant** | | |
| CMDTY | Commodities, forex and REITs | Oil, gold and commodity ETFs, currencies and USD/CAD, and real estate through REITs. |
| CRYPTO | Crypto | Bitcoin, Ethereum and stablecoins, buying crypto in Canada, crypto ETFs, perps and the risks. |
| DATA | Data, flows and forecasting | Free data sources, insider and fund filings, short interest, COT, options flow, forecasting and prediction markets. |
| QUANT | Quant track in Python | pandas for prices and fundamentals, returns and volatility, regression, factor sorts and how backtests mislead. |
| **History and careers** | | |
| HIST | Crashes, scams and case studies | What broke in the big crashes and blow-ups, the risk lesson from each, and how to spot scams. |
| CAREER | Careers, interviews and AI | Finance jobs and licences, building a track record, interview questions and using AI for research. |

## Suggested paths

Read the Foundations group first, in order (MKT, ACCT, RISK, MIND). Every other part assumes it. After that, pick the path that fits your goal.

The trader path:

1. CHRT, then SWNG
2. DAY, if you want intraday trading
3. VOL, then FUT and OPT
4. ICT, once you can read charts without it
5. DATA and QUANT, to test your own ideas

The investor path:

1. FIN, then VAL
2. MACRO, then BOND
3. ETF
4. CMDTY and CRYPTO, if they interest you
5. DATA

The career path:

1. FIN and VAL
2. MACRO and BOND
3. OPT and QUANT
4. HIST
5. CAREER

The paths overlap, and you can mix them. Each part overview says what that part needs first.

## How a lesson is laid out

Every lesson takes about 30 minutes and has the same shape.

- The tag line names the kind of lesson (idea, skill, strategy, data, Canada, code, case study or career) and the part code.
- The first sentence says what you can do after the lesson.
- The idea starts with a situation and numbers, then the plain explanation, then the name of the thing.
- How it works gives the method as numbered steps, with every formula explained symbol by symbol and a worked example you can check with a calculator.
- Charts, figures and diagrams appear where they help. Some lessons have an In code box with a short Python snippet. It is optional.
- A For Canadians box covers accounts, taxes and brokers where they matter, with a source and the year.
- Common mistakes lists up to three, each with its fix.
- Try it has 3 to 5 exercises with answers you can open to check.
- Practice today is a 10 minute task, and Key terms lists the new words.

The last lesson of each part ends with a part check of 6 to 8 questions.

## The 30-minute day

A day has three blocks: 15 minutes reading, 5 minutes on Try it and 10 minutes of practice. [The 30-minute routine](the-30-minute-routine.md) shows how to fit it around the market day.

## Where the practice lives

The practice is chart drills, paper trading and a trade journal. [Chart drills](../practice/chart-drills.md) show a made-up chart and ask a question about it. Two more practice pages are planned: Paper trading and The trade journal. Until they exist, parts 4, 7, 8, 14, 15 and 16 describe the same work in their own lessons.

## Tracking progress

Tick each lesson on [your progress page](../progress.md) when you finish it. On the website, ticks are saved in your browser only. In VS Code, change `[ ]` to `[x]` in `docs/progress.md`.

## Charts use made-up data

Real price history is licensed, so every price chart in the book is drawn from made-up data. The stocks are made up too ("Stock A", "Stock B"). Real tickers appear only for real facts, such as a filing or an index. Real numbers, such as a filing's revenue or a CPI release, are quoted in text with a source and a date.
