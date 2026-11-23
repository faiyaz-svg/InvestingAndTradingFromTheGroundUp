# Part 15: Options

Calls and puts, pricing, the Greeks, implied volatility, the main strategies and options in Canadian accounts.

Before this part: Parts 3 and 14. The math book's normal distribution lesson helps.

<!-- lessons:start -->
## Lessons

1. [Calls and puts](01-calls-and-puts.md) (idea)
2. [Payoff diagrams](02-payoff-diagrams.md) (skill)
3. [The options chain and moneyness](03-the-chain-and-moneyness.md) (skill)
4. [What sets an option's price](04-what-sets-an-option-price.md) (idea)
5. [Put-call parity](05-put-call-parity.md) (idea)
6. [Delta and gamma](06-delta-and-gamma.md) (idea)
7. [Theta, vega and rho](07-theta-vega-and-rho.md) (idea)
8. [Implied volatility](08-implied-volatility.md) (idea)
9. [Covered calls and cash-secured puts](09-covered-calls-and-cash-secured-puts.md) (strategy)
10. [Vertical spreads](10-vertical-spreads.md) (strategy)
11. [Straddles and strangles](11-straddles-and-strangles.md) (strategy)
12. [Iron condors and butterflies](12-iron-condors-and-butterflies.md) (strategy)
13. [Calendars and diagonals](13-calendars-and-diagonals.md) (strategy)
14. [Assignment, exercise and 0DTE](14-assignment-exercise-and-0dte.md) (skill)
15. [Options in Canadian accounts](15-options-in-canadian-accounts.md) (canada, review)

<!-- lessons:end -->

## Cheat sheet

Prices are per share; one contract is 100 shares. Buy at the ask, sell at the bid.

### Terms and rules

| Item | Rule |
|---|---|
| Contract cost | Premium x 100 |
| Call, put | Right to buy, right to sell at the strike |
| Intrinsic value | Call: max(S - K, 0). Put: max(K - S, 0) |
| Time value | Premium less intrinsic value |
| Put-call parity | C - P = S - K e^(-rT) (lesson 5) |
| Expected move | S x IV x sqrt(T). One day: IV / sqrt(252) |
| Greeks | Delta: change per US$1 in the stock. Gamma: change in delta. Theta: loss per day. Vega: per volatility point. Rho: per percentage point of rate |

### Strategies on the chain (lessons 9 to 13)

| Strategy | Net | Max profit | Max loss | Breakeven |
|---|---|---|---|---|
| Covered call (shares 50.20, sell 52.50 call 2.10) | Debit 48.10 | US$440 | US$4,810 | 48.10 |
| Cash-secured put (sell 47.50 put 1.80) | Credit 1.80 | US$180 | US$4,570 | 45.70 |
| Bull call spread 50/55 | Debit 2.15 | US$285 | US$215 | 52.15 |
| Bull put spread 50/45 | Credit 1.30 | US$130 | US$370 | 48.70 |
| Long straddle 50 | Debit 6.20 | Unlimited | US$620 | 43.80 and 56.20 |
| Long strangle 47.50/52.50 | Debit 4.10 | Unlimited | US$410 | 43.40 and 56.60 |
| Iron condor 45/47.50/52.50/55 | Credit 1.20 | US$120 | US$130 | 46.30 and 53.70 |
| Call butterfly 47.50/50/52.50 | Debit 0.60 | US$190 | US$60 | 48.10 and 51.90 |
| Call calendar 50 (Jan/Feb) | Debit 0.80 | About US$119 (model) | US$80 | About 47.13 and 53.66 |

Debit spread: max profit (width - debit) x 100, max loss debit x 100. Credit spread: max profit credit x 100, max loss (width - credit) x 100.

### Greeks of each position (per contract)

| Position | Delta | Gamma | Theta per day | Vega per point |
|---|---|---|---|---|
| Covered call | +56.64 | -5.40 | +1.78 | -9.87 |
| Bull call spread | +25.71 | +0.21 | -0.39 | +1.02 |
| Long straddle | +13.34 | +10.25 | -3.31 | +19.75 |
| Iron condor | -3.42 | -1.48 | +0.30 | -2.40 |
| Call calendar | +0.94 | -1.35 | +0.50 | +2.11 |

### Before every option trade

1. Max loss with fees (both legs, opening and closing) is at most your 1R.
2. The bid and ask spread of each leg, and the order placed near the middle.
3. Assignment: which leg is short, and the ex-dividend date.
4. The expiry day plan: close before the last session if a short strike is near the stock.
5. IV against the move you expect, and any event before expiry.
6. Your account type allows the strategy (lesson 15).

### Expiry and Canada

| Item | Rule |
|---|---|
| Exercise by exception | In the money by US$0.01 or more is exercised unless the holder says no (OCC) |
| Early exercise of a call | Likely if the dividend is larger than the time value plus interest |
| 0DTE | Gamma peaks near expiry. 1R is the premium plus fees |
| Wealthsimple (as of 2026) | Long options, covered calls in TFSA and RRSP. Spreads need a margin account |
| Tax | Ask a professional. Capital or income depends on the facts (IT-479R, archived) |

