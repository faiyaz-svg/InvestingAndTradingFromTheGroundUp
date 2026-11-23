# Financial ratios

The ratios from [company financials](../09-company-financials/index.md) and [valuation and research](../10-valuation-and-research/index.md), with what each one tells you, its usual caveat and the lesson that teaches it. [Formulas](formulas.md) has the same expressions with their symbols.

A bar over a letter (\(\bar{E}\)) means the average of the opening and closing balance. Every ratio is only as good as the inputs, so compare a company with its own past and with peers in the same industry.

## Profit and growth

| Ratio | Formula | What it tells you | Usual caveat | Lesson |
|---|---|---|---|---|
| Margin (gross, operating, EBITDA, net) | \( \text{Margin} = \frac{\text{Profit measure}}{R} \) | Cents of profit left from each sales dollar at that stage of the income statement | Margins differ by industry, so a 10% net margin is thin for software and good for a distributor | [Margins and growth](../09-company-financials/06-margins-and-growth.md) |
| Growth | \( g = \frac{X_1 - X_0}{X_0} \) | The change from one period to the next | One year is not a trend | [Margins and growth](../09-company-financials/06-margins-and-growth.md) |
| CAGR | \( \text{CAGR} = \left(\frac{X_n}{X_0}\right)^{1/n} - 1 \) | The steady yearly rate that gives the same end value | \(n\) is the number of years, not the number of data points | [Margins and growth](../09-company-financials/06-margins-and-growth.md) |
| Operating leverage | EBIT growth divided by revenue growth | How much faster profit moves than sales when costs are fixed | It works in both directions: a sales fall cuts EBIT by more | [Margins and growth](../09-company-financials/06-margins-and-growth.md) |

## Returns on capital

| Ratio | Formula | What it tells you | Usual caveat | Lesson |
|---|---|---|---|---|
| ROE | \( \text{ROE} = \frac{NI}{\bar{E}} \) | Profit per dollar of shareholders' money | Buybacks and losses shrink equity and can inflate it | [Returns on capital](../09-company-financials/07-returns-on-capital.md) |
| ROA | \( \text{ROA} = \frac{NI}{\bar{A}} \) | Profit per dollar of everything the company owns | Banks and insurers hold mostly financial assets, so treat them separately | [Returns on capital](../09-company-financials/07-returns-on-capital.md) |
| ROIC | \( \text{ROIC} = \frac{\text{NOPAT}}{\bar{IC}} \) | Operating profit after tax per dollar of capital funding the operations; value is created when it is above the cost of capital | Providers define invested capital differently, so use one formula for every company | [Returns on capital](../09-company-financials/07-returns-on-capital.md) |
| DuPont | \( \text{ROE} = \frac{NI}{R} \times \frac{R}{\bar{A}} \times \frac{\bar{A}}{\bar{E}} \) | Splits ROE into net margin, asset turnover and the equity multiplier | Two firms with equal ROE can differ a lot, and the leveraged one is the fragile one | [Returns on capital](../09-company-financials/07-returns-on-capital.md) |

## Liquidity and solvency

| Ratio | Formula | What it tells you | Usual caveat | Lesson |
|---|---|---|---|---|
| Current ratio | \( \frac{CA}{CL} \) | Whether assets usable within a year cover liabilities due within a year | A high ratio built on slow inventory is weaker than it looks | [Debt, liquidity and solvency](../09-company-financials/08-debt-liquidity-and-solvency.md) |
| Quick ratio | \( \frac{\text{Cash} + AR}{CL} \) | A stricter version that leaves out inventory and prepaid items | Some sources also add short-term investments | [Debt, liquidity and solvency](../09-company-financials/08-debt-liquidity-and-solvency.md) |
| Debt to equity | \( \frac{D}{E} \) | How much debt sits against shareholders' equity | Lease treatment differs, so say what you counted | [Debt, liquidity and solvency](../09-company-financials/08-debt-liquidity-and-solvency.md) |
| Net debt | \( D - \text{Cash} \) | The debt left if the company paid it down with its cash | Check that the cash is free to use, and look at due dates | [Debt, liquidity and solvency](../09-company-financials/08-debt-liquidity-and-solvency.md) |
| Interest coverage | \( \frac{\text{EBIT}}{I} \) | How many times operating profit covers the interest bill | Stress it: ask what a bad year does | [Debt, liquidity and solvency](../09-company-financials/08-debt-liquidity-and-solvency.md) |
| Net debt to EBITDA | Net debt divided by EBITDA | Years of operating earnings needed to repay net debt | Uses EBITDA, which skips capex | [Debt, liquidity and solvency](../09-company-financials/08-debt-liquidity-and-solvency.md) |

## Per-share figures and earnings quality

| Ratio | Formula | What it tells you | Usual caveat | Lesson |
|---|---|---|---|---|
| Basic EPS | \( \frac{NI - P}{\bar{N}} \) | Profit per weighted average share | Use the weighted average count, not last quarter's quote page | [Shares, EPS, dilution and buybacks](../09-company-financials/09-shares-eps-dilution-and-buybacks.md) |
| Diluted EPS | Same, with the larger count from options and RSUs (treasury stock method) | EPS if the promises of shares were used today | It is a calculation, not a forecast | [Shares, EPS, dilution and buybacks](../09-company-financials/09-shares-eps-dilution-and-buybacks.md) |
| Cash conversion | \( \frac{\text{CFO}}{NI} \) | Above 1 means cash exceeds profit | One year can mislead | [GAAP, non-GAAP and earnings quality](../09-company-financials/10-gaap-non-gaap-and-earnings-quality.md) |
| Accrual ratio | \( \frac{NI - \text{CFO}}{\bar{A}} \) | The part of profit not yet cash, as a share of assets; low or negative is the better sign | Use a trend over three or more years | [GAAP, non-GAAP and earnings quality](../09-company-financials/10-gaap-non-gaap-and-earnings-quality.md) |
| DSO | \( \frac{AR}{R} \times 365 \) | Days of sales sitting in receivables | A flag is a question for the notes, not proof of a problem | [GAAP, non-GAAP and earnings quality](../09-company-financials/10-gaap-non-gaap-and-earnings-quality.md) |
| DIO | \( \frac{\text{Inventory}}{C} \times 365 \) | Days of cost of goods sold sitting in inventory | Same as DSO | [GAAP, non-GAAP and earnings quality](../09-company-financials/10-gaap-non-gaap-and-earnings-quality.md) |
| Earnings surprise | \( \frac{A - E}{\lvert E\rvert} \) | Actual against the consensus | The market trades the surprise, not the number | [Earnings season and earnings calls](../09-company-financials/11-earnings-season-and-calls.md) |

