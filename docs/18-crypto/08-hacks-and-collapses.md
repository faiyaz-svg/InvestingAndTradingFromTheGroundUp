# Hacks and collapses

<span class="tag tag-case">Case study</span> <span class="tag tag-part">CRYPTO</span>

After this lesson you can describe what happened at Mt. Gox, Terra and FTX using regulator and court sources, say what failed in each, and turn them into a checklist for custody, counterparty and stablecoin risk.

Before this: [Blockchains, keys and wallets](02-blockchains-keys-and-wallets.md), [Ethereum, stablecoins and DeFi](03-ethereum-stablecoins-and-defi.md). You need: a calculator.

## The idea

A price chart shows what a coin did. It does not show whether the place holding your coins still existed. Three failures show three different risks: a platform whose coins were stolen, a token whose design could not survive a run, and an exchange that used customer money for its own bets. Each case below uses regulator or prosecutor documents.

## The cases

### A hacked exchange in 2014: custody

Mt. Gox was a Tokyo-based bitcoin exchange. In February 2014 it halted withdrawals and then filed for bankruptcy protection, saying a large number of bitcoins were missing, and the loss was later alleged to have started in 2011. In June 2023 the US Justice Department announced charges against two Russian nationals, Alexey Bilyuchenko and Aleksandr Verner. The indictment alleges that from September 2011 through at least May 2014 they and others took about 647,000 bitcoin, most of what Mt. Gox customers held, and laundered it ([Justice Department release](https://www.justice.gov/usao-sdny/pr/russian-nationals-charged-hacking-one-cryptocurrency-exchange-and-illicitly-operating)). These are allegations, not proven facts.

The lesson is custody. Customers held a claim on the exchange, not their own keys (lesson 2), so the theft was their loss. Creditors waited for years to learn what they would get back.

### Terra and Luna, May 2022: algorithmic stablecoins

TerraUSD (UST) was an algorithmic stablecoin. It had no dollar reserve. It was meant to stay at US$1 because the system let anyone swap 1 UST for US$1 worth of a sister token, Luna, and the other way round. The SEC's press release describes what happened in May 2022: after UST dropped below its peg, UST and Terraform's other tokens fell to nearly zero, wiping out about US$40 billion in market value ([SEC press release 2024-73](https://www.sec.gov/news/press-release/2024-73), as of 2026). After a jury found Terraform Labs and its founder Do Kwon liable for securities fraud in April 2024, the two agreed in June 2024 to pay more than US$4.5 billion, according to the same release.

The design flaw can be shown with simple numbers. A swap that creates Luna when UST is redeemed gives the system a feedback loop.

<div class="example" markdown>

### Worked example: a stylized death spiral

Assume the system redeems 1 UST for US$1 of newly created Luna. Each round, holders redeem 1,000,000 UST. These numbers are made up and simplified.

| Luna price | New Luna created for 1,000,000 UST |
|---|---|
| US$10.00 | 100,000 |
| US$5.00 | 200,000 |
| US$2.00 | 500,000 |
| US$1.00 | 1,000,000 |

1. At US$10.00, 1,000,000 / 10 = 100,000 new Luna.
2. New supply pushes the Luna price down, so the next round of redemptions creates more.
3. At US$1.00 the same redemption creates 1,000,000 Luna, ten times the first round.
4. Each increase in supply lowers the price further, and the falling price scares more UST holders into redeeming.

Nothing outside the system buys the new Luna. The peg held only while people believed it would hold.

</div>

### FTX, November 2022: counterparty risk

FTX was a large exchange. It collapsed in November 2022. Prosecutors in New York said its founder, Sam Bankman-Fried, used FTX customers' money to prop up the finances of Alameda, his trading firm. A jury found him guilty on seven counts on November 2, 2023, and on March 28, 2024 he was sentenced to 25 years in prison, with a forfeiture order of more than US$11 billion ([US Attorney's Office, SDNY](https://www.justice.gov/usao-sdny/pr/samuel-bankman-fried-sentenced-25-years-prison)). Press reports of the trial gave different estimates of the customer losses, so this lesson does not quote one.

The lesson is counterparty risk. A balance on an exchange screen is a promise. If the exchange lends or spends the assets behind that promise, the screen can still show a balance until the day withdrawals stop.

## Turning the cases into rules

| Risk | Case | What to check |
|---|---|---|
| Custody | Mt. Gox | Who holds the keys? How much of your holding sits in one place? |
| Counterparty | FTX | Does the firm publish proof of reserves from an independent auditor, rather than a promise? Is the entity registered where you live (lesson 4)? |
| Stablecoin design | Terra | What backs the token? Is it reserves, or a rule that needs buyers to keep it up? |

1. List every place you hold crypto, with the C$ amount at each.
2. For each, answer the check in the table. If you cannot, treat the amount as at risk of total loss.
3. Set a cap for any one counterparty, as part 3 does for any single position, and do not rely on the price staying up to bail you out.

<div class="canada" markdown>

### For Canadians

Canadian regulators lean on registration and custody terms for platforms (lesson 4). Wealthsimple's crypto page says its holdings are not covered by CIPF or CDIC ([Wealthsimple Crypto](https://www.wealthsimple.com/en-ca/product/crypto), as of 2026), so the protection that applies to stocks does not apply to coins held there. A registered platform has been reviewed. It has not been insured.

</div>

## Common mistakes

- Judging a platform by its past price chart or by its sponsor deals. Neither says whether it holds your coins.
- Treating a stablecoin's calm chart as proof of safety. A stablecoin is calm until its reserve or design is tested.
- Keeping everything in one place because it is convenient.

## Try it

1\. A holder keeps C$6,000 at an exchange, C$3,000 in self-custody and C$1,000 in an ETF. What share sits with the exchange as counterparty?

<details class="solution" markdown>
<summary>Answer</summary>

6,000 / 10,000 = 60%.

</details>

2\. In the death-spiral table, redemptions of 1,000,000 UST at a Luna price of US$0.50 create how many Luna?

<details class="solution" markdown>
<summary>Answer</summary>

1,000,000 / 0.50 = 2,000,000 Luna.

</details>

3\. Why does an exchange balance differ from coins in your own wallet?

<details class="solution" markdown>
<summary>Answer</summary>

The balance is a claim on the exchange, which holds the keys. Coins in your wallet are controlled by your keys and need no one's cooperation to move.

</details>

4\. A stablecoin reports US$1,000 million of tokens and US$1,000 million of reserves, but the reserves are in a single bank. What question is still open?

<details class="solution" markdown>
<summary>Answer</summary>

Whether that one bank can pay on demand. The backing is full on paper, and the concentration in one counterparty is a risk.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Make the list from the steps above: every place you hold or might hold crypto, with the C$ amount and the answer to its check. |
| 3 | Read the SEC press release on Terraform (link above) and note two sentences about what happened in May 2022. |
| 2 | Write in your [trade journal](../practice/trade-journal.md) the largest amount you would leave at one platform. |

</div>

## Key terms

- **Counterparty risk**: the risk that the firm on the other side of your holding or trade cannot pay.
- **Proof of reserves**: a published check that a platform holds the assets behind customers' balances.
- **Peg**: the target price a stablecoin is designed to hold.
- **Death spiral**: a feedback loop in which a falling price causes actions that push the price down further.
- **Run**: many holders trying to redeem at once.

Next: [Crypto taxes and position sizing](09-crypto-taxes-and-sizing.md)
