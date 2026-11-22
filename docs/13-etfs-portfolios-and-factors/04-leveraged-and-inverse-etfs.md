# Leveraged and inverse ETFs

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">ETF</span>

After this lesson you can work out what a daily-reset leveraged or inverse ETF returns over two days or a year, and explain why it can lose money when its index ends flat.

Before this: [How ETFs work](01-how-etfs-work.md), [Index funds, fees and tracking](02-index-funds-fees-and-tracking.md). The math book's [Investing returns and risk](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/06-investing-and-retirement/01-investing-returns-and-risk/) shows why a loss and a gain of the same size do not cancel. You need: a calculator.

## The idea

A **leveraged ETF** aims to return a multiple of its index's return, such as 2 or 3 times. An **inverse ETF** aims for the opposite, such as -1 times. Both do it by holding derivatives (swaps or futures, parts 14 and 15) that give more exposure than the fund's cash. The catch is in the wording of the goal: the multiple applies to each day. The fund resets its exposure every day, so over any longer period its return is not the multiple of the index's return.

The SEC and FINRA warn about this in an investor alert, "Leveraged and Inverse ETFs: Specialized Products with Extra Risks for Buy-and-Hold Investors" ([SEC investor alert, 2009](https://www.sec.gov/files/investor/pubs/leveragedetfs-alert.htm)). It says that over periods longer than one day their performance can differ significantly from the stated daily objective, and that losses are possible even when the index gains over the longer term.

## How it works

Two days with a 2x fund. The index starts at 100 and the fund at US$100. This is the alert's own hypothetical, and we compute it here.

<div class="example" markdown>

### Worked example: two days, 2x daily reset

1. Day 1: the index falls 10%, from 100 to 90. The 2x fund falls 20%, from US$100 to US$80.
2. Day 2: the index rises 10%, from 90 to 99. The 2x fund rises 20%, from US$80 to US$96.
3. The index lost 99 / 100 - 1 = -1%. The fund lost 96 / 100 - 1 = -4%, which is four times the index's loss, not two.
4. A 3x fund does the same with 30% moves: 100 to 70 to 91, a loss of 9% for an index loss of 1%.
5. An inverse (-1x) fund: day 1 the index falls 10% so the fund gains 10%, 100 to 110. Day 2 the index rises 10% so the fund loses 10%, 110 to 99. The index and its inverse fund both lost 1%.

</div>

The gap has a formula. If the daily index returns are \(r_1\) and \(r_2\) and the multiple is \(L\), the fund's two-day return is

\[ (1 + L r_1)(1 + L r_2) - 1 = L(r_1 + r_2) + L^2 r_1 r_2 \]

while \(L\) times the index's two-day return is \(L(r_1 + r_2 + r_1 r_2)\). The difference is \(L(L-1) r_1 r_2\).

- \(L\) is the multiple (2 for 2x), with no unit.
- \(r_1, r_2\) are the index's daily returns, as fractions.
- When the two days go opposite ways, \(r_1 r_2\) is negative, so the difference hurts. When they go the same way (a steady trend), \(r_1 r_2\) is positive and the daily reset helps: two +10% days give an index gain of 21% and a 2x fund gain of 44%, more than 2 x 21%.

For \(L = 2\) in step 3, \(L(L-1) r_1 r_2 = 2 \times (-0.10)(0.10) = -0.02\), which matches 2 x (-1%) = -2% against the fund's -4%.

### Volatility decay

Over many days, the size of the daily swings (volatility) decides how much the fund loses to this effect. A common approximation for the long-run growth rate of a fund with multiple \(L\) is

\[ g_L \approx L\mu - \frac{L^2 \sigma^2}{2} \]

- \(\mu\) is the index's average yearly return as a fraction (arithmetic).
- \(\sigma\) is the index's yearly volatility, as a fraction.
- \(g_L\) is the fund's yearly growth rate of the log-style average, before fees and financing costs.

This assumes returns that follow a random walk, so use it as a sense of size. With \(\mu = 8\%\):

| Volatility \(\sigma\) | Index (\(L=1\)) | 2x fund | 3x fund | Inverse (\(L=-1\)) |
|---|---|---|---|---|
| 20% | 6.0% | 8.0% | 6.0% | -10.0% |
| 30% | 3.5% | -2.0% | -16.5% | -12.5% |

At 20% volatility the 2x fund still beats the index on this formula. At 30% it loses money while the index earns 3.5%. The cost grows with the square of the multiple, so the 3x fund is hit hardest. These figures ignore fees, and these funds usually charge more than index funds.

The figure is one made-up path: an index with no drift and a daily volatility of 1.8%, 250 days. I picked a path where the index ends near where it began so the effect is easy to see; the formula says the effect is there on average, and a trending path would show the opposite. Look at how the fund (solid) ends below even the "twice the index's total return" line (dashed).

![A zero-drift index, twice its total return and a 2x daily-reset fund over 250 trading days; the fund ends lowest](../assets/figures/13-etfs-portfolios-and-factors/leveraged-decay-dark.svg#only-dark)
![A zero-drift index, twice its total return and a 2x daily-reset fund over 250 trading days; the fund ends lowest](../assets/figures/13-etfs-portfolios-and-factors/leveraged-decay-light.svg#only-light)

### What the SEC's examples show

The same alert gives real cases from December 1, 2008 to April 30, 2009. An index gained about 2%, while a 2x leveraged ETF on it fell 6% and a 2x inverse ETF fell 25%. In another case an index rose about 8%, while a 3x leveraged ETF fell 53% and a 3x inverse ETF fell 90% ([SEC investor alert](https://www.sec.gov/files/investor/pubs/leveragedetfs-alert.htm)). Choppy markets did the damage.

## What this means for you

These funds are designed for one-day exposure. Held longer, they behave like a different product from "2x the index", and the result depends on the path. A trader who holds one for a day knows what they own. A holder who thinks of one as a cheap way to get double the index return over a year does not, and the rules of [Risk first](../03-risk-and-position-sizing/01-risk-first.md) apply with more force: size the position by what it can lose in a day, not by the index it follows.

<div class="canada" markdown>

### For Canadians

Canadian-listed leveraged and inverse ETFs also exist, with the same daily reset logic. Read the prospectus for the stated goal and the period it applies to, and check that your broker allows the fund in your account type. This book does not recommend any.

</div>

## In code

Simulate the 2x fund day by day and compare it with twice the index's total return.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np

r = np.random.default_rng(8).normal(0.0, 0.018, 250)    # made-up daily index returns
index = 100 * np.prod(1 + r)
fund = 100 * np.prod(1 + 2 * r)
naive = 100 * (1 + 2 * (index / 100 - 1))
print(round(index, 1), round(fund, 1), round(naive, 1))
```

</details>

## Common mistakes

- Reading "2x" as "twice the return over my holding period". It is twice the daily return.
- Using an inverse fund as a long-term short. Both the index and the inverse fund can lose in a choppy market.
- Looking only at the multiple and ignoring the fee and financing cost, which are higher than for index funds.

## Try it

1\. An index falls 5% on day 1 and rises 5% on day 2. A 2x daily-reset fund starts at US$100. What is its value after two days?

<details class="solution" markdown>
<summary>Answer</summary>

Day 1: -10%, so US$90. Day 2: +10%, so 90 x 1.10 = US$99. The index is at 0.95 x 1.05 = 0.9975, down 0.25%. The fund is down 1%.

</details>

2\. An index rises 4% on each of two days. What is the 2x fund's two-day return, and how does it compare with twice the index's return?

<details class="solution" markdown>
<summary>Answer</summary>

Index: 1.04 x 1.04 = 1.0816, up 8.16%. Fund: 1.08 x 1.08 = 1.1664, up 16.64%. Twice the index's return is 16.32%, so the fund is 0.32 points ahead in a trend.

</details>

3\. With \(\mu = 8\%\) and \(\sigma = 25\%\), what does the formula give for a 2x fund?

<details class="solution" markdown>
<summary>Answer</summary>

2 x 0.08 - (4 x 0.0625) / 2 = 0.16 - 0.125 = 0.035, so 3.5% a year. The index gives 0.08 - 0.0625/2 = 4.875%.

</details>

4\. Why is the inverse fund in the worked example down 1% when the index is also down 1%?

<details class="solution" markdown>
<summary>Answer</summary>

The fund resets each day. It gains 10% off a base of 100 to reach 110, then loses 10% of 110, which is 11, to reach 99. The loss is larger than the gain because it is taken from a larger base.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Pick a 2x or 3x ETF and its index on an issuer's page. Find the stated goal and the period it covers. Write it down. |
| 3 | Look up the fund's return and its index's return over one year, from the issuer's page. Compare the fund's return with the multiple times the index. |
| 2 | Write one line on why you would or would not hold a daily-reset fund for a month. |

</div>

## Key terms

- **Leveraged ETF**: an ETF that aims to return a multiple of its index's daily return.
- **Inverse ETF**: an ETF that aims to return the opposite of its index's daily return.
- **Daily reset**: the fund's exposure is restored to the stated multiple at the end of each day.
- **Volatility decay**: the loss in a daily-reset fund's long-run growth that comes from the size of daily swings.

Next: [Asset allocation](05-asset-allocation.md)
