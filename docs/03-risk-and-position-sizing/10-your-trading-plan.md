# Your trading plan

<span class="tag tag-skill">Skill</span> <span class="tag tag-review">Review</span> <span class="tag tag-part">RISK</span>

After this lesson you can write a one-page risk plan with numbers for risk per trade, portfolio heat, loss limits and drawdown rules, and use it as a checklist before each trade.

Before this: every lesson in this part, mainly [Position sizing with fixed fractional risk](04-fixed-fractional-sizing.md) and [Portfolio heat and correlation](07-portfolio-heat-and-correlation.md). You need: a calculator and a text file or sheet of paper.

## The idea

The math in this part gives you numbers: the loss at a stop, the size of a position, the heat of a portfolio, the depth of a drawdown. Numbers you only know in your head change when you are stressed, up or down on the day. A **trading plan** writes them down once, in advance, in a form you can check against.

This part's plan is a risk plan. It says how much you may lose and when you stop. It does not say what to buy or when: entries come from the strategy parts later in the book. Each part of the book fills a different section of the plan.

## How it works

A plan has three kinds of rule: how much to risk on one trade, how much to risk in total, and what to do when you are losing. The loss rules are the new piece in this lesson.

### Loss limits

A **daily loss limit** is the most you will lose in one day, counted in R. When you hit it, you stop trading until tomorrow. A **weekly loss limit** works the same way for a week. They keep one bad stretch from turning into a large drawdown. They are also easy to count in R: two full stop-outs at 1% each are a loss of 2%.

A **drawdown rule** changes the risk per trade as the account falls. Lesson 1 showed that a deeper hole needs a bigger climb, and lesson 8 showed that drawdowns come even with an edge. A common design has two steps: cut the risk per trade at a first level, and stop trading to review at a second level.

<div class="example" markdown>

### Worked example: a plan for one account

The account is US$25,000. These numbers are an example to show the arithmetic. They are not a recommendation.

1. Risk per trade: 1% of the account = US$250. Planned reward at least 2R before entering.
2. Portfolio heat cap: 5% = US$1,250 of open risk.
3. Group cap: 2% = US$500 of open risk in one sector.
4. Daily loss limit: 2R = US$500 (2% of the account). Weekly limit: 5% = US$1,250.
5. First drawdown step: at 10% below the peak, the account is 25,000 x 0.90 = US$22,500. Cut risk to 0.5%, which is 22,500 x 0.005 = US$112.50 per trade.
6. Second drawdown step: at 15% below the peak, the account is 25,000 x 0.85 = US$21,250. Stop trading and review all trades since the peak.
7. Check the climb: from the first step, recovering the 10% needs 11.1% (lesson 1).

</div>

### The single-loss rule

No single trade may lose more than 1R plus fees. The one exception is a gap through the stop (lesson 6), which you accept in advance and size for.

### A checklist before each trade

1. Is the stop set from structure or ATR, and written down (lesson 5)?
2. Is the size computed from the stop, rounded down (lesson 4)?
3. Is the planned reward at least the plan's minimum, in R (lessons 2 and 3)?
4. Do costs and a likely slippage still leave the trade worth taking (lesson 6)?
5. Does heat plus this trade stay under the cap, and the group under its cap (lesson 7)?
6. Has the daily or weekly limit been hit? Is a drawdown step active, with a smaller risk (lesson 8)?

If any answer is no, the trade does not happen.

### The one-page plan

Copy this into a file and fill every blank with a number, in your account's currency. A line you cannot fill means a decision you have not made yet.

| Section | Your rule |
|---|---|
| Account and currency (for example TFSA, USD) | ____ |
| Account value at the start of the month | ____ |
| Risk per trade, as a percent and in dollars | ____ |
| Minimum planned reward, in R | ____ |
| Stop rule (structure, ATR multiple, or both) | ____ |
| Maximum portfolio heat, percent and dollars | ____ |
| Maximum risk in one sector or group | ____ |
| Maximum number of open positions | ____ |
| Costs per round trip in R (commission, spread, currency) | ____ |
| Daily loss limit, in R and as a percent | ____ |
| Single-loss rule (1R plus fees, gaps as the exception) | ____ |
| Weekly loss limit, as a percent | ____ |
| Drawdown step 1: level and the smaller risk per trade | ____ |
| Drawdown step 2: level and what happens (stop and review) | ____ |
| Times you will not trade (before earnings, the first minutes after the open) | ____ |
| When you review the plan, and how | ____ |

The plan only works if you follow it when it is uncomfortable. Part 4 covers why that is hard and how to build the habit ([Biases that cost traders money](../04-psychology-journal-and-paper-trading/01-biases-that-cost-traders.md)).

