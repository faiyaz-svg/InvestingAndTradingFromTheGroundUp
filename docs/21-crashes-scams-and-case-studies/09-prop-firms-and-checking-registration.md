# Prop firms and checking registration

<span class="tag tag-canada">Canada</span> <span class="tag tag-review">Review</span> <span class="tag tag-part">HIST</span>

After this lesson you can work out what a "funded trader" evaluation costs you in expectation, check whether a firm or person is registered in Canada, say what CIPF does and does not cover, and report suspected fraud.

Before this: [Pump and dumps, finfluencers and signal groups](08-pump-and-dumps-finfluencers-and-signal-groups.md), [Drawdowns and risk of ruin](../03-risk-and-position-sizing/08-drawdowns-and-risk-of-ruin.md). You need: a calculator.

## The idea

A **proprietary trading firm** (prop firm) trades with its own money and pays traders a share of profits. A newer model, a "funded trader" program, charges the trader a fee for an **evaluation**: a test period in which you trade an account under set rules. If you pass, you are offered a "funded" account and a share of the profits. This lesson describes how the fees and rules work and how to check a firm. It names no firm and does not rate any program.

## How an evaluation works

Programs differ, so read the terms. A typical structure has these parts:

- A **fee** paid before you start, and sometimes monthly until you pass.
- An account size, such as US$50,000, which the rules use. Check in the terms whether the account is real or simulated.
- A **profit target**, such as 8% of the account, to pass.
- A **maximum drawdown**, a limit on losses. It may be **static**, a fixed floor below the starting balance, or **trailing**, a floor that moves up with your highest balance.
- A **profit split**, such as 80% to the trader on a funded account, and conditions for withdrawing.

<div class="example" markdown>

### Worked example: the rules in dollars

The terms (made-up): fee US$150, account US$50,000, profit target 8%, maximum drawdown 10%, profit split 80%.

1. Profit target: 0.08 x 50,000 = US$4,000.
2. Maximum drawdown: 0.10 x 50,000 = US$5,000. With a static floor, the evaluation ends at US$45,000.
3. If you risk 1% of the account, US$500, per trade, ten full losses in a row reach the floor.
4. With a trailing floor, the floor moves with your highest balance. If you reach US$53,000, the floor is 53,000 - 5,000 = US$48,000.

A trailing floor leaves less room after a good run. Part 3's drawdown rules apply here, with a hard limit set by someone else.

</div>

### What the fee costs

The fee is paid whether or not you pass. If one attempt passes with probability \(p\), you need on average \(1/p\) attempts, so one pass costs the fee divided by \(p\).

\[ \text{cost per pass} = \frac{\text{fee}}{p} \]

- \(\text{fee}\) is the cost of one attempt, in US$.
- \(p\) is the probability that one attempt passes, a fraction.

<div class="example" markdown>

### Worked example: expected cost of a pass

1. If p = 25%, the cost per pass is 150 / 0.25 = US$600.
2. If p = 20%, it is 150 / 0.20 = US$750.

The pass rate \(p\) is the number to ask for. A firm may publish one. This lesson does not quote one, because no regulator source gives it, so try a range of values and see how the cost per pass changes. You can estimate your own p by practising the rules in a paper account ([Paper trading](../practice/paper-trading.md)).

</div>

## Is the firm registered

In Canada, advising on securities or dealing in them as a business generally needs registration. Whether a prop firm needs it depends on what it does, so check. The OSC's investor warnings list has included proprietary trading firms described as not registered ([OSC investor warnings and alerts](https://www.osc.ca/en/investors/investor-warnings-and-alerts), as of 2026). A polished site proves nothing.

Three official tools:

