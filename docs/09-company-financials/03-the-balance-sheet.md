# The balance sheet

<span class="tag tag-data">Data</span> <span class="tag tag-part">FIN</span>

After this lesson you can read a balance sheet, check that assets equal liabilities plus equity, and work out working capital, depreciation and goodwill.

Before this: [The income statement](02-the-income-statement.md). You need: a calculator.

## The idea

An income statement covers a period. A **balance sheet** is a snapshot at one date: what the company owns, what it owes, and what is left for shareholders. Northwind's balance sheet at December 31, 2025 shows US$1,075 million of assets. Lenders and suppliers have a claim on US$425 million of that, and shareholders on the other US$650 million.

That split is the whole structure:

\[ A = L + E \]

- \(A\) is total assets: what the company owns or is owed, in US$ millions.
- \(L\) is total liabilities: what it owes to others.
- \(E\) is shareholders' equity: the difference, \(A - L\). It is also called book value, and it is an accounting figure, not the market cap.

Every transaction changes at least two lines so that the equation still holds. That is why a statement that does not balance has an error in it.

## How it works

Assets and liabilities are listed with the most liquid (closest to cash) first. **Current** means due or usable within a year; **non-current** means longer.

| US$ millions | Dec 31, 2024 | Dec 31, 2025 |
|---|---|---|
| Cash | 150 | 130 |
| Accounts receivable | 125 | 150 |
| Inventory | 100 | 120 |
| Prepaid and other | 25 | 30 |
| Total current assets | 400 | 430 |
| Property, plant and equipment (PP&E), net | 400 | 450 |
| Intangible assets | 60 | 55 |
| Goodwill | 140 | 140 |
| Total assets | 1,000 | 1,075 |
| Accounts payable | 80 | 95 |
| Accrued expenses | 45 | 55 |
| Current portion of debt | 25 | 25 |
| Total current liabilities | 150 | 175 |
| Long-term debt | 275 | 250 |
| Total liabilities | 425 | 425 |
| Common stock and paid-in capital | 300 | 340 |
| Retained earnings | 275 | 410 |
| Treasury stock | 0 | -100 |
| Total shareholders' equity | 575 | 650 |
| Total liabilities and equity | 1,000 | 1,075 |

Look at the figure: the left bar of each pair (assets) is as tall as the right bar (liabilities plus equity). In the right bar, payables are accounts payable plus accrued expenses (95 + 55 = 150 in FY2025), and debt is the current portion plus long-term debt.

