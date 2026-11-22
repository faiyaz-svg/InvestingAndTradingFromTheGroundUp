# Part 9: Company financials

Reading 10-Ks and 10-Qs: the three statements, margins, returns, debt, dilution and earnings quality.

Before this part: Part 1.

<!-- lessons:start -->
## Lessons

1. [Filings and EDGAR](01-filings-and-edgar.md) (data)
2. [The income statement](02-the-income-statement.md) (data)
3. [The balance sheet](03-the-balance-sheet.md) (data)
4. [The cash flow statement](04-the-cash-flow-statement.md) (data)
5. [How the three statements connect](05-how-the-statements-connect.md) (data)
6. [Margins and growth](06-margins-and-growth.md) (data)
7. [Returns on capital](07-returns-on-capital.md) (data)
8. [Debt, liquidity and solvency](08-debt-liquidity-and-solvency.md) (data)
9. [Shares, EPS, dilution and buybacks](09-shares-eps-dilution-and-buybacks.md) (data)
10. [GAAP, non-GAAP and earnings quality](10-gaap-non-gaap-and-earnings-quality.md) (data)
11. [Earnings season and earnings calls](11-earnings-season-and-calls.md) (data, review)

<!-- lessons:end -->

## Cheat sheet

### Filings

| Form | Holds | When |
|---|---|---|
| 10-K | Audited annual report | Yearly |
| 10-Q | Unaudited quarter | Three a year |
| 8-K | An event (Item 2.02 earnings release, 5.02 officer change) | When it happens |

10-K Items to know: 1 Business, 1A Risk Factors, 7 MD&A, 7A Market Risk, 8 Financial Statements, 9A Controls. Canada: SEDAR+.

### Formulas

| Measure | Formula | Notes |
|---|---|---|
| Gross profit | \( R - C \) | Revenue minus COGS |
| EBIT | Gross profit minus operating expenses | Operating income |
| EBITDA | \( \text{EBIT} + D \) | \(D\) is depreciation and amortization |
| Net income | \( (\text{EBIT} - I)(1 - t) \) | \(I\) interest, \(t\) tax rate |
| Margin | Profit measure \( / R \) | Gross, operating, EBITDA, net |
| CAGR | \( (X_n / X_0)^{1/n} - 1 \) | \(n\) years |
| Balance sheet | \( A = L + E \) | Must always hold |
| Working capital | \( CA - CL \) | Current assets minus current liabilities |
| CFO (indirect) | \( NI + D + S + \Delta W \) | \(S\) stock-based pay, \(\Delta W\) working capital change |
| Free cash flow | \( \text{CFO} - \text{capex} \) | After stock-based pay: subtract \(S\) |
| ROE, ROA | \( NI / \bar{E} \), \( NI / \bar{A} \) | Average balances |
| ROIC | \( \text{NOPAT} / \bar{IC} \) | NOPAT = EBIT(1 - t); IC = debt + equity - cash |
| DuPont | Net margin x asset turnover x equity multiplier | Equals ROE |
| Current, quick ratio | \( CA / CL \), (cash + receivables) \( / CL \) | Liquidity |
| Debt to equity | \( D / E \) | Total debt over equity |
| Net debt | Debt minus cash | Also net debt over EBITDA |
| Interest coverage | EBIT \( / I \) | Times |
| Basic EPS | \( (NI - P) / \bar{N} \) | Weighted average shares |
| Net new option shares | \( n - nK/\bar{P} \) | Treasury stock method; zero if \(K > \bar{P}\) |
| Cash conversion | CFO \( / NI \) | Above 1 is healthy |
| Accrual ratio | \( (NI - \text{CFO}) / \bar{A} \) | Lower is better |
| DSO, DIO | AR \( / R \times 365 \), inventory \( / C \times 365 \) | Days |
| Earnings surprise | \( (A - E) / \lvert E \rvert \) | Actual against consensus |

### Statement links

| Link | Check |
|---|---|
| Net income to retained earnings | Opening + net income - dividends = closing |
| Net income to cash flow | First line of CFO |
| Cash flow to cash | Opening cash + net change = closing cash |
| PP&E | Opening + capex - depreciation = closing |
| Equity and balance | \( A = L + E \) |

### Red flags

- Receivables or inventory growing much faster than revenue.
- Net income above CFO for several years.
- "One-time" charges every year, and a widening gap between GAAP and adjusted EPS.
- Restatements, auditor changes, weak controls (Item 9A).
- Buybacks that only offset share issuance.

### Earnings day order

1. Surprise against consensus (EPS and revenue).
2. GAAP to non-GAAP reconciliation.
3. Guidance against consensus.
4. Cash flow, debt and buybacks.
5. The tone of the call and the questions asked.
