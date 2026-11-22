# A long-term portfolio

<span class="tag tag-canada">Canada</span> <span class="tag tag-review">Review</span> <span class="tag tag-part">ETF</span>

After this lesson you can write a one-page plan for a long-term portfolio in Canada: the mix, the funds, which account holds each fund, and how you add money and rebalance.

Before this: [US-listed or Canadian-listed ETFs](03-us-vs-canadian-listed-etfs.md), [Asset allocation](05-asset-allocation.md), [Rebalancing](07-rebalancing.md), [Account types for trading](../02-accounts-currency-and-taxes/01-account-types-for-trading.md). The math book's [Retirement accounts](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/06-investing-and-retirement/03-retirement-accounts/) covers how the accounts work. You need: a calculator.

## The idea

A long-term portfolio puts the earlier pieces (an allocation, funds, fees, a rebalancing rule) in one plan, and adds one question: which account holds which fund. The same C$100,000 can pay different amounts of tax and foreign withholding depending on where each fund sits. This is **asset location**, as distinct from asset allocation (what you hold overall).

Location will not rescue a mix you cannot hold through a bad year.

## How it works

Four steps.

1. Fix the overall mix across all accounts (lesson 5).
2. Pick one fund per slice (lessons 2 and 3).
3. Place each fund in an account by the rules below.
4. Write the rebalancing rule and how you add money (lesson 7).

### Rules for location

These are rules of thumb, not tax advice.

| Fund | Where it tends to fit | Why |
|---|---|---|
| US stocks, held in a US-listed ETF | RRSP | The treaty exempts the RRSP from the 15% US withholding (lesson 3). In a TFSA the 15% is lost, and you also pay the conversion cost. |
| International stocks | TFSA, RRSP or non-registered, in a Canadian-listed fund that holds stocks directly | A US-listed fund gets no RRSP advantage on the foreign layer, and a wrapper adds a second layer (lesson 3). |
| Bonds and cash | RRSP or TFSA | Interest is taxed as income each year in a non-registered account. |
| Canadian stocks | Non-registered, or any account | No foreign withholding. Check the CRA's page on the tax on Canadian dividends for a non-registered account. |
| Highest-growth holdings | TFSA | Growth is never taxed there. |

<div class="example" markdown>

### Worked example: placing a portfolio across three accounts

Target: US stocks 30%, Canadian stocks 15%, international stocks 15%, bonds 40%. Accounts: RRSP C$60,000, TFSA C$25,000, non-registered C$15,000.

1. RRSP (C$60,000): US stocks C$30,000 in a US-listed ETF, bonds C$30,000.
2. TFSA (C$25,000): international stocks C$15,000 (Canadian-listed, direct), bonds C$10,000.
3. Non-registered (C$15,000): Canadian stocks C$15,000.
4. Check the totals: US 30,000, Canadian 15,000, international 15,000, bonds 30,000 + 10,000 = 40,000. This matches the target.

The location saves withholding on the US stocks. With a dividend yield of 1.5% (made up), the tax in the TFSA would be 30,000 x 0.015 x 0.15 = C$67.50 a year, and the RRSP holding pays C$0. Moving C$30,000 into a US-listed ETF from a C$ balance at a 1.5% conversion fee costs C$450 on the way in, so the saving covers that leg in 450 / 67.50 = 6.7 years (the sale fee comes on top).

</div>

### The FHSA is a separate goal

The FHSA allows C$8,000 a year and C$40,000 for life, as of 2026 (part 2). Its money is for a first home, usually on a shorter clock. Treat it as its own portfolio with its own mix, not as a slice of the long-term one. If you plan to buy in 3 years with C$16,000 in it, a 20 / 80 stock and bond mix has an expected return of 0.2 x 7 + 0.8 x 3 = 3.8% on lesson 5's inputs and a stress-year return of 0.2 x (-40) + 0.8 x 5 = -4%, or a loss of C$640. A 60 / 40 mix would lose 22%, or C$3,520, close to the deposit date.

### Adding money: lump sum or monthly

You get C$12,000 and can invest it now or in 12 monthly payments of C$1,000. Vanguard studied this in 2012 and, as summaries report it, found that investing the lump sum first beat 12-month dollar-cost averaging about two-thirds of the time in the US, UK and Australia, because markets rise more often than they fall, so money waiting in cash misses the rise. I could not open the paper. Vanguard's own page reports that lump-sum investing won between 61.6% and 73.7% of rolling one-year periods from 1976 to 2022, depending on the market, in a comparison whose base case spreads the money over three months. The same page says cost averaging can guard against losses in extreme down markets, and limits growth in every other condition ([Vanguard, as of 2026](https://www.nl.vanguard/professional/vanguard-365/cost-averaging)).

<div class="example" markdown>

### Worked example: three price paths

A fund starts at C$100 and moves by a fixed 1% a month for 12 months (made up, to show the two ends).

| Path | Price after 12 months | Lump sum C$12,000 | C$1,000 a month |
|---|---|---|---|
| Rising 1% a month | C$112.68 | C$13,521.90 | C$12,809.33 |
| Flat | C$100.00 | C$12,000.00 | C$12,000.00 |
| Falling 1% a month | C$88.64 | C$10,636.62 | C$11,247.90 |

