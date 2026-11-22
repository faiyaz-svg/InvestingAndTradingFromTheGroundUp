# Free cash flow

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">VAL</span>

After this lesson you can work out levered and unlevered free cash flow, explain why they differ, and say which one a DCF uses.

Before this: [The cash flow statement](../09-company-financials/04-the-cash-flow-statement.md), [Enterprise value and EV/EBITDA](02-enterprise-value-and-ev-ebitda.md). You need: a calculator.

## The idea

Northwind reported US$165 million of net income in FY2025. It could not pay that out. It spent US$80 million on equipment and tied up US$25 million more in receivables and inventory. **Free cash flow** (FCF) is the cash a business generates after the spending needed to keep it running and growing. It is what is left for the people who fund the company.

Part 9 defined FCF as operating cash flow minus capex. That figure is called **levered free cash flow** here, because it is measured after the company paid interest to its lenders. It belongs to shareholders (and to whoever the company chooses to pay with it). A DCF needs a second version that ignores how the company is funded.

## How it works

### Levered free cash flow

\[ \text{Levered FCF} = \text{CFO} - \text{capex} \]

- CFO is cash flow from operations, from the cash flow statement. It is after interest and after taxes.
- Capex is capital spending on property and equipment, from the investing section.

Northwind: 205 - 80 = US$125 million. Two things to know. First, CFO adds back stock-based pay (US$30 million), a real cost paid in shares. FCF after stock pay is 125 - 30 = US$95 million ([GAAP, non-GAAP and earnings quality](../09-company-financials/10-gaap-non-gaap-and-earnings-quality.md)). Second, it is after interest, so it depends on how much debt the company carries.

### Unlevered free cash flow

\[ \text{UFCF} = \text{EBIT} \times (1 - t) + \text{D\&A} - \text{capex} - \Delta \text{NWC} \]

- EBIT is operating profit before interest and tax, in US$ millions.
- \(t\) is the tax rate (25% for Northwind). EBIT x (1 - t) is NOPAT, the operating profit after the tax it would pay with no debt ([Returns on capital](../09-company-financials/07-returns-on-capital.md)).
- D&A is depreciation and amortization, added back because it used no cash.
- Capex is spending on long-lived assets, subtracted.
- \(\Delta\text{NWC}\) is the increase in net working capital: receivables + inventory + prepaid expenses - payables - accrued expenses. A rise ties up cash, so it is subtracted.

**Unlevered free cash flow** is the cash the operations produce before any payment to lenders. Because it ignores the financing mix, it is the cash flow of the business itself, and it matches enterprise value: both belong to lenders and shareholders together. That is why the DCF discounts it (lesson 5).

<div class="example" markdown>

### Worked example: free cash flow for FY2025

Net working capital: FY2024 = 125 + 100 + 25 - 80 - 45 = 125. FY2025 = 150 + 120 + 30 - 95 - 55 = 150. The increase is 25.

1. NOPAT = 235 x (1 - 0.25) = US$176.25 million.
2. UFCF = 176.25 + 35 - 80 - 25 = US$106.25 million.

Now bridge to levered FCF.

3. After-tax interest = 15 x (1 - 0.25) = US$11.25 million. Lenders were paid this, so levered FCF is lower by this amount.
4. Stock pay of US$30 million is an expense in EBIT that CFO adds back, so levered FCF is higher by this amount.
5. Levered FCF = 106.25 - 11.25 + 30 = US$125 million. It matches CFO - capex = 205 - 80.

</div>

The figure follows the same steps.

![Northwind FY2025 bridge: EBIT 235, tax -58.75, D&A +35, capex -80, working capital -25 give unlevered FCF 106.25; after-tax interest -11.25 and stock pay +30 give levered FCF 125, in US$ millions](../assets/figures/10-valuation-and-research/fcf-bridge-dark.svg#only-dark)
![Northwind FY2025 bridge: EBIT 235, tax -58.75, D&A +35, capex -80, working capital -25 give unlevered FCF 106.25; after-tax interest -11.25 and stock pay +30 give levered FCF 125, in US$ millions](../assets/figures/10-valuation-and-research/fcf-bridge-light.svg#only-light)

In the UFCF formula, EBIT is already after stock pay, so UFCF treats stock pay as a cost. That is the safer choice for a DCF: if you add it back, you need to count the new shares it creates.

### Which one to use

| Use | Measure | Compare with |
|---|---|---|
| DCF of the whole business (lesson 5) | Unlevered FCF | Enterprise value |
| FCF yield for a shareholder | Levered FCF | Market cap |
| Dividend and buyback capacity | Levered FCF | Dividends and buybacks |

Northwind's FCF yield = 125 / 4,925 = 2.54%. Its cash conversion = FCF / net income = 125 / 165 = 76%. The gap exists because capex (80) is far above D&A (35): the company is investing for growth.

Companies and data sites define FCF in different ways: some subtract capitalized software, some add back stock pay, some subtract leases. Read the definition before you compare.

## In code

<details class="code" markdown>
<summary>In code</summary>

```python
ebit, tax, da, capex = 235, 0.25, 35, 80
nwc_prev = 125 + 100 + 25 - 80 - 45
nwc_now = 150 + 120 + 30 - 95 - 55
ufcf = ebit * (1 - tax) + da - capex - (nwc_now - nwc_prev)
lfcf = ufcf - 15 * (1 - tax) + 30   # less after-tax interest, plus stock pay
print(ufcf, lfcf)                   # 106.25 125.0
```

</details>

## Common mistakes

- Using EBITDA as free cash flow. It skips capex, tax and working capital.
- Adding interest-related items to UFCF. Interest belongs in the discount rate (lesson 4), not in the cash flow.
- Treating a one-year drop in capex as lasting. A company cannot underinvest forever.

## Try it

1\. A company has EBIT of US$80 million, a 25% tax rate, D&A of US$10 million, capex of US$25 million, and net working capital rises by US$5 million. Find UFCF.

<details class="solution" markdown>
<summary>Answer</summary>

NOPAT = 80 x 0.75 = 60. UFCF = 60 + 10 - 25 - 5 = US$40 million.

</details>

2\. The same company has CFO of US$62 million. What is levered FCF?

<details class="solution" markdown>
<summary>Answer</summary>

Levered FCF = 62 - 25 = US$37 million.

</details>

3\. Northwind's market cap is US$4,925 million. What is its levered FCF yield after stock pay (US$95 million)?

<details class="solution" markdown>
<summary>Answer</summary>

95 / 4,925 = 1.93%.

</details>

4\. Northwind's UFCF divided by its EV (5,220) is a yield on the whole business. Find it.

<details class="solution" markdown>
<summary>Answer</summary>

106.25 / 5,220 = 2.04%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | From a real company's 10-K, find CFO, capex, interest paid and stock-based pay. Compute levered FCF and FCF after stock pay. |
| 3 | Compute the FCF yield on its market cap. |
| 2 | Write one sentence: is its capex above or below D&A, and why? |

</div>

## Key terms

- **Free cash flow (FCF)**: cash generated after the spending needed to run and grow the business.
- **Levered free cash flow**: CFO minus capex, after interest to lenders.
- **Unlevered free cash flow (UFCF)**: EBIT x (1 - t) + D&A - capex - change in net working capital, before payments to lenders.
- **NOPAT**: operating profit after the tax it would pay with no debt.
- **Net working capital (NWC)**: receivables, inventory and prepaid expenses minus payables and accrued expenses.
- **FCF yield**: free cash flow divided by market cap (or UFCF divided by EV).

Next: [Discount rates, CAPM and WACC](04-discount-rates-capm-and-wacc.md)