1. **CSA National Registration Search** at [aretheyregistered.ca](https://www.aretheyregistered.ca) lists registered individuals and firms across Canada, and can show disciplinary history ([CSA National Registration Search](https://info.securities-administrators.ca/nrsmobile/nrssearch.aspx?lang=EN)).
2. **CIRO AdvisorReport** shows whether an advisor is currently or formerly regulated by the Canadian Investment Regulatory Organization (CIRO, the self-regulator of investment dealers) and any disclosed disciplinary actions ([CIRO, Know Your Advisor](https://www.ciro.ca/office-investor/know-your-advisor-advisor-report), as of 2026). AdvisorReport covers only currently regulated advisors; CIRO's disciplinary case search keeps records of former advisors who were disciplined. It has no reports for mutual fund dealer representatives, who are in the CSA search.
3. **The CSA's investor alerts** list firms to avoid ([CSA investor alerts](https://www.securities-administrators.ca)).

## CIPF: what protects your account

The Canadian Investor Protection Fund (CIPF) protects clients of member firms if a firm becomes insolvent and cannot return your cash or securities. As of 2026 it covers up to C$1 million for general accounts combined (cash, margin, TFSA, FHSA), a separate C$1 million for retirement accounts (RRSP, RRIF, LIF) and a separate C$1 million for RESPs. It does not cover market losses, and claims must be made within 180 days ([CIPF, About CIPF coverage](https://www.cipf.ca/cipf-coverage/about-cipf-coverage), as of 2026).

CIPF covers property held at a member firm. An evaluation fee paid to a non-member is not property held at a dealer. Check your own broker: is it a CIRO member, and is it listed as a CIPF member? Confirm this on the broker's site and in the registration search, not from this book.

## Reporting a suspected fraud

If you think you are a victim, the CSA's alert says to contact your provincial securities regulator, the Canadian Anti-Fraud Centre, your bank and the police. In Ontario, the OSC's Inquiries and Contact Centre takes reports of securities fraud, including through an online form, and says to report quickly ([OSC investor warnings and alerts](https://www.osc.ca/en/investors/investor-warnings-and-alerts), as of 2026). Keep the messages, payment records and names.

<div class="canada" markdown>

### For Canadians

A US firm is not on the CSA's registration lists unless it is also registered in Canada. A fee paid in USD by card carries a conversion cost ([USD or CAD, and currency conversion fees](../02-accounts-currency-and-taxes/03-usd-vs-cad-and-fx-fees.md)). Payouts may be income for the CRA ([Capital gains versus business income](../02-accounts-currency-and-taxes/07-capital-gains-vs-business-income.md)).

</div>

## Common mistakes

- Judging a program by its best payout. Ask for the pass rate.
- Reading "I found no complaint" as "it is registered". Registration is a list lookup.
- Assuming CIPF protects every fee. It covers property at member firms, not market losses.

## Try it

1\. An evaluation costs US$99 and you pass 1 attempt in 3. What is the expected cost of one pass?

<details class="solution" markdown>
<summary>Answer</summary>

p = 1/3. Cost per pass = 99 / (1/3) = US$297.

</details>

2\. A fee is US$200 and the payout after a pass is US$1,000. What pass rate breaks even?

<details class="solution" markdown>
<summary>Answer</summary>

Break-even p = 200 / 1,000 = 20%.

</details>

3\. You hold C$100,000 in a TFSA and C$1.3 million in a cash account at one CIRO member firm. How much is covered by CIPF's general account limit, as of 2026?

<details class="solution" markdown>
<summary>Answer</summary>

Cash and TFSA accounts count together as general accounts: C$1.4 million held, C$1 million covered.

</details>

## Part check

1\. You buy US$10,000 of Stock A with 10% of your own money. How far must the price fall before your own money is gone?

<details class="solution" markdown>
<summary>Answer</summary>

The loan is US$9,000, so your money is gone at a fall of 10% (lesson 1).

</details>

2\. A fund has 28 to 1 leverage. What fall in asset value removes its equity?

<details class="solution" markdown>
<summary>Answer</summary>

1 / 28 = 3.57%, or 3.6% (lesson 2).

</details>

3\. Name the main risk in each case: the 2008 repo run, the 2010 flash crash, GameStop and SVB.

<details class="solution" markdown>
<summary>Answer</summary>

2008: funding and counterparty risk. 2010: liquidity risk. GameStop: short-selling cost and broker restrictions. SVB: duration risk and a run by uninsured depositors.

</details>

4\. You short 200 shares of Stock A at US$30. The price rises to US$75. What is the loss, and is there a limit on how large it can get?

<details class="solution" markdown>
<summary>Answer</summary>

(75 - 30) x 200 = US$9,000. No: the price has no ceiling (lesson 5).

</details>

5\. A signal group shows 9 wins in 10 trades. Give two reasons the win rate is not enough.

<details class="solution" markdown>
<summary>Answer</summary>

The standard error is sqrt(0.9 x 0.1 / 10) = 9.5 points, so 10 trades say little. And the win rate ignores the size of wins and losses (lesson 8).

</details>

6\. Which tool do you use first to check whether a person or firm is registered in Canada, and which to see a CIRO-regulated advisor's disciplinary record?

<details class="solution" markdown>
<summary>Answer</summary>

The CSA National Registration Search first, then the CIRO AdvisorReport.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Look up your own broker in the CSA National Registration Search and the CIPF member list. Write the dates and what you found. |
| 3 | Pick one prop firm or signal group you have seen advertised. Write its fee, the profit target, the drawdown rule and whether it publishes a pass rate. Work out the cost per pass at a pass rate of 20%. |
| 3 | In your [trade journal](../practice/trade-journal.md), write the largest exposure and the largest loss you could take today across all your accounts, and which lesson of this part addresses the biggest one. |

</div>

## Key terms

- **Proprietary trading firm (prop firm)**: a firm that trades its own money.
- **Evaluation**: a paid test in which a trader follows set rules to qualify for a funded account.
- **Maximum drawdown (evaluation)**: the loss limit; static, from the start, or trailing, from the highest balance.
- **Profit split**: the share of profits the trader keeps.
- **National Registration Search**: the CSA's lookup of registered individuals and firms in Canada.
- **AdvisorReport**: CIRO's lookup of an advisor's registration and disciplinary history.
- **CIRO**: the Canadian Investment Regulatory Organization, the self-regulator of investment dealers.
- **CIPF**: the Canadian Investor Protection Fund, which protects clients of member firms if a firm fails.

Next: [The map of finance jobs](../22-careers-interviews-and-ai/01-the-map-of-finance-jobs.md)
