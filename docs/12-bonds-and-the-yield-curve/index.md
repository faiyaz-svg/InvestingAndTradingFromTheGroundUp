# Part 12: Bonds and the yield curve

Bond prices and yields, Treasuries, the yield curve, duration, credit and bond ETFs.

Before this part: Part 11. The math book's lesson on present value, NPV and bond prices helps.

<!-- lessons:start -->
## Lessons

1. [Bond prices and yields](01-bond-prices-and-yields.md) (idea)
2. [Treasuries and TIPS](02-treasuries-and-tips.md) (idea)
3. [The yield curve](03-the-yield-curve.md) (data)
4. [Duration and convexity](04-duration-and-convexity.md) (idea)
5. [Credit spreads and high yield](05-credit-spreads-and-high-yield.md) (idea)
6. [Bond ETFs, and rates against stocks](06-bond-etfs-and-rates-vs-stocks.md) (idea, review)

<!-- lessons:end -->

## Cheat sheet

### Formulas

| Item | Formula | Notes |
|---|---|---|
| Bond price (semiannual) | \( P = \sum_{k=1}^{N} \frac{C}{(1+i)^k} + \frac{F}{(1+i)^N} \) | \(C\) = coupon rate x \(F\) / 2, \(i\) = yield / 2, \(N\) = 2 x years |
| Current yield | annual coupon / price | Ignores the gain or loss at maturity |
| Yield to maturity | the \(y\) that makes the price formula equal the market price | Solve by trial or bisection |
| Accrued interest | \( C \times d / D \) | Dirty price = clean price + accrued |
| Bill price | \( P = F (1 - d\,t/360) \) | \(d\) is the discount rate |
| Bill bond-equivalent yield | \( 365\,d / (360 - d\,t) \) | Gain / price, 365-day year |
| TIPS principal | \( F \times \) index ratio | Maturity pays the larger of adjusted and original principal |
| Breakeven inflation | \( (1 + y_{nom}) / (1 + y_{real}) - 1 \) | About nominal yield minus real yield |
| 2s10s and 3m10y | \( y_{10Y} - y_{2Y} \), \( y_{10Y} - y_{3M} \) | Negative means inverted |
| Recession probability (Estrella and Trubin) | \( \Phi(-0.6045 - 0.7374\,S) \) | \(S\) = 10Y minus 3M, in points. 12 months ahead |
| Sahm gap | 3-month average unemployment minus its 12-month low | Signals at 0.50 points or more |
| Modified duration | \( D_{mac} / (1 + y/2) \) | Years |
| Price change | \( \Delta P / P \approx -D_{mod}\,\Delta y + \tfrac12 C (\Delta y)^2 \) | \(\Delta y\) as a fraction |
| DV01 | \( D_{mod} \times P \times 0.0001 \) | US$ per basis point |
| Credit spread | corporate yield minus Treasury yield | Basis points |
| Expected loss | \( p \times (1 - R) \) | Default probability and recovery rate |
| Earnings yield | \( E / P = 1 / (P/E) \) | Compare with bond yields with care |

### Rules to keep

- Price and yield move in opposite directions. Longer maturity and lower coupon mean higher duration.
- Bill discount rates are not yields. Convert before comparing.
- An inversion is a 12-month-ahead probability signal. Use monthly averages, not one day, and name the spread.
- Investment grade is BBB- (S&P) or Baa3 (Moody's) and above.
- A bond ETF has no maturity. Estimate its year with yield minus duration times the change in yield.

### Checklist for reading a bond or bond fund

1. Yield to maturity, or the 30-day SEC yield for a fund.
2. Duration, and the price change for a 1 point rise in yield.
3. Credit rating and spread to a Treasury of similar maturity.
4. Fees (expense ratio) and, for a single bond, the accrued interest.

