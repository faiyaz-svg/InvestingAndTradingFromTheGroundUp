# Growth data: GDP, retail sales and PMIs

<span class="tag tag-data">Data</span> <span class="tag tag-part">MACRO</span>

After this lesson you can read a GDP release and its revisions, say what retail sales and the PMIs measure, and explain the 50 line.

Before this: [The jobs report](05-the-jobs-report.md). The math book covers the base: [GDP and the circular flow](https://faiyaz-svg.github.io/MathFromTheGroundUp/07-economics-math/01-measuring-the-economy/05-gdp-and-the-circular-flow/) and [nominal vs real GDP](https://faiyaz-svg.github.io/MathFromTheGroundUp/07-economics-math/01-measuring-the-economy/06-nominal-vs-real-gdp-and-the-deflator/). You need: a calculator.

## The idea

Growth data answers one question: is the economy producing more or less than before? GDP gives the answer late and in full. Retail sales and the purchasing managers' indexes (PMIs) give it early and in part. A trader reads all three and expects the early ones to be noisy.

### GDP

The BEA publishes gross domestic product at 8:30 a.m. ET ([BEA release schedule](https://www.bea.gov/news/schedule), as of 2026). It publishes three estimates for each quarter. The **advance estimate** comes about a month after the quarter ends, the **second estimate** about two months after, and the **third estimate** about three months after. Each uses more complete source data than the one before ([BEA, GDP release additional information](https://www.bea.gov/news/gdp-release-additional-information)).

How big are the revisions? The BEA's long-run averages, based on 1996 through 2025, put the average revision without regard to sign at 0.5 percentage points (annual rate) from advance to second, 0.6 from advance to third, and 0.3 from second to third (same page, as of 2026). A first print of 2.0% growth is therefore, on average, off by about 0.6 percentage points in either direction. The BEA also updates GDP once a year, and later annual revisions can change earlier quarters more.

GDP growth is quoted at an **annual rate**: the quarter's growth, restated as the pace if it continued for four quarters, as in lesson 1.

\[ g_{\text{annual}} = (1 + g_{\text{quarter}})^4 - 1 \]

- \(g_{\text{quarter}}\) is real GDP growth over one quarter, as a fraction (0.5% is 0.005).
- \(g_{\text{annual}}\) is the annual rate, the number quoted in the headline.

Real GDP is adjusted for price changes, nominal GDP is not. The headline is real.

### Retail sales

The Census Bureau publishes advance monthly sales for retail and food services at 8:30 a.m. ET ([Census economic indicator calendar](https://www.census.gov/economic-indicators/calendar-listview.html), as of 2026). It counts spending at stores, restaurants and online sellers, in dollars of the month, so rising prices alone can raise it. Retail sales is revised in later months, like the other releases.

### PMIs

A **purchasing managers' index** (PMI) is a monthly survey of purchasing executives. ISM publishes the Manufacturing PMI on the first business day of the month at 10:00 a.m. ET, and the Services PMI on the third business day at 10:00 a.m. ET. Dates can shift around holidays such as New Year's Day, so check the ISM calendar ([ISM, as of 2026](https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/)). S&P Global publishes its own PMIs for US manufacturing and services.

Each survey question asks whether something (new orders, say) is higher, the same or lower than last month. The answers become a **diffusion index**:

\[ D = P_{\text{higher}} + 0.5 \times P_{\text{same}} \]

- \(P_{\text{higher}}\) is the percentage of respondents who report an increase.
- \(P_{\text{same}}\) is the percentage who report no change.
- \(D\) is the index, from 0 to 100.

If everyone says "no change", \(D\) is 50. That is the **50 line**: above 50, more respondents report growth than decline in that activity, and below 50, more report decline. It is a reading about direction from the prior month, not a level of output. A reading of 51 and one of 49 are close together, even though they fall on opposite sides of the line.

<div class="example" markdown>

### Worked example: a diffusion index and an annual rate

Everything is made up. A survey asks 100 managers about new orders: 40 say higher, 30 say the same, 30 say lower.

1. D = 40 + 0.5 x 30 = 55. Above the 50 line, so more managers report growth than decline.

A quarter's real GDP grows 0.5%.

2. Annual rate = 1.005^4 - 1 = 2.02%, so 2.0%.

The advance estimate is 2.0%, and the average advance-to-third revision is 0.6 points. A third estimate near 1.4% or 2.6% would be an ordinary revision. A third estimate of 3.5% would not.

</div>

### Sentiment surveys

The Conference Board and the University of Michigan each survey households about confidence and sentiment. Their indexes are on different scales and use different questions, so compare each with its own history. They are the soft data of the calendar: opinions, not counts.

## Hard data and soft data

Traders call GDP and retail sales **hard data**: they count transactions. PMIs and sentiment surveys are **soft data**: they record opinions. Soft data comes sooner and often moves first. Hard data is more reliable but late. When the two disagree, the gap is a topic of its own, and neither is always right.

## Common mistakes

- Reading the PMI as a growth rate. A 52 is not 2% growth. It says more managers report increases than decreases.
- Treating the first GDP print as the final one. The revisions are large relative to many surprises.
- Ignoring prices in retail sales. A 0.5% rise with 0.4% price rises is a small rise in volume.

## Try it

1\. 35 managers say higher, 45 say the same and 20 say lower. What is the diffusion index?

<details class="solution" markdown>
<summary>Answer</summary>

D = 35 + 0.5 x 45 = 57.5. Above the 50 line.

</details>

2\. Real GDP grows 0.6% in a quarter. What is the annual rate?

<details class="solution" markdown>
<summary>Answer</summary>

1.006^4 - 1 = 0.0243, which is 2.4%.

</details>

3\. The ISM Manufacturing PMI for March is due on the first business day of April. April 1 falls on a Wednesday. On what day, and at what time ET?

<details class="solution" markdown>
<summary>Answer</summary>

Wednesday, April 1, at 10:00 a.m. ET (it is the first business day, as long as the NYSE is open).

</details>

4\. A first GDP print is 1.8%. The average advance-to-third revision is 0.6 percentage points. What range is a typical outcome?

<details class="solution" markdown>
<summary>Answer</summary>

About 1.2% to 2.4% (1.8 minus 0.6 and plus 0.6). It is an average, not a limit.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Open the BEA's latest GDP release. Write the growth rate and which estimate it is (advance, second or third). |
| 3 | Open the latest ISM Manufacturing PMI report page and write the headline number and whether it is above 50. |
| 2 | Write in your [trade journal](../practice/trade-journal.md) one sentence on whether hard and soft data agree right now. |

</div>

## Key terms

- **Advance estimate**: the first GDP estimate, about a month after the quarter ends.
- **Second estimate**: the GDP estimate about two months after the quarter ends.
- **Third estimate**: the GDP estimate about three months after the quarter ends.
- **Annual rate**: a quarter's growth restated as the pace over four quarters.
- **Retail sales**: the Census Bureau's monthly count of spending at stores, restaurants and online sellers.
- **Purchasing managers' index (PMI)**: a monthly survey index of purchasing executives.
- **Diffusion index**: an index built from the share of respondents who report an increase, a decrease or no change.
- **50 line**: the PMI level at which as many respondents report growth as decline.
- **Hard data**: releases that count transactions, such as GDP.
- **Soft data**: survey releases that record opinions, such as PMIs.

Next: [The economic calendar](07-the-economic-calendar.md)
