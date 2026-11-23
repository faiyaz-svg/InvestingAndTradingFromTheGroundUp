# Part 16: Volatility and event trading

Realized and implied volatility, the VIX, regimes, earnings, data days, opex and rebalances.

Before this part: Part 15.

<!-- lessons:start -->
## Lessons

1. [Realized and implied volatility](01-realized-vs-implied-volatility.md) (idea)
2. [The VIX and the term structure](02-the-vix-and-term-structure.md) (data)
3. [Volatility regimes](03-volatility-regimes.md) (strategy)
4. [Earnings trades and IV crush](04-earnings-trades-and-iv-crush.md) (strategy)
5. [FOMC, CPI and other data days](05-fomc-cpi-and-data-days.md) (strategy)
6. [Opex, gamma and index rebalances](06-opex-gamma-and-index-rebalances.md) (strategy, review)

<!-- lessons:end -->

## Cheat sheet

### Formulas

| Item | Formula or rule |
|---|---|
| Realized volatility | Standard deviation of daily log returns x sqrt(252). Use 21 days for one month |
| One-day move from a yearly volatility | Volatility / sqrt(252). Over 30 days: volatility x sqrt(30/365) |
| Variance risk premium | Implied variance less later realized variance. In points: IV - realized |
| VIX | 30-day expected volatility of the S&P 500 from SPX option prices. Not tradable; VIX futures are |
| Roll cost in contango | (VIX - one-month future) / one-month future per month, if the VIX does not move |
| Regime rule (lesson 3) | 20-day realized volatility / median of the previous 120 days. Above 1.5 is high volatility |
| Volatility targeting | w = min(1, target / realized) |
| Implied move | At-the-money straddle price / stock price, from the expiry that holds the event |
| Event trade size | 1R / (risk per unit + expected slippage), rounded down |
| Dealer hedge | Contracts x 100 x gamma = shares to trade per US$1 move |

### Event checklist

| Step | Question |
|---|---|
| 1 | What is the event, and what time (ET)? Check the agency or company page |
| 2 | What does the market expect: implied move, or the one-day move from IV? |
| 3 | Plan: stand aside, hold, or trade the break? Write it the night before |
| 4 | Size by maximum loss or stop distance, with fees and event-day slippage |
| 5 | Exit: target, stop, and a time. Defined risk if the position is options |
| 6 | After: record the R and compare the actual move with the implied one |

### Calendar

| Event | When |
|---|---|
| CPI, jobs report | 8:30 a.m. ET, an hour before the open |
| FOMC statement | 2:00 p.m. ET |
| Earnings | Before the open or after the close; use the company's own date |
| Monthly opex | Third Friday of the month |
| S&P 500 rebalance | Effective before the open on the Monday after the third Friday of March, June, September, December |

### What tests found

| Idea | Result |
|---|---|
| Variance risk premium | Index variance swap rates sat above later realized variance (Carr and Wu 2009); the premium predicts returns (Bollerslev, Tauchen and Zhou 2009) |
| Volatility-managed portfolios | Good in-sample (Moreira and Muir 2017), weak in real time (Cederburg et al. 2020) |
| Pre-FOMC drift | Found by Lucca and Moench (2015), largely gone after 2015 (Kurov et al.) |
| Dealer gamma trading | No published test of a profitable rule that this book found |
| S&P 500 inclusion | About 3% in the 1980s, 7.4% in the 1990s, under 1% in the past decade (Greenwood and Sammon 2025) |
