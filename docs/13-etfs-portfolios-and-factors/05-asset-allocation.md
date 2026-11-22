# Asset allocation

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">ETF</span>

After this lesson you can choose a stock and bond mix by testing what each mix could lose in a bad year, in dollars, and split it into funds.

Before this: [Index funds, fees and tracking](02-index-funds-fees-and-tracking.md), [Account types for trading](../02-accounts-currency-and-taxes/01-account-types-for-trading.md). The math book's [Investing returns and risk](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/06-investing-and-retirement/01-investing-returns-and-risk/) covers average returns and volatility. You need: a calculator.

## The idea

You have C$50,000 for the long term. Before you pick a single fund, you choose how much goes in each broad kind of asset: stocks, bonds and cash. That choice is your **asset allocation**. A stock fund holds shares of companies. A bond fund holds loans to governments and companies that pay interest (part 12 starts with [Bond prices and yields](../12-bonds-and-the-yield-curve/01-bond-prices-and-yields.md)). Cash is a savings account or a money market fund.

The allocation drives most of what your portfolio does from year to year. Stocks have higher expected returns and larger swings, and bonds the reverse. Ibbotson and Kaplan studied balanced funds and found that the allocation policy explained about 90% of the variation in a typical fund's returns over time, about 40% of the differences between funds, and about 100% of the level of return ([Financial Analysts Journal, 2000](https://doi.org/10.2469/faj.v56.n1.2327)). Read the three numbers as three answers to three different questions. They say that what you hold in each asset class matters more than which individual stocks you pick, not that you cannot do better.

## How it works

A method in five steps.

1. Write the goal and the date you need the money. Money for a home in 3 years and money for retirement in 30 years need different mixes.
2. Find your **risk capacity**: how large a loss you could take without changing your plans. A steady income and a long horizon raise it.
3. Find your **risk tolerance**: how large a loss you could watch without selling in a panic. Write it as a dollar loss on your actual account, not as "moderate".
4. Test candidate mixes. For each, compute the expected return and the loss in a stress year (below), and keep the most stock-heavy mix whose stress loss you could sit through.
5. Split each part into funds, and write the target weights down.

For the test in step 4, the portfolio's expected return is the weighted average of the parts:

\[ E[R_p] = w_s E[R_s] + w_b E[R_b] \]

- \(w_s\) and \(w_b\) are the weights in stocks and bonds, as fractions that add to 1.
- \(E[R_s]\) and \(E[R_b]\) are the expected yearly returns, as fractions. These are assumptions, not forecasts.

The stress loss uses the same weights on a bad year, \(w_s r_s + w_b r_b\), where \(r_s\) and \(r_b\) are the made-up stress returns.

<div class="example" markdown>

### Worked example: three mixes for one account

Assume stocks return 7% a year on average and bonds 3% (made-up inputs, and the bond lessons say why they are not fixed). The stress year is stocks -40% and bonds +5%.

| Mix (stocks / bonds) | Expected return | Stress-year return | Stress-year loss on C$50,000 |
|---|---|---|---|
| 80 / 20 | 0.8 x 7 + 0.2 x 3 = 6.2% | 0.8 x (-40) + 0.2 x 5 = -31% | C$15,500 |
| 60 / 40 | 0.6 x 7 + 0.4 x 3 = 5.4% | 0.6 x (-40) + 0.4 x 5 = -22% | C$11,000 |
| 40 / 60 | 0.4 x 7 + 0.6 x 3 = 4.6% | 0.4 x (-40) + 0.6 x 5 = -13% | C$6,500 |

If a C$15,500 drop would make you sell, the 80 / 20 mix is not yours, whatever its expected return. Moving from 60 / 40 to 80 / 20 adds 0.8 percentage points of expected return and 9 points of stress loss.

</div>

### Splitting the mix into funds

A 60 / 40 mix still leaves choices. A common split of the stock part is by region: your home market, the US and the rest of the world. Canada is a small part of the global stock market and its index is concentrated in a few sectors, so a portfolio of only Canadian stocks is less diversified than it looks. A market-cap split follows what the world's markets are worth; a tilt toward home is a choice, and lesson 10 comes back to it. The bond part can split into government and corporate bonds and by maturity, which part 12 covers in [Duration and convexity](../12-bonds-and-the-yield-curve/04-duration-and-convexity.md).

Rules of thumb, such as "hold your age in bonds", are starting points. They have no evidence behind a particular number. Use the stress test instead, and revisit the mix when your goal, date or income changes.

<div class="canada" markdown>

### For Canadians

An all-in-one asset allocation ETF (lesson 3) packages a mix such as 60 / 40 in one ticker, and a registered account (TFSA, RRSP, FHSA) holds it like any other fund. Your allocation is across all your accounts together, not per account, so work out the total mix first and then place funds in accounts (lesson 10).

</div>

## In code

A small function to run the test for any mix.

<details class="code" markdown>
<summary>In code</summary>

```python
def mix(stock_w, e_s=0.07, e_b=0.03, r_s=-0.40, r_b=0.05, amount=50_000):
    bond_w = 1 - stock_w
    expected = stock_w * e_s + bond_w * e_b
    stress = stock_w * r_s + bond_w * r_b
    return round(100 * expected, 1), round(100 * stress, 1), round(-amount * stress)

for w in (0.8, 0.6, 0.4):
    print(w, mix(w))
```

</details>

## Common mistakes

- Choosing a mix from past returns alone. Pick it from the loss you can bear, then check the return.
- Counting each account separately. Your mix is the sum of all accounts, including a workplace plan.
- Treating the expected returns as promises. The inputs are assumptions, and a different pair changes every row.

## Try it

1\. Assume stocks return 7% and bonds 3%. What is the expected return of a 70 / 30 mix?

<details class="solution" markdown>
<summary>Answer</summary>

0.7 x 7 + 0.3 x 3 = 4.9 + 0.9 = 5.8%.

</details>

2\. In the stress year (stocks -40%, bonds +5%), what does the 70 / 30 mix return, and what is the loss on C$80,000?

<details class="solution" markdown>
<summary>Answer</summary>

0.7 x (-40) + 0.3 x 5 = -28 + 1.5 = -26.5%. Loss = 0.265 x 80,000 = C$21,200.

</details>

3\. You could tolerate at most a C$9,000 loss in the stress year on C$50,000. Which of the three mixes in the worked example fits?

<details class="solution" markdown>
<summary>Answer</summary>

Only 40 / 60, with a stress loss of C$6,500. The 60 / 40 mix loses C$11,000, which is over C$9,000.

</details>

4\. Why does the stress test use dollars on your actual account?

<details class="solution" markdown>
<summary>Answer</summary>

People judge a loss by what it takes from their account, not by a percentage in a table. A -22% loss is a number until it is C$11,000 that you needed.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Add the value of every account you hold, at every broker, and write your current stock, bond and cash percentages. |
| 4 | Run the stress test on your actual mix with the table's inputs. Write the dollar loss. |
| 2 | Write the largest dollar loss you could sit through without selling. Compare it with the stress loss. |

</div>

## Key terms

- **Asset allocation**: the split of a portfolio among broad asset classes such as stocks, bonds and cash.
- **Risk capacity**: the loss you could take without changing your plans.
- **Risk tolerance**: the loss you could watch without selling in a panic.
- **Stress year**: a made-up bad year used to test a portfolio.

Next: [Diversification and correlation](06-diversification-and-correlation.md)
