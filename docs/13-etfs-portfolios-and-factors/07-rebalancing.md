# Rebalancing

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">ETF</span>

After this lesson you can compute the trades that bring a portfolio back to its target weights, choose between a calendar rule and a threshold rule, and say what the evidence supports about rebalancing.

Before this: [Asset allocation](05-asset-allocation.md), [Diversification and correlation](06-diversification-and-correlation.md). The math book's [Index funds, fees and dollar-cost averaging](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/06-investing-and-retirement/02-index-funds-fees-and-dollar-cost-averaging/) has a short section on rebalancing. You need: a calculator.

## The idea

You set a 60 / 40 mix of stocks and bonds on US$100,000. A year later stocks are up 25% and bonds up 2%. Nobody traded, but the mix changed: stocks are now about 65% of the portfolio. You hold more risk than you chose. **Drift** is this movement of weights away from the target as prices change. **Rebalancing** is trading to bring the weights back.

The reason to rebalance is risk, not return. A portfolio that drifts toward its best-performing asset becomes riskier each year, and a rising stock weight means a larger loss when stocks fall. Rebalancing sells some of what rose and buys what lagged, which feels wrong while it is happening.

## How it works

For each fund, the trade is the target weight times the portfolio value, minus what you hold:

\[ T_i = w_i^{*} V - H_i \]

- \(w_i^{*}\) is the target weight of fund \(i\), as a fraction.
- \(V\) is the total portfolio value now, in your currency.
- \(H_i\) is the current value of fund \(i\).
- \(T_i\) is the trade: positive means buy, negative means sell. The trades add to zero if you add no cash.

<div class="example" markdown>

### Worked example: a drifted 60 / 40

Start: US$60,000 stocks, US$40,000 bonds. After a year, stocks return 25% and bonds 2%.

1. Stocks: 60,000 x 1.25 = US$75,000. Bonds: 40,000 x 1.02 = US$40,800. Total \(V\) = US$115,800.
2. Weights: stocks 75,000 / 115,800 = 64.77%, bonds 35.23%.
3. Targets: stocks 0.6 x 115,800 = US$69,480. Bonds 0.4 x 115,800 = US$46,320.
4. Trades: stocks 69,480 - 75,000 = -US$5,520 (sell). Bonds 46,320 - 40,800 = +US$5,520 (buy).

</div>

### When to rebalance

A **calendar rule** rebalances on fixed dates, such as once a year. It needs no monitoring. A **threshold rule** (also called a tolerance band) rebalances when any weight is more than a set distance from its target, for example 5 percentage points. It reacts to large moves and does nothing in quiet years. For most broadly diversified stock and bond portfolios, the same Vanguard paper suggests checking once or twice a year and rebalancing at a 5 percentage point threshold, preferring annual rebalancing when taxes or costs matter. It also says there is no optimal frequency or threshold, so treat 5 as a common choice rather than a rule.

In the example, stocks drifted 4.77 points, so a 5-point band does not trigger and an annual calendar rule does. If stocks had risen 40% and bonds were flat, stocks would be 84,000 / 124,000 = 67.74%, a drift of 7.74 points. The band triggers, and the target is 0.6 x 124,000 = US$74,400, so you sell US$9,600.

You can often avoid selling. If you add US$5,000 of new money to the drifted portfolio, the new total is US$120,800 and the bond target is 0.4 x 120,800 = US$48,320. Bonds need US$7,520, which is more than US$5,000, so you put all US$5,000 in bonds and sell nothing. The weights become stocks 75,000 / 120,800 = 62.1% and bonds 37.9%, closer to target.

### What the evidence says

Vanguard studied U.S. stocks and bonds from 1926 to 2009 and found that risk-adjusted returns were not meaningfully different between monthly, quarterly and annual rebalancing, while the number of trades and costs rose a lot with frequency. It concluded there was no single best frequency or threshold, and that the purpose of rebalancing is to keep the portfolio's risk, not to raise return ([Vanguard, "Best practices for portfolio rebalancing", 2010, as reprinted by AAII](https://www.aaii.com/journal/article/best-practices-for-portfolio-rebalancing?printerfriendly=true)). I read the AAII reprint, which Vanguard's authors adapted from the 2010 paper, not the original.

You will also read about a **rebalancing bonus**: extra long-run growth from selling high and buying low. It is real in one situation, shown below, and not a general result. It needs assets with similar long-run returns, high volatility and low correlation, and prices that swing back. In a steady trend, rebalancing sells the winner too early and the bonus turns negative.

