# Part 6: ICT and smart money concepts, tested

Liquidity, fair value gaps, order blocks and sessions: what each idea says and what tests found.

Before this part: Part 5.

<!-- lessons:start -->
## Lessons

1. [What ICT and smart money concepts claim](01-what-ict-and-smc-claim.md) (idea)
2. [Liquidity and stop runs](02-liquidity-and-stop-runs.md) (strategy)
3. [Fair value gaps](03-fair-value-gaps.md) (strategy)
4. [Order blocks and breakers](04-order-blocks-and-breakers.md) (strategy)
5. [Sessions, kill zones and premium and discount](05-sessions-kill-zones-and-premium-discount.md) (strategy)
6. [Testing smart money claims](06-testing-smc-claims.md) (data, review)

<!-- lessons:end -->

## Cheat sheet

### Definitions

| Term | Rule used in this part |
|---|---|
| Swing high or low | A bar whose high (low) is beyond the bars on both sides |
| Break of structure (BOS) | A close beyond the last swing point, with the trend |
| Change of character (CHoCH) | The first close beyond a swing point, against the trend |
| Equal highs or lows | Two or more swing points within 0.2% of each other |
| Sweep | A bar trades through equal highs (lows) and closes back inside |
| Bullish fair value gap | Bar 1 high below bar 3 low; zone from bar 1 high to bar 3 low |
| Bearish fair value gap | Bar 1 low above bar 3 high; zone from bar 3 high to bar 1 low |
| Consequent encroachment | The 50% midpoint of a gap |
| Bullish order block | The last down candle before an upward displacement that breaks structure |
| Breaker block | An order block that price closed through, now with the opposite role |

### Formulas

| Formula | Symbols | Use |
|---|---|---|
| \( \text{level}_k = H - k\,(H-L) \) | \(H\) swing high, \(L\) swing low, \(k\) fraction | Retracement level of a rising swing |
| \( k = 0.5 \) | | Equilibrium |
| \( k = 0.62 \) to \( 0.79 \) | 0.705 is the middle | Optimal trade entry zone |
| \( t = \bar{x} / (s/\sqrt{n}) \) | \(\bar{x}\) mean R, \(s\) standard deviation of R, \(n\) trades | Is the edge distinguishable from zero |
| \( n = (t\,s/\bar{x})^2 \) | | Trades needed for a target t |

### Times (ET, Toronto)

- Asian range about 8 p.m. to midnight. London kill zone 2 to 5 a.m. New York kill zone 7 to 10 a.m. London close 10 a.m. to noon. Teachers differ by up to an hour.
- London is 5 hours ahead of Toronto, except 4 hours from March 8 to 28 and October 25 to 31 in 2026 (the US and UK change clocks on different days).
- US stocks: regular session 9:30 a.m. to 4 p.m. ET.

### Checklist before you trust a rule

1. Every parameter written down before looking.
2. Last third of the data kept back.
3. Costs counted in R.
4. Baseline compared (all bars, random bars, placebo candles).
5. Every variant tried is counted.
6. Enough trades for the size of edge (use the formula above).

### What the evidence says

- Stop and take-profit orders cluster at visible prices in currency data (Osler 2003, 2005).
- Activity varies by hour (Andersen and Bollerslev 1998).
- We found no peer-reviewed tests of fair value gaps, order blocks, breakers, kill zones as a direction signal, or the 62% to 79% zone.

