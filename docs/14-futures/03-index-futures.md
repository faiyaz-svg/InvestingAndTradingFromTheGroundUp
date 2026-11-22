# Index futures: ES, MES, NQ and MNQ

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">FUT</span>

After this lesson you can read a contract spec, compute tick value and notional, and size an index futures trade by risk in R.

Before this: [Margin, leverage and mark to market](02-margin-leverage-and-mark-to-market.md), [Position sizing with fixed fractional risk](../03-risk-and-position-sizing/04-fixed-fractional-sizing.md). You need: a calculator.

## The idea

The most traded index futures in North America track the S&P 500 and the Nasdaq-100 (see [Indexes, sectors and market cap](../01-how-markets-work/10-indexes-sectors-and-market-cap.md)). CME Group lists each in two sizes. The **E-mini** contracts, ES (S&P 500) and NQ (Nasdaq-100), came first. The **Micro E-mini** contracts, MES and MNQ, are one tenth the size, so a small account can use them.

The spec is what turns a quoted price into dollars. Three numbers matter.

- The **multiplier** is the US$ value of one index point.
- The **tick size** is the smallest price step. For these four contracts it is 0.25 index points.
- The **tick value** is tick size times multiplier, the US$ value of one tick.

| | ES | MES | NQ | MNQ |
|---|---|---|---|---|
| Index | S&P 500 | S&P 500 | Nasdaq-100 | Nasdaq-100 |
| Multiplier | US$50 | US$5 | US$20 | US$2 |
| Tick size | 0.25 | 0.25 | 0.25 | 0.25 |
| Tick value | US$12.50 | US$1.25 | US$5.00 | US$0.50 |
| Expiry months | Mar, Jun, Sep, Dec | same | same | same |
| Settlement | Cash | Cash | Cash | Cash |

These are CME Group's specs as of 2026 ([Micro E-mini S&P 500](https://www.cmegroup.com/markets/equities/sp/micro-e-mini-sandp-500.html), [E-mini S&P 500](https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.html), [E-mini Nasdaq-100](https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.html), [Micro E-mini Nasdaq-100](https://www.cmegroup.com/markets/equities/nasdaq/micro-e-mini-nasdaq-100.html)). Specs and margins can change, so check the contract page before you trade. The expiry months are the quarterly cycle: March (H), June (M), September (U) and December (Z), with a month letter and a year digit in the symbol, as in [Tickers and symbols](../00-start-here/tickers-and-symbols.md). Lesson 4 covers the expiry rules.

## Notional value and tick value

Notional value for one contract is the index level times the multiplier. At an index level of 6,000 (a made-up level), one MES is 6,000 x 5 = US$30,000. One ES is 6,000 x 50 = US$300,000. Ten MES equal one ES in size, and one tick on ten MES is 10 x 1.25 = US$12.50, the same as one tick on ES.

The number of ticks between your entry and stop is what you size from. A move of \(x\) index points is \(x / 0.25\) ticks.

## Sizing a trade by risk in R

Part 3's method carries over with one change: risk per contract replaces risk per share ([R-multiples](../03-risk-and-position-sizing/02-r-multiples.md)).

\[ \text{contracts} = \left\lfloor \frac{f \times A}{T \times V} \right\rfloor \]

- \(f\) is the fraction of the account risked, such as 0.01.
- \(A\) is the account value, in US$.
- \(T\) is the number of ticks from entry to stop.
- \(V\) is the tick value, in US$ per tick per contract. \(T \times V\) is the risk per contract.
- The brackets mean round down, so the loss at the stop stays inside \(f \times A\).

<div class="example" markdown>

### Worked example: a long on the made-up micro contract

Account US$25,000, risk 1%. The chart below is a made-up micro index future (MXF) with MES specs: US$5 per point, 0.25 tick, US$1.25 tick value. You buy at 6,011.00 with a stop at 6,003.00, below the 6,005.31 low of the 1:10 to 2:15 p.m. range. The target is 6,027.00.

1. Risk amount = 0.01 x 25,000 = US$250.00.
2. Stop distance = 6,011.00 - 6,003.00 = 8.00 points = 32 ticks.
3. Risk per contract = 32 x 1.25 = US$40.00.
4. Contracts = 250 / 40 = 6.25, which rounds down to 6.
5. Actual risk = 6 x 40 = US$240.00, which is 0.96% of the account. This is 1R.
6. Notional = 6,011 x 5 x 6 = US$180,330, which is 7.2 times the account. With the made-up margin of US$2,400 per contract, margin is 6 x 2,400 = US$14,400, 57.6% of the account.
7. Target distance = 6,027.00 - 6,011.00 = 16.00 points = 64 ticks. Reward = 64 x 1.25 x 6 = US$480.00, which is 2.0R.

