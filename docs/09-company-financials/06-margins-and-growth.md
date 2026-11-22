# Margins and growth

<span class="tag tag-data">Data</span> <span class="tag tag-part">FIN</span>

After this lesson you can work out gross, operating, EBITDA and net margins, growth rates and a compound annual growth rate, and say what operating leverage did to a company's profit.

Before this: [How the three statements connect](05-how-the-statements-connect.md), [percent change](https://faiyaz-svg.github.io/MathFromTheGroundUp/02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications/) in the math book. You need: a calculator.

## The idea

Northwind's revenue grew 15% in FY2025. Its net income grew 34.1%. Why did profit grow more than twice as fast as sales? The answer is in the margins. A **margin** is a profit measure divided by revenue. It says how many cents of each sales dollar stay at that stage of the income statement, and it lets you compare a US$1,150 million company with a US$11 billion one.

## How it works

### The margins

\[ \text{Margin} = \frac{\text{Profit measure}}{R} \]

- \(R\) is revenue for the same period, in US$ millions.
- The profit measure is gross profit (gross margin), EBIT (operating margin), EBITDA (EBITDA margin) or net income (net margin).

| | FY2024 | FY2025 | Change (percentage points) |
|---|---|---|---|
| Gross margin | 40.0% | 42.0% | +2.0 |
| EBITDA margin | 21.0% | 23.5% | +2.5 |
| Operating margin | 18.0% | 20.4% | +2.4 |
| Net margin | 12.3% | 14.3% | +2.0 |

Each uses the lesson 2 numbers: gross profit 400 and 483, EBITDA 210 and 270, EBIT 180 and 235, net income 123 and 165, over revenue of 1,000 and 1,150. Percentages are rounded to one decimal at the end, so a change is computed from the unrounded values.

Gross margin tells you about the product: pricing power and unit costs. A rise from 40.0% to 42.0% means each sales dollar leaves 2 more cents after the direct costs. Operating margin tells you about the whole business, because it includes selling, research and overhead. Net margin adds interest and taxes, so it moves with the debt load and the tax rate.

### Growth

**Growth** is the percentage change from one period to the next:

\[ g = \frac{X_1 - X_0}{X_0} \]

- \(X_0\) is the earlier value and \(X_1\) the later one, in the same units.

For a series over several years, the **compound annual growth rate** (CAGR) is the single yearly rate that gives the same end value:

\[ \text{CAGR} = \left(\frac{X_n}{X_0}\right)^{1/n} - 1 \]

- \(X_0\) is the starting value and \(X_n\) the value after \(n\) years.
- \(n\) is the number of years between them (not the number of data points).

The math book covers [compounding](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/02-interest-and-growth/02-compound-interest/); a CAGR is that formula solved for the rate.

### Operating leverage

Some costs do not move with sales in the short run: rent, salaries, research. When revenue grows, those costs grow more slowly, so a larger share of each new dollar of revenue becomes profit. This is **operating leverage**. A rough gauge is the ratio of EBIT growth to revenue growth.

<div class="example" markdown>

### Worked example: why profit outgrew sales

1. Revenue growth = (1,150 - 1,000) / 1,000 = 15.0%.
2. EBIT growth = (235 - 180) / 180 = 30.6%.
3. Net income growth = (165 - 123) / 123 = 34.1%.
4. Operating leverage = 30.6 / 15.0 = 2.04. EBIT grew about twice as fast as revenue.

The reason shows in each cost as a share of revenue. SG&A went from 130 / 1,000 = 13.0% to 145 / 1,150 = 12.6%. R&D went from 6.0% to 5.9%. Gross margin also rose 2.0 points. The two effects together widened the operating margin by 2.4 points. Net income grew faster still because interest expense fell (16 to 15) and the tax rate stayed at 25%.

</div>

Operating leverage works in both directions. If Northwind's revenue fell 15% next year and its costs did not fall at the same pace, EBIT would fall by more than 15%. A company with a high share of fixed costs has bigger swings in profit than in sales.

### Reading margins

A margin on its own says little. Three comparisons make it useful:

1. Against the company's own past, over several years: is it rising, flat or sliding?
2. Against peers in the same industry. Margins differ by business: a software company may have a gross margin near 80%, and a grocer near 25%.
3. Against growth. Rising revenue with falling margins can mean the company is buying growth with discounts or heavy spending.

<div class="canada" markdown>

### For Canadians

When you compare a Canadian company with a US one, margins are unit-free, so currency does not matter for the ratio. It matters when you compare growth in absolute dollars across a period when CAD and USD moved, so check whether the filing gives a "constant currency" growth figure and how the company defines it (lesson 10).

</div>

## Common mistakes

- Subtracting two margins and calling the result a percent. From 40.0% to 42.0% is 2.0 percentage points. It is a 5% increase in the margin, which is a different statement.
- Comparing margins across industries. A 10% net margin is thin for software and good for a distributor.
- Reading one year of growth as a trend. Use a CAGR over several years, and look at what happened in the year in between.

## Try it

1\. A company's revenue was US$600 million three years ago and is US$864 million now. What is the CAGR?

<details class="solution" markdown>
<summary>Answer</summary>

(864 / 600)^(1/3) - 1 = 1.44^(0.3333) - 1 = 1.1292 - 1, so 12.9% a year (rounded to one decimal).

</details>

2\. Northwind's gross profit was US$400 million on revenue of US$1,000 million in FY2024, and US$483 million on US$1,150 million in FY2025. What were the gross margins, and the change in percentage points?

<details class="solution" markdown>
<summary>Answer</summary>

FY2024: 400 / 1,000 = 40.0%. FY2025: 483 / 1,150 = 42.0%. Change = +2.0 percentage points.

</details>

3\. A company's revenue grows 8% and its EBIT grows 20%. What is its operating leverage ratio? What does a 5% revenue drop do to EBIT if the ratio holds?

<details class="solution" markdown>
<summary>Answer</summary>

20 / 8 = 2.5. A 5% revenue drop gives about a 2.5 x 5 = 12.5% drop in EBIT.

</details>

4\. Northwind's FY2025 operating expenses are US$248 million. If its SG&A had stayed at 13.0% of revenue, what would SG&A be, and how much lower would EBIT be?

<details class="solution" markdown>
<summary>Answer</summary>

SG&A at 13.0% of 1,150 = US$149.5 million, against the actual 145. EBIT would be 149.5 - 145 = US$4.5 million lower, so 230.5.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 6 | From a real company's last two 10-Ks, write revenue, gross profit, operating income and net income for the last three years. Compute the four margins for each year. |
| 2 | Compute the revenue CAGR over the three years. |
| 2 | Write one sentence on whether operating leverage helped or hurt. |

</div>

## Key terms

- **Margin**: a profit measure divided by revenue.
- **Gross margin**: gross profit divided by revenue.
- **Operating margin**: operating income (EBIT) divided by revenue.
- **EBITDA margin**: EBITDA divided by revenue.
- **Net margin**: net income divided by revenue.
- **Growth**: the percentage change from one period to the next.
- **Compound annual growth rate (CAGR)**: the single yearly rate that turns a start value into an end value.
- **Operating leverage**: profit growing faster than sales because many costs do not rise with sales.
- **Percentage points**: the unit for a change between two percentages.

Next: [Returns on capital](07-returns-on-capital.md)
