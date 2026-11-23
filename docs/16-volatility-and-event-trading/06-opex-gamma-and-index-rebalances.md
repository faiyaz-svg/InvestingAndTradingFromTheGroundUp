# Opex, gamma and index rebalances

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-review">Review</span> <span class="tag tag-part">VOL</span>

After this lesson you can say what happens on a monthly options expiration day, explain the dealer gamma theory and what evidence supports it, describe how an index rebalance can move a stock, and run the part's paper block of event trades.

Before this: [Assignment, exercise and 0DTE](../15-options/14-assignment-exercise-and-0dte.md), [Delta and gamma](../15-options/06-delta-and-gamma.md), [Indexes, sectors and market cap](../01-how-markets-work/10-indexes-sectors-and-market-cap.md), [Expiry and rolling](../14-futures/04-expiry-and-rolling.md). You need: a calculator.

## The idea

Many contracts end on the same day. Monthly equity options expire on the third Friday of the month ([Calls and puts](../15-options/01-calls-and-puts.md)). Cboe's standard S&P 500 index options (SPX) are settled on the third Friday as well, or the business day before if the exchange is closed, and its weekly SPX options now expire every business day from Monday to Friday ([Cboe, SPX weeklys](https://www.cboe.com/insights/posts/how-to-make-the-most-of-added-spxw-options-expirations/), as of 2026). In March, June, September and December, index futures expire that day too (part 14). Traders call the monthly date **opex**, short for options expiration, and the quarterly one with futures **triple witching**.

Why would that day matter for price? One theory gives a reason.

## How it works

### Dealer gamma

A **dealer** (an options market maker) takes the other side of customer option trades and then hedges its delta with stock or futures ([Who is on the other side](../01-how-markets-work/06-who-is-on-the-other-side.md)). The hedge changes with the price because of gamma ([Delta and gamma](../15-options/06-delta-and-gamma.md)). The theory has two cases.

- If dealers are net short options, they are short gamma. When the stock rises, their delta turns more negative, so they buy stock to hedge, and when it falls they sell. Their hedging pushes in the same direction as the move and can amplify it.
- If dealers are net long options, they are long gamma. They sell into rises and buy into falls, which dampens moves.

<div class="example" markdown>

### Worked example: the size of a hedge

Stock A is US$50.00. Customers hold 2,000 call contracts struck at 50, 30 days left, IV 30%, and the dealers are short them. Each contract covers 100 shares, so 200,000 shares.

1. Gamma of the 50 call with 30 days left is 0.0925 per share.
2. A US$1 rise changes the dealers' hedge by 200,000 x 0.0925 = 18,500 shares, which they buy.
3. With one day left, gamma is 0.5081, so the same US$1 rise needs 200,000 x 0.5081 = 101,620 shares.

Gamma grows as expiry nears, so the forced hedging per dollar is about 5.5 times larger on the last day.

</div>

