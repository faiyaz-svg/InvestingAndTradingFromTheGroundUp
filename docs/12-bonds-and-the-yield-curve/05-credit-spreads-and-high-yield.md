# Credit spreads and high yield

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">BOND</span>

After this lesson you can read a credit rating, compute a credit spread, split a spread into expected loss and a risk premium, and estimate what a spread widening does to a bond's price.

Before this: [Treasuries and TIPS](02-treasuries-and-tips.md), [Duration and convexity](04-duration-and-convexity.md). You need: a calculator.

## The idea

A Treasury is the base case: the US government pays on time. A company that borrows by selling bonds can fail to pay. That risk is **credit risk**, and the bond has to pay more to make up for it. Bond B is a made-up 10-year bond from a strong company, yielding 5.00%. A 10-year Treasury yields 4.00% (also made up for this lesson). The difference is 1.00 percentage point, or 100 basis points. That difference is the **credit spread**:

\[ \text{Spread} = y_{corp} - y_{Treasury} \]

- \(y_{corp}\) is the corporate bond's yield to maturity.
- \(y_{Treasury}\) is the yield of a Treasury with about the same maturity.
- The spread is in percentage points, or in basis points (1 percentage point is 100 basis points).

A weaker borrower pays a wider spread. Bond C, from a weak company, yields 8.00% against the same 4.00% Treasury, a spread of 400 basis points.

### Ratings

