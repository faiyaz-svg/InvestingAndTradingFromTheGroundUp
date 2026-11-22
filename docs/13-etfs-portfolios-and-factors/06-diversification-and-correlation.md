# Diversification and correlation

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">ETF</span>

After this lesson you can compute the volatility of a two-asset portfolio from the weights, the volatilities and the correlation, and say why holding more stocks stops helping after a point and why correlations rise in a crash.

Before this: [Asset allocation](05-asset-allocation.md), [Portfolio heat and correlation](../03-risk-and-position-sizing/07-portfolio-heat-and-correlation.md). The math book's [Investing returns and risk](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/06-investing-and-retirement/01-investing-returns-and-risk/) works a two-asset example; here we go further. You need: a calculator.

## The idea

You hold a stock fund whose yearly return swings with a standard deviation of 16%. You add a bond fund with a standard deviation of 6%. Does the portfolio swing like the average of the two, about 12% for a 60 / 40 mix? It swings less, about 10.35%, because the two funds do not move in step. The size of the saving depends on one number, the correlation between them.

The **correlation** \(\rho\) is a number from -1 to 1. At 1 the two assets move in perfect step. At 0 they are unrelated. At -1 they move in opposite directions. **Diversification** is holding assets that do not move together, so that a loss in one is partly offset by the others. It is the one place in finance where you get something for free: lower risk with no change in the weighted average return.

## How it works

For two assets with weights \(w_1\) and \(w_2 = 1 - w_1\), the portfolio's variance is

\[ \sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho \, \sigma_1 \sigma_2 \]

- \(w_1, w_2\) are the weights, as fractions that add to 1.
- \(\sigma_1, \sigma_2\) are the yearly standard deviations of each asset's return, as fractions.
- \(\rho\) is their correlation, with no unit.
- \(\sigma_p\) is the square root of this, the portfolio's yearly standard deviation.

The first two terms are what each asset contributes alone. The third is the interaction, and it is the only one that changes with \(\rho\). At \(\rho = 1\) the formula collapses to \(\sigma_p = w_1\sigma_1 + w_2\sigma_2\), a plain weighted average, so there is no gain.

<div class="example" markdown>

### Worked example: a 60 / 40 stock and bond mix

Stocks: \(w_1 = 0.6\), \(\sigma_1 = 0.16\). Bonds: \(w_2 = 0.4\), \(\sigma_2 = 0.06\). Correlation 0.2.

1. Stock term: 0.6^2 x 0.16^2 = 0.36 x 0.0256 = 0.009216.
2. Bond term: 0.4^2 x 0.06^2 = 0.16 x 0.0036 = 0.000576.
3. Interaction: 2 x 0.6 x 0.4 x 0.2 x 0.16 x 0.06 = 0.0009216.
4. Variance = 0.009216 + 0.000576 + 0.0009216 = 0.0107136. Standard deviation = sqrt(0.0107136) = 10.35%.
5. The weighted average of the two standard deviations is 0.6 x 16 + 0.4 x 6 = 12.0%. Diversification removed 1.65 points.

On C$50,000, a one-standard-deviation year is a move of about C$5,175 for the mix, against C$6,000 if the correlation were 1.

</div>

The same weights with other correlations: at \(\rho = 0\) the volatility is 9.90%, at \(\rho = -0.3\) it is 9.17%, at \(\rho = 0.8\) it is 11.61%, and at \(\rho = 1\) it is 12.00%. The figure shows the volatility for every stock weight at three correlations. Look at the left end of the orange line (correlation 0.2): a small bond-heavy portfolio with 5% to 10% in stocks has a slightly lower volatility than 100% bonds.

