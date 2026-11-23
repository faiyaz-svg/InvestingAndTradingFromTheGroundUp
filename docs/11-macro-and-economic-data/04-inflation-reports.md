# Inflation reports: CPI, PCE and PPI

<span class="tag tag-data">Data</span> <span class="tag tag-part">MACRO</span>

After this lesson you can tell the four inflation measures apart, say which one the Fed targets, and work out why headline and core inflation can differ in the same month.

Before this: [Interest rates and asset prices](03-interest-rates-and-asset-prices.md). For the maths of price indexes, see [CPI and inflation](https://faiyaz-svg.github.io/MathFromTheGroundUp/07-economics-math/01-measuring-the-economy/07-cpi-and-inflation/) and [index numbers](https://faiyaz-svg.github.io/MathFromTheGroundUp/07-economics-math/01-measuring-the-economy/04-index-numbers/) in the math book. You need: a calculator.

## The idea

The inflation report is the data release with the biggest effect on rate expectations, because the Fed's job is to keep inflation near 2%. But "inflation" is not one number. Four reports each measure a price index, and they can differ in the same month.

| Measure | Publisher | What it prices | Time |
|---|---|---|---|
| CPI (Consumer Price Index) | BLS | What urban households pay for a basket of goods and services | 8:30 a.m. ET |
| Core CPI | BLS | The same, without food and energy | 8:30 a.m. ET |
| PCE price index, and core PCE | BEA | A wider measure of household spending | 8:30 a.m. ET |
| PPI (Producer Price Index) | BLS | What domestic producers receive for their output | 8:30 a.m. ET |

The times come from the [BLS release calendar](https://www.bls.gov/schedule/news_release/) (CPI and PPI) and the [BEA schedule](https://www.bea.gov/news/schedule) (the personal income and outlays report, which contains PCE), as of 2026. As an example of timing, the October 2026 CPI was scheduled for November 10, 2026, and the October 2026 personal income and outlays for November 25, 2026.

The **CPI** is the BLS's measure of the average change over time in the prices paid by consumers. The CPI-U version covers urban households, which is over 90% of the US population ([BLS CPI questions and answers](https://www.bls.gov/cpi/questions-and-answers.htm)). **Core** CPI leaves out food and energy, whose prices swing a lot, to show the underlying trend. The **PCE price index** comes from the BEA. The Fed says it prefers PCE largely because it covers a wide range of household spending ([Federal Reserve FAQ](https://www.federalreserve.gov/faqs/economy_14419.htm)), and its 2% goal is stated in PCE terms ([Federal Reserve FAQ](https://www.federalreserve.gov/faqs/economy_14400.htm)). The two indexes weight and calculate their items differently, so they can give different readings. The **PPI** measures the average change in selling prices received by domestic producers for their output ([BLS PPI](https://www.bls.gov/ppi/)). It is a price at the factory gate, so it often moves before consumer prices do, though not always.

So why do traders watch CPI more than PCE if the Fed targets PCE? CPI comes out first: in the 2026 example above, November 10 against November 25 for the same month. Analysts update their PCE forecasts as soon as CPI and PPI are out.

## How it works

Three readings come from each report. They all sit in the release's first lines.

1. Month-over-month (m/m): the change from the prior month, usually seasonally adjusted. This is the number the market trades on.
2. Year-over-year (y/y): the change from the same month a year earlier. It is what the news quotes, and it moves slowly.
3. Headline against core: the all-items number against the version without food and energy.

The all-items change is a weighted average of its parts. A made-up example shows the headline-versus-core gap.

<div class="example" markdown>

### Worked example: why core ran hotter than headline

Suppose, in a made-up basket, food and energy are 20% of spending and everything else (core) is 80%. In one month, core prices rise 0.4% and food and energy prices fall 0.2%.

1. Headline m/m = 0.80 x 0.4% + 0.20 x (-0.2%) = 0.32% - 0.04% = 0.28%, which rounds to 0.3%.
2. Core m/m = 0.4%.

The headline looks calm at 0.3%, while the core is 0.4%. A trader reading the Fed's mind looks at core, because food and energy often reverse. Real weights differ from these made-up ones, and the BLS publishes them.

From the index itself: suppose the made-up index is 320.00 last month, 320.96 this month and 310.00 a year ago.

3. m/m = 320.96 / 320.00 - 1 = 0.30%.
4. y/y = 320.96 / 310.00 - 1 = 3.5% (rounded to one decimal).

</div>

The figure shows year-over-year CPI, all items and core, from BLS data.

![Line chart of yearly CPI inflation, 2017 to 2025, all items and core: mostly between 1.5% and 3% before 2021, a dip in 2020, a peak in 2022, then a fall to about 2.7% by December 2025.](../assets/figures/11-macro-and-economic-data/cpi-headline-core-dark.svg#only-dark)
![Line chart of yearly CPI inflation, 2017 to 2025, all items and core: mostly between 1.5% and 3% before 2021, a dip in 2020, a peak in 2022, then a fall to about 2.7% by December 2025.](../assets/figures/11-macro-and-economic-data/cpi-headline-core-light.svg#only-light)

Source: BLS Public Data API, series CUUR0000SA0 (all items) and CUUR0000SA0L1E (all items less food and energy), not seasonally adjusted, downloaded November 21, 2026; yearly change computed by the book. The dashed line marks 2% for reference only: the Fed's goal is for PCE, not CPI. The break near the end is a month with no data: the BLS table carries the note "Data unavailable due to the 2025 lapse in appropriations" for October 2025.

In this data, headline CPI peaked at 9.1% in June 2022 and core at 6.6% in September 2022. Headline moved first and further because energy prices moved first and further. The gap between the lines in 2022 is the food and energy part of the example above, at a large scale.

### How to read a release

Check the headline m/m against the consensus, then core m/m against its consensus, then the pieces that moved the number (shelter, used cars, energy, services excluding housing). Markets care about core and services most because those are the sticky parts. Part 16 covers trading these days ([FOMC, CPI and other data days](../16-volatility-and-event-trading/05-fomc-cpi-and-data-days.md)).

## Common mistakes

- Treating y/y as news. A y/y figure is made of twelve months, eleven of which the market already knows. The surprise sits in the latest month.
- Mixing seasonally adjusted and unadjusted numbers. Monthly changes are quoted seasonally adjusted. The BLS computes y/y changes from unadjusted data, as the figure does, so compare like with like.
- Assuming CPI and PCE match. They differ in coverage and weights, and the gap changes from month to month.

## Try it

1\. Core CPI has a 75% weight, and food and energy 25%. Core rises 0.3% and food and energy rise 0.7%. What is the headline m/m?

<details class="solution" markdown>
<summary>Answer</summary>

0.75 x 0.3% + 0.25 x 0.7% = 0.225% + 0.175% = 0.40%.

</details>

2\. An index is 250.00 in March, 250.75 in April and 240.00 a year before April. Compute m/m and y/y for April.

<details class="solution" markdown>
<summary>Answer</summary>

m/m = 250.75 / 250.00 - 1 = 0.30%. y/y = 250.75 / 240.00 - 1 = 4.48%, so 4.5%.

</details>

3\. Which agency publishes PCE, and why do traders still watch CPI first?

<details class="solution" markdown>
<summary>Answer</summary>

The BEA publishes PCE. CPI is released about two weeks earlier, and analysts update their PCE forecasts after it.

</details>

4\. The consensus for core CPI is +0.3% m/m and the actual is +0.4%. Is this a surprise in the direction of tighter or easier Fed policy?

<details class="solution" markdown>
<summary>Answer</summary>

S = 0.4 - 0.3 = +0.1 percentage points, a hotter reading. It leans toward tighter policy (a later cut or a higher rate), which lesson 8 works through.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Open the latest [BLS CPI release](https://www.bls.gov/cpi/). Write the headline and core m/m and y/y. |
| 3 | Write the two items that moved the most, in your own words. |
| 2 | Look up the consensus for the next CPI in a free calendar and write it in your [trade journal](../practice/trade-journal.md). |

</div>

## Key terms

- **CPI**: the BLS's index of prices paid by urban consumers.
- **Core**: an inflation measure that leaves out food and energy.
- **PCE price index**: the BEA's measure of prices for household spending, and the Fed's target measure.
- **PPI**: the BLS's index of prices received by domestic producers.
- **Month-over-month (m/m)**: the change from the previous month.
- **Year-over-year (y/y)**: the change from the same month a year earlier.

Next: [The jobs report](05-the-jobs-report.md)
