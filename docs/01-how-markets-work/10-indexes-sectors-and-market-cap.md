# Indexes, sectors and market cap

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">MKT</span>

After this lesson you can compute an index level two ways (price-weighted and cap-weighted), explain why they move differently, and name the sectors a stock can belong to.

Before this: [Dividends, splits and corporate actions](09-dividends-splits-and-corporate-actions.md). You need: a calculator.

## The idea

When the news says "the market rose 1%", it means an index rose. An **index** is a list of stocks combined into one number, so you can follow a market or a part of it without tracking each stock. The rule for combining them is the **weighting**, and it decides which stocks move the number.

Take three made-up stocks. Stock A trades at US$200 and has 10 million shares, Stock B trades at US$50 with 100 million shares, and Stock C trades at US$10 with 300 million shares. Their market caps (lesson 1) are US$2.0 billion, US$5.0 billion and US$3.0 billion. Stock A has the highest price and the smallest company. Watch what that does under two weightings.

## How it works

### Price-weighted

A **price-weighted index** adds up the share prices and divides by a number called the **divisor**.

\[ I = \frac{\sum P_i}{d} \]

- \(P_i\) is the price of stock \(i\), in US$.
- \(d\) is the divisor, a number the index provider sets so the starting level is what it wants.
- \(I\) is the index level, in points.

