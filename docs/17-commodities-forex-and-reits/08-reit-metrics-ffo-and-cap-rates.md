# REIT metrics: FFO and cap rates

<span class="tag tag-data">Data</span> <span class="tag tag-part">CMDTY</span>

After this lesson you can turn a REIT's income statement into FFO and AFFO, compute the payout ratio, and estimate a net asset value from NOI and a cap rate.

Before this: [REITs explained](07-reits-explained.md), [The income statement](../09-company-financials/02-the-income-statement.md), [GAAP, non-GAAP and earnings quality](../09-company-financials/10-gaap-non-gaap-and-earnings-quality.md). You need: a calculator.

## The idea

REIT A, the made-up apartment REIT from lesson 7, has 20 million shares at US$31.50 and pays US$1.89 per share. Its income statement for the year (US$ millions, made up) is:

| Line | US$ millions |
|---|---|
| Rental revenue | 168.0 |
| Property operating expenses | -60.0 |
| Net operating income (NOI) | 108.0 |
| General and administrative | -12.0 |
| Depreciation of real estate | -42.0 |
| Interest expense | -36.0 |
| Income before gains | 18.0 |
| Gain on sale of a property | +12.0 |
| Net income | 30.0 |

Earnings per share are 30.0 / 20 = US$1.50. The dividend of US$1.89 is 1.89 / 1.50 = 126% of earnings. On this view REIT A pays more than it earns. That looks unsustainable, and it is not what is happening. Net income is a poor measure for a REIT, for two reasons. Depreciation of US$42.0 million is a charge with no cash leaving the company, and buildings often hold or gain value instead of wearing out. And the gain of US$12.0 million came from a one-time sale, not from rent.

## How it works

**Net operating income (NOI)** is rental revenue minus the costs of running the properties, before interest, depreciation and head office costs. It measures what the buildings earn.