## Try it

1\. Using the example plan, your account has grown to US$30,000. What are the dollar risk per trade, the heat cap and the daily loss limit?

<details class="solution" markdown>
<summary>Answer</summary>

Risk per trade = 1% of 30,000 = US$300. Heat cap = 5% = US$1,500. Daily loss limit = 2R = US$600.

</details>

2\. Your account peaked at US$30,000 and is now US$26,400. Which drawdown step applies, and what is the risk per trade?

<details class="solution" markdown>
<summary>Answer</summary>

Drawdown = (30,000 - 26,400) / 30,000 = 12.0%. That is past the first step (10%) and short of the second (15%), so risk is cut to 0.5% of the current account: 0.005 x 26,400 = US$132.00 per trade.

</details>

3\. You lose two trades in a row at 1R each on a US$25,000 account with a 2R daily limit. A third setup appears. What does the plan say?

<details class="solution" markdown>
<summary>Answer</summary>

The two losses total 2R = US$500, which is the daily limit. You stop for the day and the third setup is not taken.

</details>

## Part check

1\. An account is down 40% from its peak. What gain recovers it?

<details class="solution" markdown>
<summary>Answer</summary>

0.40 / (1 - 0.40) = 0.40 / 0.60 = 66.7%.

</details>

2\. You buy at US$20.00 with a stop at US$19.20 and sell at US$21.60. What is the result in R?

<details class="solution" markdown>
<summary>Answer</summary>

Risk per share = 0.80. Gain per share = 1.60. r = 1.60 / 0.80 = +2.0R.

</details>

3\. A strategy wins 35% of the time, with winners averaging +2.5R and losers averaging -1R. What is the expectancy, and is the win rate above break-even?

<details class="solution" markdown>
<summary>Answer</summary>

E = 0.35 x 2.5 - 0.65 x 1 = 0.875 - 0.65 = +0.225R. Break-even win rate = 1 / (1 + 2.5) = 28.6%, so 35% is above it.

</details>

4\. Your account is C$20,000 and you risk 0.5%. Stock A costs US$60.00, your stop is US$58.00, and US$1 = C$1.40. How many shares?

<details class="solution" markdown>
<summary>Answer</summary>

Risk = C$100. In US$: 100 / 1.40 = US$71.43. Risk per share = 2.00. Shares = 71.43 / 2.00 = 35.71, so 35 shares.

</details>

5\. Account US$20,000, heat cap 5%. Open risk is US$300, US$450 and US$200. A new trade would risk US$100. Is it allowed?

<details class="solution" markdown>
<summary>Answer</summary>

Open risk = US$950, which is 4.75%. Adding US$100 gives US$1,050, or 5.25%, which is over the 5% cap (US$1,000). Not allowed at that size. The most the new trade can risk is US$50.

</details>

6\. A bet wins half the time and pays 2 to 1. What is the Kelly fraction, and what is half Kelly? Compare half Kelly with a 1% risk per trade.

<details class="solution" markdown>
<summary>Answer</summary>

f* = 0.50 - 0.50 / 2 = 0.25, so 25%. Half Kelly is 12.5%. A risk of 1% is one twenty-fifth of the Kelly fraction, a very cautious fraction.

</details>

7\. You buy at US$60.00 with a stop at US$58.00. The stock gaps down and opens at US$55.00. What is the result in R?

<details class="solution" markdown>
<summary>Answer</summary>

(60.00 - 55.00) / (60.00 - 58.00) = 5.00 / 2.00, so -2.5R.

</details>

8\. The account peaked at US$12,000 and is now US$10,200. What is the drawdown, and what gain recovers it?

<details class="solution" markdown>
<summary>Answer</summary>

Drawdown = (12,000 - 10,200) / 12,000 = 15.0%. Gain needed = 12,000 / 10,200 - 1 = 17.6%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 6 | Fill in the one-page plan with your own numbers. Use the example above as a guide. |
| 3 | Size three setups from [chart drills](../practice/chart-drills.md) with your plan: stop, shares, heat after each. |
| 1 | Save the plan as a file you can open before trading. |

</div>

## Key terms

- **Trading plan**: a written set of rules and numbers, made in advance, that you check each trade against.
- **Daily loss limit**: the most you will lose in a day, in R, after which you stop.
- **Weekly loss limit**: the same limit over a week, as a percent of the account.
- **Drawdown rule**: a rule that cuts risk per trade, or stops trading, at set drawdown levels.
- **Pre-trade checklist**: the questions you answer before each order.

Next: [Biases that cost traders money](../04-psychology-journal-and-paper-trading/01-biases-that-cost-traders.md)
