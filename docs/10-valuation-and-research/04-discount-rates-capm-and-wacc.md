# Discount rates, CAPM and WACC

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">VAL</span>

After this lesson you can build a discount rate for a company: the cost of equity from CAPM, the cost of debt, and the weighted average of the two (WACC).

Before this: [Free cash flow](03-free-cash-flow.md), [Present and future value](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/03-time-value-of-money/01-present-and-future-value/) in the math book. You need from the math book: US$1 received in \(n\) years is worth \(1/(1+r)^n\) today.

## The idea

A promise of US$100 in a year is worth less than US$100 today, and a riskier promise is worth even less. The **discount rate** is the yearly rate you use to turn future cash flows into today's value. It has two parts: what you could earn with no risk, and a payment for taking the risk.

Pick the rate too low and every stock looks cheap. It is the most important single input in a DCF (lesson 5), and nobody can measure it exactly. This lesson builds one from standard pieces and shows how much it moves.

## How it works

### Cost of equity: CAPM

The **cost of equity** is the return shareholders require for holding the stock. The **capital asset pricing model** (CAPM) writes it as:

\[ k_e = r_f + \beta \times \text{ERP} \]

- \(k_e\) is the cost of equity, in percent per year.
- \(r_f\) is the risk-free rate: what a safe investment pays. In US$ valuation, use the 10-year Treasury yield, published daily on [Treasury's interest rate page](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202611). It was 4.92% on November 20, 2026 (as of 2026). Treasuries are explained in Treasuries and TIPS<!-- link: ../12-bonds-and-the-yield-curve/02-treasuries-and-tips.md -->.
- \(\beta\) (beta) measures how much the stock has moved with the market. It is the slope from regressing the stock's returns on the market's returns, often 5 years of monthly returns against the S&P 500. A beta of 1.4 means the stock tended to move 1.4% for each 1% market move. Data sites publish betas, and different sites give different values because the window and the index differ.
- ERP is the **equity risk premium**: the extra return investors expect from the stock market over the risk-free rate. It cannot be observed. It is an assumption. Aswath Damodaran (NYU Stern) publishes his implied estimates by year back to 1960, computed two ways, on [his data page](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/implpr.html). Other sources give other numbers. This book uses 4.5% for the example and says so wherever it matters.

The idea behind CAPM is that only risk you cannot diversify away earns a premium (Modern portfolio theory<!-- link: ../13-etfs-portfolios-and-factors/08-modern-portfolio-theory.md -->). Its record in data is mixed, so treat it as a convention that gives a sensible number, not as a law.

Northwind (beta 1.0, assumed for the example): \(k_e\) = 4.92% + 1.0 x 4.5% = 9.42%.

![Cost of equity against beta: a straight line from the 4.92% risk-free rate at beta 0, through 8.52% at beta 0.8, 9.42% at beta 1.0 and 11.22% at beta 1.4](../assets/figures/10-valuation-and-research/capm-line-dark.svg#only-dark)
![Cost of equity against beta: a straight line from the 4.92% risk-free rate at beta 0, through 8.52% at beta 0.8, 9.42% at beta 1.0 and 11.22% at beta 1.4](../assets/figures/10-valuation-and-research/capm-line-light.svg#only-light)

### Cost of debt

The **cost of debt** is the interest rate the company pays on its borrowing, \(k_d\). Interest is tax deductible, so the cost after tax is \(k_d \times (1 - t)\). Northwind paid US$15 million of interest on average debt of (300 + 275) / 2 = US$287.5 million, so \(k_d\) = 15 / 287.5 = 5.2%. After tax: 5.2% x (1 - 0.25) = 3.9%. For a company with traded bonds, use the current yield on those bonds instead of the past average.

### WACC

\[ \text{WACC} = \frac{E}{E + D}\, k_e + \frac{D}{E + D}\, k_d (1 - t) \]

- \(E\) is the market value of equity and \(D\) the debt, both in US$ millions. Use market values, not book values.
- The fractions are the shares of funding from each source.

The **weighted average cost of capital** (WACC) is the blended rate the whole business must earn to pay its funders. It is the rate for discounting unlevered free cash flow, which belongs to lenders and shareholders together.

<div class="example" markdown>

### Worked example: a WACC from the inputs

1. \(E\) = 5,075 (diluted equity value, lesson 2). \(D\) = 275. \(E + D\) = 5,350.
2. Weights: 5,075 / 5,350 = 94.86% equity and 275 / 5,350 = 5.14% debt.
3. WACC = 0.9486 x 9.42% + 0.0514 x 3.9% = 8.936% + 0.200% = 9.14%.

The next lessons round it to 9.1%.

</div>

Northwind has little debt, so WACC is close to the cost of equity. Debt is cheaper than equity, so a company that borrows more lowers its WACC on paper, but it also raises the risk of the equity (and its beta), so the gain is smaller than it looks.

### Using the rate

Three cautions. The weights should reflect the company's long-run mix of funding, not a one-day market cap. The rate should be in the same currency as the cash flows. And small changes in the inputs move the result: a beta of 1.4 instead of 1.0 raises \(k_e\) to 11.22% and WACC to 10.84%, which cuts the DCF value from US$39.42 to US$29.84 a share, about a quarter (lesson 5 builds that value).

<div class="canada" markdown>

### For Canadians

If you value a Canadian company in C$, use a C$ risk-free rate. The Bank of Canada publishes the Government of Canada 10-year benchmark yield on its [selected bond yields page](https://www.bankofcanada.ca/rates/interest-rates/canadian-bonds/) (3.81% on November 19, 2026, as of 2026). Mixing a US$ rate with C$ cash flows, or the reverse, misstates the value.

</div>

## In code

<details class="code" markdown>
<summary>In code</summary>

```python
rf, beta, erp, tax = 0.0492, 1.0, 0.045, 0.25
ke = rf + beta * erp
kd = 15 / ((300 + 275) / 2)           # interest / average debt
E, D = 5075, 275
wacc = E / (E + D) * ke + D / (E + D) * kd * (1 - tax)
print(f"ke {ke:.2%}  kd {kd:.1%}  WACC {wacc:.2%}")
```

</details>

## Common mistakes

- Using the coupon on old debt as the cost of debt. Use today's yield for that borrower.
- Using book value of equity in the WACC weights. Use market value.
- Quoting a WACC to two decimals as if it were exact. It is a range, and lesson 5 shows the range in value.

## Try it

1\. The 10-year Treasury yield is 4.00%, the ERP is 5.0% and a stock's beta is 1.2. Find the cost of equity.

<details class="solution" markdown>
<summary>Answer</summary>

\(k_e\) = 4.00% + 1.2 x 5.0% = 10.0%.

</details>

2\. A company pays 6.0% on its debt and its tax rate is 25%. What is the after-tax cost of debt?

<details class="solution" markdown>
<summary>Answer</summary>

6.0% x (1 - 0.25) = 4.5%.

</details>

3\. The company has equity of US$700 million (market value) and debt of US$300 million. Its \(k_e\) is 10.0% and after-tax \(k_d\) is 4.5%. Find WACC.

<details class="solution" markdown>
<summary>Answer</summary>

Weights: 70% and 30%. WACC = 0.70 x 10.0% + 0.30 x 4.5% = 7.0% + 1.35% = 8.35%.

</details>

4\. Northwind's beta is 1.4 instead of 1.0, with the same other inputs. Find \(k_e\) and WACC.

<details class="solution" markdown>
<summary>Answer</summary>

\(k_e\) = 4.92% + 1.4 x 4.5% = 11.22%. WACC = 0.9486 x 11.22% + 0.0514 x 3.9% = 10.64% + 0.20% = 10.84%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 3 | Open the Treasury page above and write today's 10-year yield with its date. |
| 3 | Look up the beta of a stock you know on two data sites. Write both and the difference. |
| 4 | Compute its cost of equity with an ERP of 4.0% and again with 5.5%. Note how much the answer moves. |

</div>

## Key terms

- **Discount rate**: the yearly rate used to turn future cash flows into present value.
- **Risk-free rate**: the return on a safe investment, taken here as the 10-year Treasury yield.
- **Beta**: how much a stock has moved for each 1% move in the market.
- **Equity risk premium (ERP)**: the extra return expected from stocks over the risk-free rate, an assumption.
- **CAPM**: cost of equity = risk-free rate + beta x ERP.
- **Cost of equity**: the return shareholders require.
- **Cost of debt**: the interest rate a company pays, after tax if used in WACC.
- **WACC**: the weighted average cost of capital, the blended rate for the whole business.

Next: [A DCF step by step](05-dcf-step-by-step.md)
