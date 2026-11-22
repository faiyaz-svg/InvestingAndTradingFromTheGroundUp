# How markets react to data

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">MACRO</span>

After this lesson you can trace a data surprise through rate expectations to yields, the dollar and stocks, and say when good news for the economy is bad news for stocks.

Before this: [Interest rates and asset prices](03-interest-rates-and-asset-prices.md), [Inflation reports: CPI, PCE and PPI](04-inflation-reports.md) and [The economic calendar](07-the-economic-calendar.md). You need: a calculator.

## The idea

At 8:30 a.m. ET core CPI comes in hotter than expected. In the next minute, Treasury yields rise, the US dollar strengthens and stock index futures fall. Nothing about any company changed. What changed is the market's guess about what the Fed will do next.

The chain has four links, and each one is a step.

1. The data surprises (lesson 1).
2. The market revises the expected path of the federal funds rate, which shows in fed funds futures and in short-term Treasury yields (lesson 2).
3. Higher expected rates raise discount rates, and that lowers the present value of stocks, most of all for companies whose cash is far away (lesson 3). Higher US rates also tend to lift the dollar, because dollar assets pay more.
4. Prices adjust in rates first, because rates are closest to the Fed, and in stocks and currencies a moment later.

### Why good news can be bad news

A strong jobs report means the economy is healthy, which is good for profits. It also means the Fed may keep rates higher for longer, which is bad for the discount rate. Which effect wins depends on what the market is worried about.

- When inflation is the worry and the Fed is raising rates or holding them high, strong data raises expected rates, and stocks fall. Traders call this "good news is bad news".
- When growth is the worry, as in a slowdown, weak data raises the odds of a recession, and stocks fall on bad news.

The effect is documented. Boyd, Hu and Jagannathan ("The Stock Market's Reaction to Unemployment News: Why Bad News Is Usually Good for Stocks", *Journal of Finance*, 2005) found that news of rising unemployment was good for stocks on average during expansions and bad for them during contractions. They attribute this to interest-rate news dominating in expansions and news about future dividends dominating in contractions. It is a study of one data series over one period, and the sign of the reaction changes with the regime, so you check the regime each time and don't treat it as a rule.

## How it works

The size of a reaction scales with the surprise, not the number. An in-line print leaves prices near where they were, because the market had already priced it.

<div class="example" markdown>

### Worked example: a hot CPI print

Everything here is made up. The consensus for core CPI is +0.3% m/m, and the actual is +0.5%.

1. Surprise: S = 0.5 - 0.3 = +0.2 percentage points. At the yearly pace, 1.005^12 - 1 = 6.2%, against 1.003^12 - 1 = 3.7% for the consensus.
2. Rate expectations. Before the release, the fed funds futures price for the month after the next meeting is 96.55. After it, 96.45. Using the lesson 2 formula with a range of 3.50% to 3.75% and a 25 bp cut: before, odds of a cut are (3.625 - 3.45) / 0.25 = 70%. After, they are (3.625 - 3.55) / 0.25 = 30%.
3. Short-term yields. The 2-year Treasury yield goes from 3.80% to 3.92%, which is +12 bp.
4. The dollar. USD/CAD goes from 1.3800 to 1.3869, which is +0.5%. The US dollar buys more Canadian dollars.
5. Stocks. A made-up index goes from 5,000 to 4,940, which is -1.2%.

The odds fall by 40 percentage points, yields rise, the dollar rises and stocks fall. All four moves point the same way, because all four come from one change: a later or smaller cut.

</div>

The bars show the odds before and after.

![Bar chart of made-up market-implied odds of a 25 bp cut: 70% before the CPI release and 30% after.](../assets/figures/11-macro-and-economic-data/odds-before-after-dark.svg#only-dark)
![Bar chart of made-up market-implied odds of a 25 bp cut: 70% before the CPI release and 30% after.](../assets/figures/11-macro-and-economic-data/odds-before-after-light.svg#only-light)

### What the first minutes look like

Liquidity is thin around a release, spreads widen (Part 1, [Bid, ask and the order book](../01-how-markets-work/04-bid-ask-and-the-order-book.md)), and fills in a fast market can be far from the last price. The first move can reverse as traders read the details. Many traders wait until the details settle before acting, and some do not trade the release at all. That is a choice for your plan. Part 16 covers how options and volatility behave on these days (FOMC, CPI and other data days<!-- link: ../16-volatility-and-event-trading/05-fomc-cpi-and-data-days.md -->).

### Sorting a surprise

A short table helps sort the direction, as long as you check the regime first.

| Data | Hotter or stronger | Weaker |
|---|---|---|
| Inflation (CPI, PCE, PPI) | Rates up, dollar up, stocks down | Rates down, dollar down, stocks up |
| Jobs, wages | Rates up (if inflation is the worry) | Rates down (until recession fear takes over) |
| Growth (GDP, PMIs, retail sales) | Rates up, stocks mixed | Rates down, stocks mixed |

The "stocks mixed" cells are the honest ones: growth data moves profit forecasts and rates in opposite directions.

## Common mistakes

- Expecting one fixed reaction. The sign of the stock reaction to strong data depends on the regime.
- Trading the headline before the details. A jobs headline can reverse once earnings and revisions are read.
- Forgetting the move may already be priced. Prices move on the surprise relative to consensus, so a report that matches the consensus moves little.

## Try it

1\. Fed funds futures move from 96.60 to 96.50 after a data release. The range is 3.50% to 3.75% and a cut is 25 bp. What were the odds before and after?

<details class="solution" markdown>
<summary>Answer</summary>

Before: (3.625 - 3.40) / 0.25 = 90%. After: (3.625 - 3.50) / 0.25 = 50%.

</details>

2\. USD/CAD rises from 1.3500 to 1.3568 after a data release. What is the percentage change, and what does it say about the dollar?

<details class="solution" markdown>
<summary>Answer</summary>

1.3568 / 1.3500 - 1 = 0.50%. The US dollar strengthened against the Canadian dollar.

</details>

3\. A payrolls number beats the consensus by 60,000 jobs, the Fed is worried about inflation and stocks fall. Name the effect.

<details class="solution" markdown>
<summary>Answer</summary>

Good news is bad news: strong data raised the expected rate path, which raised discount rates.

</details>

4\. The consensus for core CPI is +0.3% and the actual is +0.3%. What do you expect prices to do, and why?

<details class="solution" markdown>
<summary>Answer</summary>

Little. The surprise is 0, so the market's rate expectations barely change.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Pick the last CPI or jobs release. Write the consensus, the actual and the surprise, then the move in the 2-year yield and an index that day, from a free chart site. |
| 3 | Write whether the move agrees with the table above. |
| 2 | If it did not, write one reason in your [trade journal](../practice/trade-journal.md). |

</div>

## Key terms

- **Reaction function**: how asset prices respond to a surprise, which depends on what the market is worried about.
- **Good news is bad news**: strong data that lowers stocks because it raises expected interest rates.
- **Rate path**: the market's expected series of policy rate changes over coming meetings.

Next: [The business cycle and sectors](09-the-business-cycle-and-sectors.md)