**Funds from operations (FFO)** corrects net income for the two items above. Nareit, the US REIT trade association, defines it as net income under GAAP, excluding depreciation and amortization related to real estate, and excluding gains and losses from sales of certain real estate assets (and impairment write-downs of depreciable real estate) ([Nareit, Funds From Operations](https://www.reit.com/glossary/funds-operation-ffo), as of 2026).

\[ \text{FFO} = NI + D - G \]

- \(NI\) is net income under GAAP, in US$.
- \(D\) is depreciation and amortization of real estate, added back because it is non-cash, in US$.
- \(G\) is gains on property sales, subtracted (a loss is added back), in US$.

**Adjusted funds from operations (AFFO)** goes one step further toward cash. It subtracts the spending needed to keep the buildings competitive and non-cash income. There is no single official definition, so each REIT defines its own and reconciles it in its earnings release. Read that reconciliation before you compare two REITs.

<div class="example" markdown>

### Worked example: from net income to AFFO

1. FFO = 30.0 + 42.0 - 12.0 = US$60.0 million. Per share: 60.0 / 20 = US$3.00.
2. REIT A reports recurring capital spending of US$14.0 million (repairs, new roofs, tenant improvements that keep rents up) and US$4.0 million of **straight-line rent**, rent that accounting spreads evenly over the lease although the cash arrives later. Both are subtracted.
3. AFFO = 60.0 - 14.0 - 4.0 = US$42.0 million. Per share: 42.0 / 20 = US$2.10.
4. **Payout ratio** = dividend / AFFO per share = 1.89 / 2.10 = 90.0%. On FFO it is 1.89 / 3.00 = 63.0%. On net income it was 126%.
5. Price to FFO = 31.50 / 3.00 = 10.5. AFFO yield = 2.10 / 31.50 = 6.67%.

On cash, REIT A covers its dividend with US$0.21 per share to spare. Net income suggested a shortfall that was not there. The picture is a bridge from 30 to 60 to 42.

</div>

![A waterfall from net income of 30 to FFO of 60 to AFFO of 42, in US$ millions](../assets/figures/17-commodities-forex-and-reits/ffo-bridge-dark.svg#only-dark)
![A waterfall from net income of 30 to FFO of 60 to AFFO of 42, in US$ millions](../assets/figures/17-commodities-forex-and-reits/ffo-bridge-light.svg#only-light)

FFO and AFFO are non-GAAP measures, so Part 9's warnings apply: check what was added back ([GAAP, non-GAAP and earnings quality](../09-company-financials/10-gaap-non-gaap-and-earnings-quality.md)). A REIT that calls everything "recurring" capital spending can flatter its AFFO.

### Cap rate and net asset value

The **capitalization rate (cap rate)** is a building's NOI divided by its value:

\[ \text{cap rate} = \frac{NOI}{V} \]

- \(NOI\) is the property's yearly net operating income, in US$.
- \(V\) is the property's value, in US$.
- The result is a yearly yield on the property before any loan. A lower cap rate means a higher price for the same NOI.

**Net asset value (NAV)** is the estimated value of the properties minus the REIT's debt, often given per share. To estimate it, pick a cap rate for the portfolio, divide NOI by it, and subtract the debt.

<div class="example" markdown>

### Worked example: NAV for REIT A

REIT A has US$720.0 million of debt (36.0 interest at 5.0%). An analyst uses a 7.5% cap rate (made up).

1. Property value = 108.0 / 0.075 = US$1,440.0 million.
2. NAV = 1,440.0 - 720.0 = US$720.0 million. Per share: 720.0 / 20 = US$36.00.
3. The share price of US$31.50 is 31.50 / 36.00 - 1 = -12.5%, a 12.5% discount to NAV.
4. Reverse it: the market value of the equity is 31.50 x 20 = US$630.0 million. Adding the debt gives US$1,350.0 million for the properties. The cap rate the market is paying is 108.0 / 1,350.0 = 8.0%.

A discount to NAV can mean the market uses a higher cap rate than the analyst, expects NOI to fall, or distrusts the debt. A NAV is only as good as the cap rate chosen.

</div>

## In code

<details class="code" markdown>
<summary>In code</summary>

```python
ni, dep, gain = 30.0, 42.0, 12.0
capex, straight_line = 14.0, 4.0
shares, price, div = 20.0, 31.50, 1.89
noi, debt, cap = 108.0, 720.0, 0.075

ffo = ni + dep - gain
affo = ffo - capex - straight_line
print(ffo, affo)                                  # 60.0 42.0
print(round(div / (affo / shares), 3))            # payout of AFFO: 0.9
nav = (noi / cap - debt) / shares
print(round(nav, 2), round(price / nav - 1, 3))   # 36.0 -0.125
```

</details>

<div class="canada" markdown>

### For Canadians

Canadian REITs report FFO and AFFO per unit in their results, sometimes with their own definitions. Find the reconciliation in the filing on SEDAR+, and check what each adjustment is. For a US REIT, the reconciliation is in the earnings release attached to a Form 8-K, which Part 9 shows how to find ([Filings and EDGAR](../09-company-financials/01-filings-and-edgar.md)).

</div>

## Common mistakes

- Using P/E on a REIT. Depreciation and sale gains distort earnings, so use price to FFO or AFFO.
- Comparing AFFO across REITs without reading the definitions. Two REITs with the same cash flow can report different AFFO.
- Treating a NAV as a price target. A different cap rate gives a different NAV, and cap rates move with interest rates (lesson 9).

## Try it

1\. A REIT has net income US$50.0 million, real estate depreciation US$80.0 million and a gain on a sale of US$20.0 million. What is FFO?

<details class="solution" markdown>
<summary>Answer</summary>

FFO = 50.0 + 80.0 - 20.0 = US$110.0 million.

</details>

2\. The same REIT has 40 million shares, pays US$2.20 per share and has AFFO of US$95.0 million. What is the payout ratio on AFFO?

<details class="solution" markdown>
<summary>Answer</summary>

AFFO per share = 95.0 / 40 = US$2.375. Payout = 2.20 / 2.375 = 92.6%.

</details>

3\. A building has NOI of US$4.2 million and is sold for US$60.0 million. What is the cap rate?

<details class="solution" markdown>
<summary>Answer</summary>

4.2 / 60.0 = 0.070, which is 7.0%.

</details>

4\. A REIT has NOI of US$90.0 million, debt of US$500.0 million, 25 million shares and a cap rate of 6.0%. What is NAV per share?

<details class="solution" markdown>
<summary>Answer</summary>

Value = 90.0 / 0.06 = US$1,500.0 million. NAV = 1,500.0 - 500.0 = US$1,000.0 million. Per share = 1,000.0 / 25 = US$40.00.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 6 | Open one REIT's latest earnings release. Find net income, the FFO reconciliation and AFFO. Write the three numbers and the adjustments between them. |
| 2 | Compute its payout ratio on AFFO. |
| 2 | Write the share price divided by FFO per share in your [journal](../practice/trade-journal.md). |

</div>

## Key terms

- **Net operating income (NOI)**: property revenue minus property operating expenses, before interest, depreciation and head office costs.
- **Funds from operations (FFO)**: net income plus real estate depreciation, minus gains (plus losses) on property sales.
- **Adjusted funds from operations (AFFO)**: FFO adjusted for recurring capital spending and non-cash items, defined by each REIT.
- **Straight-line rent**: rent that accounting spreads evenly over a lease.
- **Payout ratio**: the dividend divided by FFO or AFFO per share.
- **Capitalization rate (cap rate)**: NOI divided by property value.
- **Net asset value (NAV)**: estimated property value minus debt, often per share.

Next: [Rates and real estate](09-rates-and-real-estate.md)
