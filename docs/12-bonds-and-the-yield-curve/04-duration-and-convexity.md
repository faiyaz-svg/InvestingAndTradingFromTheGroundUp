# Duration and convexity

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">BOND</span>

After this lesson you can compute a bond's Macaulay and modified duration, estimate a price change from a yield change, correct the estimate with convexity, and state a bond's DV01.

Before this: [Bond prices and yields](01-bond-prices-and-yields.md), [The yield curve](03-the-yield-curve.md). You need: a calculator. The math book's [bond price lesson](https://faiyaz-svg.github.io/MathFromTheGroundUp/07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices/) shows that longer bonds fall more when rates rise. Here we measure by how much.

## The idea

Lesson 1 showed that Bond A, a 10-year bond with a 4% coupon, falls from US$1,000 to US$922.05 when its yield rises from 4% to 5%. A 2-year bond with the same coupon falls far less. Traders need one number that says how sensitive a bond is, so they can compare a 2-year note with a 30-year bond, or size a hedge.

That number is **duration**. It has two forms that are close to each other. The first is a time: the average wait for your money.

### Macaulay duration

The **Macaulay duration** is the weighted average time until you receive the bond's cash flows, where each cash flow is weighted by its share of the bond's price.

\[ D_{mac} = \frac{1}{P} \sum_{k=1}^{N} \frac{t_k \times CF_k}{(1+i)^k} \]

- \(P\) is the bond's price, in US$.
- \(CF_k\) is the cash flow in period \(k\): the coupon, plus face value in the last period.
- \(t_k\) is the time of that cash flow in years (period \(k\) divided by 2).
- \(i\) is the yield per period (the yearly yield divided by 2), and \(N\) is the number of periods.
- \(D_{mac}\) is in years.

<div class="example" markdown>

### Worked example: a 3-year bond

A bond has US$1,000 face value, a 4% coupon paid semiannually (US$20) and 3 years to maturity. The yield is 5%, so \(i\) = 0.025.

| Period | Time (years) | Cash flow (US$) | Present value (US$) | Weight (PV / price) | Weight x time |
|---|---|---|---|---|---|
| 1 | 0.5 | 20 | 19.51 | 0.0201 | 0.0100 |
| 2 | 1.0 | 20 | 19.04 | 0.0196 | 0.0196 |
| 3 | 1.5 | 20 | 18.57 | 0.0191 | 0.0286 |
| 4 | 2.0 | 20 | 18.12 | 0.0186 | 0.0373 |
| 5 | 2.5 | 20 | 17.68 | 0.0182 | 0.0454 |
| 6 | 3.0 | 1,020 | 879.54 | 0.9045 | 2.7134 |

The price is the sum of the present values: US$972.46. The Macaulay duration is the sum of the last column: 2.85 years. It is below the 3-year maturity because the coupons arrive earlier. A bond with no coupon has a duration equal to its maturity.

</div>

### Modified duration and the price estimate

The second form turns time into sensitivity. **Modified duration** divides by one plus the per-period yield:

\[ D_{mod} = \frac{D_{mac}}{1 + y/2}, \qquad \frac{\Delta P}{P} \approx -D_{mod} \times \Delta y \]

- \(y\) is the yearly yield as a fraction, and \(\Delta y\) is the change in yield as a fraction (1 percentage point is 0.01).
- \(\Delta P / P\) is the percentage price change as a fraction.
- The minus sign says price moves opposite to yield.

For the 3-year bond, \(D_{mod}\) = 2.854 / 1.025 = 2.78. If the yield rises 1 percentage point, the estimate is -2.78 x 0.01 = -2.78%. The actual price at a 6% yield is US$945.83, which is -2.74%. The estimate is close, and it overstates the loss a little. That small gap is convexity.

Duration grows with maturity and falls with a higher coupon. For bonds that sell at par (yield equal to the 4% coupon), the table shows the pattern. The values were computed with the formula above.

| Maturity | Modified duration (years) |
|---|---|
| 2 years | 1.90 |
| 5 years | 4.49 |
| 10 years | 8.18 |
| 30 years | 17.38 |

So a 1 percentage point rise in yield costs about 1.9% on the 2-year bond and about 17.4% on the 30-year bond.

### Convexity

Duration is the slope of the price-yield curve at one point. The curve bends, so a straight line is only right near that point. The bend is **convexity**, the curvature of price against yield:

\[ \frac{\Delta P}{P} \approx -D_{mod}\,\Delta y + \tfrac{1}{2}\, C\, (\Delta y)^2, \qquad C = \frac{1}{P} \sum_{k=1}^{N} \frac{CF_k \, k(k+1)/4}{(1+i)^{k+2}} \]

- \(C\) is the convexity, in years squared.
- \((\Delta y)^2\) is positive whatever the sign of \(\Delta y\), so the correction always adds to the price.

The figure shows Bond A. The orange line is the true price, the dashed blue line is the duration estimate drawn at a 4% yield, and the shaded gap is convexity. The true price is above the line on both sides.

