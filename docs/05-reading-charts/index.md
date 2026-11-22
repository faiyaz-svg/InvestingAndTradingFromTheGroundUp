# Part 5: Reading charts

Candles, trend, levels, volume and the common indicators, with what tests found about patterns.

Before this part: Parts 1 and 3.

<!-- lessons:start -->
## Lessons

1. [Candles, bars and timeframes](01-candles-bars-and-timeframes.md) (skill)
2. [Trend and market structure](02-trend-and-market-structure.md) (skill)
3. [Support and resistance](03-support-and-resistance.md) (skill)
4. [Volume and relative volume](04-volume-and-relative-volume.md) (skill)
5. [Moving averages](05-moving-averages.md) (skill)
6. [Momentum indicators: RSI, MACD and stochastics](06-momentum-indicators.md) (skill)
7. [Volatility indicators: ATR, Bollinger and Keltner](07-volatility-indicators.md) (skill)
8. [VWAP and anchored VWAP](08-vwap-and-anchored-vwap.md) (skill)
9. [Chart patterns and the evidence](09-chart-patterns-and-the-evidence.md) (skill)
10. [Gaps](10-gaps.md) (skill)
11. [Multiple timeframes and relative strength](11-multi-timeframe-and-relative-strength.md) (skill, review)

<!-- lessons:end -->

## Cheat sheet

### Formulas

| Formula | Symbols | Use |
|---|---|---|
| \( \text{Range} = H-L,\ \text{Body} = \lvert C-O\rvert \) | \(O,H,L,C\) the bar's prices | Size of a candle |
| \( \text{CL} = (C-L)/(H-L) \) | close location, 0 to 1 | Who held the close |
| \( \text{RVOL} = V_t/\bar V_{20} \) | \(\bar V_{20}\) mean volume of the previous 20 bars | Busy or quiet |
| \( \text{SMA}_N = \frac1N\sum C_{t-i} \) | \(N\) bars | Trend filter |
| \( \text{EMA}_t = kC_t+(1-k)\text{EMA}_{t-1},\ k=2/(N+1) \) | seeded with the SMA | Faster average |
| \( \text{RSI} = 100-100/(1+RS) \) | \(RS\) = average gain / average loss (Wilder, 14) | Strength of a move |
| \( \text{MACD} = \text{EMA}_{12}-\text{EMA}_{26} \) | signal = EMA 9 of MACD | Trend momentum |
| \( \%K = 100(C-LL_{14})/(HH_{14}-LL_{14}) \) | lowest low, highest high of 14 bars | Close in the range |
| \( TR = \max(H-L,\lvert H-C_{p}\rvert,\lvert L-C_{p}\rvert) \) | \(C_p\) previous close | Bar size with gaps |
| \( ATR_t = ((N-1)ATR_{t-1}+TR_t)/N \) | \(N=14\) | Stop distance |
| Bollinger \( = \text{SMA}_{20} \pm 2\sigma \) | \(\sigma\) population standard deviation | Volatility bands |
| \( \text{VWAP} = \sum TP\,V/\sum V,\ TP=(H+L+C)/3 \) | resets each session | Average price paid |
| \( RS_t = 100\,(S_t/S_0)/(I_t/I_0) \) | stock \(S\), index \(I\) | Relative strength line |
| Gap in ATR \( = (O_t-C_{t-1})/ATR_{t-1} \) | | Size of a gap |

### Trend and levels

- Swing high or low: 5 bars on each side. Uptrend: higher highs and higher lows. Downtrend: lower highs and lower lows.
- Invalidation level: the last swing low in an uptrend (last swing high in a downtrend). A close beyond it ends the call.
- A level is a zone from two or more swing points. A break is a close beyond the zone, not a wick.
- A broken zone often turns into the opposite (role reversal).

### Pattern rules

| Pattern | Trigger | Stop | Measured target |
|---|---|---|---|
| Bull flag | Close above the flag high | Below the flag low | Pole height added to the entry |
| Ascending triangle | Close above the flat top | Below the last rising low | Widest height added to the break |
| Head and shoulders | Close below the neckline | Above the right shoulder | Head height below the neckline |
| Double top | Close below the middle low | Above the second peak | Peak-to-low height below the low |

### Gap types

| Type | Where | Volume | Usual outcome |
|---|---|---|---|
| Common | Inside a range | Ordinary | Fills within days |
| Breakaway | Out of a range or pattern | Heavy | Often not filled |
| Runaway | Mid-trend | Moderate | Often not filled |
| Exhaustion | Late in a trend | Very heavy | Reversal, fills fast |

### Checklists

Before a chart trade:

1. Weekly trend and nearest weekly level?
2. Daily setup in the same direction?
3. Level, trigger, stop and measured target written down?
4. RVOL on the trigger bar?
5. Gap or earnings date coming?
6. Size from the stop (risk per share), not from the price?

### Rules to remember

- Indicators lag the price. They describe, they do not predict.
- Tests of technical rules are mixed: positive results until the early 1990s in many studies, with data-snooping problems (Park and Irwin, 2007).
- A trigger can fail. The stop is part of the pattern.
- A gap type is known only afterwards. A stop does not protect against a gap.
