# Part 8: Day trading

Trades opened and closed the same day: premarket prep, intraday setups, the tape and daily limits.

Before this part: Parts 3 to 5, and part 7 helps.

<!-- lessons:start -->
## Lessons

1. [How day trading differs](01-how-day-trading-differs.md) (idea)
2. [Premarket prep](02-premarket-prep.md) (skill)
3. [Intraday charts and VWAP](03-intraday-charts-and-vwap.md) (skill)
4. [The opening range breakout](04-opening-range-breakout.md) (strategy)
5. [VWAP reclaims and fades](05-vwap-reclaims-and-fades.md) (strategy)
6. [News, momentum and halts](06-news-momentum-and-halts.md) (strategy)
7. [Level 2 and time and sales](07-level-2-and-time-and-sales.md) (skill)
8. [Execution costs and scalping](08-execution-costs-and-scalping.md) (idea)
9. [A day trading routine and limits](09-day-trading-routine-and-limits.md) (skill, review)

<!-- lessons:end -->

## Cheat sheet

### The day (ET)

| Time | What to expect |
|---|---|
| Before 9:15 a.m. | Prep: gap, catalyst, premarket volume, five levels, if-then line |
| 9:30 to 10:30 a.m. | The open: most volume, most setups |
| 11:30 a.m. to 2:00 p.m. | Midday: low volume, narrow ranges |
| 3:30 to 4:00 p.m. | The close: NYSE closing-auction orders due by 3:50 p.m. |

### Rules at a glance (made-up thresholds, test on paper)

| Setup | Entry | Stop | Target |
|---|---|---|---|
| Opening range breakout | Buy stop 0.01 above the first 5-minute bar's high (short: below the low), direction from the bar's colour | 0.02 beyond the other side of the range | 2R, or exit at 3:55 p.m. |
| VWAP reclaim | Buy stop 0.01 above the reclaim bar's high, after 12 or more closes below VWAP | 0.02 below the lowest low of the six bars before the reclaim bar | 2R |
| VWAP fade (short) | Sell stop 0.01 below the rejection bar's low, 2% or more above VWAP | 0.02 above the rejection bar's high | VWAP at entry plus 0.01 |
| News first pullback | Buy stop 0.01 above the first push | 0.02 below the pullback low | 2R |

### Formulas

| Formula | Meaning |
|---|---|
| Shares = floor(risk amount / (E - S)), capped by floor(buying power / E) | Size from risk, then check buying power |
| room = (L - E) / (E - S) | Distance to the nearest level, in R |
| VWAP = sum(TP x V) / sum(V), TP = (H + L + C) / 3 | Session VWAP |
| c = s + 2f + 2k, c_R = c / stop | Round-trip cost per share and in R |
| p* = (1 + c_R) / (T + 1) | Break-even win rate after costs |
| I = (B - A) / (B + A) | Book imbalance |

### Halts and restrictions (as of 2026)

| Rule | Detail |
|---|---|
| LULD band | Tier 1 above US$3.00: 5%. Tier 2 above US$3.00: 10%. Both 20% from US$0.75 to US$3.00. Bands double 3:35 to 4:00 p.m. for Tier 1 and for Tier 2 at or below US$3.00 |
| LULD pause | At a band edge for 15 seconds, then a 5-minute pause (can be extended) |
| Rule 201 | A fall of 10% from the prior close: short sales above the national best bid only, for that day and the next |

### Daily limits

| Limit | Example |
|---|---|
| Daily loss limit | 2R, or 2% of the account |
| Trade count | At most 4 trades a day |
| Cooling-off | 15 minutes after two losses in a row |
| Window | No new trades after 11:30 a.m. ET |
| Paper block 3 | 20 day trades of one setup, with costs and slippage |
