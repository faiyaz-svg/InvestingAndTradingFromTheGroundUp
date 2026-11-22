# The income statement

<span class="tag tag-data">Data</span> <span class="tag tag-part">FIN</span>

After this lesson you can read an income statement from revenue to net income, work out gross profit, operating income (EBIT), EBITDA and net income, and say when a company counts revenue.

Before this: [Filings and EDGAR](01-filings-and-edgar.md). For percentages, see [percents](https://faiyaz-svg.github.io/MathFromTheGroundUp/02-middle-school/02-ratios-rates-percents/03-percents/) in the math book. You need: a calculator.

## The idea

Northwind Tools sells industrial tools. In FY2025 it sold US$1,150 million of them, and after every cost it kept US$165 million. The **income statement** (also called the profit and loss statement, or P&L) shows how it got from the first number to the second, for a period such as a quarter or a year. It is read from the top down: each line subtracts a cost from the line above.

### Revenue

**Revenue** (or sales) is what the company earns from customers in the period. Companies use **accrual accounting**: revenue counts when it is earned, not when the cash arrives. Under US GAAP (generally accepted accounting principles, the US rulebook) a company records revenue when it hands control of the goods or services to the customer, in the amount it expects to receive.

Two Northwind cases show the difference. It ships a US$12 million order on December 20, and the customer pays on January 15. The revenue belongs to December, and the unpaid amount sits on the balance sheet as a receivable. It also sells a one-year service plan on October 1 for US$2.4 million, paid up front. The service is delivered over 12 months, so Northwind records US$0.2 million a month. By December 31 it has recorded 3 x 0.2 = US$0.6 million as revenue, and the other US$1.8 million is **deferred revenue**, a liability: cash received for service not yet delivered.

### Costs and profit, line by line

**Cost of goods sold** (COGS) is the direct cost of what was sold: materials, factory labour, shipping in. **Gross profit** is revenue minus COGS. **Operating expenses** are the costs of running the business that are not in COGS: selling, general and administrative expenses (SG&A), research and development (R&D), and depreciation and amortization (D&A, the cost of long-lived assets spread over their lives, covered in lesson 3).

**Operating income** is gross profit minus operating expenses. It is also called **EBIT**, earnings before interest and taxes. Then comes **interest expense**, the cost of borrowed money, then **income taxes**, and what is left is **net income**, the profit that belongs to shareholders.

| US$ millions | FY2024 | FY2025 |
|---|---|---|
| Revenue | 1,000 | 1,150 |
| Cost of goods sold | 600 | 667 |
| Gross profit | 400 | 483 |
| SG&A | 130 | 145 |
| R&D | 60 | 68 |
| Depreciation and amortization | 30 | 35 |
| Operating income (EBIT) | 180 | 235 |
| Interest expense | 16 | 15 |
| Income before taxes | 164 | 220 |
| Income taxes (25%) | 41 | 55 |
| Net income | 123 | 165 |

Northwind shows D&A as its own line to keep the model simple. Many real companies place it inside COGS and SG&A and disclose the amount in the cash flow statement. Stock-based pay (shares given to employees, lesson 9) is inside SG&A and R&D: US$25 million in FY2024 and US$30 million in FY2025.

The figure follows FY2025 from top to bottom. Look at how much of each revenue dollar remains after each step.

![Margin waterfall for Northwind FY2025, from revenue of 1,150 down to net income of 165](../assets/figures/09-company-financials/margin-waterfall-dark.svg#only-dark)
![Margin waterfall for Northwind FY2025, from revenue of 1,150 down to net income of 165](../assets/figures/09-company-financials/margin-waterfall-light.svg#only-light)

## How it works

Each profit line has a formula:

\[ \text{Gross profit} = R - C \qquad \text{EBIT} = \text{Gross profit} - O \qquad \text{EBITDA} = \text{EBIT} + D \]

- \(R\) is revenue and \(C\) is COGS, in US$ millions.
- \(O\) is operating expenses, including D&A.
- \(D\) is depreciation and amortization, which does not use cash in the period.
- **EBITDA** is earnings before interest, taxes, depreciation and amortization. It adds D&A back to EBIT as a rough measure of operating cash earnings before capital spending.

\[ \text{Net income} = (\text{EBIT} - I) \times (1 - t) \]

- \(I\) is interest expense.
- \(t\) is the tax rate on pretax income. Northwind's is 25%, a made-up blended rate.

<div class="example" markdown>

### Worked example: the FY2025 statement

1. Gross profit = 1,150 - 667 = US$483 million.
2. Operating expenses = 145 + 68 + 35 = US$248 million.
3. EBIT = 483 - 248 = US$235 million.
4. EBITDA = 235 + 35 = US$270 million.
5. Income before taxes = 235 - 15 = US$220 million.
6. Taxes = 0.25 x 220 = US$55 million, so net income = 220 - 55 = US$165 million.

As a share of revenue: gross margin 483 / 1,150 = 42.0%, EBIT margin 235 / 1,150 = 20.4%, net margin 165 / 1,150 = 14.3%. Rounded to one decimal at the end. Lesson 6 compares them with FY2024.

</div>

### What to check in a real statement

Real statements add lines: other income, a restructuring charge, a one-time gain. Read the line names, and ask whether a line will happen again next year. A company with a one-time gain of US$30 million in net income can look like it grew when its business did not. Use the notes and MD&A (lesson 1) to find out.

<div class="canada" markdown>

### For Canadians

A Canadian company reporting under IFRS has the same layout in spirit, but IFRS lets a company present expenses by nature (wages, materials) or by function (COGS, SG&A), and some items differ from US GAAP. Check the currency in the column header: a Canadian company's income statement is usually in CAD.

</div>

## Common mistakes

- Reading net income as cash. It is an accrual figure: the order shipped in December is revenue even if the cash arrives in January. Lesson 4 shows the cash.
- Comparing EBITDA across companies without checking what each adds back. EBITDA is not a GAAP figure, and lesson 10 returns to this.
- Forgetting that a quarter's number is not a year's. Divide or compare like with like: Q4 against Q4.

## Try it

1\. Northwind's FY2024 income statement: revenue 1,000, COGS 600, operating expenses 220, interest 16, tax rate 25%. Find gross profit, EBIT and net income.

<details class="solution" markdown>
<summary>Answer</summary>

Gross profit = 1,000 - 600 = US$400 million. EBIT = 400 - 220 = US$180 million. Pretax = 180 - 16 = 164. Tax = 0.25 x 164 = 41. Net income = US$123 million.

</details>

2\. FY2024 D&A was US$30 million. What was FY2024 EBITDA, and the EBITDA margin?

<details class="solution" markdown>
<summary>Answer</summary>

EBITDA = 180 + 30 = US$210 million. Margin = 210 / 1,000 = 21.0%.

</details>

3\. A customer prepays US$3.6 million on April 1 for a 12-month service plan. How much revenue is recorded by June 30, and how much is deferred revenue?

<details class="solution" markdown>
<summary>Answer</summary>

Monthly revenue = 3.6 / 12 = US$0.3 million. Three months = US$0.9 million recorded. Deferred revenue = 3.6 - 0.9 = US$2.7 million.

</details>

4\. Northwind's FY2025 income before taxes is US$220 million and taxes are US$55 million. What is the effective tax rate? If a one-time US$20 million gain is in the US$220 million, what is pretax income without it?

<details class="solution" markdown>
<summary>Answer</summary>

Effective rate = 55 / 220 = 25.0%. Without the gain, pretax = 220 - 20 = US$200 million.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Open the latest 10-K of a US company you know and find its income statement in Item 8. Write revenue, gross profit, operating income and net income for the last two years. |
| 3 | Compute gross, operating and net margins for the latest year. |
| 2 | Find one line that looks one-time (a gain, a charge) and note what the MD&A says about it. |

</div>

## Key terms

- **Income statement**: the report of revenue, costs and profit for a period.
- **Revenue**: what a company earns from customers in the period.
- **Accrual accounting**: recording revenue when earned and costs when incurred, not when cash moves.
- **Deferred revenue**: cash received for goods or services not yet delivered, a liability.
- **Cost of goods sold (COGS)**: the direct cost of what was sold.
- **Gross profit**: revenue minus COGS.
- **Operating expenses**: the costs of running the business outside COGS.
- **Operating income (EBIT)**: gross profit minus operating expenses; earnings before interest and taxes.
- **EBITDA**: EBIT plus depreciation and amortization.
- **Interest expense**: the cost of borrowed money.
- **Net income**: profit after interest and taxes.
- **GAAP**: generally accepted accounting principles, the US accounting rules.

Next: [The balance sheet](03-the-balance-sheet.md)
