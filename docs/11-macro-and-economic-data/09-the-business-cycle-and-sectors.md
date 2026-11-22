# The business cycle and sectors

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">MACRO</span>

After this lesson you can name the phases of the business cycle, say how long they have lasted on average, and explain why sector rotation rules are loose guides and not trading signals.

Before this: [Growth data: GDP, retail sales and PMIs](06-growth-data.md) and [Indexes, sectors and market cap](../01-how-markets-work/10-indexes-sectors-and-market-cap.md). You need: a calculator.

## The idea

Economic activity does not grow in a straight line. It rises for a few years, falls for a few months, then rises again. The pattern is the **business cycle**. Traders care because profits, interest rates and some sectors tend to move with it, and a story about "where we are in the cycle" is common in market commentary.

The textbook cycle has four phases, drawn here as a smooth wave. Real cycles are uneven in height and length.

![A stylised business cycle: early expansion, late expansion, a peak, contraction, a trough and recovery. An illustration, not data.](../assets/figures/11-macro-and-economic-data/business-cycle-dark.svg#only-dark)
![A stylised business cycle: early expansion, late expansion, a peak, contraction, a trough and recovery. An illustration, not data.](../assets/figures/11-macro-and-economic-data/business-cycle-light.svg#only-light)

An **expansion** is a period when output, jobs and spending rise. Early in an expansion, rates are usually low and growth is picking up. Late in an expansion, the economy strains, inflation tends to rise and the Fed tends to raise rates.

The **peak** is the high point, after which activity falls.

A **contraction** is a period when output and jobs fall. A **recession** is a large decline in economic activity that is spread across the economy and lasts more than a few months. In the US, the National Bureau of Economic Research (NBER) dates recessions, from the month after a peak to the month of the trough ([NBER](https://www.nber.org/research/data/us-business-cycle-expansions-and-contractions), as of 2026). A common rule of thumb is two quarters of falling real GDP, but that is a shortcut and not the NBER's definition. The NBER announces turning points after they have happened.

The **trough** is the low point, after which activity recovers.

### How long the phases last

The NBER page gives the averages. From 1945 to 2020, contractions averaged 10.3 months and expansions 64.2 months. For 1854 to 2020, contractions averaged 17.0 months and expansions 41.4 months.

<div class="example" markdown>

### Worked example: time in expansion

Using the 1945 to 2020 averages:

1. One full cycle, expansion plus contraction: 64.2 + 10.3 = 74.5 months, or 74.5 / 12 = 6.2 years.
2. Share of a cycle in expansion: 64.2 / 74.5 = 86.2%.
3. Share in contraction: 10.3 / 74.5 = 13.8%.

For 1854 to 2020: 41.4 + 17.0 = 58.4 months, and the expansion share is 41.4 / 58.4 = 70.9%.

The averages are not a schedule. Individual expansions and contractions varied widely around them. An expansion does not "run out" after 64 months.

</div>

## How it works

### Sectors and the cycle

Part 1 introduced the 11 GICS sectors. Commentary often sorts them into two groups.

- Cyclical sectors, such as consumer discretionary, industrials and financials, have profits that move with the economy.
- Defensive sectors, such as utilities, consumer staples and health care, sell things people buy in any economy, so profits move less.

The textbook story is that cyclicals lead in early expansions, and defensives hold up better in contractions. The table is that story, in its usual form.

| Phase | Typical backdrop | Sectors commonly cited as strong |
|---|---|---|
| Early expansion | Low rates, recovering demand | Consumer discretionary, financials, industrials |
| Late expansion | Rising inflation and rates | Energy, materials |
| Contraction | Falling output, falling rates | Utilities, consumer staples, health care |

Read the table as a hypothesis, not a rule. Four problems make rotation rules loose.

1. You do not know the phase when you need to. The NBER dates peaks and troughs after the fact, so a trader acting on "we are in a recession" acts late, and markets move before the data does.
2. Every cycle has a different cause. A cycle driven by oil prices, one driven by a financial crisis and one driven by a rate rise do not hit the same sectors the same way.
3. Sector contents change. The sectors are not fixed baskets, and a few very large companies can drive a sector's return (Part 1, [Indexes, sectors and market cap](../01-how-markets-work/10-indexes-sectors-and-market-cap.md)).
4. Prices look ahead. By the time a recession is clear, stocks may have fallen and be recovering.

### What tests found

One published test found something for rotation tied to the Fed's policy stance. Conover, Jensen, Johnson and Mercer ("Sector Rotation and Monetary Conditions", *The Journal of Investing*, 2008, sample from 1973 to 2005) tested a rule that favours cyclical sectors when the Fed is easing and defensive sectors when it is tightening, and reported that it beat a buy-and-hold market portfolio over their sample. We could not check the paper's cost assumptions here. It is one study of one rule on US data. Evidence that rotation by cycle phase works in real time and after costs is thin, and this lesson cites none. The cycle explains some patterns, and it doesn't give you a rule you can trade by.

A better use of the cycle is as context for your own rules. [Market regime filters](../07-swing-trading/03-market-regime-filters.md) in Part 7 give testable rules for when to take trades, and they use prices, not a story about the cycle.

## Common mistakes

- Treating the textbook table as a signal. It is a loose pattern from some past cycles, and it changes with each one.
- Calling a recession from one data release. The NBER uses a wide set of data, and its calls come late.
- Expecting the averages to apply to the next cycle. Expansions have run longer and shorter than the average.

## Try it

1\. Using the 1945 to 2020 averages, what percentage of a typical cycle is a contraction?

<details class="solution" markdown>
<summary>Answer</summary>

10.3 / (64.2 + 10.3) = 10.3 / 74.5 = 13.8%.

</details>

2\. Sort into cyclical or defensive: utilities, industrials, consumer staples, consumer discretionary.

<details class="solution" markdown>
<summary>Answer</summary>

Utilities: defensive. Industrials: cyclical. Consumer staples: defensive. Consumer discretionary: cyclical.

</details>

3\. A friend says "two quarters of negative GDP is the official definition of a recession in the US." Is it?

<details class="solution" markdown>
<summary>Answer</summary>

No. It is a rule of thumb. In the US, the NBER dates recessions, and it dates them as a contraction in economic activity from a peak to a trough.

</details>

4\. Give two reasons a rule like "rotate into utilities in a recession" is hard to use.

<details class="solution" markdown>
<summary>Answer</summary>

Any two of: the recession is dated after the fact, each cycle has a different cause, sector contents change, prices move before the data does.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Open the NBER page and write down the last three recessions with their peak and trough months. |
| 3 | Open a free sector ETF performance table and write which sector led and which lagged over the last 3 months. |
| 2 | Write in your [trade journal](../practice/trade-journal.md) whether the leaders fit the textbook table, and one reason it might not. |

</div>

## Key terms

- **Business cycle**: the repeated pattern of expansion and contraction in economic activity.
- **Expansion**: a period when output, jobs and spending rise.
- **Peak**: the high point of activity before a contraction.
- **Contraction**: a period when activity falls.
- **Recession**: a contraction in economic activity, dated in the US by the NBER.
- **Trough**: the low point of activity before a recovery.
- **Cyclical sector**: a sector whose profits move closely with the economy.
- **Defensive sector**: a sector whose profits move less with the economy.
- **Sector rotation**: shifting money between sectors according to the cycle.

Next: [QE, QT and liquidity](10-qe-qt-and-liquidity.md)
