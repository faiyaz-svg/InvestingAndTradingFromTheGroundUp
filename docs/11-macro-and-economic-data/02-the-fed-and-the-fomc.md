# The Fed and the FOMC

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">MACRO</span>

After this lesson you can say what the Federal Reserve is trying to do, list what comes out of an FOMC meeting and when, and turn a fed funds futures price into market-implied odds of a rate move.

Before this: [How the economy is measured](01-how-the-economy-is-measured.md). You need: a calculator.

## The idea

At 2:00 p.m. ET on a meeting day, the Federal Reserve posts a short statement. Within seconds, Treasury yields, the dollar and stock futures react to a few changed words. It says what the Fed's policy committee decided about one interest rate, and how it sees the economy.

The **Federal Reserve** (the Fed) is the central bank of the US. Its policy committee is the **Federal Open Market Committee** (FOMC). It has twelve voting members: the seven governors of the Federal Reserve Board, the president of the New York Fed, and four other Reserve Bank presidents who rotate in ([FOMC page](https://www.federalreserve.gov/monetarypolicy/fomc.htm), as of 2026).

### The goals

Congress gave the Fed two goals: maximum employment and stable prices, called the **dual mandate** ([Federal Reserve, statement on longer-run goals](https://www.federalreserve.gov/monetarypolicy/review-of-monetary-policy-strategy-tools-and-communications-statement-on-longer-run-goals-monetary-policy-strategy.htm)). The Fed defines stable prices as inflation of 2 percent over the longer run, measured by the annual change in the personal consumption expenditures (PCE) price index ([Federal Reserve FAQ](https://www.federalreserve.gov/faqs/economy_14400.htm)). Lesson 4 covers PCE.

### The tool: one overnight rate

The FOMC mainly steers the **federal funds rate**, the rate at which banks lend each other reserve balances overnight ([Federal Reserve, open market operations](https://www.federalreserve.gov/monetarypolicy/openmarket.htm)). Reserve balances are the deposits banks hold at the Fed. The FOMC does not set one number. It sets a **target range**, such as 3.50% to 3.75%, and the actual rate trades inside it. The Fed also pays banks an administered rate, the **interest on reserve balances** (IORB), which helps keep the federal funds rate in the range ([Federal Reserve, interest on reserve balances](https://www.federalreserve.gov/monetarypolicy/reserve-balances.htm)). A bank has little reason to lend reserves for less than it can earn by leaving them at the Fed.

Rate changes are small and quoted in **basis points** (bp). One basis point is 0.01 percentage points, so a 25 bp cut moves a range from 3.50% to 3.75% down to 3.25% to 3.50%.

## How it works

The FOMC meets eight times a year. The 2026 dates, from the [Fed's calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) (as of 2026), are January 27 to 28, March 17 to 18, April 28 to 29, June 16 to 17, July 28 to 29, September 15 to 16, October 27 to 28 and December 8 to 9. Each meeting produces these items.

| Item | What it is | When |
|---|---|---|
| Statement | A short text with the rate decision and the Fed's view of the economy | Last day of the meeting, 2:00 p.m. ET (the [October 28, 2026 statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm) says "2:00 p.m. EDT") |
| Press conference | The Chair answers questions | After the statement, on the same day |
| Summary of Economic Projections (SEP) | Each participant's forecasts for growth, unemployment, inflation and the policy rate | March, June, September and December meetings only |
| Dot plot | The SEP chart of each participant's projected policy rate, one dot per person | Same four meetings |
| Minutes | A detailed account of the discussion | Three weeks after the meeting |

The statement is read for changes: a dropped phrase or an added sentence moves markets. The dots are projections, not promises. The minutes matter when the discussion was more divided than the statement suggested.

### Market-implied odds

Before each meeting, traders ask what the market expects. One answer comes from **fed funds futures**, contracts whose price settles at 100 minus the average federal funds rate over a month. A price of 96.50 means the market expects an average rate of 3.50% over that month. CME Group publishes a tool called [FedWatch](https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html) built on this idea. Part 14 covers futures contracts in general.

If the contract month starts after a meeting, the price gives the odds directly. Suppose the rate is now in the middle of its range, \(R_0\), and a cut would be \(\Delta\):

\[ p = \frac{R_0 - (100 - F)}{\Delta} \]

- \(p\) is the market-implied probability of the cut, a fraction.
- \(R_0\) is the current rate if nothing changes, in percent.
- \(F\) is the futures price, so \(100 - F\) is the implied average rate in percent.
- \(\Delta\) is the size of the cut, in percentage points.

This treats the choice as "cut or hold". It ignores the gap between the effective rate and the middle of the range, and it ignores that a month containing the meeting is only partly after it. A real tool adjusts for both.

<div class="example" markdown>

### Worked example: from a futures price to odds

Everything here is made up. The target range is 3.50% to 3.75%, so we take \(R_0\) as 3.625%. A 25 bp cut is \(\Delta\) = 0.25.

1. The futures month starts after the meeting, and the price is 96.50. The implied average rate is 100 - 96.50 = 3.50%.
2. p = (3.625 - 3.50) / 0.25 = 0.50, so the market sees a 50% chance of a 25 bp cut.
3. If the price rises to 96.55, the implied rate is 3.45% and p = (3.625 - 3.45) / 0.25 = 0.70, a 70% chance.

A higher futures price means a lower expected rate, so higher odds of a cut. At a price of 96.375 the implied rate is 3.625% and the odds are 0%.

</div>

The next lesson shows why rate changes move stock prices. Part 16 covers trading around meeting days (FOMC, CPI and other data days<!-- link: ../16-volatility-and-event-trading/05-fomc-cpi-and-data-days.md -->).

<div class="canada" markdown>

### For Canadians

The Fed's decisions move USD/CAD and the prices of US stocks you hold in a Wealthsimple or IBKR account, whatever the account type (TFSA, RRSP, FHSA, cash or margin). The Bank of Canada sets its own rate, and lesson 11 covers how the gap between the two moves the exchange rate.

</div>

## Common mistakes

- Treating the dot plot as a promise.
- Reading the rate decision alone. When the market expected the move, the wording and the press conference carry the news.
- Using the futures odds as a forecast. They are market prices, so they include risk premiums and move with every release.

## Try it

1\. A fed funds futures price is 96.60. The range is 3.50% to 3.75%, and a cut would be 25 bp. What are the implied odds of a cut?

<details class="solution" markdown>
<summary>Answer</summary>

Implied rate = 100 - 96.60 = 3.40%. p = (3.625 - 3.40) / 0.25 = 0.90, so 90%.

</details>

2\. The range is 3.50% to 3.75%. Write the new range after a 25 bp cut and after a 50 bp hike.

<details class="solution" markdown>
<summary>Answer</summary>

After a 25 bp cut: 3.25% to 3.50%. After a 50 bp hike: 4.00% to 4.25%.

</details>

3\. Which 2026 meetings include a Summary of Economic Projections?

<details class="solution" markdown>
<summary>Answer</summary>

March 17 to 18, June 16 to 17, September 15 to 16 and December 8 to 9.

</details>

4\. The meeting ends on October 28, 2026. When are the minutes due?

<details class="solution" markdown>
<summary>Answer</summary>

Three weeks later: October 28 plus 21 days is November 18, 2026, which matches the Fed's calendar.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Open the latest FOMC statement on federalreserve.gov. Write the decision, and note what it says about inflation and jobs in your own words. |
| 3 | Open the [FOMC calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) and mark the next meeting and its minutes date in your [trade journal](../practice/trade-journal.md). |
| 2 | Write whether the next meeting has an SEP. |

</div>

## Key terms

- **Federal Reserve (the Fed)**: the central bank of the US.
- **FOMC**: the Federal Open Market Committee, which sets the policy rate.
- **Dual mandate**: the Fed's two goals, maximum employment and stable prices.
- **Federal funds rate**: the overnight rate at which banks lend reserve balances to each other.
- **Target range**: the band the FOMC sets for the federal funds rate.
- **Interest on reserve balances (IORB)**: the rate the Fed pays banks on their reserves.
- **Basis point (bp)**: one hundredth of a percentage point.
- **Summary of Economic Projections (SEP)**: the FOMC participants' forecasts, published four times a year.
- **Dot plot**: the SEP chart of each participant's projected policy rate.
- **Minutes**: the detailed record of an FOMC meeting, released three weeks later.
- **Fed funds futures**: contracts that settle at 100 minus a month's average federal funds rate.

Next: [Interest rates and asset prices](03-interest-rates-and-asset-prices.md)