![Volatility of a stock and bond mix against the stock weight at correlations of 1.0, 0.2 and minus 0.3](../assets/figures/13-etfs-portfolios-and-factors/correlation-risk-dark.svg#only-dark)
![Volatility of a stock and bond mix against the stock weight at correlations of 1.0, 0.2 and minus 0.3](../assets/figures/13-etfs-portfolios-and-factors/correlation-risk-light.svg#only-light)

### How many stocks are enough

Take \(N\) stocks held in equal weights, each with volatility \(\sigma\), and an average pairwise correlation \(\rho\). The portfolio's variance is

\[ \sigma_p^2 = \sigma^2 \left( \frac{1}{N} + \left(1 - \frac{1}{N}\right) \rho \right) \]

For \(\sigma = 30\%\) and \(\rho = 0.3\):

| Number of stocks \(N\) | 1 | 5 | 10 | 30 | 100 | Very large |
|---|---|---|---|---|---|---|
| Portfolio volatility | 30.0% | 19.9% | 18.2% | 17.1% | 16.6% | 16.4% |

The first few stocks do most of the work. After about 30, adding more shaves little off, because the risk left is the part all stocks share, which comes from the market, and no number of stocks removes it. The floor is \(\sigma \sqrt{\rho} = 30\% \times 0.548 = 16.4\%\). That shared part is **systematic risk** (market risk). The part you can diversify away is **idiosyncratic risk** (the risk specific to a company). An index fund holds hundreds of stocks to remove the second and accept the first.

### Correlations rise when markets fall

The inputs above are averages, and a correlation is not a constant. Longin and Solnik studied monthly returns for the five largest stock markets from 1958 to 1996, and found that the correlation between markets rises in bear markets but not in bull markets ([Journal of Finance, 2001](https://econpapers.repec.org/RePEc:bla:jfinan:v:56:y:2001:i:2:p:649-676)). The time you most want a diversifier to work is the time it works least.

Two stock funds, each with volatility 20%, held 50 / 50, show the size of this. At \(\rho = 0.5\) the portfolio's volatility is 17.32%. If the correlation rises to 0.9 in a crash, it is 19.49%, nearly the volatility of one fund. Bonds have behaved better against stocks in many crashes, but not all: in years when both fell together, part 12 explains the reason, in [Bond ETFs, and rates against stocks](../12-bonds-and-the-yield-curve/06-bond-etfs-and-rates-vs-stocks.md).

## In code

Compute the correlation of two return series and the volatility of a mix.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np

stock = np.array([8.0, -3.0, 12.0, -15.0, 20.0, 5.0])    # made-up yearly returns, %
bond = np.array([3.0, 4.0, 2.0, 6.0, 1.0, 3.5])
rho = np.corrcoef(stock, bond)[0, 1]
w = 0.6
var = (w * stock.std(ddof=1)) ** 2 + ((1 - w) * bond.std(ddof=1)) ** 2 \
    + 2 * w * (1 - w) * rho * stock.std(ddof=1) * bond.std(ddof=1)
print(round(rho, 2), round(var ** 0.5, 2))
```

</details>

<div class="canada" markdown>

### For Canadians

Your home market is concentrated in a few sectors, so a Canadian-only stock fund is less diversified than its number of holdings suggests. Adding US and international stock funds lowers the idiosyncratic and sector risk, at the cost of currency exposure ([Currency risk on US stocks](../02-accounts-currency-and-taxes/05-currency-risk-on-us-stocks.md)).

</div>

## Common mistakes

- Counting holdings instead of exposures. Ten funds that all hold the same large US stocks are one bet.
- Using a calm-period correlation for a stress test. Use a higher one, such as 0.8 to 0.9 between stock funds.
- Expecting diversification to remove market risk. It removes company-specific risk only.

## Try it

1\. Stocks (\(\sigma = 18\%\)) and bonds (\(\sigma = 5\%\)) are held 50 / 50 with correlation 0.1. What is the portfolio's volatility?

<details class="solution" markdown>
<summary>Answer</summary>

Variance = 0.25 x 0.0324 + 0.25 x 0.0025 + 2 x 0.5 x 0.5 x 0.1 x 0.18 x 0.05 = 0.0081 + 0.000625 + 0.00045 = 0.009175. Volatility = sqrt(0.009175) = 9.58%.

</details>

2\. What would it be at a correlation of 1, and how many points did diversification save?

<details class="solution" markdown>
<summary>Answer</summary>

0.5 x 18 + 0.5 x 5 = 11.5%. The saving is 11.5 - 9.58 = 1.92 points.

</details>

3\. Twenty equal-weight stocks, each with volatility 25% and average correlation 0.4. What is the portfolio's volatility, and what is the floor?

<details class="solution" markdown>
<summary>Answer</summary>

Variance = 0.0625 x (1/20 + (19/20) x 0.4) = 0.0625 x (0.05 + 0.38) = 0.0625 x 0.43 = 0.026875. Volatility = 16.39%. The floor is 25 x sqrt(0.4) = 15.81%.

</details>

4\. Why do portfolio managers stress-test with a higher correlation than the average of calm years?

<details class="solution" markdown>
<summary>Answer</summary>

Because correlation tends to rise in bear markets (Longin and Solnik, 2001), so the average understates the correlation in the years that matter most.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Pick two funds you hold. Download 3 years of monthly returns for each from the issuer or your broker, and compute the correlation in a spreadsheet or the In code box. |
| 3 | Compute the volatility of a 50 / 50 mix of the two, at your computed correlation and at 0.9. |
| 2 | Write one line on whether you hold one exposure under two names. |

</div>

## Key terms

- **Correlation**: a number from -1 to 1 that says how closely two returns move together.
- **Diversification**: holding assets that do not move together, to lower risk.
- **Systematic risk (market risk)**: the risk all stocks share, which diversification cannot remove.
- **Idiosyncratic risk**: the risk specific to one company, which diversification removes.

Next: [Rebalancing](07-rebalancing.md)