The lump sum wins when prices rise and loses when they fall.

</div>

## The one-page plan

Write these lines and keep them with your account statements:

- Goal and date, per account group.
- Target mix and the funds for each slice, with their fees (lesson 2).
- Which account holds which fund.
- Rebalancing rule and the date or band (lesson 7).
- How much you add and when.

<div class="canada" markdown>

### For Canadians

Check your TFSA and RRSP room in CRA My Account before you contribute, and keep your US dividend withholding records for the tax return (part 2). If the cost of your foreign property passes C$100,000, Form T1135 applies ([CRA Q&A, as of 2026](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html)). Brokers differ on which funds each account allows, so check Wealthsimple or IBKR before you plan around a fund.

</div>

## Common mistakes

- Planning the location before the allocation. Fix the mix first.
- Splitting each account into the same mix. The portfolio's mix is what matters, so place funds where they are taxed least.

## Try it

1\. A TFSA holds C$20,000 of a US-listed ETF of US stocks yielding 2%. How much US withholding is lost a year, and would an RRSP lose any?

<details class="solution" markdown>
<summary>Answer</summary>

20,000 x 0.02 x 0.15 = C$60 a year in the TFSA. The RRSP would lose C$0 at the US layer.

</details>

2\. Why do bonds usually go in a registered account before Canadian stocks do?

<details class="solution" markdown>
<summary>Answer</summary>

Bond interest is taxed as income each year in a non-registered account, so sheltering it saves more tax than sheltering stock growth.

</details>

3\. A fund starts at C$100 and falls 1% a month for 12 months. Which wins on C$12,000, the lump sum or C$1,000 a month?

<details class="solution" markdown>
<summary>Answer</summary>

Monthly buying: C$11,247.90 against C$10,636.62 for the lump sum.

</details>

## Part check

1\. An ETF has a NAV of US$40.00 and trades at US$40.10. What is the premium, and what does an authorized participant do?

<details class="solution" markdown>
<summary>Answer</summary>

(40.10 - 40.00) / 40.00 = 0.25%. The AP delivers a basket of stocks for new ETF shares and sells them at the higher price, which pushes the price back toward NAV.

</details>

2\. An index earns 7% before costs. How much more is US$10,000 worth after 30 years in a fund charging 0.10% than in one charging 0.50%?

<details class="solution" markdown>
<summary>Answer</summary>

At 0.10%: 10,000 x 1.069^30 = US$74,016.95. At 0.50%: 10,000 x 1.065^30 = US$66,143.66. The difference is US$7,873.28.

</details>

3\. You hold a US-listed ETF of US stocks. Which account loses 15% of the dividend to US withholding that it cannot recover: the TFSA or the RRSP?

<details class="solution" markdown>
<summary>Answer</summary>

The TFSA. The RRSP is exempt under the treaty.

</details>

4\. A 2x daily-reset fund starts at US$100. Its index rises 5% on day 1 and falls 5% on day 2. What is the fund's value, and what happened to the index?

<details class="solution" markdown>
<summary>Answer</summary>

Day 1: +10%, so US$110. Day 2: -10%, so US$99. The fund lost 1%. The index went 1.05 x 0.95 = 0.9975, a loss of 0.25%.

</details>

5\. Two funds, each with volatility 20% and 10%, are held 50 / 50 with a correlation of 0.5. What is the portfolio's volatility?

<details class="solution" markdown>
<summary>Answer</summary>

Variance = 0.25 x 0.04 + 0.25 x 0.01 + 2 x 0.5 x 0.5 x 0.5 x 0.20 x 0.10 = 0.01 + 0.0025 + 0.005 = 0.0175. Volatility = 13.23%.

</details>

6\. A 50 / 50 portfolio of US$20,000 now holds US$12,000 in stocks and US$8,000 in bonds. What trade rebalances it?

<details class="solution" markdown>
<summary>Answer</summary>

Each target is US$10,000. Sell US$2,000 of stocks and buy US$2,000 of bonds.

</details>

7\. A factor earned 4% a year in the sample. What does McLean and Pontiff's post-publication decline of 58% leave?

<details class="solution" markdown>
<summary>Answer</summary>

4 x 0.42 = 1.68% a year.

</details>

8\. You receive C$12,000. In which kind of market does the lump sum beat monthly investing, and roughly how often did it in Vanguard's study?

<details class="solution" markdown>
<summary>Answer</summary>

When prices rise during the 12 months. It won about two-thirds of the time in the study, because markets rise more often than they fall.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Write your one-page plan from the list above, with your real accounts, funds and fees. |
| 3 | Compute the yearly withholding on your US holdings in each account, using the table in lesson 3. |
| 2 | Put the next rebalancing date in your calendar. |

</div>

## Key terms

- **Asset location**: which account holds which fund, chosen to lower tax and withholding.
- **Lump sum**: investing a whole amount at once.
- **Dollar-cost averaging**: investing equal amounts at regular dates.
- **One-page plan**: a written summary of your goal, mix, funds, accounts and rules.

Next: What futures are<!-- link: ../14-futures/01-what-futures-are.md -->
