# A DCF step by step

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">VAL</span>

After this lesson you can build a five-year discounted cash flow (DCF) valuation, with a terminal value by Gordon growth and by an exit multiple, and turn it into a value per share and a sensitivity table.

Before this: [Discount rates, CAPM and WACC](04-discount-rates-capm-and-wacc.md), [Free cash flow](03-free-cash-flow.md), [Present value, NPV and bond prices](https://faiyaz-svg.github.io/MathFromTheGroundUp/07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices/) and [Annuities and geometric series](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/03-time-value-of-money/02-annuities-and-geometric-series/) in the math book. You need from them: present value of a cash flow, and the sum of a growing perpetuity. A calculator or the code below.

## The idea

A company is worth the cash it will hand to its funders, discounted to today. A **discounted cash flow** (DCF) valuation forecasts that cash for some years, adds a value forever everything after the forecast, and discounts it all at the WACC. The result is an enterprise value, which you turn into a value per share.

Treat the output as the answer to "what is the price if my assumptions are true", not as a measurement. Every step below is an assumption you can change.

## How it works

1. Forecast revenue, EBIT margin, D&A, capex and working capital for 5 years, and compute unlevered FCF (lesson 3) for each.
2. Choose the discount rate (lesson 4) and a terminal value method.
3. Compute the terminal value at the end of year 5.
4. Discount every cash flow and the terminal value to today, and add them: enterprise value.
5. Subtract debt and add cash to get equity value, and divide by diluted shares.

### Step 1: the forecast

Northwind's assumptions (made up for teaching). Revenue grows 15%, 13%, 11%, 9% and 7%, from US$1,150 million in FY2025. EBIT margin rises from 20.4% in FY2025 to 21.5%, 22.5%, 23%, 23.5% and 24%. D&A is 3% of revenue. Capex falls from 6.5% to 4.2% of revenue as the build-out slows. Working capital grows by 17% of each year's revenue increase (FY2025: 25 / 150). The tax rate is 25%. Cash flows arrive at each year end, and we value the company at the end of FY2025.

| US$ millions | FY2026 | FY2027 | FY2028 | FY2029 | FY2030 |
|---|---|---|---|---|---|
| Revenue | 1,322.5 | 1,494.4 | 1,658.8 | 1,808.1 | 1,934.7 |
| EBIT | 284.3 | 336.2 | 381.5 | 424.9 | 464.3 |
| NOPAT (EBIT x 0.75) | 213.3 | 252.2 | 286.1 | 318.7 | 348.2 |
| + D&A | 39.7 | 44.8 | 49.8 | 54.2 | 58.0 |
| - Capex | 86.0 | 86.7 | 86.3 | 85.0 | 81.3 |
| - Change in NWC | 29.3 | 29.2 | 27.9 | 25.4 | 21.5 |
| Unlevered FCF | 137.6 | 181.1 | 221.7 | 262.6 | 303.5 |

### Steps 2 to 4: terminal value and discounting

A DCF cannot forecast forever, so the **terminal value** (TV) stands for all cash flows after year 5. There are two methods.

**Gordon growth** assumes the cash flow grows at a steady rate \(g\) forever:

\[ \text{TV}_5 = \frac{\text{UFCF}_5 \times (1 + g)}{r - g} \]

- \(\text{UFCF}_5\) is the year 5 unlevered FCF, US$303.5 million.
- \(g\) is the terminal growth rate, 3.0%. It should not exceed the long-run growth of the economy, and it must stay below \(r\), the WACC (9.1%).

**Exit multiple** assumes the business sells at the end of year 5 for a multiple of that year's EBITDA: \(\text{TV}_5 = \text{EBITDA}_5 \times \text{multiple}\). Use a multiple from mature peers, not today's rich one (lesson 7).

Every cash flow is discounted by \(1/(1+r)^n\), where \(n\) is the year.

<div class="example" markdown>

### Worked example: the base case DCF

Discount factors at 9.1%: 0.9166, 0.8401, 0.7701, 0.7058, 0.6470.

1. Present value of the forecast cash flows: 126.2 + 152.2 + 170.7 + 185.3 + 196.4 = US$830.7 million (before rounding the table entries).
2. TV = 303.5 x 1.03 / (0.091 - 0.03) = US$5,124.8 million. Its present value = 5,124.8 x 0.6470 = US$3,315.5 million.
3. Enterprise value = 830.7 + 3,315.5 = US$4,146.3 million.
4. Equity value = 4,146.3 - 275 + 130 = US$4,001.3 million.
5. Value per share = 4,001.3 / 101.5 = US$39.42. (The 101.5 million counts options at the US$50 price. At US$39.42 fewer option shares would count, about 101.1 million, a change of under 1%, so we keep 101.5.)

The base case value is 21% below the US$50.00 price (39.42 / 50.00 = 0.788).

</div>

<div class="example" markdown>

### Worked example: the exit multiple method

Year 5 EBITDA = 464.3 + 58.0 = US$522.4 million. At 13 times: TV = US$6,790.7 million. Its present value = 6,790.7 x 0.6470 = US$4,393.3 million.

Enterprise value = 830.7 + 4,393.3 = US$5,224.0 million. Equity = 5,224.0 - 145 = US$5,079.0 million. Per share = 5,079.0 / 101.5 = US$50.04.

</div>

The two methods disagree by US$10.62 a share, and the reason is informative. The Gordon value equals 5,124.8 / 522.4 = 9.8 times year 5 EBITDA. A 13 times exit multiple, put back into the Gordon formula, implies growth forever of 4.4% (solve TV for \(g\)). Today's 19.3 times is the market's price for fast growth, and 13 times in year 5 still assumes a premium. Cross-check each method with the other.

### Terminal value is most of the value

In the Gordon case, the present value of the terminal value is 3,315.5 / 4,146.3 = 80% of enterprise value. With the exit multiple it is 84%.

![Stacked bars of present value. Gordon growth at 9.1% and 3.0%: 831 from years 1 to 5 and a terminal value that is 80% of an enterprise value of 4,146. Exit multiple of 13 times EBITDA: 84% of 5,224. Gordon growth at 10.1% and 2.0%: 75% of 3,169](../assets/figures/10-valuation-and-research/tv-share-dark.svg#only-dark)
![Stacked bars of present value. Gordon growth at 9.1% and 3.0%: 831 from years 1 to 5 and a terminal value that is 80% of an enterprise value of 4,146. Exit multiple of 13 times EBITDA: 84% of 5,224. Gordon growth at 10.1% and 2.0%: 75% of 3,169](../assets/figures/10-valuation-and-research/tv-share-light.svg#only-light)

A DCF is mostly a statement about what happens after year 5, the part you can forecast least. That is the main weakness of the method.

### Sensitivity

Value per share (US$) for different discount rates and terminal growth rates, all else equal. The base case is the middle cell.

| WACC \ terminal growth | 2.0% | 2.5% | 3.0% | 3.5% | 4.0% |
|---|---|---|---|---|---|
| 8.1% | 40.87 | 44.08 | 47.91 | 52.58 | 58.39 |
| 8.6% | 37.47 | 40.14 | 43.29 | 47.05 | 51.63 |
| 9.1% | 34.55 | 36.80 | 39.42 | 42.51 | 46.21 |
| 9.6% | 32.01 | 33.93 | 36.15 | 38.72 | 41.75 |
| 10.1% | 29.80 | 31.45 | 33.33 | 35.50 | 38.03 |

![Heatmap of Northwind value per share for WACC from 8.1% to 10.1% and terminal growth from 2.0% to 4.0%, from US$29.80 to US$58.39, shaded red below the US$50 price and green above](../assets/figures/10-valuation-and-research/sensitivity-dark.svg#only-dark)
![Heatmap of Northwind value per share for WACC from 8.1% to 10.1% and terminal growth from 2.0% to 4.0%, from US$29.80 to US$58.39, shaded red below the US$50 price and green above](../assets/figures/10-valuation-and-research/sensitivity-light.svg#only-light)

A one point change in WACC (9.1% to 8.1%) moves the value from US$39.42 to US$47.91, a 22% rise. Only three cells reach the market price, all at a WACC of 8.6% or lower and growth of 3.5% or higher. Report a DCF as a range, not a number.

## In code

<details class="code" markdown>
<summary>In code</summary>

```python
rev0, tax, da_pct, nwc_pct = 1150, 0.25, 0.03, 0.17
growth = [0.15, 0.13, 0.11, 0.09, 0.07]
margin = [0.215, 0.225, 0.23, 0.235, 0.24]
capex = [0.065, 0.058, 0.052, 0.047, 0.042]
debt, cash, shares = 275, 130, 101.5

def dcf(wacc=0.091, g=0.03, exit_multiple=None):
    rev, pv = rev0, 0.0
    for n, (gr, m, cx) in enumerate(zip(growth, margin, capex), start=1):
        new = rev * (1 + gr)
        ufcf = new * m * (1 - tax) + new * da_pct - new * cx - (new - rev) * nwc_pct
        pv += ufcf / (1 + wacc) ** n
        rev = new
    ebitda = rev * (margin[-1] + da_pct)
    tv = ebitda * exit_multiple if exit_multiple else ufcf * (1 + g) / (wacc - g)
    ev = pv + tv / (1 + wacc) ** 5
    return (ev - debt + cash) / shares

print(f"Gordon {dcf():.2f}  exit multiple {dcf(exit_multiple=13):.2f}")
for w in (0.081, 0.091, 0.101):
    print(w, [round(dcf(w, g), 2) for g in (0.02, 0.03, 0.04)])
```

</details>

## Common mistakes

- Setting the terminal growth rate near or above the discount rate. The formula explodes, and no company outgrows the economy forever.
- Taking the exit multiple from today's market without a haircut, which copies the market's price into the answer.
- Forgetting to subtract debt (and add cash) between enterprise value and equity value.

## Try it

1\. A company's year 5 UFCF is US$100 million, WACC is 10% and terminal growth is 3%. Find the terminal value at year 5 and its present value.

<details class="solution" markdown>
<summary>Answer</summary>

TV = 100 x 1.03 / (0.10 - 0.03) = US$1,471.4 million. PV = 1,471.4 / 1.10^5 = 1,471.4 / 1.6105 = US$913.6 million.

</details>

2\. The present value of years 1 to 5 is US$300 million, and the PV of the terminal value is US$913.6 million. Debt is US$200 million, cash is US$50 million, and there are 100 million diluted shares. Find the value per share.

<details class="solution" markdown>
<summary>Answer</summary>

EV = 300 + 913.6 = 1,213.6. Equity = 1,213.6 - 200 + 50 = 1,063.6. Per share = US$10.64. The terminal value is 913.6 / 1,213.6 = 75% of EV.

</details>

3\. Using Northwind's table, what is the value per share at a 9.6% WACC and 2.5% growth, and how far is it below the price?

<details class="solution" markdown>
<summary>Answer</summary>

US$33.93. It is 50.00 - 33.93 = US$16.07 below the price, or 32%.

</details>

4\. Year 5 EBITDA is US$200 million and the exit multiple is 10. What is the terminal value, and what is its PV at 8% (5 years)?

<details class="solution" markdown>
<summary>Answer</summary>

TV = US$2,000 million. PV = 2,000 / 1.08^5 = 2,000 / 1.4693 = US$1,361.2 million.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Run the code above. Change the year 5 capex to 6% of revenue and write the new value. |
| 3 | Find the cell in the sensitivity table closest to the price and write the two assumptions it needs. |
| 2 | Write the terminal value share for your own change. |

</div>

## Key terms

- **Discounted cash flow (DCF)**: a valuation that discounts forecast cash flows to present value.
- **Terminal value (TV)**: the value at the end of the forecast of all later cash flows.
- **Gordon growth**: terminal value of a cash flow that grows at a steady rate forever.
- **Exit multiple**: a terminal value set as a multiple of final-year EBITDA.
- **Sensitivity table**: the value for a grid of two assumptions.

Next: [Reverse DCF and market expectations](06-reverse-dcf-and-expectations.md)