![Price of a 10-year 4% coupon bond against its yield, with the duration tangent at 4% below the curve on both sides](../assets/figures/12-bonds-and-the-yield-curve/price-yield-dark.svg#only-dark)
![Price of a 10-year 4% coupon bond against its yield, with the duration tangent at 4% below the curve on both sides](../assets/figures/12-bonds-and-the-yield-curve/price-yield-light.svg#only-light)

<div class="example" markdown>

### Worked example: a 10-year bond, a 1 point move each way

Bond A (10 years, 4% coupon) at a 4% yield has price US$1,000.00, \(D_{mod}\) = 8.18 and \(C\) = 78.9.

1. Yield up 1 point: duration alone gives -8.18%. Adding the convexity term, 0.5 x 78.9 x 0.01^2 = +0.39%, gives -7.78%. Repricing gives -7.79%.
2. Yield down 1 point: duration alone gives +8.18%. With convexity, +8.57%. Repricing gives +8.58%.
3. Yield up 2 points: duration alone gives -16.35%. With convexity, -14.77%. Repricing gives -14.88%.

The bigger the move, the more duration alone is off. A bond with more convexity gains more when yields fall and loses less when they rise, which investors like. Long bonds have much more of it: the 30-year bond in the table has a convexity of 421, against 79 for Bond A.

</div>

### DV01

Traders quote risk in dollars. **DV01** is the dollar value of one basis point: the change in price when the yield moves by 0.01 percentage points.

\[ DV01 = D_{mod} \times P \times 0.0001 \]

For Bond A, per US$1,000 of face value: 8.18 x 1,000 x 0.0001 = US$0.82. For US$100,000 of face value, DV01 is US$81.76. If the yield rises 25 basis points, the position loses about 25 x 81.76 = US$2,044. Because DV01 is in dollars, you can add it across bonds and compare a bond position against a hedge.

## In code

The duration, convexity and DV01 of Bond A, and the check against repricing.

<details class="code" markdown>
<summary>In code</summary>

```python
def cash_flows(face, coupon_rate, years):
    n = int(round(2 * years))
    return [(k, face * coupon_rate / 2 + (face if k == n else 0)) for k in range(1, n + 1)]

def price(face, c, y, years):
    i = y / 2
    return sum(cf / (1 + i) ** k for k, cf in cash_flows(face, c, years))

def measures(face, c, y, years):
    i = y / 2
    p = price(face, c, y, years)
    cfs = cash_flows(face, c, years)
    d_mac = sum(k / 2 * cf / (1 + i) ** k for k, cf in cfs) / p
    conv = sum(cf * k * (k + 1) / 4 / (1 + i) ** (k + 2) for k, cf in cfs) / p
    return p, d_mac, d_mac / (1 + i), conv

p, d_mac, d_mod, conv = measures(1000, 0.04, 0.04, 10)
print(round(d_mac, 2), round(d_mod, 2), round(conv, 1))   # 8.34 8.18 78.9
print(round(d_mod * 100_000 * 0.0001, 2))                  # DV01 per US$100,000 face: 81.76
dy = 0.01
approx = -d_mod * dy + 0.5 * conv * dy**2
actual = price(1000, 0.04, 0.05, 10) / p - 1
print(round(100 * approx, 2), round(100 * actual, 2))      # -7.78 -7.79
```

</details>

## Common mistakes

- Using duration for a large move. Past about 1 or 2 percentage points, add the convexity term or reprice the bond.
- Reading duration as the maturity. Macaulay duration is in years and always below maturity for a coupon bond. Modified duration measures price sensitivity.
- Forgetting that duration changes. As yield and time move, so does duration, so a hedge needs rechecking.

## Try it

1\. A bond has a modified duration of 6.0. Yields rise 0.50 percentage points. What is the approximate price change?

<details class="solution" markdown>
<summary>Answer</summary>

-6.0 x 0.005 = -3.0%.

</details>

2\. The 3-year bond in the table has \(D_{mac}\) = 2.854 at a 5% yield. Find \(D_{mod}\) and the DV01 per US$1,000 face (price US$972.46).

<details class="solution" markdown>
<summary>Answer</summary>

\(D_{mod}\) = 2.854 / 1.025 = 2.78. DV01 = 2.78 x 972.46 x 0.0001 = US$0.27.

</details>

3\. You hold US$250,000 face value of Bond A at par. What is your DV01, and what is the approximate loss from a 30 basis point rise?

<details class="solution" markdown>
<summary>Answer</summary>

DV01 = 8.18 x 250,000 x 0.0001 = US$204.39. Loss = 30 x 204.39 = US$6,132, about 2.45% of US$250,000 (8.18 x 0.003).

</details>

4\. Two bonds have the same duration of 8. Bond X has higher convexity. Yields fall 1 point, and then rise 1 point. Which bond is better off both times?

<details class="solution" markdown>
<summary>Answer</summary>

Bond X. The duration term is the same for both. The convexity term, 0.5 x C x 0.01^2, is positive in both cases and larger for X.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 6 | Change the code to price a 5-year bond with a 3% coupon at a 4% yield. Print its duration, convexity and DV01 per US$100,000 face. |
| 4 | Estimate its price change for a 0.75 point rise with and without convexity, then reprice it to see which is closer. |

</div>

## Key terms

- **Duration**: a measure of how much a bond's price changes when yields change.
- **Macaulay duration**: the weighted average time to a bond's cash flows, in years.
- **Modified duration**: Macaulay duration divided by one plus the per-period yield. It gives the percentage price change per unit of yield change.
- **Convexity**: the curvature of the price-yield relationship, the correction to the duration estimate.
- **DV01**: the dollar change in a bond's price for a one basis point change in yield.
- **Basis point**: one hundredth of a percentage point (0.01%).

Next: [Credit spreads and high yield](05-credit-spreads-and-high-yield.md)