One ES would risk 8 x 50 = US$400 on the same stop, more than the US$250 budget, so the answer for ES is 0 contracts.

</div>

The chart shows the day. Look for the 1:10 to 2:15 p.m. range, the entry at 2:20 p.m. and the push to the target in the last bar.

```chart
data: 14-futures/mxf-5m.json
title: MXF (made-up micro index future), 5-minute: a range, then a push up
show: volume
level: 6003.00 | Stop
level: 6027.00 | Target
marker: 2026-09-16 14:20 | below | Entry 6,011
marker: 2026-09-16 15:55 | above | Target hit
range: 2026-09-16 09:30 to 2026-09-16 15:55
caption: Entry at 6,011.00, stop at 6,003.00 (32 ticks), target at 6,027.00 (2R).
```

Notional is not risk. Seven times your account in notional sounds large, but the stop caps the planned loss at US$240. The caveat is that a stop is not a guarantee: a fast move can fill it past 6,003.00, and a gap after the session break can too. Add slippage and fees to the cost in R ([Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md)).

## In code

A contract-count function, and the numbers from the example.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def contracts(account, risk_pct, entry, stop, tick=0.25, tick_value=1.25):
    ticks = abs(entry - stop) / tick
    risk_per_contract = ticks * tick_value
    return math.floor(account * risk_pct / 100 / risk_per_contract)

print(contracts(25_000, 1, 6011.00, 6003.00))
print(contracts(25_000, 1, 6011.00, 6003.00, tick_value=12.50))
```

The code prints 6 for the micro contract and 0 for the E-mini on the same stop.

</details>

<div class="canada" markdown>

### For Canadians

CME contracts are quoted and settled in US dollars, so risk in R should be measured in your account's currency at the current rate ([Currency risk on US stocks](../02-accounts-currency-and-taxes/05-currency-risk-on-us-stocks.md)). Canada's own index future is in lesson 7 ([Futures in Canada](07-futures-in-canada.md)).

</div>

## Common mistakes

- Using the tick value of ES for MES. Tick values differ by a factor of ten.
- Counting points, not ticks, in the formula. 8 points is 32 ticks.
- Placing the stop by the number of contracts you want. Set the stop from the chart first, then compute contracts.

## Try it

1\. What is the tick value of one MNQ contract?

<details class="solution" markdown>
<summary>Answer</summary>

0.25 x US$2 = US$0.50.

</details>

2\. A made-up Nasdaq-100 level is 21,000. What is the notional of 1 NQ and of 1 MNQ?

<details class="solution" markdown>
<summary>Answer</summary>

NQ: 21,000 x 20 = US$420,000. MNQ: 21,000 x 2 = US$42,000.

</details>

3\. Account US$25,000, risk 1%, MNQ entry 21,000.00, stop 20,970.00. How many contracts?

<details class="solution" markdown>
<summary>Answer</summary>

Stop distance = 30.00 points = 120 ticks. Risk per contract = 120 x 0.50 = US$60.00. Risk amount = US$250.00. 250 / 60 = 4.17, which rounds down to 4 contracts. Actual risk = US$240.00.

</details>

4\. In the worked example, the stop fills 2 ticks worse, at 6,002.50. What is the loss in US$ and in R?

<details class="solution" markdown>
<summary>Answer</summary>

2 ticks = 0.50 points. The loss per contract is 8.50 points = 34 ticks x 1.25 = US$42.50. For 6 contracts, US$255.00. In R: 255 / 240 = 1.06R.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | On a micro contract's quote page, write the multiplier, tick size, tick value and expiry months. Compare them with the table. |
| 5 | Pick a stop on a chart in [chart drills](../practice/chart-drills.md) and compute contracts for a US$25,000 account at 1% risk. |

</div>

## Key terms

- **E-mini**: the standard-size CME contract on an index, such as ES and NQ.
- **Micro E-mini**: a contract one tenth the size of the E-mini, such as MES and MNQ.
- **Tick size**: the smallest price step of a contract.
- **Tick value**: tick size times multiplier, the US$ value of one tick.
- **Contract month**: the month a contract expires, shown by a letter in its symbol.

Next: [Expiry and rolling](04-expiry-and-rolling.md)
