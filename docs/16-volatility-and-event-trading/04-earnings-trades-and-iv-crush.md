# Earnings trades and IV crush

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">VOL</span>

After this lesson you can read the move an option market expects into an earnings report, work out what a long straddle earns or loses before and after the report, and choose a defined-risk structure that matches your view on the move.

Before this: [Straddles and strangles](../15-options/11-straddles-and-strangles.md), [Theta, vega and rho](../15-options/07-theta-vega-and-rho.md), [Implied volatility](../15-options/08-implied-volatility.md), [Gaps](../05-reading-charts/10-gaps.md). You need: a calculator.

## The idea

Stock A reports earnings before the open on Monday, October 19, 2026 (made-up). On the Friday close, October 16, it is US$60.51. The options expiring October 23 carry an implied volatility of 55%, far above the stock's usual level. Why would anyone pay that? Because a report can move the price by several percent in one jump, and the options price that jump.

The market's estimate of the jump is the **implied move**: the price of the at-the-money straddle (a call and a put at the same strike) divided by the stock price. It is the expected move of lesson 8 in part 15, read off the front expiry that contains the report ([Implied volatility](../15-options/08-implied-volatility.md)). It is the expected size of the move, not one standard deviation. Here one standard deviation is 0.55 x \( \sqrt{7/365} \) = 7.6%, and a straddle costs about 0.8 of that, since it pays the average size of the move: 0.8 x 7.6% = 6.1%.

## How it works

### The run-up and the crush