## Valuation multiples

| Ratio | Formula | What it tells you | Usual caveat | Lesson |
|---|---|---|---|---|
| P/E | \( \frac{P}{\text{EPS}} \) | What the market pays for each dollar of yearly profit | Trailing uses the past four quarters and forward uses an estimate, so do not compare one with the other | [Price multiples](../10-valuation-and-research/01-multiples.md) |
| Earnings yield | \( \frac{\text{EPS}}{P} \) | Profit per dollar paid, readable like an interest rate | Compare it with a risk-free yield | [Price multiples](../10-valuation-and-research/01-multiples.md) |
| P/S | \( \frac{\text{market cap}}{\text{revenue}} \) | A price against sales, useful when earnings are negative or swing | Ignores margins | [Price multiples](../10-valuation-and-research/01-multiples.md) |
| P/B | \( \frac{\text{market cap}}{\text{book equity}} \) | A price against accounting equity | Suits banks and insurers and misleads for software, whose value is not on the balance sheet | [Price multiples](../10-valuation-and-research/01-multiples.md) |
| PEG | \( \frac{\text{P/E}}{g} \) | P/E adjusted for expected growth | A rule of thumb with no theory behind it, and the growth input is a guess | [Price multiples](../10-valuation-and-research/01-multiples.md) |
| EV | \( \text{equity value} + \text{debt} + \text{preferred stock} + \text{minority interest} - \text{cash} \) | The price of the whole business net of cash | Count options and RSUs, and check that the cash is free | [Enterprise value and EV/EBITDA](../10-valuation-and-research/02-enterprise-value-and-ev-ebitda.md) |
| EV/EBITDA | \( \frac{\text{EV}}{\text{EBITDA}} \) | A whole-business price against profit before interest | Capital needs differ across industries | [Enterprise value and EV/EBITDA](../10-valuation-and-research/02-enterprise-value-and-ev-ebitda.md) |
| EV/sales | \( \frac{\text{EV}}{\text{revenue}} \) | The same against sales | Ignores margins | [Enterprise value and EV/EBITDA](../10-valuation-and-research/02-enterprise-value-and-ev-ebitda.md) |
| Levered FCF | \( \text{CFO} - \text{capex} \) | Cash left after interest and capital spending | CFO adds back stock pay, so look at FCF after it too | [Free cash flow](../10-valuation-and-research/03-free-cash-flow.md) |
| Unlevered FCF | \( \text{EBIT} \times (1 - t) + \text{D\&A} - \text{capex} - \Delta \text{NWC} \) | Cash from operations before financing, the input to a DCF | Interest belongs in the discount rate, not in this cash flow | [Free cash flow](../10-valuation-and-research/03-free-cash-flow.md) |
| WACC | \( \frac{E}{E + D}\, k_e + \frac{D}{E + D}\, k_d (1 - t) \) | The blended cost of equity and debt, used to discount | It is a range, not an exact figure, and weights use market values | [Discount rates, CAPM and WACC](../10-valuation-and-research/04-discount-rates-capm-and-wacc.md) |
| Economic profit | \( \text{NOPAT} - \text{WACC} \times \text{invested capital} \) | Profit above the cost of capital | Depends on the same ROIC and WACC choices | [Moats and qualitative research](../10-valuation-and-research/08-moats-and-qualitative-research.md) |

## Industry measures

The [comparables lesson](../10-valuation-and-research/07-comparables-and-industry-kpis.md) gives these with numbers. Each one is useful against the same industry's peers and misleading across industries.

| Industry | Measure | What it tells you |
|---|---|---|
| Software | Annual recurring revenue (ARR) | The yearly value of subscription contracts |
| Software | Net revenue retention, \( \frac{\text{start ARR} + \text{expansion} - \text{contraction} - \text{churn}}{\text{start ARR}} \) | How much last year's customers pay now, with new customers left out |
| Software | Rule of 40 | Revenue growth % plus free cash flow margin % should be at least 40 (a rule of thumb) |
| Banks | Net interest margin | Net interest income divided by average earning assets |
| Banks | Efficiency ratio | Non-interest expense divided by revenue; lower is better |
| Banks | CET1 | The highest-quality capital a bank holds, as a ratio of risk-weighted assets |
| Retail | Same-store sales | Sales growth of stores open at least a year, with new openings removed |
| Retail | Inventory turns | Cost of goods sold divided by inventory; a falling rate with flat sales warns that goods are not selling |
| Energy | Reserve life | Proved reserves divided by yearly output |
| Energy | Breakeven price | The commodity price at which a project earns zero |
| REITs | FFO and cap rate | Covered in [REIT metrics: FFO and cap rates](../17-commodities-forex-and-reits/08-reit-metrics-ffo-and-cap-rates.md) |
