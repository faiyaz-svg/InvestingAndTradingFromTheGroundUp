# Reverse DCF and market expectations

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">VAL</span>

After this lesson you can take a market price and solve for the growth, or the discount rate, that it implies, then judge whether that is believable.

Before this: [A DCF step by step](05-dcf-step-by-step.md). You need: the code in lesson 5, or a spreadsheet.

## The idea

A normal DCF starts with your assumptions and ends with a value. You then compare it with the price and ask whether the stock is cheap. The weakness is that your answer is only as good as your forecast, and you tend to forecast what you already believe.

A **reverse DCF** turns the question around. Fix everything except one assumption, set the value equal to the market price, and solve for that assumption. The result is what the market is expecting, if the rest of your model is right. You then ask a plainer question: is that expectation reasonable?

## How it works

1. Take the base-case model from lesson 5 (margins, capex, working capital, WACC, terminal growth).
2. Choose one unknown: revenue growth, the discount rate or the terminal growth rate.
3. Find the value of the unknown that makes the DCF value per share equal the price. There is no closed form, so use trial and error or a root finder (the code below halves the search interval 80 times).
4. Compare the answer with the company's history, its peers and the economy.

The value moves one way when the unknown rises, so a search always finds one answer.

<div class="example" markdown>

### Worked example: what the price implies

The base case gives US$39.42 a share. The price is US$50.00. Three ways to close the gap, one at a time:

1. Growth. Keep the base margins, capex, WACC (9.1%) and terminal growth (3.0%), and give revenue one constant growth rate for FY2026 to FY2030. The rate that gives US$50.00 is 19.4% a year. FY2030 revenue would be 1,150 x 1.194^5 = US$2,794 million, against US$1,935 million in the base case. The base case grows 11.0% a year on average.
2. Discount rate. Keep the base forecast and solve for the rate that gives US$50.00: 7.9%, against 9.1% for the WACC.
3. Terminal growth. Keep the base forecast and WACC, and solve for \(g\): 4.4%, against 3.0%.

Each one says the same thing in a different unit: the price needs either much faster growth, a lower required return or a higher long-run growth rate than the base case.

</div>

The figure shows the second answer. The curve is value per share at each discount rate. It crosses the price line at 7.9%.

