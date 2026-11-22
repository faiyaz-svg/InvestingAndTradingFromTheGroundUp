# Part 13: ETFs, portfolios and factors

How ETFs work, which to hold from Canada, allocation, rebalancing, portfolio theory and factors.

Before this part: Parts 2 and 12.

<!-- lessons:start -->
## Lessons

1. [How ETFs work](01-how-etfs-work.md) (idea)
2. [Index funds, fees and tracking](02-index-funds-fees-and-tracking.md) (idea)
3. [US-listed or Canadian-listed ETFs](03-us-vs-canadian-listed-etfs.md) (canada)
4. [Leveraged and inverse ETFs](04-leveraged-and-inverse-etfs.md) (idea)
5. [Asset allocation](05-asset-allocation.md) (skill)
6. [Diversification and correlation](06-diversification-and-correlation.md) (idea)
7. [Rebalancing](07-rebalancing.md) (skill)
8. [Modern portfolio theory](08-modern-portfolio-theory.md) (idea)
9. [Factor investing](09-factor-investing.md) (strategy)
10. [A long-term portfolio](10-a-long-term-portfolio.md) (canada, review)

<!-- lessons:end -->

## Cheat sheet

### Formulas

| Name | Formula | Notes |
|---|---|---|
| NAV per share | \((A - L) / N\) | Assets less liabilities over shares |
| Premium or discount | \((P - \text{NAV}) / \text{NAV}\) | Price above NAV is a premium |
| Fee over \(n\) years | \(V_0 (1 + g - f)^n\) | \(g\) return before fees, \(f\) expense ratio |
| Tracking difference | fund return minus index return | Over a year or more |
| Tracking error | \(\sqrt{12} \times \text{sd}(\text{monthly differences})\) | Steadiness of the gap |
| Round-trip spread cost | ask minus bid, over the midpoint | Paid each round trip |
| Leveraged fund, two days | \(L(r_1 + r_2) + L^2 r_1 r_2\) | Daily reset; gap to \(L\) times the index is \(L(L-1) r_1 r_2\) |
| Volatility decay | \(g_L \approx L\mu - L^2\sigma^2/2\) | Before fees and financing |
| Two-asset volatility | \(\sqrt{w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2 w_1 w_2 \rho \sigma_1\sigma_2}\) | Correlation \(\rho\) |
| Minimum-variance weight in A | \((\sigma_B^2 - \rho\sigma_A\sigma_B) / (\sigma_A^2 + \sigma_B^2 - 2\rho\sigma_A\sigma_B)\) | Two assets |
| Sharpe ratio | \((\mu_p - r_f) / \sigma_p\) | Higher is more return per unit of risk |
| Rebalancing trade | \(w^{*} V - H\) | Positive is a buy |
| Beta | \(\text{Cov}(r_i, r_m) / \text{Var}(r_m)\) | Slope of excess returns on the market's |
| Three-factor model | \(r - r_f = \alpha + b\,\text{MKT} + s\,\text{SMB} + h\,\text{HML} + \varepsilon\) | Fama and French, 1993 |

### Rules and checklists

- ETF price stays near NAV because authorized participants create shares when the price is above NAV and redeem them when it is below.
- Compare funds on fee, tracking difference and spread together.
- US stocks: a US-listed ETF in an RRSP avoids the 15% US withholding. In a TFSA the 15% is lost whichever listing you use, and brokers treat the FHSA the same way (check yours). Weigh the RRSP saving against the conversion cost.
- International stocks: prefer a fund that holds the stocks directly. A Canadian fund holding a US-listed international ETF has a second layer of withholding.
- Leveraged and inverse ETFs reset daily. Over longer periods the result depends on the path.
- Choose the mix by the dollar loss in a stress year that you could sit through.
- Correlations rise in bear markets. Stress-test with a high value.
- Rebalance by a calendar rule or a band (5 percentage points is common), use new money first, and rebalance in registered accounts before taxable ones.
- Optimizer weights are sensitive to noisy inputs. Use the ideas more than the exact numbers.
- Factor premiums were about 58% lower after publication in one study of 97 predictors (McLean and Pontiff, 2016).
- Location: US stocks in the RRSP, bonds in registered accounts, international stocks in a directly held Canadian-listed fund, the FHSA as its own goal.
- A written one-page plan: goal, mix, funds, accounts, rebalancing rule, contributions.