Credit rating agencies grade a borrower's ability to repay, using letters. S&P Global Ratings and Moody's are the two best known ([S&P, understanding credit ratings](https://www.spglobal.com/ratings/en/credit-ratings/about/understanding-credit-ratings)). The line that matters sits between BBB- (S&P) or Baa3 (Moody's), and the grade below it.

| S&P | Moody's | Group | Meaning |
|---|---|---|---|
| AAA | Aaa | Investment grade | Highest rating |
| AA+, AA, AA- | Aa1, Aa2, Aa3 | Investment grade | Very strong |
| A+, A, A- | A1, A2, A3 | Investment grade | Strong |
| BBB+, BBB, BBB- | Baa1, Baa2, Baa3 | Investment grade | Adequate. BBB- and Baa3 are the lowest investment grade |
| BB+, BB, BB- | Ba1, Ba2, Ba3 | High yield | Speculative. BB+ and Ba1 are the highest |
| B+, B, B- | B1, B2, B3 | High yield | Weaker |
| CCC+, CCC, CCC- | Caa1, Caa2, Caa3 | High yield | Very weak |
| CC, C, D | Ca, C | High yield | Near default or in default. S&P uses D for default |

**Investment grade** bonds are rated BBB- or Baa3 and above. **High yield** bonds, also called junk bonds, are rated below that. The higher yield is the payment for the higher chance of default. Many pension funds and some bond funds can hold only investment grade bonds, so a bond that drops below the line, a **fallen angel**, can face forced selling. A rating is an agency's opinion. It lags the market, and prices often move before a downgrade.

![Yield made of a 4.00% Treasury yield, expected loss and risk premium: 5.00% for Bond B and 8.00% for Bond C](../assets/figures/12-bonds-and-the-yield-curve/credit-stack-dark.svg#only-dark)
![Yield made of a 4.00% Treasury yield, expected loss and risk premium: 5.00% for Bond B and 8.00% for Bond C](../assets/figures/12-bonds-and-the-yield-curve/credit-stack-light.svg#only-light)

The figure splits each bond's yield into the Treasury yield and the credit spread, and the spread into expected loss and a risk premium. The next section computes those two pieces. The numbers are made up.

## How it works

### Default, recovery and expected loss

A **default** is a missed payment of interest or principal that the borrower does not cure. After a default, bondholders usually get back part of what they are owed. The share of face value they recover is the **recovery rate**. The share lost is the loss given default, one minus the recovery rate. If a US$1,000 bond defaults and recovers 40%, holders get US$400 and lose US$600.

The yield to maturity is what the bond pays if nothing goes wrong. Part of the spread covers the yearly loss you expect from defaults, called the **expected loss**:

\[ EL = p \times (1 - R) \]

- \(p\) is the probability of default in a year, as a fraction.
- \(R\) is the recovery rate, as a fraction of face value.
- \(EL\) is the expected yearly loss, as a fraction of face value.

<div class="example" markdown>

### Worked example: what the spread pays for

Bond C has a 400 basis point spread. Suppose, with made-up inputs, its yearly default probability is 2.0% and its recovery rate is 40%.

1. Expected loss: 0.02 x (1 - 0.40) = 0.012, so 1.20% a year.
2. Risk premium: the rest of the spread, 4.00 - 1.20 = 2.80 percentage points. This pays you for bearing the risk that defaults come in worse than expected, and for being hard to sell in a crisis.
3. Expected return, roughly: 8.00 - 1.20 = 6.80%, compared with 4.00% on the Treasury.

Bond B has a 100 basis point spread. With a default probability of 0.2% and the same 40% recovery, expected loss is 0.002 x 0.60 = 0.12%, and the risk premium is 0.88 percentage points.

The yield is a promise, and the expected return is lower. A high yield is a sign of risk as much as reward. These inputs are for the example only. The rating agencies publish default studies, and you should look up real rates before using any.

</div>

### Spreads move

Spreads change every day. They widen when investors expect more defaults or want less risk, and narrow when they expect fewer. The change in price from a change in spread follows the same duration rule as a change in Treasury yield:

\[ \frac{\Delta P}{P} \approx -D_{mod} \times \Delta s \]

- \(D_{mod}\) is the bond's modified duration, in years.
- \(\Delta s\) is the change in the spread, as a fraction (50 basis points is 0.005).

If Bond B has a modified duration of 7 and its spread widens by 50 basis points while Treasury yields do not change, its price falls about 7 x 0.005 = 3.5%. A corporate bondholder takes two risks: the Treasury yield and the spread. They can move in opposite directions. In a market scare, Treasury yields can fall while spreads widen, so the two effects partly offset each other.

Part 13 shows how bond funds hold these bonds in a portfolio (How ETFs work<!-- link: ../13-etfs-portfolios-and-factors/01-how-etfs-work.md -->).

## Common mistakes

- Comparing yields of bonds with different credit quality and maturity. Compare the spread to a Treasury with a similar maturity.
- Treating the yield as the return. The yield assumes no default, so subtract an expected loss before you compare it with a safer bond.
- Trusting a rating as a price signal. Ratings follow events, and spreads often widen months before a downgrade.

## Try it

1\. A 5-year corporate bond yields 6.30%. The 5-year Treasury yields 4.10%. What is the credit spread in basis points?

<details class="solution" markdown>
<summary>Answer</summary>

6.30 - 4.10 = 2.20 percentage points, which is 220 basis points.

</details>

2\. A bond has a yearly default probability of 1.5% and a recovery rate of 35%. Find the expected loss.

<details class="solution" markdown>
<summary>Answer</summary>

0.015 x (1 - 0.35) = 0.00975, which is 0.975% a year.

</details>

3\. The bond in exercise 2 has a spread of 280 basis points. How much is the risk premium?

<details class="solution" markdown>
<summary>Answer</summary>

2.80 - 0.975 = 1.825 percentage points.

</details>

4\. A bond has a modified duration of 5.5, and its spread widens by 120 basis points while Treasury yields stay flat. What is the approximate price change? What if Treasury yields also fall by 40 basis points?

<details class="solution" markdown>
<summary>Answer</summary>

Spread only: -5.5 x 0.012 = -6.6%. Adding the Treasury move: the total yield change is +120 - 40 = +80 basis points, so -5.5 x 0.008 = -4.4%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Look up the S&P rating of one company you know that has bonds outstanding (its investor relations page lists them). Write the rating, and whether it is investment grade. |
| 5 | Open FRED and search for the series BAMLH0A0HYM2 (the ICE BofA US High Yield Index option-adjusted spread). Write the latest value and its level a year ago. |

</div>

## Key terms

- **Credit risk**: the risk that a borrower does not pay as promised.
- **Credit spread**: a corporate bond's yield minus the yield of a Treasury of similar maturity.
- **Credit rating**: an agency's letter grade for a borrower's ability to repay.
- **Investment grade**: rated BBB- (S&P) or Baa3 (Moody's) or higher.
- **High yield**: rated below investment grade, also called junk.
- **Fallen angel**: a bond downgraded from investment grade to high yield.
- **Default**: a missed payment of interest or principal.
- **Recovery rate**: the share of face value bondholders get back after a default.
- **Expected loss**: the default probability times one minus the recovery rate.

Next: [Bond ETFs, and rates against stocks](06-bond-etfs-and-rates-vs-stocks.md)
