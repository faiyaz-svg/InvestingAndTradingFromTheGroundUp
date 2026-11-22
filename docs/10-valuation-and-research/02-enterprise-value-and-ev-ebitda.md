# Enterprise value and EV/EBITDA

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">VAL</span>

After this lesson you can work out a company's enterprise value from its market cap and balance sheet, and use EV/EBITDA and EV/sales to compare companies with different amounts of debt.

Before this: [Price multiples](01-multiples.md), [Debt, liquidity and solvency](../09-company-financials/08-debt-liquidity-and-solvency.md). You need: a calculator.

## The idea

Two companies each have a market cap of US$1,000 million and earn US$100 million of EBITDA (operating profit before depreciation and amortization). Stock B has no debt. Stock C owes US$400 million and holds US$100 million of cash. Which one is cheaper?

Buying all of Stock B costs US$1,000 million. Buying all of Stock C costs US$1,000 million for the shares, plus you take on US$400 million of debt, less the US$100 million of cash you get with it: US$1,300 million for the same EBITDA. Stock C is more expensive per dollar of operating profit, and a P/E or P/S would not show it.

**Enterprise value** (EV) is the price of the whole business, debt and equity together, net of the cash it holds. It is what a buyer pays for the operations.

## How it works

\[ \text{EV} = \text{equity value} + \text{debt} + \text{preferred stock} + \text{minority interest} - \text{cash} \]

- Equity value is the market cap, with the share count adjusted for dilution (step 1 below).
- Debt is short-term plus long-term borrowings, in US$ millions.
- Preferred stock is a class of shares that pays a fixed dividend and ranks ahead of common shares. Many companies have none.
- Minority interest (also called non-controlling interest) is the part of a consolidated subsidiary that outsiders own. The income statement counts 100% of the subsidiary's profit, so EV adds the outside owners' share to match.
- Cash means cash and short-term investments, which a buyer could use to pay down debt.

Steps:

1. Equity value: use diluted shares. Options in the money and restricted stock units become shares ([Shares, EPS, dilution and buybacks](../09-company-financials/09-shares-eps-dilution-and-buybacks.md)). Use the treasury stock method at the current price.
2. Add debt, preferred stock and minority interest from the latest balance sheet.
3. Subtract cash.
4. Divide by a measure from before interest: EBITDA, EBIT or sales.

\[ \text{EV/EBITDA} = \frac{\text{EV}}{\text{EBITDA}} \qquad \text{EV/sales} = \frac{\text{EV}}{\text{revenue}} \]

The numerator and the denominator must match. EV belongs to everyone who funds the business (lenders and shareholders), so it goes with a profit that is before interest (EBITDA, EBIT, sales). Market cap belongs to shareholders only, so it goes with profit after interest (net income, EPS). Mixing them, such as EV / net income, gives a number that means nothing.

<div class="example" markdown>

### Worked example: enterprise value from the balance sheet

Price US$50.00. Shares outstanding 98.5 million. Options: 4.0 million with a US$20 strike. RSUs: 0.6 million.

1. Net new option shares = 4.0 - 4.0 x 20 / 50 = 2.4 million. Diluted shares = 98.5 + 2.4 + 0.6 = 101.5 million.
2. Equity value = 50.00 x 101.5 = US$5,075 million (the basic market cap is 4,925).

   This part values the company at year end, so it uses the 98.5 million shares outstanding then. Part 9's diluted EPS of US$1.61 divides by 102.5 million, the average count over FY2025 (99.5 + 2.4 + 0.6). Both are right: one is a point in time, the other an average over the year.
3. Debt = 25 + 250 = US$275 million. Cash = US$130 million. No preferred stock or minority interest.
4. EV = 5,075 + 275 - 130 = US$5,220 million.

Northwind's FY2025 EBITDA is EBIT + D&A = 235 + 35 = US$270 million.

- EV/EBITDA = 5,220 / 270 = 19.3
- EV/EBIT = 5,220 / 235 = 22.2
- EV/sales = 5,220 / 1,150 = 4.54

</div>

The figure shows the steps from the market cap to EV.