![Northwind DCF value per share against the discount rate, falling from about US$72 at 6.5% to about US$23 at 13%; the market price of US$50.00 crosses the curve at an implied rate of 7.9% and the base case at 9.1% gives US$39.42](../assets/figures/10-valuation-and-research/value-vs-rate-dark.svg#only-dark)
![Northwind DCF value per share against the discount rate, falling from about US$72 at 6.5% to about US$23 at 13%; the market price of US$50.00 crosses the curve at an implied rate of 7.9% and the base case at 9.1% gives US$39.42](../assets/figures/10-valuation-and-research/value-vs-rate-light.svg#only-light)

### A quick reverse DCF on the whole business

A shortcut uses the Gordon formula on today's numbers. If enterprise value is a growing perpetuity of unlevered FCF:

\[ \text{EV} = \frac{\text{UFCF} \times (1 + g)}{r - g} \quad\Rightarrow\quad g = \frac{r \times \text{EV} - \text{UFCF}}{\text{EV} + \text{UFCF}} \]

- EV is US$5,220 million (lesson 2), UFCF is US$106.25 million (lesson 3) and \(r\) is 9.1%.
- \(g\) is the growth rate, forever, that the price needs.

g = (0.091 x 5,220 - 106.25) / (5,220 + 106.25) = 368.8 / 5,326.3 = 6.9%. No company grows 6.9% forever (it would outgrow the economy), so the price needs a period of fast growth first, which is what the full reverse DCF measured. The shortcut is a quick test, not a forecast.

### Reading the answer

The point is not to find the market wrong. Ask:

- Has the company ever grown that fast for that long? Northwind grew revenue 15% in FY2025 from a smaller base, and growth rates fall as companies get bigger.
- What would the margin need to be? Solve again with margin as the unknown.
- Does the peer group, or the company's own history, support it?

If the implied growth is below what the company has done and the industry supports, the market is asking for little. If it is far above, you need a reason to believe in the extra growth, and that reason is your thesis (lesson 9). A reverse DCF also keeps you from falling in love with your own forecast: it states the claim the price is making, and you check it.

Reverse DCF has the same limits as DCF. A different WACC or margin changes the implied growth. The market price also holds the views of many investors with different horizons and discount rates, so there is no single "market expectation", only a price that is consistent with some set of assumptions.

## In code

<details class="code" markdown>
<summary>In code</summary>

```python
rev0, tax, da_pct, nwc_pct = 1150, 0.25, 0.03, 0.17
margin = [0.215, 0.225, 0.23, 0.235, 0.24]
capex = [0.065, 0.058, 0.052, 0.047, 0.042]
debt, cash, shares, price = 275, 130, 101.5, 50.0

def value(growth, wacc=0.091, g=0.03):
    rev, pv = rev0, 0.0
    for n, (gr, m, cx) in enumerate(zip(growth, margin, capex), start=1):
        new = rev * (1 + gr)
        ufcf = new * m * (1 - tax) + new * da_pct - new * cx - (new - rev) * nwc_pct
        pv += ufcf / (1 + wacc) ** n
        rev = new
    ev = pv + ufcf * (1 + g) / (wacc - g) / (1 + wacc) ** 5
    return (ev - debt + cash) / shares

lo, hi = 0.0, 0.6
for _ in range(80):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if value([mid] * 5) < price else (lo, mid)
print(f"implied growth {mid:.1%}, revenue in FY2030 {rev0 * (1 + mid) ** 5:,.0f}")
```

</details>

## Common mistakes

- Solving for one assumption while the others are unrealistic. The answer inherits their errors.
- Treating the implied number as a forecast. It is a claim to test.
- Stopping at the number. Compare it with history and peers, or it teaches nothing.

## Try it

1\. A stock's base case DCF value is US$30 and its price is US$40. With all else equal, does the price imply faster or slower growth than your base case?

<details class="solution" markdown>
<summary>Answer</summary>

Faster (or a lower discount rate). A higher price needs more cash flow or a lower rate, and growth is the usual lever.

</details>

2\. Using the Gordon shortcut, a company has EV of US$2,000 million, UFCF of US$80 million and a WACC of 8%. Find the implied perpetual growth.

<details class="solution" markdown>
<summary>Answer</summary>

g = (0.08 x 2,000 - 80) / (2,000 + 80) = 80 / 2,080 = 3.85%.

</details>

3\. Northwind's implied growth is 19.4% a year for five years. How many times larger is FY2030 revenue than FY2025's US$1,150 million?

<details class="solution" markdown>
<summary>Answer</summary>

1.194^5 = 2.43, so revenue would be 2.4 times larger, US$2,794 million.

</details>

4\. At a discount rate of 7.9% Northwind's DCF equals the price, and at 9.1% it is US$39.42. If the true required return is 9.1%, what are you assuming when you buy at US$50.00?

<details class="solution" markdown>
<summary>Answer</summary>

That cash flows turn out better than the base case, enough to close a US$10.58 (21%) gap between price and value. At 9.1% you are betting on your forecast beating the base case, not on the discount rate.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 6 | Run the code above, then change the target price to US$40 and US$60. Write the implied growth for each. |
| 4 | Compare each with Northwind's FY2025 growth (15%) and say which you find believable, and why. |

</div>

## Key terms

- **Reverse DCF**: solving a DCF for the assumption that makes the value equal the market price.
- **Implied growth**: the growth rate a price needs, given the other assumptions.
- **Implied discount rate**: the rate at which the DCF value equals the price.
- **Market expectations**: the cash flows and risks consistent with the current price.

Next: [Comparables and industry KPIs](07-comparables-and-industry-kpis.md)
