# The jobs report

<span class="tag tag-data">Data</span> <span class="tag tag-part">MACRO</span>

After this lesson you can read the monthly jobs report line by line, say which survey each number comes from, and place weekly jobless claims and JOLTS next to it.

Before this: [Inflation reports: CPI, PCE and PPI](04-inflation-reports.md). The math book covers the rate itself: [unemployment and labour statistics](https://faiyaz-svg.github.io/MathFromTheGroundUp/07-economics-math/01-measuring-the-economy/08-unemployment-rate-and-labour-statistics/). You need: a calculator.

## The idea

The monthly jobs report is the release with the most attention after CPI. Its official name is the **Employment Situation**, and the BLS publishes it at 8:30 a.m. ET, usually on a Friday ([BLS release calendar](https://www.bls.gov/schedule/news_release/), as of 2026; the next two are November 6 and December 4, 2026).

The report has two parts from two different surveys, which is why its numbers can disagree.

### The establishment survey

The **establishment survey** (the Current Employment Statistics survey) asks employers. The BLS describes a sample of about 119,000 businesses and government agencies, covering about 622,000 worksites, or about 26 percent of nonfarm payroll jobs ([BLS technical note](https://www.bls.gov/news.release/empsit.tn.htm), as of 2026). It counts jobs on employers' payrolls, hours and pay.

Three headline numbers come from it. **Nonfarm payrolls** is the monthly change in the number of paid jobs outside farms, and it is the number everyone quotes ("the economy added 190,000 jobs"). **Average hourly earnings** is the average pay per hour, and its percentage change is the market's wage-inflation signal. Hours worked is how long the average worker was on the job.

### The household survey

The **household survey** (the Current Population Survey) asks people, not employers. The Census Bureau surveys about 60,000 eligible households for the BLS ([BLS technical note](https://www.bls.gov/news.release/empsit.tn.htm)). A person counts as unemployed when they have no job, are available for work and made specific active efforts to find one in the last four weeks (people on temporary layoff expecting recall also count). The **unemployment rate** is the share of the labour force that is unemployed. It comes from this survey, not from payrolls.

\[ u = \frac{U}{L} \times 100 \]

- \(u\) is the unemployment rate, in percent.
- \(U\) is the number of unemployed people, in millions.
- \(L\) is the labour force, the employed plus the unemployed, in millions.

## How it works

Read the report in this order.

1. The payrolls headline against its consensus. Mind the revisions: the report also revises the two previous months.
2. The unemployment rate against its consensus, in percentage points.
3. Average hourly earnings, monthly and yearly.
4. The revisions, added to the new month's number, to see the real change in the picture (lesson 1 worked one).

The **revisions** are part of the design. The BLS treats the two latest months as preliminary, because they rest on incomplete returns, and each gets two further revisions. Once a year, the sample-based estimates are adjusted to counts from unemployment insurance records, called the **benchmark revision** ([BLS technical note](https://www.bls.gov/news.release/empsit.tn.htm)). So a month's job count can change three times in the first months, and again at the benchmark.

<div class="example" markdown>

### Worked example: rate and earnings

Everything here is made up.

Last month: 160.0 million employed and 6.9 million unemployed. This month: 160.2 million employed and 7.2 million unemployed.

1. Last month's labour force: 160.0 + 6.9 = 166.9 million. Rate = 6.9 / 166.9 = 4.13%, so 4.1%.
2. This month's labour force: 160.2 + 7.2 = 167.4 million. Rate = 7.2 / 167.4 = 4.30%, so 4.3%.
3. The rate rose 0.2 percentage points (4.3 - 4.1, rounded values), even though employment also rose. More people joined the labour force and looked for work than found it.

Average hourly earnings were US$36.00 last month and US$36.18 this month.

4. Change = 36.18 / 36.00 - 1 = 0.5%.

A traders' reading: jobs up, unemployment up, wages up 0.5% in a month. That mixes strong and weak signals, and the market focuses on whichever one moves rate expectations. Lesson 8 shows how.

</div>

### Two other labour releases

**Weekly jobless claims.** The Labor Department publishes the number of people filing new claims for unemployment insurance every Thursday at 8:30 a.m. ET ([Department of Labor claims release](https://oui.doleta.gov/unemploy/claims_arch.asp), as of 2026; a Thursday holiday moves the release). It is the first look at the job market in a given month, and it moves less on any one week than on a trend over four weeks.

**JOLTS.** The Job Openings and Labor Turnover Survey, from the BLS, estimates job openings, hires and separations each month ([BLS JOLTS](https://www.bls.gov/jlt/)). It comes out at 10:00 a.m. ET ([BLS release calendar](https://www.bls.gov/schedule/news_release/), as of 2026) and shows how many jobs employers want to fill, which payrolls do not.

The three labour numbers differ in speed and detail. Claims are weekly and fast. Payrolls are monthly and broad. JOLTS is monthly, with a delay, and shows demand for workers.

## Common mistakes

- Reading the payrolls number alone. The unemployment rate and wages can point the other way, and revisions can change the headline.
- Expecting the two surveys to agree. Different samples and definitions give different monthly changes.
- Reacting to one week of claims. Weekly claims are noisy, so compare against a four-week average.

## Try it

1\. There are 150.0 million employed and 6.0 million unemployed. What is the unemployment rate?

<details class="solution" markdown>
<summary>Answer</summary>

L = 156.0 million. u = 6.0 / 156.0 = 3.85%, so 3.8% (rounded to one decimal).

</details>

2\. Hourly earnings were US$34.50 and are US$34.76. What is the monthly percentage change?

<details class="solution" markdown>
<summary>Answer</summary>

34.76 / 34.50 - 1 = 0.75%, so 0.8% when rounded to one decimal.

</details>

3\. Which survey does the unemployment rate come from, and which does payrolls come from?

<details class="solution" markdown>
<summary>Answer</summary>

The unemployment rate comes from the household survey. Payrolls come from the establishment survey.

</details>

4\. At what time does each release come out: the jobs report, weekly claims and JOLTS?

<details class="solution" markdown>
<summary>Answer</summary>

The jobs report and weekly claims at 8:30 a.m. ET, and JOLTS at 10:00 a.m. ET.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Open the latest [Employment Situation](https://www.bls.gov/news.release/empsit.nr0.htm) summary. Write payrolls, the unemployment rate, hourly earnings and the revisions to the two prior months. |
| 3 | Open the latest claims release and write the initial claims and the four-week average. |
| 2 | Write in your [trade journal](../practice/trade-journal.md) which of the three signals pointed up and which pointed down. |

</div>

## Key terms

- **Employment Situation**: the BLS's monthly jobs report.
- **Establishment survey**: the survey of employers that gives payrolls, hours and earnings.
- **Nonfarm payrolls**: the monthly change in paid jobs outside farms.
- **Average hourly earnings**: the average pay per hour, from the establishment survey.
- **Household survey**: the survey of households that gives the unemployment rate.
- **Unemployment rate**: unemployed people as a share of the labour force.
- **Benchmark revision**: the yearly adjustment of payroll estimates to unemployment insurance records.
- **Jobless claims**: the weekly count of new unemployment insurance claims.
- **JOLTS**: the BLS survey of job openings, hires and separations.

Next: [Growth data: GDP, retail sales and PMIs](06-growth-data.md)
