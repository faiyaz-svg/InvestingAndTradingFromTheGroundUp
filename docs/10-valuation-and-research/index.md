# Part 10: Valuation and research

Multiples, enterprise value, free cash flow, discount rates, DCFs and writing a stock pitch.

Before this part: Part 9. The math book's lessons on present value and NPV help.

<!-- lessons:start -->
## Lessons

1. [Price multiples](01-multiples.md) (skill)
2. [Enterprise value and EV/EBITDA](02-enterprise-value-and-ev-ebitda.md) (skill)
3. [Free cash flow](03-free-cash-flow.md) (skill)
4. [Discount rates, CAPM and WACC](04-discount-rates-capm-and-wacc.md) (skill)
5. [A DCF step by step](05-dcf-step-by-step.md) (skill)
6. [Reverse DCF and market expectations](06-reverse-dcf-and-expectations.md) (skill)
7. [Comparables and industry KPIs](07-comparables-and-industry-kpis.md) (skill)
8. [Moats and qualitative research](08-moats-and-qualitative-research.md) (skill)
9. [Writing a stock pitch](09-writing-a-stock-pitch.md) (skill, review)

<!-- lessons:end -->

## Cheat sheet

| Measure | Formula | Northwind (US$50.00) |
|---|---|---|
| P/E | price / EPS (trailing: last 4 quarters, forward: next 12 months or year) | 31.1 trailing, 25.1 forward |
| Earnings yield | EPS / price | 3.22% |
| P/S | market cap / revenue | 4.28 |
| P/B | market cap / book equity | 7.58 |
| PEG | P/E / expected EPS growth in % | 2.07 at 15% |
| Enterprise value | diluted equity value + debt + preferred + minority interest - cash | 5,220 |
| EV/EBITDA, EV/sales | EV / EBITDA, EV / revenue | 19.3, 4.54 |
| Levered FCF | CFO - capex | 125 |
| Unlevered FCF | EBIT x (1 - t) + D&A - capex - change in NWC | 106.25 |
| Cost of equity (CAPM) | risk-free rate + beta x ERP | 9.42% |
| Cost of debt after tax | pre-tax rate x (1 - t) | 3.9% |
| WACC | E/(E+D) x cost of equity + D/(E+D) x after-tax cost of debt | 9.14% (9.1% used) |
| Terminal value (Gordon) | UFCF in year N x (1 + g) / (WACC - g) | 5,124.8 |
| Terminal value (exit multiple) | EBITDA in year N x multiple | 6,790.7 at 13 times |
| Equity value per share | (EV - debt + cash) / diluted shares | 39.42 (base DCF) |
| Implied growth (reverse DCF) | the growth that makes the DCF equal the price | 19.4% a year |
| Economic profit | NOPAT - WACC x invested capital | 107.1 |

Rules to remember:

- Match the numerator and the denominator: EV goes with EBITDA, EBIT and sales; market cap goes with net income and EPS.
- Use diluted shares (options by the treasury stock method, plus RSUs).
- Discount unlevered FCF at the WACC. Discount levered FCF at the cost of equity.
- Terminal growth stays below the discount rate and the economy's long-run growth. The terminal value is 75% to 84% of the value in Northwind DCFs.
- The equity risk premium and beta are assumptions. Show a sensitivity table, not a single value.
- Rating or target above the price is not enough: compare the upside with your required return.

Industry measures:

| Industry | Measures |
|---|---|
| Software | ARR, net revenue retention = (start + expansion - contraction - churn) / start, rule of 40 = growth % + FCF margin % |
| Banks | NIM = net interest income / average earning assets, efficiency ratio = non-interest expense / revenue, CET1 = CET1 capital / risk-weighted assets |
| Retail | Same-store sales growth, inventory turns = COGS / inventory |
| Energy | Proved reserves, reserve life = reserves / output, breakeven price |

Stock pitch checklist: thesis, variant view, catalysts, valuation range with probabilities, risks, what would change your mind.

