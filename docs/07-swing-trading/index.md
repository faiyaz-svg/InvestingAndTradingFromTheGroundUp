# Part 7: Swing trading

Trades held for days to weeks: finding setups, entries, stops, targets and a weekly routine.

Before this part: Parts 3 to 5.

<!-- lessons:start -->
## Lessons

1. [What swing trading is](01-what-swing-trading-is.md) (idea)
2. [Scanners and watchlists](02-scanners-and-watchlists.md) (skill)
3. [Market regime filters](03-market-regime-filters.md) (strategy)
4. [Trend pullback setups](04-trend-pullback-setups.md) (strategy)
5. [Breakouts and bases](05-breakouts-and-bases.md) (strategy)
6. [Short-term mean reversion](06-short-term-mean-reversion.md) (strategy)
7. [Entries, stops and targets](07-entries-stops-and-targets.md) (skill)
8. [Managing the trade](08-managing-the-trade.md) (skill)
9. [A weekly swing routine](09-weekly-swing-routine.md) (skill, review)

<!-- lessons:end -->

## Cheat sheet

Swing trade: held 2 to 20 trading days, decided after the close, risk 1% per trade sized from the stop ([Position sizing](../03-risk-and-position-sizing/04-fixed-fractional-sizing.md)). All numbers below are the book's own choices, not tested standards.

### Regime filter

| Test | Favourable | Unfavourable |
|---|---|---|
| Trend | Index closes above its 200-day SMA | Closes below it |
| Breadth | More than 50% of the universe above its 50-day SMA | 50% or fewer |
| Volatility | Daily index moves mostly under 2% | Several moves of 2% or more this week |

All favourable: full size. Trend favourable and one other not: half size. Trend unfavourable: no new pullback or breakout longs.

### Universe filters

Price at least US$10, average volume at least 1 million shares, average dollar volume at least US$20 million, market cap at least US$2 billion, ATR percent 2% to 6%. Exclude earnings inside the hold window and pending deals.

### The three setups

| | Trend pullback | Breakout from a base | Short-term mean reversion |
|---|---|---|---|
| Filter | Close above a rising 50-day SMA | Base of 20 or more bars, depth 15% or less, rising 50-day SMA | Close above the 200-day SMA |
| Trigger | First close above the prior bar's high after 3 or more down closes and a touch of the 20-day EMA | Close above the pivot, volume 1.5 times the 20-day average, close in the upper half | First close with RSI(2) under 10 |
| Entry | Buy stop 0.01 above the trigger bar's high, next session only | Next open, skip if more than 2 ATR above the pivot | Next open |
| Stop | Pullback low minus 0.25 ATR | Pivot minus 1 ATR | Entry minus 2 ATR |
| Target | Prior high, skip if under 2R | Entry plus 3R | First close above the 5-day SMA |
| Other exit | Time stop at 10 days | Any close under the pivot, exit at the next open; time stop at 15 days | Time stop at 5 days |

### Formulas

- Shares = floor(0.01 x account / (entry - stop)).
- Break-even win rate for a reward of \(r\) R and a loss of 1R: \(1 / (1 + r)\). At 2R: 33.3%. At 3R: 25%.
- Average dollar volume = average volume x price. ATR percent = ATR / close.
- Portfolio heat = sum of shares x (price - stop), divided by the account.

### Managing

- The stop moves only toward profit. Never widen it.
- Exit choices: fixed target, trailing stop (highest close minus 2 ATR), indicator exit (close under the 20-day EMA). Measure them in your journal.
- A stop fills at the open if the open is past it. A gap can cost more than 1R.
- Check the earnings calendar when you scan. Sell before the report unless your plan accepts a loss above 1R.

### Weekly routine

Sunday: review the journal (15 min), regime and earnings calendar (8), scan and watchlist (7). Weekdays after the close: stops, fills, scan, orders (12). Before the open: check orders and news (3). Paper block 2: 20 swing trades of one setup, then continue to 30 before going live.

### What tests found

| Idea | Source | Finding in one line |
|---|---|---|
| Trend filters | Faber (2007) | A 10-month average rule lowered drawdowns versus buy and hold in that paper |
| Time-series momentum | Moskowitz, Ooi and Pedersen (2012) | A contract's own past 1 to 12 month return predicted its next return in 58 futures |
| 52-week high | George and Hwang (2004) | Nearness to the high predicted returns over 6 months and did not reverse |
| Short-term reversal | Jegadeesh (1990), Lehmann (1990) | Losers of the past month or week tended to beat past winners |
| Reversal and liquidity | Nagel (2012) | Reversal returns rose when the VIX was high |
| RSI(2) | Connors and Alvarez (2009) | A trading book, not peer-reviewed, tests not independently replicated as far as found |
| Stops | Kaminski and Lo (2014) | A stop lowers expected return in a random walk and can raise it with momentum |
