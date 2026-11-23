# Short interest and borrow

<span class="tag tag-data">Data</span> <span class="tag tag-part">DATA</span>

After this lesson you can read a short interest report, work out days to cover and the share of float sold short, estimate a borrow fee, and say what research found about heavily shorted stocks.

Before this: [Short selling](../01-how-markets-work/08-short-selling.md). You need: a calculator.

## The idea

Stock A has 40 million shares in its float. Short sellers have borrowed and sold 6.0 million of them. That is a bet against the stock, and it is also a pile of future buying, because every short has to be covered one day.

Lesson 8 of part 1 introduced **short interest**, the number of shares sold short and not yet covered, and **days to cover**, short interest divided by average daily volume. Here we read the data, see how old it is, and look at the cost side: the borrow.

### Where the data comes from

FINRA requires its member firms to report short positions in all equity securities twice a month. The [FINRA short interest page](https://www.finra.org/filing-reporting/short-interest) says reports are due by 6 p.m. ET on the second business day after a reporting settlement date that FINRA sets, and publication follows. FINRA's 2026 table lists these dates (as of 2026):

| Settlement date | Report due | Published |
|---|---|---|
| Friday, November 13 | Tuesday, November 17 | Tuesday, November 24 |
| Monday, November 30 | Wednesday, December 2 | Wednesday, December 9 |
| Tuesday, December 15 | Thursday, December 17 | Thursday, December 24 |
| Thursday, December 31 | Tuesday, January 5 | Tuesday, January 12 |

The count is as of the settlement date, so the number you see on November 24 describes November 13: 11 days earlier. A short seller who covered on November 16 is still in it. FINRA also filed a 2026 rule change (SR-FINRA-2026-012) to report more often and in more detail, and its [filing page](https://www.finra.org/rules-guidance/rule-filings/sr-finra-2026-012) marks it withdrawn, so check the schedule before you rely on one.

```mermaid
flowchart LR
  A[Nov 13 settlement date] --> B[Nov 17 firms report]
  B --> C[Nov 24 published]
```

The published number is always older than it looks.

## How it works

Three numbers come out of one report:

\[ \text{Days to cover} = \frac{S}{V} \qquad \text{Short percent of float} = \frac{S}{F} \]

- \(S\) is short interest in shares.
- \(V\) is average daily volume in shares (use the same window each time, such as 30 days).
- \(F\) is the float, the shares available to trade.

A short position also costs money. The **borrow fee** is an annual rate the lender charges, passed on by your broker, so for a short held \(d\) days it is the position value times the rate times \(d/365\). A stock with few shares available to lend is **hard to borrow**: the fee is high, and the broker may refuse the short. This links back to the locate rule in part 1.

<div class="example" markdown>

### Worked example: reading one report

Stock A (made-up) has short interest of 6.0 million shares, average daily volume of 1.5 million shares and a float of 40 million. The next report shows 7.2 million.

1. Days to cover: 6.0 / 1.5 = 4.0 days.
2. Short percent of float: 6.0 / 40 = 15.0%.
3. Change: (7.2 - 6.0) / 6.0 = +20.0%, so the new days to cover is 7.2 / 1.5 = 4.8.
4. Borrow: a US$5,000 short held 30 days at a 25% annual fee costs 5,000 x 0.25 x 30 / 365 = US$102.74. At 2% the same position costs US$8.22.

A fee of 25% is a market saying shares are scarce. It costs 2.05% of the position in 30 days, before any move in the price.

</div>

### What research found

Desai, Ramesh, Thiagarajan and Balachandran studied Nasdaq stocks from June 1988 to December 1994 ([Journal of Finance, 2002](https://econpapers.repec.org/RePEc:bla:jfinan:v:57:y:2002:i:5:p:2263-2287)). Heavily shorted stocks had negative abnormal returns of about 0.76% to 1.13% a month after adjusting for market, size, book-to-market and momentum, and were more likely to be delisted.

Asquith, Pathak and Ritter tested a longer period and both NYSE-Amex and Nasdaq stocks ([Journal of Financial Economics, 2005](https://www.nber.org/papers/w10434)). By their abstract, heavily shorted stocks generally underperformed on an equal-weighted basis, but not on a value-weighted basis. They find that many documented patterns do not hold up, and they warn that conclusions drawn from short subperiods, such as 1988 to 1994, can mislead.

Read together: heavy shorting has gone with weak returns in some periods, mostly in equal-weighted results, and the effect is not stable. Neither study is a trading rule.

<div class="canada" markdown>

### For Canadians

Short selling is not allowed in registered accounts (TFSA, RRSP, FHSA) and needs a non-registered margin account, as lesson 8 of part 1 notes. FINRA's data covers US-listed stocks. Look up the borrow fee in your broker's own tools before you plan a short, because it differs by broker and by day.

</div>

## Common mistakes

- Treating high short interest as a sure squeeze. The data shows shorts exist, not that they will be forced to cover.
- Using days to cover with a stale volume figure. Use the same recent window each time.
- Ignoring the borrow fee when a short is held for weeks.

## Try it

1\. Short interest is 9.0 million shares and average daily volume is 3.0 million. Days to cover?

<details class="solution" markdown>
<summary>Answer</summary>

9.0 / 3.0 = 3.0 days.

</details>

2\. The float is 60 million shares and short interest is 9.0 million. What share of float is short?

<details class="solution" markdown>
<summary>Answer</summary>

9.0 / 60 = 15.0%.

</details>

3\. You short US$8,000 of a stock for 45 days at a 12% annual borrow fee. What does the borrow cost?

<details class="solution" markdown>
<summary>Answer</summary>

8,000 x 0.12 x 45 / 365 = US$118.36.

</details>

4\. FINRA's settlement date is Tuesday, December 15, 2026 and the publication date is Thursday, December 24. How many calendar days old is the data when published?

<details class="solution" markdown>
<summary>Answer</summary>

9 days (December 15 to December 24).

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Pick two stocks. Find short interest, average volume and float, and compute days to cover and short percent of float. |
| 3 | Write the settlement date of the figure and today's date, and the gap in days. |
| 3 | Find the borrow fee in your broker's tools for one stock, and compute the cost of a 30-day US$5,000 short. |

</div>

## Key terms

- **Borrow fee**: the yearly rate charged to borrow shares for a short.
- **Hard to borrow**: a stock with few shares available to lend, so fees are high and shorting may be refused.
- **Settlement date (short interest)**: the date a short interest count is measured.

Next: [The Commitments of Traders report](05-commitments-of-traders.md)
