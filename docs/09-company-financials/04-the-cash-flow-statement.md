# The cash flow statement

<span class="tag tag-data">Data</span> <span class="tag tag-part">FIN</span>

After this lesson you can read a cash flow statement, rebuild operating cash flow from net income with the indirect method, and work out capex and free cash flow.

Before this: [The balance sheet](03-the-balance-sheet.md). You need: a calculator.

## The idea

Northwind reported US$165 million of net income in FY2025, yet its cash fell from US$150 million to US$130 million. Both are true. Net income is an accrual figure (lesson 2), so it counts revenue before the cash arrives and subtracts costs, such as depreciation, that used no cash this year. The **cash flow statement** tracks the actual movement of cash and explains the change in the cash line of the balance sheet.

It has three sections.

| Section | What it covers |
|---|---|
| Operating activities (CFO) | Cash from running the business: customers in, suppliers, staff and taxes out |
| Investing activities (CFI) | Buying and selling long-lived assets, such as factories and other companies |
| Financing activities (CFF) | Cash to and from lenders and shareholders: debt, dividends, buybacks, new shares |

## How it works

### Operating cash flow, indirect method

Companies report operating cash flow by the **indirect method**: start with net income, add back non-cash charges, then adjust for changes in working capital. The method is "indirect" because it works from profit instead of listing cash received and paid.

\[ \text{CFO} = NI + D + S + \Delta W \]

- \(NI\) is net income, in US$ millions.
- \(D\) is depreciation and amortization, an expense that used no cash this year.
- \(S\) is stock-based compensation, an expense paid in shares, not cash (lesson 9).
- \(\Delta W\) is the change in working capital items. An increase in an asset (receivables, inventory) uses cash, so it is subtracted. An increase in a liability (payables, accrued expenses) holds cash back, so it is added.

<div class="example" markdown>

### Worked example: the FY2025 cash flow

Start with the two balance sheets from lesson 3.

1. Net income: +165. D&A: +35. Stock-based pay: +30.
2. Receivables rose from 125 to 150: -25. Inventory rose from 100 to 120: -20. Prepaid and other rose from 25 to 30: -5.
3. Accounts payable rose from 80 to 95: +15. Accrued expenses rose from 45 to 55: +10.
4. Working capital change = -25 - 20 - 5 + 15 + 10 = -25.
5. CFO = 165 + 35 + 30 - 25 = US$205 million.

Investing: capex of 80 for PP&E, so CFI = -US$80 million.

Financing: debt repaid -25, buybacks -100, dividends -30, cash from employees exercising options +10. CFF = -25 - 100 - 30 + 10 = -US$145 million.

Net change in cash = 205 - 80 - 145 = -US$20 million. Opening cash 150, so closing cash = 150 - 20 = US$130 million, which matches the balance sheet.

</div>

| US$ millions | FY2025 |
|---|---|
| Net income | 165 |
| Depreciation and amortization | 35 |
| Stock-based compensation | 30 |
| Change in receivables | -25 |
| Change in inventory | -20 |
| Change in prepaid and other | -5 |
| Change in accounts payable | 15 |
| Change in accrued expenses | 10 |
| Cash from operating activities | 205 |
| Capital expenditures | -80 |
| Cash from investing activities | -80 |
| Repayment of debt | -25 |
| Share repurchases | -100 |
| Dividends paid | -30 |
| Proceeds from option exercises | 10 |
| Cash from financing activities | -145 |
| Net change in cash | -20 |
| Cash at start of year | 150 |
| Cash at end of year | 130 |

Northwind pays tax and interest in the year it expenses them, so the model needs no extra adjustment. Real statements often add deferred taxes and other lines; US GAAP also reports interest paid and taxes paid in notes.

### Capex and free cash flow

**Capital expenditure** (capex) is cash spent on long-lived assets. **Free cash flow** (FCF) is what is left from operations after that spending, available for debt, dividends, buybacks or cash on hand:

\[ \text{FCF} = \text{CFO} - \text{capex} \]

Northwind's FCF is 205 - 80 = US$125 million, which is 125 / 1,150 = 10.9% of revenue. The figure walks from net income to FCF. Look at how depreciation and stock-based pay lift cash above profit while working capital and capex take it back.

![Northwind FY2025 cash bridge from net income of 165 to operating cash flow of 205 to free cash flow of 125](../assets/figures/09-company-financials/cash-bridge-dark.svg#only-dark)
![Northwind FY2025 cash bridge from net income of 165 to operating cash flow of 205 to free cash flow of 125](../assets/figures/09-company-financials/cash-bridge-light.svg#only-light)

Northwind returned 100 + 30 = US$130 million to shareholders, more than its US$125 million of FCF, and paid down 25 of debt. The gap came out of the cash balance. A company can do that for a year or two. Doing it for many years needs borrowing. Part 10 uses FCF in valuation (Free cash flow<!-- link: ../10-valuation-and-research/03-free-cash-flow.md -->).

Stock-based pay is a real cost paid in shares, and CFO adds it back. If the company had paid those employees in cash, FCF would be 125 - 30 = US$95 million. Lesson 9 returns to this.

## Common mistakes

- Treating CFO as hard to move. Working capital shifts it: stretching payables for a quarter raises CFO without improving the business.
- Calling a rising receivables line good news. It uses cash. If receivables grow faster than revenue (Northwind's grew 20% against revenue growth of 15%), ask why.
- Reading negative CFI as bad. A growing company has negative investing cash flow because it invests. The question is what the investment earns (lesson 7).

## Try it

1\. A company has net income of US$80 million, D&A of US$20 million, stock-based pay of US$10 million, a US$15 million increase in receivables and a US$5 million increase in payables. Find CFO.

<details class="solution" markdown>
<summary>Answer</summary>

CFO = 80 + 20 + 10 - 15 + 5 = US$100 million.

</details>

2\. The same company spends US$35 million on capex. What is its FCF, and what share of net income is that?

<details class="solution" markdown>
<summary>Answer</summary>

FCF = 100 - 35 = US$65 million. Share of net income = 65 / 80 = 81.3%.

</details>

3\. Northwind's inventory had risen from US$100 million to US$120 million. What does that do to operating cash flow, and by how much?

<details class="solution" markdown>
<summary>Answer</summary>

It lowers CFO by US$20 million, because cash was spent on inventory still on the shelf.

</details>

4\. Northwind's cash at the start of FY2025 was US$150 million, CFO 205, CFI -80 and CFF -145. What is the ending cash? Does it match the balance sheet?

<details class="solution" markdown>
<summary>Answer</summary>

150 + 205 - 80 - 145 = US$130 million. It matches the Dec 31, 2025 cash line in lesson 3.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | In a real 10-K, find the cash flow statement. Write CFO, capex and the free cash flow (CFO minus capex) for the last two years. |
| 3 | Compare CFO with net income. Which is larger, and by how much? |
| 2 | List the three largest financing uses of cash (debt, dividends, buybacks). |

</div>

## Key terms

- **Cash flow statement**: the report of cash in and out, in three sections, that explains the change in cash.
- **Operating activities (CFO)**: cash from running the business.
- **Investing activities (CFI)**: cash spent on or raised from long-lived assets.
- **Financing activities (CFF)**: cash to and from lenders and shareholders.
- **Indirect method**: starting from net income and adjusting for non-cash items and working capital.
- **Stock-based compensation**: pay in shares or options instead of cash, an expense that uses no cash.
- **Free cash flow (FCF)**: operating cash flow minus capex.

Next: [How the three statements connect](05-how-the-statements-connect.md)