What tests found: Ni, Pearson, Poteshman and White (Review of Financial Studies, 2021) found that the hedging of option market makers is linked to higher stock return volatility and a greater chance of large price moves ([paper](https://doi.org/10.1093/rfs/hhaa082)). Earlier, Ni, Pearson and Poteshman (Journal of Financial Economics, 2005) found that stock closing prices cluster at option strikes on expiration dates. These results support a hedging effect in general. They do not show that you can trade it, because dealer positions are not observed. Data vendors estimate them by assuming who is long and who is short, and different assumptions give different answers. This book found no published test that a rule built on estimated dealer gamma earns money after costs, so it makes no claim that one does.

### Opex and pin risk

The assignment risk of part 15 sits on this day: a stock that closes near a heavily traded strike leaves holders and writers unsure what will be exercised ([Assignment, exercise and 0DTE](../15-options/14-assignment-exercise-and-0dte.md)). Manage short options near a strike before the close.

### Index rebalances

An index fund must hold what its index holds. When an index adds a stock, funds that track it buy. S&P Dow Jones Indices rebalances the S&P 500 quarterly, in March, June, September and December, and the changes take effect before the open on the Monday after the third Friday. It announces additions some days earlier (the release linked below is dated September 4 for a September 21 change), and can also change the index off schedule ([S&P Dow Jones Indices, an announcement](https://press.spglobal.com/2026-09-04-Bloom-Energy,-Illumina,-and-Everpure-Set-to-Join-S-P-500-Others-to-Join-S-P-100,-S-P-MidCap-400,-and-S-P-SmallCap-600), as of 2026). 

The chart is a made-up Stock B added to a made-up index. The gap is the announcement, and the marker is the close before the effective date.

```chart
data: 16-volatility-and-event-trading/stock-b-index-add.json
title: Stock B, daily: a jump on an index addition, then a fade
level: 33.03 | Close before the announcement
marker: 2026-07-06 | below | Opens at 35.18
marker: 2026-07-17 | above | Close before the effective date
range: 2026-06-15 to 2026-08-11
caption: Stock B closed at 33.03 on July 3, opened at 35.18 on July 6 (+6.5%), closed at 37.00 on July 13, at 35.70 on July 17 and at 33.75 on August 11.
```

A holder from the July 3 close is up 8.1% on July 17 (35.70 / 33.03) and 2.2% on August 11. A buyer at Monday's close of 35.08 is down 3.8% by August 11 (33.75 / 35.08).

What tests found: Shleifer (Journal of Finance, 1986) and Harris and Gurel (Journal of Finance, 1986) found abnormal returns of about 3% around S&P 500 additions, and Harris and Gurel found that most of the price rise reversed within about two weeks. Greenwood and Sammon (Journal of Finance, 2025) found that the effect has faded, from an average of 7.4% in the 1990s to less than 1% over the past decade ([paper](https://econpapers.repec.org/RePEc:bla:jfinan:v:80:y:2025:i:2:p:657-698)). 

## Paper block 6

The book sets six paper blocks ([paper trading](../practice/paper-trading.md)). Block 6 is 10 event trades, to plan the event, the size and the exit before it happens.

- Choose events from this part: earnings with a defined-risk structure, a data or FOMC day, or an expiration or rebalance day.
- Before the event, write the plan in the journal: the instrument, the entry, the stop or maximum loss, the target, the size in R, and the time you will be out.
- Size by the maximum loss, including fees and the slippage you expect on a wide event-day spread.
- Follow each trade to its exit even when it loses, and record the R.
- Apply the realism rules on the paper trading page.

## Part check

1\. A stock's 21-day realized volatility is 24% and its 30-day IV is 30%. What is the gap, and what is it called?

<details class="solution" markdown>
<summary>Answer</summary>

30 - 24 = 6 volatility points. It is the variance risk premium in volatility terms.

</details>

2\. The VIX is 20. What is the one-day one-standard-deviation move for the S&P 500?

<details class="solution" markdown>
<summary>Answer</summary>

20 / 15.8745 = 1.26%.

</details>

3\. A product holds a one-month VIX future at 20.00 while the VIX stays at 18.50. What is the one-month result?

<details class="solution" markdown>
<summary>Answer</summary>

(18.50 - 20.00) / 20.00 = -0.075, so -7.5%.

</details>

4\. Today's 20-day realized volatility is 15% and the baseline median is 9%. Which regime does the lesson 3 rule give?

<details class="solution" markdown>
<summary>Answer</summary>

15 / 9 = 1.67, above 1.5, so a high-volatility regime.

</details>

5\. A stock is US$82.00 and its front-expiry straddle costs US$4.10. What is the implied move?

<details class="solution" markdown>
<summary>Answer</summary>

4.10 / 82.00 = 0.05, so 5.0%.

</details>

6\. A micro future is worth US$5 a point. You size for a stop 22 points away with 1R = US$200, and the stop fills 4 points worse. How many contracts, and what is the loss in R?

<details class="solution" markdown>
<summary>Answer</summary>

Risk per contract = 22 x 5 = US$110. 200 / 110 = 1.8, so 1 contract. The loss is 26 x 5 = US$130, which is 130 / 200 = 0.65R of the US$200 limit.

</details>

7\. Dealers are short 1,000 calls (100,000 shares) with gamma 0.0925. How many shares must they buy for a US$1 rise?

<details class="solution" markdown>
<summary>Answer</summary>

100,000 x 0.0925 = 9,250 shares.

</details>

## Try it

1\. A stock goes from US$40.00 to US$44.00 on the effective date of an index addition, after closing at US$37.00 before the announcement. What is the total gain from the announcement close, and the gain from US$40.00 to US$44.00?

<details class="solution" markdown>
<summary>Answer</summary>

44.00 / 37.00 - 1 = 0.1892, so +18.9% in total. From US$40.00 to US$44.00 the gain is 44.00 / 40.00 - 1 = 10.0%.

</details>

2\. Dealers are short 500 call contracts with gamma 0.0925. How many shares must they buy for a US$2 rise, to a first approximation?

<details class="solution" markdown>
<summary>Answer</summary>

500 x 100 x 0.0925 = 4,625 shares per US$1, so about 9,250 shares for US$2.

</details>

3\. What is the third Friday of December 2026?

<details class="solution" markdown>
<summary>Answer</summary>

December 1, 2026 is a Tuesday, so the Fridays are the 4th, 11th and 18th. The third Friday is December 18, 2026.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Find the next monthly expiration (third Friday) and the next quarterly index rebalance date. Write both in your journal calendar. |
| 4 | Write the plan for your first block 6 trade: event, instrument, size in R, exit time. Use the [paper trading](../practice/paper-trading.md) rules. |
| 2 | Open [chart drills](../practice/chart-drills.md) and answer one set of the part 16 items. |

</div>

## Key terms

- **Opex**: monthly options expiration, on the third Friday of the month.
- **Triple witching**: the quarterly date when index futures, index options and stock options expire together.
- **Dealer**: an options market maker that hedges the delta of the options it sells.
- **Dealer gamma**: the gamma of dealers' net option position, which sets whether their hedging amplifies or dampens price moves.
- **Pinning**: the tendency of a stock to close near an option strike on expiration day.
- **Index rebalance**: a scheduled change to an index's members or weights, which index funds must copy.

Next: [Commodity markets](../17-commodities-forex-and-reits/01-commodity-markets.md)
