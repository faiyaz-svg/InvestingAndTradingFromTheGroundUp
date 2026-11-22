# Debt, liquidity and solvency

<span class="tag tag-data">Data</span> <span class="tag tag-part">FIN</span>

After this lesson you can work out the current ratio, quick ratio, debt to equity, net debt and interest coverage, and judge whether a company can pay its bills now and over the next few years.

Before this: [Returns on capital](07-returns-on-capital.md). You need: a calculator.

## The idea

A profitable company can still fail if it cannot pay what it owes when it is due. Two questions matter. **Liquidity** is whether the company can meet its bills over the next year. **Solvency** is whether it can carry its debt over the long run. The balance sheet and the income statement together answer both.

Debt is not bad in itself. Borrowing at 5% to fund a project that earns 20% raises returns for shareholders. The risk is that the interest is a fixed bill. A bad year does not lower it, and a lender can demand repayment or force a restructuring when a company misses a payment.

## How it works

### Liquidity

\[ \text{Current ratio} = \frac{CA}{CL} \qquad \text{Quick ratio} = \frac{\text{Cash} + AR}{CL} \]

- \(CA\) is current assets and \(CL\) is current liabilities, in US$ millions (lesson 3).
- \(AR\) is accounts receivable.
- The **current ratio** asks whether the assets due or usable within a year cover the liabilities due within a year.
- The **quick ratio** is a stricter version that leaves out inventory and prepaid items, which are slow to turn into cash. Some sources also include short-term investments (marketable securities) in the numerator. Northwind has none.

### Leverage and solvency

\[ \text{Debt to equity} = \frac{D}{E} \qquad \text{Net debt} = D - \text{Cash} \qquad \text{Interest coverage} = \frac{\text{EBIT}}{I} \]

- \(D\) is total debt: the current portion plus long-term debt. Some analysts also count lease obligations; say which you used.
- \(E\) is shareholders' equity.
- **Net debt** is debt less cash. It says how much debt would remain if the company paid it down with the cash it holds. It can be negative when cash exceeds debt.
- \(I\) is interest expense. **Interest coverage** is how many times operating profit covers the interest bill.

A common companion is net debt divided by EBITDA, the number of years of operating earnings it would take to repay net debt.

<div class="example" markdown>

### Worked example: the FY2025 ratios

From lessons 2 and 3: current assets 430, current liabilities 175, cash 130, receivables 150, debt 25 + 250 = 275, equity 650, EBIT 235, EBITDA 270, interest 15.

1. Current ratio = 430 / 175 = 2.46.
2. Quick ratio = (130 + 150) / 175 = 1.60.
3. Debt to equity = 275 / 650 = 0.42.
4. Net debt = 275 - 130 = US$145 million.
5. Net debt to EBITDA = 145 / 270 = 0.54 times.
6. Interest coverage = 235 / 15 = 15.7 times.

FY2024: current ratio 400 / 150 = 2.67, quick ratio 275 / 150 = 1.83, debt to equity 300 / 575 = 0.52, net debt 300 - 150 = US$150 million, interest coverage 180 / 16 = 11.3 times.

</div>

Every measure moved in a safer direction, except the current and quick ratios, which slipped as cash fell by 20 (lesson 4) and current liabilities rose. Both are still high. The US$25 million of debt due next year is under 20% of the US$130 million of cash.

### Stress test

A ratio on good numbers can hide a weak spot. Ask what a bad year does. If Northwind's EBIT fell by half, to 117.5, with interest unchanged at 15, coverage would be 117.5 / 15 = 7.8 times. That is still comfortable. A company with coverage near 1.5 times would not survive the same drop: its profit would no longer cover the interest.

### Where to find the detail

The ratios use totals. The 10-K's debt note (in Item 8) gives what you need to judge more: each loan or bond, its interest rate, when it is due, and any **covenants**, promises to lenders such as keeping coverage above a set level, whose breach can make the debt due immediately. Item 7A shows how much of the debt has a floating rate, which costs more when rates rise. Northwind's US$15 million of interest on an average of US$287.5 million of debt is an average rate of 5.2%.

<div class="canada" markdown>

### For Canadians

Under IFRS, lease liabilities are recorded on the balance sheet for almost all leases, so a Canadian company's debt can look larger than a comparable US company's. Compare on the same basis, and for a Canadian company with US-dollar debt, check whether the debt is in USD or CAD, because the exchange rate changes what the debt is worth in the other currency.

</div>

## Common mistakes

- Using the current ratio alone. A high ratio built on slow inventory and old receivables is weaker than it looks, which is why the quick ratio exists.
- Looking at the debt total without the due dates. US$300 million due in five years is easier than US$300 million due next quarter.
- Ignoring cash. Gross debt of US$275 million sounds heavy, but net debt of US$145 million is the figure that shows what the company really owes.

## Try it

1\. A company has current assets of US$240 million (cash 40, receivables 80, inventory 110, prepaid 10) and current liabilities of US$150 million. Find the current and quick ratios.

<details class="solution" markdown>
<summary>Answer</summary>

Current ratio = 240 / 150 = 1.60. Quick ratio = (40 + 80) / 150 = 0.80.

</details>

2\. The company has debt of US$320 million, equity of US$400 million, cash of US$40 million and EBITDA of US$100 million. Find debt to equity, net debt and net debt to EBITDA.

<details class="solution" markdown>
<summary>Answer</summary>

Debt to equity = 320 / 400 = 0.80. Net debt = 320 - 40 = US$280 million. Net debt to EBITDA = 280 / 100 = 2.8 times.

</details>

3\. Northwind's FY2025 EBITDA is US$270 million and interest is US$15 million. What is EBITDA coverage? If EBIT fell 50% to US$117.5 million, what is the interest coverage?

<details class="solution" markdown>
<summary>Answer</summary>

EBITDA coverage = 270 / 15 = 18.0 times. At EBIT of 117.5, coverage = 117.5 / 15 = 7.8 times.

</details>

4\. A company has EBIT of US$60 million and interest of US$40 million. Is it comfortable? What happens if EBIT falls 30%?

<details class="solution" markdown>
<summary>Answer</summary>

Coverage = 60 / 40 = 1.5 times, which is thin. A 30% fall gives EBIT of 42, so coverage = 42 / 40 = 1.05 times, barely above 1. The company would struggle to pay interest from operating profit.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 6 | For a real company, find the balance sheet and compute the current ratio, quick ratio, debt to equity and net debt for the latest year. |
| 2 | Find the interest expense on its income statement and compute interest coverage. |
| 2 | Open the debt note and write when the largest amount of debt falls due. |

</div>

## Key terms

- **Liquidity**: the ability to meet bills due within a year.
- **Solvency**: the ability to carry debt over the long run.
- **Current ratio**: current assets divided by current liabilities.
- **Quick ratio**: cash plus receivables divided by current liabilities.
- **Debt to equity**: total debt divided by shareholders' equity.
- **Net debt**: total debt minus cash.
- **Interest coverage**: EBIT divided by interest expense.
- **Covenant**: a promise to lenders whose breach can make debt due at once.

Next: [Shares, EPS, dilution and buybacks](09-shares-eps-dilution-and-buybacks.md)