![Northwind's market cap of 4,925 plus 150 for options and stock units gives 5,075; plus debt of 275 and minus cash of 130 gives an enterprise value of 5,220 US$ millions](../assets/figures/10-valuation-and-research/ev-bridge-dark.svg#only-dark)
![Northwind's market cap of 4,925 plus 150 for options and stock units gives 5,075; plus debt of 275 and minus cash of 130 gives an enterprise value of 5,220 US$ millions](../assets/figures/10-valuation-and-research/ev-bridge-light.svg#only-light)

### Preferred stock and minority interest

Stock D has a market cap of US$2,000 million, debt of US$600 million, cash of US$150 million, preferred stock of US$100 million and minority interest of US$80 million. EV = 2,000 + 600 + 100 + 80 - 150 = US$2,630 million. With EBITDA of US$250 million, EV/EBITDA = 2,630 / 250 = 10.5.

### What EBITDA hides

EBITDA is a rough stand-in for operating cash flow. It ignores capex, taxes and working capital. Northwind's EBITDA is US$270 million, but its unlevered free cash flow (lesson 3) is US$106.25 million, 39% of EBITDA. A capital-heavy business (a railway, a telecom) can show a low EV/EBITDA and still have little cash left after capex. EV/EBITDA is useful for comparing companies in the same industry with similar capital needs, and less useful across industries.

Lease treatment also differs. Under US GAAP, operating lease cost is inside EBITDA and the lease liability is usually left out of debt. Under IFRS, lease costs are depreciation and interest, so EBITDA is higher and lease liabilities count as debt. Compare a US company with a Canadian one with that in mind, and check each data provider's definition.

## In code

<details class="code" markdown>
<summary>In code</summary>

```python
def enterprise_value(price, shares, options, strike, rsu, debt, cash, preferred=0, minority=0):
    net_options = max(options - options * strike / price, 0)
    equity = price * (shares + net_options + rsu)
    return equity + debt + preferred + minority - cash

ev = enterprise_value(50.00, 98.5, 4.0, 20.0, 0.6, 275, 130)
print(f"EV {ev:,.0f}  EV/EBITDA {ev / 270:.1f}  EV/sales {ev / 1150:.2f}")
```

</details>

## Common mistakes

- Using the basic share count for equity value. Options and RSUs are claims on the company, so count them.
- Subtracting cash that is not free, such as cash held in a foreign subsidiary that would be taxed to bring home, or cash a bank must hold. Check the notes.
- Comparing EV/EBITDA across industries. Capital needs and growth differ too much.

## Try it

1\. Stock E has a market cap of US$3,000 million, debt of US$800 million and cash of US$300 million. Its EBITDA is US$250 million. Find EV and EV/EBITDA.

<details class="solution" markdown>
<summary>Answer</summary>

EV = 3,000 + 800 - 300 = US$3,500 million. EV/EBITDA = 3,500 / 250 = 14.0.

</details>

2\. Stock F has the same market cap and EBITDA as Stock E but no debt and US$300 million of cash. Find its EV/EBITDA.

<details class="solution" markdown>
<summary>Answer</summary>

EV = 3,000 - 300 = US$2,700 million. EV/EBITDA = 2,700 / 250 = 10.8. The same market cap and profit give a much lower multiple once debt and cash count.

</details>

3\. A company has a price of US$20, 50 million shares, 6 million options with a strike of US$10 and no RSUs. What is its diluted equity value?

<details class="solution" markdown>
<summary>Answer</summary>

Net new shares = 6 - 6 x 10 / 20 = 3 million. Diluted shares = 53 million. Equity value = 20 x 53 = US$1,060 million.

</details>

4\. Northwind's price falls to US$40. Find the new net option shares, equity value and EV.

<details class="solution" markdown>
<summary>Answer</summary>

Net option shares = 4.0 - 4.0 x 20 / 40 = 2.0 million. Diluted shares = 98.5 + 2.0 + 0.6 = 101.1 million. Equity value = 40 x 101.1 = US$4,044 million. EV = 4,044 + 275 - 130 = US$4,189 million.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Pick a company with debt. From its latest 10-K balance sheet, find debt and cash, and build its EV with the steps above. |
| 3 | Compare your EV/EBITDA with the one on a data site. Note the difference and guess where it comes from (leases, cash, share count). |
| 2 | Write one line on why EV/EBITDA suits this company or does not. |

</div>

## Key terms

- **Enterprise value (EV)**: equity value plus debt, preferred stock and minority interest, minus cash.
- **EBITDA**: earnings before interest, taxes, depreciation and amortization.
- **EV/EBITDA**: enterprise value divided by EBITDA.
- **EV/sales**: enterprise value divided by revenue.
- **Preferred stock**: shares with a fixed dividend that rank ahead of common shares.
- **Minority interest**: the share of a consolidated subsidiary owned by outside investors.

Next: [Free cash flow](03-free-cash-flow.md)
