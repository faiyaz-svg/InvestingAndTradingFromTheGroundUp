# Comparables and industry KPIs

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">VAL</span>

After this lesson you can value a company against a peer group with a multiple, and read the main performance measures used in software, banking, retail and energy.

Before this: [Enterprise value and EV/EBITDA](02-enterprise-value-and-ev-ebitda.md), [A DCF step by step](05-dcf-step-by-step.md). You need: a calculator.

## The idea

A DCF values a company from its own cash flows. **Comparable company analysis** ("comps") values it from what the market pays for similar companies. If four peers trade at 12 to 21 times EBITDA, a similar company probably trades somewhere in that band. Comps are fast and they carry the market's mood, which is both their appeal and their flaw: if the whole group is overpriced, comps will say your stock is fairly priced.

## How it works

1. Pick 4 to 10 peers: same industry, similar size, growth and margins, same business model.
2. Pick the multiple that fits (EV/EBITDA for most industrial companies, EV/sales for fast growers with thin profit, P/E for stable profits, P/B for banks).
3. Compute each peer's multiple from the same data source and the same period (all trailing, or all forward).
4. Take the median, which resists one odd peer. Look at the range too.
5. Multiply the median by your company's metric to get a value, then adjust for differences in growth, margin and risk.

<div class="example" markdown>

### Worked example: a company against four peers

Peers (made up), with enterprise value and EBITDA in US$ millions:

| | EV | EBITDA | EV/EBITDA | Revenue growth | EBITDA margin |
|---|---|---|---|---|---|
| Stock B | 2,900 | 200 | 14.5 | 8% | 22% |
| Stock C | 6,800 | 400 | 17.0 | 12% | 28% |
| Stock D | 4,200 | 200 | 21.0 | 20% | 24% |
| Stock E | 3,000 | 250 | 12.0 | 4% | 20% |
| Northwind | 5,220 | 270 | 19.3 | 15% | 23.5% |

1. The median of 12.0, 14.5, 17.0 and 21.0 is (14.5 + 17.0) / 2 = 15.75.
2. Implied enterprise value = 15.75 x 270 = US$4,252.5 million.
3. Equity value = 4,252.5 - 145 = US$4,107.5 million (debt 275, cash 130).
4. Per share = 4,107.5 / 101.5 = US$40.47.

The range: at 12.0 times the value is (3,240 - 145) / 101.5 = US$30.49 and at 21.0 times it is (5,670 - 145) / 101.5 = US$54.43.

</div>