Implied volatility tends to rise into a known report and fall once it passes. Patell and Wolfson (Journal of Accounting and Economics, 1979) studied call prices around annual earnings announcements and found systematic changes in the volatility that Black-Scholes prices imply ([Patell and Wolfson, 1979](https://www.gsb.stanford.edu/faculty-research/publications/anticipated-information-releases-reflected-call-option-prices)). The rise is the **IV run-up**. The fall afterwards is the **IV crush** of part 15 ([Theta, vega and rho](../15-options/07-theta-vega-and-rho.md)): the uncertainty is gone, so the market stops paying for it.

### Pricing the report

We use the Black-Scholes helper from part 15 with a 4% rate. Stock A: \( S = \) 60.51, strike 60.50, 7 days to expiry, IV 55%.

<div class="example" markdown>

### Worked example: a long straddle before a report

1. The 60.50 call is 1.8657 and the 60.50 put is 1.8093. The straddle costs 3.6750, or US$367.50 per contract.
2. The implied move is 3.6750 / 60.51 = 0.0607, so 6.1%. The breakevens at expiry are 60.50 plus and minus 3.675: 56.83 and 64.17.
3. The report is bad. At Monday's close, October 19, Stock A is 54.15, down 10.5% from 60.51 (it opened at 54.82). Four days are left and IV has fallen to 32%.
4. The call is worth 0.0002 and the put 6.3237. The straddle is worth 6.3239, a gain of 6.3239 - 3.6750 = 2.6489, or US$264.89 per contract (+72%).

The move, 10.5%, was larger than the implied 6.1%, and the straddle won even after the crush.

</div>

The figure shows the straddle's profit at expiry. Look at the shaded band: it spans the breakevens, and its half-width is the straddle price.

![Profit of the Stock A 60.50 straddle at expiry, with breakevens at 56.83 and 64.17](../assets/figures/16-volatility-and-event-trading/expected-move-dark.svg#only-dark)
![Profit of the Stock A 60.50 straddle at expiry, with breakevens at 56.83 and 64.17](../assets/figures/16-volatility-and-event-trading/expected-move-light.svg#only-light)

```chart
data: 16-volatility-and-event-trading/stock-a-earnings-gap.json
title: Stock A, daily: a gap down through the implied move
level: 60.51 | Close before the report
marker: 2026-10-19 | below | Opens at 54.82
range: 2026-09-14 to 2026-11-02
caption: Stock A closed at 60.51 on October 16 and gapped to 54.82 on October 19, down 9.4%, against an implied move of 6.1%.
```

Now the other outcome. Stock B closes at 47.28 on October 16, with a 47.50 straddle at an IV of 50%.

<div class="example" markdown>

### Worked example: the same trade with a small move

1. The 47.50 call is 1.2186 and the put 1.4022. The straddle costs 2.6208, or US$262.08, an implied move of 2.6208 / 47.28 = 5.5%.
2. Stock B reports and gaps up 1.8% to 48.13. At Monday's close it is 48.23, up 2.0%. IV falls to 30% with four days left.
3. The call is worth 1.0482 and the put 0.2974. The straddle is worth 1.3456, a change of 1.3456 - 2.6208 = -1.2752, or -US$127.52 per contract (-48.7%).

The stock moved 2.0%, well inside the implied 5.5%. The straddle bought both the move and the volatility, and only the volatility fell.

</div>

```chart
data: 16-volatility-and-event-trading/stock-b-earnings-calm.json
title: Stock B, daily: a gap inside the implied move
level: 47.28 | Close before the report
marker: 2026-10-19 | below | Opens at 48.13
range: 2026-09-14 to 2026-11-02
caption: Stock B closed at 47.28 on October 16 and opened at 48.13 on October 19, up 1.8%, against an implied move of 5.5%.
```

### Why the crush works against a long straddle

Before the report you pay the implied move. You win only if the actual move is bigger. The crush works against you even in the trade that moves: if Stock A had closed flat at 60.51 on Monday, the straddle would be worth 1.6170, a loss of 2.0580, or US$205.80 (-56%), with nothing but the crush and three days of decay. Because the price already contains the expected jump, a straddle needs the realized move to beat the implied one. That depends on how the realized jumps compare with the implied ones over many reports, and this book found no test of it that it can confirm, so it makes no claim.

### Defined-risk structures

A long straddle risks its whole premium, which is 1.47R of US$250 here, so one contract does not fit a 1% rule (part 15, [Straddles and strangles](../15-options/11-straddles-and-strangles.md)). Three structures change that.

- A long strangle, with out-of-the-money strikes, costs less and needs a larger move.
- A vertical spread (part 15, [Vertical spreads](../15-options/10-vertical-spreads.md)) bets on a direction with a capped loss.
- A short iron condor ([Iron condors and butterflies](../15-options/12-iron-condors-and-butterflies.md)) sells the crush. It collects a credit if the stock stays between the short strikes, and its loss is capped.

<div class="example" markdown>

### Worked example: an iron condor on the calm report

Model mid prices at 50% IV: buy the 42.50 put at 0.0810, sell the 45 put at 0.4371, sell the 50 call at 0.4067, buy the 52.50 call at 0.1007.

1. Credit = 0.4371 + 0.4067 - 0.0810 - 0.1007 = 0.6621, so US$66.21 per contract.
2. Maximum loss = (2.50 - 0.6621) x 100 = US$183.79. One contract fits a US$250 1R, at 0.74R.
3. After the calm report, at 30% IV, the legs are worth 0.0, 0.0067, 0.0989 and 0.0017. Buying the condor back costs 0.0067 + 0.0989 - 0.0017 = 0.1039.
4. Profit = 0.6621 - 0.1039 = 0.5582, so US$55.82 per contract, or 0.22R.

If Stock B had gapped past 42.50 or 52.50, the loss would have been the maximum, US$183.79. The prices are model mids; four legs on a report day have wide spreads that shrink the credit.

</div>

When this fails: the stock moves more than the options priced (for the short structures), or less (for the long ones), and the spreads around a report can be wide. For direction without options, see how stocks drift after a gap ([Gaps](../05-reading-charts/10-gaps.md)).

<div class="canada" markdown>

### For Canadians

Long options are the simplest fit for a TFSA or RRSP, and a short iron condor needs a margin account at some brokers. Part 15 lists what we could confirm ([Options in Canadian accounts](../15-options/15-options-in-canadian-accounts.md)). Find the report date on the company's investor-relations page or its press release, not a third-party list.

</div>

## Common mistakes

- Buying a straddle because the move "will be big". The price already holds a big move, so compare your estimate with the implied move.
- Comparing the report move with an IV quoted for a month. Use the expiry that contains the report.
- Sizing a short structure by the credit. Size it by the maximum loss.

## Try it

1\. Stock A is US$60.51 and the straddle costs US$3.675. What is the implied move in percent and in dollars?

<details class="solution" markdown>
<summary>Answer</summary>

3.675 / 60.51 = 0.0607, so 6.1%, or US$3.68 a share.

</details>

2\. Stock B gaps 3.0% up from 47.28. Is that more or less than its implied move of 5.5%?

<details class="solution" markdown>
<summary>Answer</summary>

Less. 3.0 / 5.5 = 0.55, so about 0.55 of the implied move.

</details>

3\. The straddle on Stock B costs US$262.08 and your 1R is US$250. What is its cost in R?

<details class="solution" markdown>
<summary>Answer</summary>

262.08 / 250 = 1.05R, so one contract is more than the 1R limit and you buy zero contracts.

</details>

4\. A condor collects US$66.21 on a width of 2.50. What is the maximum loss and how many contracts fit a US$250 1R?

<details class="solution" markdown>
<summary>Answer</summary>

(2.50 - 0.6621) x 100 = US$183.79. 250 / 183.79 = 1.36, so 1 contract.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Find a stock that reports this week. Write the front-expiry at-the-money straddle price and divide by the stock price to get the implied move. |
| 3 | Look up its last four earnings gaps. Write each as a percent of the pre-report close and compare with the implied move. |
| 3 | Open [chart drills](../practice/chart-drills.md) and answer the earnings gap items. |

</div>

## Key terms

- **Implied move**: the at-the-money straddle price divided by the stock price, the move the options market expects.
- **IV run-up**: the rise in implied volatility into a known report.
- **IV crush**: the fall in implied volatility once the report has passed.

Next: [FOMC, CPI and other data days](05-fomc-cpi-and-data-days.md)
