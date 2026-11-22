# Price multiples

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">VAL</span>

After this lesson you can work out the P/E (trailing and forward), P/S, P/B, PEG and earnings yield of a stock, and say what each one does and does not tell you.

Before this: [Shares, EPS, dilution and buybacks](../09-company-financials/09-shares-eps-dilution-and-buybacks.md), [Reading a quote page](../01-how-markets-work/11-reading-a-quote-page.md). You need: a calculator.

## The idea

A stock at US$50 tells you nothing until you know what a share earns. A US$50 stock that earns US$5 a share is cheap next to a US$50 stock that earns US$0.50. A **multiple** divides the price (or the company's value) by a number from the financial statements, so stocks of different sizes can be compared on one scale.

This part values one made-up company, Northwind Tools Inc., from part 9. Its price is US$50.00, the close before its FY2025 report ([Earnings season and earnings calls](../09-company-financials/11-earnings-season-and-calls.md)). Its FY2025 numbers (US$ millions): revenue 1,150, net income 165, shareholders' equity 650. It has 98.5 million shares outstanding and reported diluted EPS of US$1.61.

## How it works

### P/E: trailing and forward

\[ \text{P/E} = \frac{P}{\text{EPS}} \]

- \(P\) is the share price in US$.
- EPS is earnings per share in US$, from the income statement (lesson 9 of part 9).

The **trailing P/E** uses EPS from the last four reported quarters. The **forward P/E** uses an estimate of EPS for the next 12 months or the next fiscal year. Trailing is a fact about the past. Forward is a forecast, so it is only as good as the forecast, and it is usually lower for a growing company.

Northwind: EPS = 165 / 102.5 = US$1.61 (1.6098 before rounding). The 102.5 million is the average diluted count over FY2025, as in part 9. Trailing P/E = 50.00 / 1.6098 = 31.1. For forward EPS, suppose FY2026 net income is US$202.0 million on 101.5 million diluted shares (the year-end count, lesson 2): EPS = US$1.99 and the forward P/E = 50.00 / 1.99 = 25.1. This forecast is the base case of lesson 5.

A P/E of 31.1 says the market pays US$31.10 for each US$1 of yearly profit.

### Earnings yield

\[ \text{Earnings yield} = \frac{\text{EPS}}{P} = \frac{1}{\text{P/E}} \]

It turns the P/E upside down, so it reads like an interest rate: the profit per dollar paid. Northwind: 1.6098 / 50.00 = 3.22%. Compare it with a risk-free rate. The 10-year Treasury yield was 4.92% on November 20, 2026 ([Treasury daily rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202611), as of 2026). An earnings yield below the Treasury yield means the buyer is counting on earnings growth to make up the gap.

### P/S and P/B

\[ \text{P/S} = \frac{\text{market cap}}{\text{revenue}} \qquad \text{P/B} = \frac{\text{market cap}}{\text{book equity}} \]

- Market cap is price times shares outstanding: 50.00 x 98.5 = US$4,925 million ([What a stock is](../01-how-markets-work/01-what-a-stock-is.md)).
- Revenue is the last 12 months of sales. Book equity is assets minus liabilities from the balance sheet.

**Price-to-sales** (P/S) works when earnings are negative or swing from year to year, because revenue is steadier. It ignores margins: a US$1 of sales at a 5% margin is worth less than at a 25% margin. **Price-to-book** (P/B) compares the price with the accounting value of the equity. It suits banks and insurers, whose assets are close to market value, and misleads for companies whose value is brands or software, which the balance sheet does not carry.

Northwind: P/S = 4,925 / 1,150 = 4.28. P/B = 4,925 / 650 = 7.58.

### PEG

\[ \text{PEG} = \frac{\text{P/E}}{g} \]

- \(g\) is expected EPS growth in percent per year, entered as a number (15 for 15%).

The **PEG ratio** adjusts the P/E for growth. If analysts expect 15% a year, PEG = 31.1 / 15 = 2.07. A PEG near 1 is a common rule of thumb for "fairly priced", but it is only a rule of thumb: it has no theory behind it, the growth input is a guess, and it ignores risk and how long the growth lasts.

<div class="example" markdown>

### Worked example: two stocks, one price

Stock A and Stock B both trade at US$40.

| | Stock A | Stock B |
|---|---|---|
| EPS, last 12 months | US$2.00 | US$1.00 |
| Expected EPS growth | 5% a year | 25% a year |
| P/E | 40 / 2.00 = 20.0 | 40 / 1.00 = 40.0 |
| Earnings yield | 5.0% | 2.5% |
| PEG | 20.0 / 5 = 4.0 | 40.0 / 25 = 1.6 |

Stock B looks twice as expensive on P/E and cheaper on PEG. Neither number settles it: Stock B has to deliver 25% growth, and the PEG does not say for how many years.

</div>

## Where multiples fail

A multiple compares; it does not value. It is only useful against something: the company's own history, its peers (lesson 7) or the market. Four traps:

1. Negative or near-zero earnings make the P/E meaningless. Use P/S or an operating measure (lesson 2).
2. Cyclical companies (steel, oil, homebuilders) look cheapest at peak earnings and dearest at the trough, so the P/E points the wrong way.
3. One-off items, such as a gain on selling a business, inflate EPS. Check the quality of earnings ([GAAP, non-GAAP and earnings quality](../09-company-financials/10-gaap-non-gaap-and-earnings-quality.md)).
4. P/E mixes the effect of debt with the effect of the business. Two companies with the same operations but different debt have different P/Es. Enterprise value (lesson 2) fixes that.

## In code

The multiples as a small function, using the numbers above.

<details class="code" markdown>
<summary>In code</summary>

```python
price = 50.00
shares_out = 98.5          # million, shares outstanding
eps = 165 / 102.5          # diluted EPS, US$
revenue, equity = 1150, 650  # US$ millions
mcap = price * shares_out

pe = price / eps
print(f"P/E {pe:.1f}  earnings yield {eps / price:.2%}")
print(f"P/S {mcap / revenue:.2f}  P/B {mcap / equity:.2f}  PEG {pe / 15:.2f}")
```

</details>

## Common mistakes

- Comparing a trailing P/E with a forward P/E. State which one a data site shows before you compare.
- Using the PEG with a growth rate that includes a one-year jump. Use a multi-year estimate.
- Using P/B for a software company. Most of its value is not on the balance sheet.

## Try it

1\. Stock C trades at US$36. It earned US$2.40 per share over the last 12 months. Find the P/E and the earnings yield.

<details class="solution" markdown>
<summary>Answer</summary>

P/E = 36 / 2.40 = 15.0. Earnings yield = 2.40 / 36 = 6.67%.

</details>

2\. Stock C's analysts expect EPS of US$2.70 next year. What is the forward P/E, and what EPS growth does that imply?

<details class="solution" markdown>
<summary>Answer</summary>

Forward P/E = 36 / 2.70 = 13.3. Growth = 2.70 / 2.40 - 1 = 12.5%.

</details>

3\. Stock C has a P/E of 15.0 and expected EPS growth of 12.5% a year. What is its PEG?

<details class="solution" markdown>
<summary>Answer</summary>

PEG = 15.0 / 12.5 = 1.2.

</details>

4\. A company has 40 million shares, a US$25 price, US$600 million of revenue and US$200 million of book equity. Find P/S and P/B.

<details class="solution" markdown>
<summary>Answer</summary>

Market cap = 25 x 40 = US$1,000 million. P/S = 1,000 / 600 = 1.67. P/B = 1,000 / 200 = 5.00.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Open the quote page of a stock you know. Write down its trailing P/E and check whether the page says it uses reported or adjusted EPS. |
| 4 | Find that company's latest 10-K on EDGAR ([Filings and EDGAR](../09-company-financials/01-filings-and-edgar.md)) and recompute P/S from revenue and shares outstanding. |
| 2 | Write the earnings yield next to the 10-year Treasury yield. |

</div>

## Key terms

- **Multiple**: a price or value divided by a financial statement number, used to compare companies.
- **Trailing P/E**: price divided by EPS of the last four quarters.
- **Forward P/E**: price divided by estimated EPS for the next 12 months or fiscal year.
- **Earnings yield**: EPS divided by price, the inverse of the P/E.
- **Price-to-sales (P/S)**: market cap divided by revenue.
- **Price-to-book (P/B)**: market cap divided by book equity.
- **PEG ratio**: the P/E divided by expected EPS growth in percent.

Next: [Enterprise value and EV/EBITDA](02-enterprise-value-and-ev-ebitda.md)
