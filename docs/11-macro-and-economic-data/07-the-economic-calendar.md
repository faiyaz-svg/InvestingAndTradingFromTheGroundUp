# The economic calendar

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">MACRO</span>

After this lesson you can build a weekly calendar of releases with times in ET, rank them by importance, and decide in advance how to treat your open positions around each one.

Before this: [Growth data: GDP, retail sales and PMIs](06-growth-data.md) and [Market hours and the opening and closing auctions](../01-how-markets-work/03-market-hours-and-auctions.md). You need: a calendar app or a spreadsheet.

## The idea

Scheduled data arrives at a known second. The price can jump in that second, with no warning and, for a market order, with no good fill (see [Order types](../01-how-markets-work/05-order-types.md)). That makes the calendar a risk tool: you can't predict the number, but you can know the minute it lands and have a rule ready.

A free **economic calendar** lists upcoming releases with the date, time, the consensus, the prior number and an importance rating. Several websites publish one. The agencies' own schedules are the source of truth, and the calendar sites copy them.

## How it works

### The release times

All of these are Eastern Time, which is Toronto's time zone, and the schedules follow daylight saving. Each time comes from the publisher's own page, as of 2026.

| Release | Publisher | Time (ET) | Source |
|---|---|---|---|
| CPI, PPI, Employment Situation | BLS | 8:30 a.m. | [BLS calendar](https://www.bls.gov/schedule/news_release/) |
| JOLTS | BLS | 10:00 a.m. | [BLS calendar](https://www.bls.gov/schedule/news_release/) |
| GDP, personal income and outlays (PCE) | BEA | 8:30 a.m. | [BEA schedule](https://www.bea.gov/news/schedule) |
| Advance retail sales | Census Bureau | 8:30 a.m. | [Census calendar](https://www.census.gov/economic-indicators/calendar-listview.html) |
| Weekly jobless claims (Thursdays) | Labor Department | 8:30 a.m. | [DOL](https://oui.doleta.gov/unemploy/claims_arch.asp) |
| ISM Manufacturing PMI (first business day) | ISM | 10:00 a.m. | [ISM](https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/) |
| ISM Services PMI (third business day) | ISM | 10:00 a.m. | [ISM](https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/) |
| FOMC statement | Federal Reserve | 2:00 p.m. | [Fed statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm) |
| Fed balance sheet (H.4.1, Thursdays) | Federal Reserve | 4:30 p.m. | [Fed H.4.1](https://www.federalreserve.gov/releases/h41/) |
| Bank of Canada rate decision | Bank of Canada | 9:45 a.m. | [BoC events](https://www.bankofcanada.ca/press/upcoming-events/) |

The figure puts the same times on one clock. Look at how many sit at 8:30, an hour before the US stock market opens at 9:30.

![A timeline from 8 a.m. to 4 p.m. ET with the 8:30 data releases, the 9:30 open, the 9:45 Bank of Canada decision, 10:00 PMIs and JOLTS, the 2:00 FOMC statement and the 4:00 close.](../assets/figures/11-macro-and-economic-data/release-clock-dark.svg#only-dark)
![A timeline from 8 a.m. to 4 p.m. ET with the 8:30 data releases, the 9:30 open, the 9:45 Bank of Canada decision, 10:00 PMIs and JOLTS, the 2:00 FOMC statement and the 4:00 close.](../assets/figures/11-macro-and-economic-data/release-clock-light.svg#only-light)

An 8:30 release lands in the pre-market, 60 minutes before the opening auction. Stocks can trade then, but the book is thin (Part 1, [Market hours and the opening and closing auctions](../01-how-markets-work/03-market-hours-and-auctions.md)), so the first reaction often shows in futures and Treasury yields first. A 10:00 release lands 30 minutes after the open. The FOMC statement lands two hours before the close.

### Building the weekly calendar

1. Pull the dates from the agencies' schedules: BLS, BEA, Census, ISM and the Fed's FOMC calendar. A week with two or more 8:30 releases is a heavy week.
2. Add the time, the prior value and the consensus for each.
3. Rank each release as high, medium or low. A simple ranking: high for CPI, the jobs report and FOMC days, medium for GDP, PCE, retail sales and the ISM PMIs, low for the rest.
4. For each high item, write your rule before the day. Options: stay out of new trades until 15 minutes after the release, cut position size, or hold as normal. Part 3's [risk rules](../03-risk-and-position-sizing/10-your-trading-plan.md) set the limits, and the rule must fit them.
5. Add holidays. When the NYSE is closed, ISM's schedule can shift, and holiday weeks move releases to other days (a Thursday holiday moves the jobless claims release).

<div class="example" markdown>

### Worked example: the first week of December 2026

Using the scheduled dates on the agency pages (as of November 2026):

| Day | Time (ET) | Release |
|---|---|---|
| Tuesday, December 1 | 10:00 a.m. | ISM Manufacturing PMI (November data) |
| Thursday, December 3 | 8:30 a.m. | Weekly jobless claims |
| Thursday, December 3 | 10:00 a.m. | ISM Services PMI |
| Friday, December 4 | 8:30 a.m. | Employment Situation (November data) |

The next week brings the FOMC meeting on December 8 to 9, with the statement at 2:00 p.m. ET on Wednesday, December 9, and the Bank of Canada decision at 9:45 a.m. ET the same day.

Counting: the jobs report at 8:30 comes 60 minutes before the 9:30 open. The FOMC statement at 2:00 p.m. comes 120 minutes before the 4:00 p.m. close. The high-ranked items are the jobs report and the FOMC day.

</div>

Dates can slip. The BLS data tables carry a footnote for October 2025 CPI that reads "Data unavailable due to the 2025 lapse in appropriations", so a government shutdown can delay or cancel a release. Recheck the agency page the day before.

## Common mistakes

- Trusting a calendar site over the agency. Sites copy times and can be late to update. Check the agency.
- Forgetting the time zone. Calendar sites often default to UTC or the site's own zone. Set it to Eastern.
- Having no rule until the minute of release. Decide the night before, when you are not watching the price.

## Try it

1\. A release is at 8:30 a.m. ET. At what time is that in Toronto?

<details class="solution" markdown>
<summary>Answer</summary>

8:30 a.m. Toronto is in the Eastern time zone, so there is no difference.

</details>

2\. How many minutes separate the 8:30 a.m. releases from the 9:30 a.m. open, and the 2:00 p.m. FOMC statement from the 4:00 p.m. close?

<details class="solution" markdown>
<summary>Answer</summary>

60 minutes and 120 minutes.

</details>

3\. Rank these as high, medium or low using the ranking above: CPI, ISM Manufacturing PMI, JOLTS.

<details class="solution" markdown>
<summary>Answer</summary>

CPI is high. ISM Manufacturing PMI is medium. JOLTS is low.

</details>

4\. Name the two releases on Thursday mornings at 8:30 and 10:00 in the first week of December 2026.

<details class="solution" markdown>
<summary>Answer</summary>

Weekly jobless claims at 8:30 a.m. and the ISM Services PMI at 10:00 a.m., both on Thursday, December 3.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 6 | Build next week's calendar: copy dates and times from the BLS, BEA and Fed pages into a table with the prior value and the consensus. |
| 2 | Rank each line high, medium or low. |
| 2 | For each high line, write one rule in your [trade journal](../practice/trade-journal.md), then check it against your trading plan. |

</div>

## Key terms

- **Economic calendar**: a list of upcoming releases with times, prior values and consensus.
- **Pre-market**: trading before the 9:30 a.m. ET open, when the book is thin.
- **Heavy week**: a week with several high-importance releases.

Next: [How markets react to data](08-how-markets-react-to-data.md)
