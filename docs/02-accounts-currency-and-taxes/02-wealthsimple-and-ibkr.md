# Wealthsimple and IBKR compared

<span class="tag tag-canada">Canada</span> <span class="tag tag-part">ACCT</span>

After this lesson you can compare two brokers on the costs and features that matter for a US-stock trader, estimate your own yearly cost with a small model, and say what CIPF does and does not protect.

Before this: [Account types for trading](01-account-types-for-trading.md). You need: a calculator.

## The idea

Both brokers let you trade US stocks in a TFSA, RRSP, FHSA, cash or margin account. They differ in what they charge, how you hold US dollars, and what the platform lets you do. Fees and features change often, so this lesson gives you the questions to ask and a small model for your own numbers, and it marks which figures come from a page I could read.

## What I could confirm and what you must check

| Item | Wealthsimple | IBKR Canada |
|---|---|---|
| Commission on US stocks | None on listed US and Canadian securities ([fee schedule](https://www.wealthsimple.com/legal/fees/trade), as of 2026) | Check the [commissions page](https://www.interactivebrokers.ca/en/pricing/commissions-home.php) |
| Trading a US stock from a CAD account | 1.5% currency conversion fee on each fill (same fee page) | No automatic conversion; you buy the currency yourself, with a small commission per conversion, see the commissions page |
| Trading from a USD account | No conversion fee; the USD account costs $10 a month plus tax (same fee page) | You hold balances in each currency in one account |
| Margin rates | CAD 3.24% to 5.70%, USD 4.50% to 8.00% by amount borrowed, set off its prime rate (4.70% CAD, 7.00% USD as its page showed in November 2026, [margin page](https://www.wealthsimple.com/en-ca/self-directed-investing/margin)) | Benchmark plus a spread by tier, see its [margin rates](https://www.interactivebrokers.ca/en/trading/margin-rates.php) |
| Margin in registered accounts | Linking a TFSA to a margin account is described on its margin page | Not allowed (lesson 1) |
| Paper trading | I found no built-in simulator on its site as of 2026, check | A paper account is created with new live accounts, or on request in Client Portal ([IBKR knowledge base](https://ibkb.interactivebrokers.com/de/node/663)) |

IBKR's pages blocked my fetch tool, so I left its fee numbers out. Open the pages in the table and write the figures into your own copy of this table. The same goes for each broker's list of products (options, futures, crypto): the Wealthsimple page I read lists them, and the IBKR product pages are linked from its commissions page.

## A cost model for your own trading

The costs of a US-stock trader at a Canadian broker are the commission, the currency conversion, the margin interest and any monthly account fee. Write them as a yearly total.

\[ \text{Yearly cost} = N \times (c + 2 f V) + F \]

- \(N\) is the number of round trips (buy then sell) per year.
- \(c\) is the commission per round trip, in C$ (zero if the broker charges none).
- \(f\) is the currency fee per conversion, as a fraction (0.015 for 1.5%).
- \(V\) is the size of each position, in C$.
- The 2 is there because a CAD-account trade converts on the buy and again on the sell.
- \(F\) is the fixed yearly fees, such as a monthly account fee times 12.

<div class="example" markdown>

### Worked example: two made-up brokers

Broker X charges no commission and a 1.5% conversion fee on every fill in a CAD account. Broker Y charges C$5 a round trip, a 0.5% conversion fee and C$120 a year. These are made-up numbers for the example, not a quote from either real broker. You make 40 round trips a year of C$8,000 each.

1. Broker X: 40 x (0 + 2 x 0.015 x 8,000) + 0 = 40 x 240 = C$9,600.
2. Broker Y: 40 x (5 + 2 x 0.005 x 8,000) + 120 = 40 x 85 + 120 = C$3,520.

The currency fee dominates. A broker with free commissions can still cost more, which is why the next lesson looks at conversion.

</div>

The same formula with a conversion-free USD account sets \(f\) to 0 on each trade, but you pay once to convert your cash into US dollars and back (lesson 3).

## CIPF

Confirm on each broker's site that it is a CIRO-regulated dealer and a **CIPF** member. CIPF (Canadian Investor Protection Fund) covers up to $1 million for all general accounts combined (cash, margin, TFSA, FHSA), a separate $1 million for registered retirement accounts (RRSP, RRIF, LIF) and a separate $1 million for RESPs ([CIPF coverage](https://www.cipf.ca/cipf-coverage/about-cipf-coverage), as of 2026). It covers assets missing if the firm becomes insolvent. It does not cover a fall in the value of your investments.

<div class="canada" markdown>

### For Canadians

If you hold US stocks at a Canadian broker, the account is still a Canadian account and CIPF applies to it. Check where the US shares are held and who the custodian is on the broker's disclosure page. Each broker's agreement also says what happens to your assets in a margin call (lesson 10).

</div>

## Common mistakes

- Comparing commissions only. The conversion fee on a US trade is often larger than any commission.
- Taking a fee from a review or blog. Brokers change fees; read the broker's own page and note the date.
- Treating CIPF as insurance against losing money in the market. It is not.

## Try it

1\. Broker X from the example has 20 round trips of C$10,000 a year. What is the yearly cost?

<details class="solution" markdown>
<summary>Answer</summary>

20 x (0 + 2 x 0.015 x 10,000) = 20 x 300 = C$6,000.

</details>

2\. Broker Y with the same trading (20 round trips of C$10,000) costs how much?

<details class="solution" markdown>
<summary>Answer</summary>

20 x (5 + 2 x 0.005 x 10,000) + 120 = 20 x 105 + 120 = C$2,220.

</details>

3\. You hold C$800,000 in a TFSA, an RRSP and a cash account at one CIPF member: C$300,000, C$300,000 and C$200,000. Which amounts are within CIPF limits if the firm fails and all of it is missing?

<details class="solution" markdown>
<summary>Answer</summary>

The TFSA and the cash account are general accounts: 300,000 + 200,000 = C$500,000, under the C$1 million limit. The RRSP is a separate category: C$300,000, under its own C$1 million. All C$800,000 is within the limits.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Open your broker's fee page and copy the commission, the conversion fee and any account fee, with the date. |
| 3 | Estimate your round trips and average position size, and compute your yearly cost with the formula. |
| 2 | Find your broker's CIPF statement and write down which accounts it covers. |

</div>

## Key terms

- **CIPF**: the Canadian Investor Protection Fund, which covers client assets if a member firm becomes insolvent.
- **CIRO**: the Canadian Investment Regulatory Organization, which regulates investment dealers.
- **Conversion fee**: a percentage the broker charges to change CAD into USD or back.
- **Round trip**: a buy and the matching sell.

Next: [USD or CAD, and currency conversion fees](03-usd-vs-cad-and-fx-fees.md)