<div class="example" markdown>

### Worked example: where the bonus comes from

Two made-up assets, X and Y, each end flat after two years. X goes +100% then -50%. Y goes -50% then +100%. Start with US$50 in each.

1. Buy and hold. Year 1: X = 100, Y = 25, total 125. Year 2: X = 50, Y = 50, total 100. No gain.
2. Rebalance each year. Year 1 gives 125, rebalanced to 62.50 each. Year 2: X = 62.50 x 0.5 = 31.25, Y = 62.50 x 2 = 125, total US$156.25.

A 56.25% gain from two assets that each went nowhere. Real assets do not swing this much, so the real bonus is far smaller, and it depends on the period.

</div>

<div class="canada" markdown>

### For Canadians

In a TFSA, RRSP or FHSA, selling one fund to buy another triggers no tax, so rebalance there first. In a non-registered account, a sale at a gain is a capital gain and counts on your return ([Capital gains or business income](../02-accounts-currency-and-taxes/07-capital-gains-vs-business-income.md)), and a sale at a loss follows the superficial loss rule ([Tax losses and the superficial loss rule](../02-accounts-currency-and-taxes/09-tax-losses-and-superficial-loss.md)). Direct new contributions to the underweight fund before you sell anything. An all-in-one ETF (lesson 3) rebalances inside the fund, so you do not trade.

</div>

## In code

A function that returns the trades for any set of weights.

<details class="code" markdown>
<summary>In code</summary>

```python
def trades(holdings, targets, new_cash=0.0):
    total = sum(holdings.values()) + new_cash
    return {k: round(targets[k] * total - holdings[k], 2) for k in holdings}

print(trades({"stocks": 75_000, "bonds": 40_800}, {"stocks": 0.6, "bonds": 0.4}))
```

</details>

## Common mistakes

- Rebalancing too often in a taxable account. Each sale can create a tax bill and costs, and the evidence does not show a gain from frequent trades.
- Skipping rebalancing because the winner "has momentum". Decide the rule before the move, then follow it.
- Treating the target as sacred after your goals change. Change the target on purpose, not by drift.

## Try it

1\. A 70 / 30 portfolio worth US$50,000 holds US$35,000 stocks and US$15,000 bonds. Stocks rise 20% and bonds fall 4%. What are the new weights?

<details class="solution" markdown>
<summary>Answer</summary>

Stocks = 35,000 x 1.20 = 42,000. Bonds = 15,000 x 0.96 = 14,400. Total = 56,400. Weights: stocks 42,000 / 56,400 = 74.47%, bonds 25.53%.

</details>

2\. What trades bring it back to 70 / 30?

<details class="solution" markdown>
<summary>Answer</summary>

Stock target = 0.7 x 56,400 = 39,480. Sell 42,000 - 39,480 = US$2,520 of stocks. Bond target = 16,920, so buy 16,920 - 14,400 = US$2,520 of bonds.

</details>

3\. With a 5-point band, does it trigger?

<details class="solution" markdown>
<summary>Answer</summary>

No. Stocks are 74.47%, 4.47 points above 70%. An annual calendar rule would rebalance, and the band would wait.

</details>

4\. You add US$3,000 instead of selling. Where does it go, and what are the weights?

<details class="solution" markdown>
<summary>Answer</summary>

New total = 59,400. Bond target = 0.3 x 59,400 = 17,820, so bonds need 3,420. That is more than US$3,000, so all of it goes to bonds. Bonds = 17,400, weight 29.29%. Stocks = 42,000, weight 70.71%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Write your target weights and your current weights from your account statements. Compute each drift in percentage points. |
| 3 | Choose a rule (once a year on a fixed date, or a band) and write it down. |
| 3 | Compute the trades for your actual portfolio, and note which accounts you would place them in. |

</div>

## Key terms

- **Drift**: the movement of portfolio weights away from the target as prices change.
- **Rebalancing**: trading to bring portfolio weights back to the target.
- **Calendar rule**: rebalancing on fixed dates.
- **Threshold rule (tolerance band)**: rebalancing when a weight is more than a set distance from its target.
- **Rebalancing bonus**: extra long-run growth that rebalancing can add when assets swing and revert.

Next: [Modern portfolio theory](08-modern-portfolio-theory.md)
