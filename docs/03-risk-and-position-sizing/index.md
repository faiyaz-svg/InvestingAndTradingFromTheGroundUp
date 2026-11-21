# Part 3: Risk and position sizing

How much to risk, how many shares to buy, and how losses and drawdowns add up.

Before this part: Part 1. The math book's probability lessons (expected value) help.

<!-- lessons:start -->
## Lessons

1. [Risk first: the math of losses](01-risk-first.md) (idea)
2. [R-multiples](02-r-multiples.md) (idea)
3. [Win rate, payoff and expectancy](03-win-rate-payoff-and-expectancy.md) (idea)
4. [Position sizing with fixed fractional risk](04-fixed-fractional-sizing.md) (skill)
5. [Where to put the stop](05-where-to-put-the-stop.md) (skill)
6. [Slippage, gaps and costs](06-slippage-gaps-and-costs.md) (idea)
7. [Portfolio heat and correlation](07-portfolio-heat-and-correlation.md) (skill)
8. [Drawdowns and risk of ruin](08-drawdowns-and-risk-of-ruin.md) (idea)
9. [The Kelly criterion and fractional Kelly](09-kelly-and-fractional-kelly.md) (idea)
10. [Your trading plan](10-your-trading-plan.md) (skill, review)

<!-- lessons:end -->

## Cheat sheet

### Formulas

| Item | Formula | Notes |
|---|---|---|
| Gain to recover a loss | \(G = L / (1 - L)\) | 10% needs 11.1%, 50% needs 100%, 75% needs 300% |
| Risk per share | \(E - S\) (long), \(S - E\) (short) | Entry minus stop |
| R (initial risk) | \(R = N \times (E - S)\) | US$ lost if the stop fills at \(S\) |
| R-multiple | \(r = (X - E)/(E - S)\) | Short: \((E - X)/(S - E)\) |
| Win rate, payoff ratio | \(p = \text{wins}/\text{trades}\), \(b = W/L\) | \(W\) and \(L\) are averages in R |
| Expectancy | \(E = pW - (1 - p)L\) | R per trade; times US$ per R for dollars |
| Break-even win rate | \(1/(1 + b)\) | b = 2 gives 33.3% |
| Standard error of win rate | \(\sqrt{p(1 - p)/n}\) | 40 trades at 45% is 7.9 points |
| Shares (fixed fractional) | \(\lfloor fA/(E - S) \rfloor\) | Round down. CAD account: divide the risk by the US$ rate first |
| True range | \(\max(H - L,\ \lvert H - C_{prev} \rvert,\ \lvert L - C_{prev} \rvert)\) | ATR is the mean of 14 |
| ATR stop | \(S = E - k \times ATR\) | k = 2 is a common start |
| Stop fill in R | \(-(E - F)/(E - S)\) | \(F\) is the real fill |
| Cost in R | \(c/(E - S)\) | Tight stops pay more per R |
| Open risk, heat | \(N(P - S)\), \(\sum \text{open risk}/A\) | From the current price to the stop |
| Effective bets | \(n/(1 + (n - 1)\rho)\) | Four stocks at 0.8 correlation are 1.18 bets |
| Drawdown | \((\text{peak} - \text{equity})/\text{peak}\) | Maximum drawdown is the largest |
| Risk of ruin (even money) | \(((1 - p)/p)^N\) | N is account divided by loss per bet |
| Kelly fraction | \(f^* = p - (1 - p)/b\) | Use half or less |

### Rules in this part

1. Decide the loss before the profit: stop first, then size.
2. Put the stop where the idea is wrong (structure, or ATR when the chart has no level), with a buffer. Never widen it after entry.
3. Size from the stop and round down. The loss at the stop should be a fixed percent of the account (1% or less while learning).
4. Count slippage, gaps and costs in R. If a gap can cost 2R, size for the gap.
5. Cap total heat and the risk in any one sector.
6. Plan drawdown steps in advance: smaller risk at one level, stop and review at the next.
7. Treat Kelly as a ceiling. Risk a small fraction of it.

### Checklist before each trade

- Stop written down and sized from it?
- Reward at least the plan's minimum in R, after costs?
- Heat and group caps still met?
- Daily, weekly and drawdown limits clear?
