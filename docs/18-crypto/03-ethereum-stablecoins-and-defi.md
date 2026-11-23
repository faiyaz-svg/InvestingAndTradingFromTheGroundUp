# Ethereum, stablecoins and DeFi

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">CRYPTO</span>

After this lesson you can say what a smart contract and gas are, explain how a fiat-backed stablecoin keeps its peg, and work out the price an automated exchange gives you and the point where a DeFi loan is liquidated.

Before this: [Blockchains, keys and wallets](02-blockchains-keys-and-wallets.md). You need: a calculator.

## The idea

Bitcoin's ledger records who owns what. Ethereum, launched in 2015, records that too, and it also runs small programs. A **smart contract** is a program stored on the blockchain that runs exactly as written when someone sends it a transaction. Nobody can edit it after it is deployed (unless its code includes a way to), and every node runs the same code and gets the same result. That makes it possible to build a loan, an exchange or a vault out of code, with no company in the middle.

Ether (ETH) is the coin used to pay for this computing. The cost of a transaction is called **gas**: each operation costs a set number of gas units, and the sender pays a price per unit in gwei (one billionth of an ETH).

\[ \text{fee} = \text{gas used} \times (\text{base fee} + \text{tip}) \]

- Gas used is a count of units. A plain ETH transfer uses 21,000.
- Base fee and tip are prices in gwei per gas unit. The base fee moves with demand and is burned (destroyed); the tip goes to the validator.