![Northwind balance sheets for FY2024 and FY2025, with assets on the left and liabilities plus equity on the right, equal in height](../assets/figures/09-company-financials/balance-sheet-dark.svg#only-dark)
![Northwind balance sheets for FY2024 and FY2025, with assets on the left and liabilities plus equity on the right, equal in height](../assets/figures/09-company-financials/balance-sheet-light.svg#only-light)

### Working capital

**Working capital** is current assets minus current liabilities: the cushion that pays the near-term bills. Northwind's is 430 - 175 = US$255 million at the end of FY2025, up from 400 - 150 = US$250 million. Receivables and inventory are not cash. They are cash tied up in the operating cycle (lesson 4 follows how that ties up cash).

### PP&E and depreciation

**PP&E** is the factories, machines and equipment the company uses over many years. A company does not expense a US$60 million machine in the year it buys it. It records an asset and spreads the cost over the machine's useful life. That spreading is **depreciation**; for intangible assets such as acquired patents it is called **amortization**. In **straight-line depreciation**, each year's charge is the cost less any final resale value, divided by the life in years.

PP&E is shown net, meaning cost less all depreciation so far (its **net book value**). It moves by a simple roll-forward:

\[ \text{PP\&E}_{\text{end}} = \text{PP\&E}_{\text{start}} + \text{capex} - \text{depreciation} \]

- Capex (capital expenditure) is spending on new PP&E in the year, here US$80 million.
- Depreciation is the year's charge, here US$30 million. The other US$5 million of Northwind's US$35 million D&A is amortization of intangibles, which fell from 60 to 55.

<div class="example" markdown>

### Worked example: a machine and a roll-forward

Northwind buys a machine for US$60 million with a 10-year life and no resale value.

1. Annual depreciation = 60 / 10 = US$6 million.
2. After 3 years, accumulated depreciation = 18, so net book value = 60 - 18 = US$42 million.

For all of PP&E in FY2025: 400 + 80 - 30 = US$450 million, matching the balance sheet.

</div>

### Goodwill

When a company buys another for more than the fair value of its identifiable assets less its liabilities, the extra is **goodwill**. Suppose Northwind pays US$90 million for a company whose identifiable net assets are worth US$70 million. It records goodwill of 90 - 70 = US$20 million. Under US GAAP goodwill is not amortized; the company tests it for **impairment** (a write-down when the asset is worth less than its book value). An impairment is a non-cash charge that cuts net income and equity.

### Debt and equity

Northwind owes US$275 million in total at the end of FY2025: US$25 million due within a year (current portion) and US$250 million later. It repaid 25 during the year. Equity has three parts here. Paid-in capital (US$340 million) is what shareholders paid in plus stock-based pay. Retained earnings (US$410 million) are all the profits kept since the company began: 275 + 165 net income - 30 dividends = 410. Treasury stock (-US$100 million) is the cost of shares the company bought back, shown as a subtraction.

<div class="canada" markdown>

### For Canadians

Under IFRS, a company may show non-current assets first, and some companies revalue property. IFRS and US GAAP (for public companies) both test goodwill for impairment instead of amortizing it. The A = L + E check is the same under both. Read the currency on the header before using a number.

</div>

## Common mistakes

- Treating equity as the market value of the company. Book equity is historical cost less depreciation and write-offs, and the market cap can be several times larger or smaller.
- Calling a company safe because working capital is positive. Check what is in it: if most of the current assets are slow inventory, the cushion is weaker.
- Ignoring goodwill. A balance sheet full of goodwill from acquisitions can be written down in one quarter.

## Try it

1\. Northwind's total liabilities at the end of FY2025 are US$425 million and equity is US$650 million. What are total assets?

<details class="solution" markdown>
<summary>Answer</summary>

A = L + E = 425 + 650 = US$1,075 million.

</details>

2\. A company has current assets of US$430 million and current liabilities of US$175 million. What is its working capital?

<details class="solution" markdown>
<summary>Answer</summary>

430 - 175 = US$255 million.

</details>

3\. A machine costs US$48 million, has an 8-year life and a resale value of US$8 million. What is the yearly straight-line depreciation and the net book value after 4 years?

<details class="solution" markdown>
<summary>Answer</summary>

Yearly charge = (48 - 8) / 8 = US$5 million. After 4 years, accumulated depreciation = 20, so net book value = 48 - 20 = US$28 million.

</details>

4\. Northwind buys another company for US$150 million. The target has identifiable assets of US$140 million and liabilities of US$40 million. How much goodwill does Northwind record?

<details class="solution" markdown>
<summary>Answer</summary>

Identifiable net assets = 140 - 40 = US$100 million. Goodwill = 150 - 100 = US$50 million.

</details>

5\. Retained earnings at the start of the year are US$275 million, net income is US$165 million and dividends are US$30 million. What is the ending balance?

<details class="solution" markdown>
<summary>Answer</summary>

275 + 165 - 30 = US$410 million.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | In a real 10-K, find the balance sheet in Item 8. Confirm that total assets equal total liabilities plus equity for the latest year. |
| 3 | Compute its working capital for the last two years. |
| 2 | Find its goodwill and write it as a percentage of total assets. |

</div>

## Key terms

- **Balance sheet**: a snapshot of assets, liabilities and equity at one date.
- **Asset**: something the company owns or is owed.
- **Liability**: something the company owes.
- **Shareholders' equity**: assets minus liabilities; also called book value.
- **Current**: due or usable within one year.
- **Working capital**: current assets minus current liabilities.
- **PP&E**: property, plant and equipment, shown net of depreciation.
- **Depreciation**: spreading the cost of a physical asset over its useful life.
- **Amortization**: the same spreading for an intangible asset.
- **Straight-line depreciation**: the same charge each year, (cost minus resale value) divided by life.
- **Net book value**: cost less accumulated depreciation.
- **Capex**: capital expenditure, spending on long-lived assets.
- **Goodwill**: the price paid for a business above the fair value of its identifiable net assets.
- **Impairment**: a write-down of an asset worth less than its book value.
- **Retained earnings**: profits kept in the company since it began.
- **Treasury stock**: shares the company bought back, shown as a deduction from equity.

Next: [The cash flow statement](04-the-cash-flow-statement.md)