The Dow Jones Industrial Average is price-weighted, with 30 stocks ([S&P Dow Jones Indices, "The Dow Turns 120"](https://www.spglobal.com/spdji/en/documents/research/spdji-the-dow-turns-120.pdf)). When a stock splits, its price drops, so the divisor is changed to keep the index level the same. Check the current divisor on the provider's site, since it changes with each such adjustment.

### Cap-weighted

A **market-cap-weighted index** gives each stock a weight proportional to its market cap. The S&P 500 is float-adjusted, meaning it counts only the shares that are available to the public (the **float**), not shares held by insiders or governments ([S&P U.S. indices methodology](https://www.spglobal.com/spdji/en/documents/methodologies/methodology-sp-us-indices.pdf)).

\[ w_i = \frac{P_i \, N_i \, f_i}{\sum_j P_j \, N_j \, f_j} \]

- \(w_i\) is stock \(i\)'s weight, a fraction of the index.
- \(P_i\) is the price in US$, \(N_i\) the shares outstanding, and \(f_i\) the float fraction (1 if all shares are public).

The Nasdaq-100 holds the 100 largest non-financial companies listed on Nasdaq, with a modified market-cap weighting ([Nasdaq-100 methodology](https://indexes.nasdaqomx.com/docs/Methodology_NDX_Effective_May_1_2026.pdf)). The weighting rules change, so read the current methodology before you rely on a weight.

<div class="example" markdown>

### Worked example: the same moves in two indexes

The weights from the starting prices:

| Stock | Price (US$) | Shares (millions) | Market cap (US$ millions) | Price weight | Cap weight |
|---|---|---|---|---|---|
| A | 200 | 10 | 2,000 | 76.9% | 20.0% |
| B | 50 | 100 | 5,000 | 19.2% | 50.0% |
| C | 10 | 300 | 3,000 | 3.8% | 30.0% |

Price-weighted: the sum of prices is 200 + 50 + 10 = 260. Choose a divisor of 2.6 so the index starts at 260 / 2.6 = 100. Cap-weighted: total market cap is US$10,000 million, and we start it at 100 too.

1. Stock A rises 10%, to US$220. The price-weighted index is (220 + 50 + 10) / 2.6 = 107.69, up 7.7%. The cap-weighted index is up 0.10 x 20.0% = 2.0%, to 102.0.
2. Instead, Stock C rises 10%, to US$11. The price-weighted index is (200 + 50 + 11) / 2.6 = 100.38, up 0.4%. The cap-weighted index is up 0.10 x 30.0% = 3.0%, to 103.0.

The same 10% move in one stock gives 7.7% or 0.4% in the price-weighted index. In the cap-weighted index it gives 2.0% or 3.0%. A price-weighted index follows the stock with the biggest price, and a cap-weighted index follows the biggest company.

3. Split: Stock A splits 2-for-1 to US$100. The price sum is now 160. To keep the index at 100, the divisor becomes 160 / 100 = 1.6.

</div>

The figure shows the two weightings for the three stocks.

![Bar chart of weights for three made-up stocks: price weights are 76.9, 19.2 and 3.8 percent, cap weights are 20, 50 and 30 percent](../assets/figures/01-how-markets-work/index-weights-dark.svg#only-dark)
![Bar chart of weights for three made-up stocks: price weights are 76.9, 19.2 and 3.8 percent, cap weights are 20, 50 and 30 percent](../assets/figures/01-how-markets-work/index-weights-light.svg#only-light)

### Size tiers

**Large-cap**, **mid-cap** and **small-cap** are labels for market cap size. The dollar boundaries differ by index provider and change over time, so look up the provider's current ranges instead of memorizing them. The S&P 500 holds large US companies and is the usual benchmark, a standard you compare a portfolio against. Its rules also require positive earnings, among other tests, and S&P decided in June 2026 to keep its eligibility rules unchanged ([S&P DJI, June 4, 2026](https://press.spglobal.com/2026-06-04-S-P-Dow-Jones-Indices-Consultation-on-Treatment-of-MegaCap-Companies-Results)).

### Sectors

Companies are grouped by what they do. The Global Industry Classification Standard (GICS) splits the market into 11 **sectors**: Communication Services, Consumer Discretionary, Consumer Staples, Energy, Financials, Health Care, Industrials, Information Technology, Materials, Real Estate and Utilities. Labels can change. In March 2023 Visa, Mastercard and PayPal moved from Information Technology to Financials, and 14 S&P 500 stocks changed sector ([State Street on the 2023 GICS changes](https://www.ssga.com/us/en/individual/etfs/insights/2023-gics-changes-companies-impacted-and-what-you-need-to-know)). A sector's past performance can look different after a reclassification.

<div class="canada" markdown>

### For Canadians

Canada's main broad index is the S&P/TSX Composite. Its rules are on the S&P Dow Jones Indices site. You can own an index through an ETF (exchange-traded fund), which Part 13 explains ([How ETFs work](../13-etfs-portfolios-and-factors/01-how-etfs-work.md)). You can also own US index ETFs from a Canadian account, where the currency and tax rules in Part 2 apply.

</div>

## Common mistakes

- Reading the Dow as "the market". It has 30 stocks and weights by price, so a US$400 stock counts more than a US$40 stock.
- Comparing an index's price level to your portfolio's return. An index level may exclude dividends. Check whether you are looking at a price index or a total return index.
- Treating sector labels as fixed. They change, and an ETF's sector weights can shift without any trade.

## Try it

1\. Index of two stocks: X at US$80 and Y at US$20. Price-weighted, divisor 1.0. X rises 5% and Y rises 20%. What is the index change?

<details class="solution" markdown>
<summary>Answer</summary>

Before: 80 + 20 = 100. After: 84 + 24 = 108. The index rose 8.0%.

</details>

2\. A cap-weighted index of X (market cap US$800 million) and Y (US$200 million). X rises 5% and Y rises 20%. What is the change?

<details class="solution" markdown>
<summary>Answer</summary>

Weights are 80% and 20%. Change = 0.80 x 5% + 0.20 x 20% = 4% + 4% = 8.0%. Check with caps: 840 + 240 = 1,080 against 1,000, up 8.0%.

</details>

3\. In the three-stock example, Stock C is 40% held by its founder, so its float fraction is 0.60. What is its float-adjusted weight?

<details class="solution" markdown>
<summary>Answer</summary>

Float cap for C = 3,000 x 0.60 = 1,800. Total = 2,000 + 5,000 + 1,800 = 8,800. Weight = 1,800 / 8,800 = 20.5% (rounded).

</details>

4\. A price-weighted index of three stocks has prices 90, 60 and 30, with a divisor of 1.8. What is the level? The 90 stock splits 3-for-1. What is the new divisor?

<details class="solution" markdown>
<summary>Answer</summary>

Level = (90 + 60 + 30) / 1.8 = 100. After the split the price is 30, so the sum is 120. New divisor = 120 / 100 = 1.2.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Find the top 10 holdings and weights of an S&P 500 ETF on its provider's page. Write the combined weight of the top 3. |
| 3 | Find the sector weights for the same fund and write the largest sector and its weight. |
| 3 | Check which index your broker's "market" tab quotes, and whether it is a price index or total return index. |

</div>

## Key terms

- **Index**: a list of stocks combined into one number.
- **Weighting**: the rule for how much each stock counts in an index.
- **Price-weighted index**: an index of summed prices divided by a divisor.
- **Divisor**: the number the price sum is divided by, adjusted for splits.
- **Market-cap-weighted index**: an index where each stock counts in proportion to its market cap.
- **Float**: the shares available to the public.
- **Large-cap, mid-cap, small-cap**: labels for market cap size, with boundaries set by each provider.
- **Benchmark**: a standard, such as an index, that you compare results against.
- **Sector**: a group of companies by what they do; GICS has 11.

Next: [Reading a quote page](11-reading-a-quote-page.md)