Ethereum changed how it agrees on blocks on September 15, 2022, in an upgrade called the **Merge**. It moved from proof of work to **proof of stake**: validators lock up ETH as a deposit, are chosen to propose and vouch for blocks, and lose part of the deposit if they cheat ([ethereum.org on the Merge](https://ethereum.org/en/roadmap/merge/), as of 2026). Proof of stake does not need the energy-hungry guessing that lesson 1 described.

<div class="example" markdown>

### Worked example: a transfer fee

Base fee 20 gwei, tip 2 gwei, a plain transfer of 21,000 gas. The ETH price is US$3,000, a made-up number for this example.

1. Price per gas: 20 + 2 = 22 gwei.
2. Fee in gwei: 21,000 x 22 = 462,000 gwei.
3. In ETH: 462,000 / 1,000,000,000 = 0.000462 ETH.
4. In dollars: 0.000462 x 3,000 = US$1.386, or US$1.39.

A complex contract call can use ten times the gas, and base fees change from block to block.

</div>

## How it works

### Stablecoins

A **stablecoin** is a token designed to hold a steady price, usually US$1. A **fiat-backed stablecoin** is issued by a company that says each token is redeemable for one dollar and that holds reserves (cash, bank deposits, short-term US government debt) against the tokens. The peg holds because traders can redeem or sell tokens near US$1 and profit if the market price drifts away.

Everything then depends on the reserves and on the issuer's honesty. The questions to ask: What exactly backs each token? Are the reserves audited or only attested, and how often? Can anyone redeem directly, or only large clients? The Canadian regulators treat fiat-backed tokens that meet their conditions as "value-referenced crypto assets" (lesson 4).

An **algorithmic stablecoin** has no such reserve. It tries to hold the peg with a rule that links it to a second token. Lesson 8 shows how that failed for Terra in May 2022.

### DeFi in outline

**DeFi** (decentralized finance) is a set of smart contracts that offer financial services without a company holding your money. Two kinds matter here.

A **decentralized exchange** uses a pool of two tokens instead of an order book. A common design is the constant-product pool: the product of the two token amounts stays fixed.

\[ x \times y = k \]

- \(x\) and \(y\) are the amounts of the two tokens in the pool.
- \(k\) is a constant. A trade changes \(x\) and \(y\) but keeps \(k\) the same (fees aside).

<div class="example" markdown>

### Worked example: buying from a pool

A pool holds 100 Coin A and 2,000 US$ stablecoin, so the pool price is 2,000 / 100 = US$20.00 per Coin A. You buy 10 Coin A. Fees are ignored.

1. k = 100 x 2,000 = 200,000.
2. After you take 10, the pool holds 90 Coin A.
3. The stablecoin amount must be 200,000 / 90 = 2,222.22.
4. You pay 2,222.22 - 2,000 = US$222.22.
5. Your average price is 222.22 / 10 = US$22.22, which is 11.1% above the old pool price of US$20.00.

That gap is slippage built into the formula: the larger your trade relative to the pool, the worse the price. The pool's price is now 2,222.22 / 90 = US$24.69.

</div>

A **lending protocol** lets you deposit collateral and borrow against it. Because no one checks your credit, loans are over-collateralized, meaning the collateral is worth more than the loan. If the collateral falls too far, the contract sells it automatically: a **liquidation**.

\[ \text{liquidation value} = \frac{\text{loan}}{\text{threshold}} \]

- Loan is the amount borrowed, in US$.
- Threshold is the highest share of the collateral's value the protocol allows to be borrowed (for example 80%).
- Liquidation value is the collateral value at which the protocol starts selling it.

A borrower deposits US$15,000 of Coin A and borrows US$10,000 of stablecoin. The loan is 10,000 / 15,000 = 66.7% of the collateral. With an 80% threshold, liquidation starts when the collateral is worth 10,000 / 0.80 = US$12,500, which is a fall of 16.7% in Coin A.

### Smart contract risk

Code has bugs. A contract holding money invites attackers, and the blockchain cannot undo a theft. Risks include coding errors, price-feed manipulation, upgrade keys held by a small group, and a stablecoin losing its peg. Auditing lowers the risk and does not remove it. Treat DeFi balances as exposed to the code's failure, in addition to the market risk of the coins.

## Common mistakes

- Calling a stablecoin "cash". It is a claim on an issuer's reserves, and it has traded below US$1 in stress.
- Reading a high DeFi yield as free money. Ask where the yield comes from and what you lend to, and what happens if the contract fails.
- Forgetting gas when the trade is small. A US$1.39 fee on a US$20 transaction is 7%.

## Try it

1\. A transfer uses 21,000 gas at 30 gwei in total. What is the fee in ETH?

<details class="solution" markdown>
<summary>Answer</summary>

21,000 x 30 = 630,000 gwei = 0.00063 ETH.

</details>

2\. The pool holds 100 Coin A and 2,000 US$. You sell 10 Coin A into it. How many US$ do you receive?

<details class="solution" markdown>
<summary>Answer</summary>

k = 200,000. The pool will hold 110 Coin A, so the US$ amount is 200,000 / 110 = 1,818.18. You receive 2,000 - 1,818.18 = US$181.82, an average of US$18.18 per Coin A.

</details>

3\. A borrower posts US$30,000 of collateral, borrows US$18,000, and the threshold is 75%. At what collateral value does liquidation start, and how far must the collateral fall?

<details class="solution" markdown>
<summary>Answer</summary>

Liquidation value = 18,000 / 0.75 = US$24,000. The fall is (30,000 - 24,000) / 30,000 = 20.0%.

</details>

4\. A fiat-backed stablecoin has 1,000 million tokens and reports reserves of US$980 million. What is the backing per token, and what does that mean?

<details class="solution" markdown>
<summary>Answer</summary>

980 / 1,000 = US$0.98 per token. If everyone redeemed, the reserves could not pay each holder US$1.00.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Find the latest reserve report of one fiat-backed stablecoin. Write what the reserves hold and who produced the report. |
| 3 | Look up the current gas price on a public tracker and compute the fee for a 21,000 gas transfer. |
| 2 | In your [trade journal](../practice/trade-journal.md), write which risk in this lesson you would find hardest to check yourself. |

</div>

## Key terms

- **Smart contract**: a program stored on a blockchain that runs as written when called.
- **Gas**: the unit that measures the computing a transaction uses on Ethereum.
- **Merge**: Ethereum's September 15, 2022 switch from proof of work to proof of stake.
- **Proof of stake**: a rule in which validators lock up coins as a deposit and are chosen to vouch for blocks.
- **Stablecoin**: a token designed to hold a steady price, usually US$1.
- **Fiat-backed stablecoin**: a stablecoin backed by reserves of cash and short-term debt.
- **Algorithmic stablecoin**: a stablecoin that tries to hold its peg by a rule instead of reserves.
- **DeFi**: decentralized finance, financial services run by smart contracts.
- **Decentralized exchange**: a smart contract that trades tokens from a pool.
- **Liquidation**: the forced sale of collateral when a loan's backing falls too low.

Next: [Buying crypto in Canada](04-buying-crypto-in-canada.md)
