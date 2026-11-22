# Part 14: Futures

Contracts, margin and leverage, index futures, rolling, contango and futures from Canada.

Before this part: Parts 3 and 12.

<!-- lessons:start -->
## Lessons

1. [What futures are](01-what-futures-are.md) (idea)
2. [Margin, leverage and mark to market](02-margin-leverage-and-mark-to-market.md) (idea)
3. [Index futures: ES, MES, NQ and MNQ](03-index-futures.md) (idea)
4. [Expiry and rolling](04-expiry-and-rolling.md) (skill)
5. [Contango, backwardation and basis](05-contango-backwardation-and-basis.md) (idea)
6. [Futures hours and sessions](06-futures-hours-and-sessions.md) (skill)
7. [Futures in Canada](07-futures-in-canada.md) (canada, review)

<!-- lessons:end -->

## Cheat sheet

Contract numbers are CME Group and Montreal Exchange specs as of 2026. Margins below are made-up examples.

| Contract | Multiplier | Tick | Tick value |
|---|---|---|---|
| ES (E-mini S&P 500) | US$50 | 0.25 | US$12.50 |
| MES (Micro S&P 500) | US$5 | 0.25 | US$1.25 |
| NQ (E-mini Nasdaq-100) | US$20 | 0.25 | US$5.00 |
| MNQ (Micro Nasdaq-100) | US$2 | 0.25 | US$0.50 |
| SXF (S&P/TSX 60, Montreal) | C$200 | 0.10 | C$20 |

| Item | Formula |
|---|---|
| P&L, long | \( (P_{\text{exit}} - P_{\text{entry}}) \times M \times n \) |
| Notional | \( P \times M \times n \) |
| Leverage | notional / margin posted |
| Daily mark to market | \( E_t = E_{t-1} + (S_t - S_{t-1}) \times M \times n \) |
| Contracts by risk | \( \lfloor f A / (T \times V) \rfloor \), with \(T\) in ticks and \(V\) the tick value |
| Fair value | \( F = S (1 + (r - d) T) \) |
| Basis | spot minus futures (check the sign convention) |

Rules and checklists:

- Margin is a deposit, not a loan, and losses can exceed it.
- A margin call happens when equity falls below maintenance. Restore to initial.
- Size by the stop in ticks, never by what margin allows.
- Index futures expire on the third Friday of March, June, September and December. Roll about a week before, when volume moves.
- Shift stops and targets across a roll by the spread between contracts.
- Back-adjusted charts change old prices. Check live prices before trading a level.
- Futures trade Sunday 6 p.m. to Friday 5 p.m. ET, with a break from 5 p.m. to 6 p.m. ET.
- Pick one session setting (all hours or regular hours) for all charts in your plan.
- Before trading in Canada: confirm the contract list and account types, the fee per side, and ask a professional about tax.