![EV/EBITDA bars: Stock B 14.5, Stock C 17.0, Stock D 21.0, Stock E 12.0 and Northwind 19.3 times, with the peer median at 15.75](../assets/figures/10-valuation-and-research/peers-dark.svg#only-dark)
![EV/EBITDA bars: Stock B 14.5, Stock C 17.0, Stock D 21.0, Stock E 12.0 and Northwind 19.3 times, with the peer median at 15.75](../assets/figures/10-valuation-and-research/peers-light.svg#only-light)

Northwind trades above the median. Its growth of 15% is above the peers' median of 10%, so some premium is fair. The comps value of US$40.47 is close to the DCF base case of US$39.42, and the US$50.00 price sits in the upper part of the peer range. Two different methods, built from different data, agree that the price asks for more than the average peer delivers. Where they agree, you gain confidence. Where they disagree, find out why before you trust either.

## Industry measures

Each industry has measures that show how the business works, and that analysts quote beside the multiples. A few, with numbers.

### Software

**Annual recurring revenue** (ARR) is the yearly value of subscription contracts, usually the monthly recurring revenue x 12. **Net revenue retention** (NRR) is how much revenue last year's customers pay now, after upgrades, downgrades and cancellations, with new customers left out.

\[ \text{NRR} = \frac{\text{start ARR} + \text{expansion} - \text{contraction} - \text{churn}}{\text{start ARR}} \]

With start ARR of US$100 million, expansion of 18, contraction of 4 and churn of 6: NRR = (100 + 18 - 4 - 6) / 100 = 108%. The customers you already have grow 8% a year with no new sales. Gross retention (the same without expansion) = (100 - 4 - 6) / 100 = 90%. The **rule of 40** is a rule of thumb: revenue growth % plus free cash flow margin % should be at least 40. A company growing 28% with a 14% FCF margin scores 42.

### Banks

A bank earns the gap between what it charges on loans and pays on deposits. The **net interest margin** (NIM) is net interest income divided by average earning assets: 1,200 / 30,000 = 4.0%. The **efficiency ratio** is non-interest expense divided by revenue (net interest income plus fee income), so lower is better. With non-interest expense of 1,200, net interest income of 1,200 and fees of 800: 1,200 / (1,200 + 800) = 60%. **CET1** (common equity tier 1) is the highest-quality capital a bank holds, shown as a ratio of risk-weighted assets: 9,000 / 75,000 = 12.0%. Regulators set minimums that change, so check the current ones for the bank you study. P/B and return on equity are the usual multiples for banks, and EBITDA and EV are rarely used, because interest is a bank's operating cost.

### Retail

**Same-store sales** (comparable sales) is the sales growth of stores open at least a year, which removes the effect of opening new stores: 520 / 500 - 1 = 4.0%. **Inventory turns** is cost of goods sold divided by inventory, here on year-end inventory: Northwind's 667 / 120 = 5.56 times, or 365 / 5.56 = 65.7 days of inventory (the same figure as the days of inventory in part 9). A falling turn rate, with sales flat, warns that goods are not selling.

### Energy

Oil and gas producers report **proved reserves**: estimated amounts of oil and gas that can be recovered from known fields under current conditions with reasonable certainty. The estimates are revised each year. Reserve life = reserves / annual output: 600 million barrels of oil equivalent at 50 million a year gives 12 years. The **breakeven price** is the oil price at which a project earns zero: lifting cost 12 + royalties and taxes 6 + development capex 22 + overhead and interest 5 = US$45 a barrel. At US$70 the margin is US$25 a barrel, and at US$50 it is US$5. Energy stocks follow the commodity price, so a P/E taken at a peak says little ([What moves oil and gold](../17-commodities-forex-and-reits/02-what-moves-oil-and-gold.md)).

### REITs

Real estate investment trusts use funds from operations (FFO) in place of earnings. The lesson [REIT metrics: FFO and cap rates](../17-commodities-forex-and-reits/08-reit-metrics-ffo-and-cap-rates.md) covers them in part 17.

## In code

<details class="code" markdown>
<summary>In code</summary>

```python
import statistics

peers = {"B": (2900, 200), "C": (6800, 400), "D": (4200, 200), "E": (3000, 250)}
multiples = {k: ev / ebitda for k, (ev, ebitda) in peers.items()}
median = statistics.median(multiples.values())
value = (median * 270 - 275 + 130) / 101.5
print(multiples, median, round(value, 2))   # median 15.75, US$40.47
```

</details>

## Common mistakes

- Choosing peers by industry label alone. A fast grower and a slow one in the same sector deserve different multiples.
- Mixing trailing multiples for some peers and forward ones for others.
- Using the average when one peer is far out. Use the median and look at the range.

## Try it

1\. Four peers trade at EV/EBITDA of 8, 10, 12 and 30. What is the median, and what is the mean?

<details class="solution" markdown>
<summary>Answer</summary>

Median = (10 + 12) / 2 = 11. Mean = (8 + 10 + 12 + 30) / 4 = 15. The outlier of 30 pulls the mean up, which is why the median is used.

</details>

2\. A company has EBITDA of US$80 million, debt of US$150 million and cash of US$30 million, with 20 million diluted shares. At a peer median of 11 times, what is its value per share?

<details class="solution" markdown>
<summary>Answer</summary>

EV = 11 x 80 = 880. Equity = 880 - 150 + 30 = 760. Per share = 760 / 20 = US$38.00.

</details>

3\. A software company starts the year with US$200 million of ARR and gets US$30 million of expansion, loses US$10 million to contraction and US$14 million to churn. Find NRR and gross retention.

<details class="solution" markdown>
<summary>Answer</summary>

NRR = (200 + 30 - 10 - 14) / 200 = 206 / 200 = 103%. Gross retention = (200 - 10 - 14) / 200 = 88%.

</details>

4\. A bank has net interest income of US$600 million, fee income of US$400 million, non-interest expense of US$550 million and average earning assets of US$15,000 million. Find the NIM and the efficiency ratio.

<details class="solution" markdown>
<summary>Answer</summary>

NIM = 600 / 15,000 = 4.0%. Efficiency ratio = 550 / (600 + 400) = 55%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 6 | Pick a company and three peers. Write each one's EV/EBITDA or P/E from one data site, and the median. |
| 4 | Write two reasons the company deserves a multiple above or below the median. |

</div>

## Key terms

- **Comparable company analysis (comps)**: valuing a company from the multiples of similar companies.
- **Peer group**: the companies chosen for comparison.
- **Annual recurring revenue (ARR)**: the yearly value of subscription contracts.
- **Net revenue retention (NRR)**: revenue from last year's customers now, as a share of last year's.
- **Rule of 40**: revenue growth % plus free cash flow margin % of at least 40.
- **Net interest margin (NIM)**: net interest income divided by average earning assets.
- **Efficiency ratio**: a bank's non-interest expense divided by its revenue.
- **CET1 ratio**: common equity tier 1 capital divided by risk-weighted assets.
- **Same-store sales**: sales growth of stores open at least a year.
- **Inventory turns**: cost of goods sold divided by inventory.
- **Proved reserves**: oil and gas that can be recovered with reasonable certainty under current conditions.
- **Breakeven price**: the commodity price at which a project earns zero.

Next: [Moats and qualitative research](08-moats-and-qualitative-research.md)
