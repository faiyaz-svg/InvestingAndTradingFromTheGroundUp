# GAAP, non-GAAP and earnings quality

<span class="tag tag-data">Data</span> <span class="tag tag-part">FIN</span>

After this lesson you can read a non-GAAP reconciliation, name what a company adds back to reach an adjusted number, and run a short test of whether earnings are backed by cash.

Before this: [Shares, EPS, dilution and buybacks](09-shares-eps-dilution-and-buybacks.md). You need: a calculator.

## The idea

When Northwind announces its results, the press release can carry two EPS numbers. GAAP diluted EPS is US$1.61. "Adjusted EPS" is US$1.83. Both are about the same year and the same company. The second is higher because the company removed a cost, and the question for you is whether that cost is real.

**GAAP** (generally accepted accounting principles) is the US rulebook the audited statements follow. A **non-GAAP measure** is a figure the company defines itself, such as adjusted EBITDA or adjusted EPS, that is not calculated under GAAP. Companies offer them because a one-off item, such as the cost of closing a factory, can hide how the ongoing business is doing. They can also be used to make results look better.

### What the SEC requires

A company that publicly discloses a non-GAAP measure must present the most directly comparable GAAP measure with it and give a reconciliation between the two. This comes from Regulation G, adopted by the SEC in January 2003 ([Conditions for Use of Non-GAAP Financial Measures](https://www.sec.gov/rules-regulations/2003/03/conditions-use-non-gaap-financial-measures)). Item 10(e) of Regulation S-K adds rules for filings and earnings releases, including that the GAAP figure appears with equal or greater prominence. The company also may not present a non-GAAP measure that is misleading. The SEC's staff has published guidance with examples of what it treats as misleading. As of 2026 the rules are in force; check the SEC's non-GAAP guidance pages for current staff views.

The reconciliation is your tool. It lists every item added or removed. Read each line and decide whether you would take it out.

## How it works

### A reconciliation

<div class="example" markdown>

### Worked example: a non-GAAP reconciliation

Northwind defines adjusted EBITDA as EBITDA plus stock-based compensation, and adjusted EPS as GAAP EPS plus after-tax stock-based compensation per share.

Adjusted EBITDA (US$ millions):

| Line | FY2025 |
|---|---|
| Net income (GAAP) | 165 |
| Interest expense | 15 |
| Income taxes | 55 |
| Depreciation and amortization | 35 |
| EBITDA | 270 |
| Stock-based compensation | 30 |
| Adjusted EBITDA | 300 |

Adjusted EPS:

1. After-tax SBC = 30 x (1 - 0.25) = US$22.5 million.
2. Adjusted net income = 165 + 22.5 = US$187.5 million.
3. Adjusted EPS = 187.5 / 102.5 = US$1.83, against GAAP diluted EPS of US$1.61.

The adjustment adds US$0.22 a share. The adjusted EBITDA margin is 300 / 1,150 = 26.1%, against an EBITDA margin of 23.5%.

</div>

Whether to add back SBC is a judgment. Companies say it is non-cash. It is also real pay, and shares given to employees reduce your slice (lesson 9). A reader who accepts the add-back should still ask what the company spends on buybacks to offset the shares. Other common add-backs are amortization of acquired intangibles, restructuring charges and legal settlements. A one-time add-back is reasonable. A "one-time" charge that appears every year is a normal cost under another name.

### Earnings quality

**Earnings quality** is how well reported profit reflects cash the business actually produces and will keep producing. Four tests use numbers you already have.

\[ \text{Cash conversion} = \frac{\text{CFO}}{NI} \qquad \text{Accrual ratio} = \frac{NI - \text{CFO}}{\bar{A}} \]

- CFO is operating cash flow and \(NI\) is net income (lesson 4).
- \(\bar{A}\) is average total assets.
- A cash conversion above 1 means cash exceeds profit. The accrual ratio is the part of profit that is not yet cash, as a share of assets. Low or negative is the better sign.

\[ \text{DSO} = \frac{AR}{R} \times 365 \qquad \text{DIO} = \frac{\text{Inventory}}{C} \times 365 \]

- **Days sales outstanding** (DSO) is how many days of sales sit in receivables.
- **Days inventory outstanding** (DIO) is how many days of COGS sit in inventory.
- \(R\) is revenue, \(C\) is COGS, \(AR\) is accounts receivable, and 365 is days in the year.

For Northwind: cash conversion = 205 / 165 = 1.24. Accrual ratio = (165 - 205) / 1,037.5 = -3.9%. FCF / net income = 125 / 165 = 0.76, lower because capex of 80 is far above D&A of 35. DSO went from 125 / 1,000 x 365 = 45.6 days to 150 / 1,150 x 365 = 47.6 days. DIO went from 100 / 600 x 365 = 60.8 days to 120 / 667 x 365 = 65.7 days.

The first two tests are healthy. The last two are small warnings: customers take about two more days to pay, and inventory stays on the shelf about five more days. Receivables and inventory both grew 20% against revenue growth of 15%. One year is not a verdict, but you would read the MD&A for the explanation, such as a big order shipped late in the quarter, and track the numbers next year.

### Red flags

| Flag | Where to look |
|---|---|
| Receivables or inventory growing much faster than revenue | Balance sheet, DSO and DIO |
| Net income far above CFO for several years | Cash flow statement, accrual ratio |
| "One-time" charges every year | Income statement, non-GAAP reconciliation |
| Growing gap between GAAP and adjusted EPS | Earnings release |
| Frequent changes to how the company reports (new segments, new metrics) | Notes and MD&A |
| A change of auditor, a restatement, or a weakness in controls | 8-K Items 4.01 and 4.02, 10-K Item 9A |

A flag is a reason to read more, not a verdict. Research has linked accruals to later returns: Sloan (1996, *The Accounting Review*) found that US companies with a high accrual share of earnings had lower stock returns in the following years than companies with a low share. He read this as investors reacting to total earnings as if accruals and cash were equally lasting, when accruals tend to fade. Later work finds the effect varies by period and method, so treat the accrual ratio as one input.

<div class="canada" markdown>

### For Canadians

Canada has its own rule: National Instrument 52-112, in force since August 25, 2021, sets disclosure rules for non-GAAP financial measures in Canadian filings, including how they are labelled and reconciled ([OSC page](https://www.osc.ca/en/securities-law/instruments-rules-policies/5/52-112/national-instrument-52-112-non-gaap-and-other-financial-measures-disclosure)). Canadian companies reporting under IFRS call them non-IFRS measures. Read the current text for exact wording.

</div>

## Common mistakes

- Reading adjusted EPS without the reconciliation. The reconciliation tells you which costs were removed.
- Using one year of accruals as a signal. Use a trend over three or more years.
- Calling a company dishonest because a ratio looks off. A flag is a question for the notes and the MD&A.

## Try it

1\. A company reports GAAP net income of US$90 million and adds back US$20 million of restructuring (after tax US$15 million) and US$12 million of after-tax stock-based pay. With 50 million diluted shares, find GAAP EPS and adjusted EPS.

<details class="solution" markdown>
<summary>Answer</summary>

GAAP EPS = 90 / 50 = US$1.80. Adjusted net income = 90 + 15 + 12 = US$117 million. Adjusted EPS = 117 / 50 = US$2.34. The adjustments add US$0.54, or 30% of GAAP EPS.

</details>

2\. Net income is US$60 million, CFO is US$45 million and average assets are US$600 million. Find cash conversion and the accrual ratio. What do they say?

<details class="solution" markdown>
<summary>Answer</summary>

Cash conversion = 45 / 60 = 0.75. Accrual ratio = (60 - 45) / 600 = 2.5%. Profit is not fully backed by cash this year. Check whether receivables or inventory grew, and look at prior years.

</details>

3\. A company's receivables were US$80 million on revenue of US$600 million last year, and US$130 million on revenue of US$700 million this year. Find DSO each year and the change.

<details class="solution" markdown>
<summary>Answer</summary>

Last year: 80 / 600 x 365 = 48.7 days. This year: 130 / 700 x 365 = 67.8 days. DSO rose by 19.1 days while revenue grew 16.7%. Receivables grew 62.5%, so check the MD&A for a reason.

</details>

4\. Northwind's FY2025 FCF is US$125 million and SBC is US$30 million. What is FCF after SBC, and as a percentage of FCF?

<details class="solution" markdown>
<summary>Answer</summary>

125 - 30 = US$95 million, which is 76.0% of FCF. Treating SBC as a cash cost cuts FCF by 24.0%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Find a recent earnings release (an 8-K, Exhibit 99.1) for a US company. Find its non-GAAP reconciliation. |
| 4 | List each add-back and write whether you would remove it, with one reason each. |
| 2 | Compute cash conversion (CFO divided by net income) for its latest year. |

</div>

## Key terms

- **GAAP**: the US accounting rules the audited statements follow.
- **Non-GAAP measure**: a figure a company defines itself that is not calculated under GAAP.
- **Reconciliation**: the table that bridges a non-GAAP measure to the nearest GAAP one.
- **Regulation G**: the SEC rule that requires the GAAP comparison and reconciliation for public non-GAAP measures.
- **Adjusted EBITDA**: EBITDA with further add-backs the company chooses.
- **Earnings quality**: how well reported profit reflects cash the business produces.
- **Cash conversion**: operating cash flow divided by net income.
- **Accrual ratio**: net income minus operating cash flow, divided by average assets.
- **Days sales outstanding (DSO)**: receivables divided by revenue, times 365.
- **Days inventory outstanding (DIO)**: inventory divided by COGS, times 365.

Next: [Earnings season and earnings calls](11-earnings-season-and-calls.md)
