# On-chain data and crypto cycles

<span class="tag tag-data">Data</span> <span class="tag tag-part">CRYPTO</span>

After this lesson you can name the common on-chain metrics and compute one of them, say what the halving-cycle story claims, and explain why four cycles cannot confirm it.

Before this: [Crypto market structure: perps, funding and liquidations](06-crypto-market-structure.md). You need: a calculator.

## The idea

A stock's trades go to a tape, but its owners are mostly hidden. A public blockchain works the other way around. Every transfer is recorded in the open: which address sent how many coins to which address, and when. **On-chain data** is that public record, turned into numbers. Analysts count transactions, track how long coins sit still, and watch how many coins move to and from exchanges.

This is a real data source that stocks do not have, and it needs care. Addresses are not people. One person can control thousands of addresses, and one exchange address can hold the coins of many customers. Every on-chain metric is an estimate built on guesses about who owns what.

## How it works

### Common metrics, as concepts

| Metric | What it counts | A common reading |
|---|---|---|
| Active addresses | Addresses that sent or received coins in a day | Network use, though one user can have many addresses |
| Transaction count and fees | Transfers and what senders paid | Demand for block space |
| Hash rate | Total proof-of-work guesses per second (bitcoin) | Mining investment and network security |
| Exchange net flow | Coins moving into minus out of exchange addresses | Coins sent in may be for sale; coins sent out may be held |
| Coin age | How long coins have sat unmoved | Long-held coins are less likely to be sold soon |
| Realized cap | Each coin valued at its price when it last moved | A cost-basis estimate for the whole network |

Most vendors publish these through an interface that is free for a few metrics and paid for the rest. Part 19 covers the licences on data like this ([Free data sources and their licences](../19-data-flows-and-forecasting/01-free-data-sources.md)).

### Realized cap and MVRV

**Market cap** values every coin at today's price. **Realized cap** values each coin at the price when it last moved on the chain, as a stand-in for what its holder paid. Their ratio is **MVRV** (market value to realized value).

\[ \text{MVRV} = \frac{\text{market cap}}{\text{realized cap}} \]

- Market cap is the coin supply times today's price, in US$.
- Realized cap is the sum, over each coin, of the price when it last moved, in US$.
- A value above 1 means holders in total sit on a gain; below 1, a loss.

<div class="example" markdown>

### Worked example: MVRV from three groups

Coin A has 1,000 coins in three groups, by when they last moved. The price today is US$15.00.

| Coins | Price when last moved |
|---|---|
| 400 | US$5.00 |
| 400 | US$12.00 |
| 200 | US$25.00 |

1. Market cap: 1,000 x 15.00 = US$15,000.
2. Realized cap: 400 x 5.00 + 400 x 12.00 + 200 x 25.00 = 2,000 + 4,800 + 5,000 = US$11,800.
3. MVRV: 15,000 / 11,800 = 1.27.
4. On average, holders are up 27%. The last 200 coins are held at a loss of (15 - 25) / 25 = -40%.

A high MVRV is often read as a sign of a stretched market and a low one as a sign of a washed-out market. Whether that reading predicts anything is a testing question. It is not a rule, and this book does not know of a test that settles it.

</div>

### The halving-cycle story

Bitcoin's halvings (lesson 1) happened at blocks 210,000, 420,000, 630,000 and 840,000: on November 28, 2012, July 9, 2016, May 11, 2020 and April 20, 2024, by UTC date (the 2024 halving fell on the evening of April 19 in Toronto; check each date on a block explorer, as of 2026). The story that traders tell goes like this: each halving cuts the new supply, demand rises, the price climbs for a year or so, peaks, then falls by a large share and bottoms before the next halving. People call that pattern the four-year cycle.

The story has some logic. It also has two problems.

First, the halving is scheduled and public, so any effect on supply is known years in advance. A market that prices in known future events would not wait for the day to react.

Second, there are four halvings. That is four cycles, and the timing of the peaks and troughs in them is the data. Four points cannot separate a real pattern from a coincidence. The standard 95% interval for a mean from \(n\) observations uses a critical value from the t distribution (see the math book's [confidence intervals](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/08-statistics/02-confidence-intervals/) lesson for the background). For \(n = 4\) that value is 3.18, against 1.96 for a large sample, so the interval is 3.18 / 1.96 = 1.62 times wider, before counting the problem that the four cycles overlap with other events: interest-rate changes, the 2022 collapses of lesson 8 and the ETF approvals of lesson 5. A pattern with four observations and five explanations is a story. This book knows of no published test that shows the halving date predicts the price peak, and this book does not recommend a trade on it.

The chart shows made-up weekly bars (built from weekday data only, unlike a real crypto market) with the shape of the story: a rise, a peak and a long fall. It teaches the arithmetic of a drawdown. It is not evidence about any real coin.

```chart
data: 18-crypto/coin-a-cycle.json
title: Coin A, weekly: a made-up boom and bust
level: 32.35 | Highest close
level: 6.80 | Last close
caption: The highest weekly close was 32.35 in the week of 2024-06-24, and the last close was 6.80.
```

The highest close is 32.35 and the last is 6.80, a drop of (6.80 - 32.35) / 32.35 = -79.0%. To get back to the old high from 6.80, the price must rise 32.35 / 6.80 - 1 = 376%. Part 3 explains why drawdowns are so hard to recover from ([Drawdowns and risk of ruin](../03-risk-and-position-sizing/08-drawdowns-and-risk-of-ruin.md)).

## Common mistakes

- Treating an address as a person. Exchanges, funds and wallets hold many customers' coins.
- Trusting a metric because its chart looks right in hindsight. Test it on data it was not fitted to.
- Building a plan on a four-point pattern.

## Try it

1\. Realized cap is US$11,800 and market cap is US$9,440. What is MVRV, and what does it say?

<details class="solution" markdown>
<summary>Answer</summary>

9,440 / 11,800 = 0.80. Holders in total sit on a loss of 20% relative to what the network last paid.

</details>

2\. After the 2024 halving a block pays 3.125 BTC, down from 6.25. By what percentage did new supply per block fall?

<details class="solution" markdown>
<summary>Answer</summary>

(3.125 - 6.25) / 6.25 = -50%.

</details>

3\. A coin falls 75% from its high. What gain is needed to return to the high?

<details class="solution" markdown>
<summary>Answer</summary>

The price is 0.25 of the high. 1 / 0.25 - 1 = 3.00, so a 300% gain.

</details>

4\. Why can four halving cycles not confirm that halvings cause price peaks?

<details class="solution" markdown>
<summary>Answer</summary>

Four observations give wide uncertainty (a t critical value of 3.18 against 1.96), and other events overlap each cycle, so the halving cannot be separated from them.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | On a free public data page, find the active addresses and the hash rate for bitcoin. Write the values and the date. |
| 3 | Find the date of the latest halving on a block explorer. Count the blocks to the next one. |
| 2 | In your [trade journal](../practice/trade-journal.md), write one on-chain metric you would want tested before you used it, and how you would test it. |

</div>

## Key terms

- **On-chain data**: the public record of transfers on a blockchain, turned into numbers.
- **Active addresses**: the number of addresses that send or receive coins in a period.
- **Hash rate**: the total proof-of-work guesses per second on the network.
- **Exchange net flow**: coins moving into exchange addresses minus coins moving out.
- **Realized cap**: the sum of each coin valued at its price when it last moved.
- **MVRV**: market cap divided by realized cap.
- **Four-year cycle**: the claim that bitcoin's price follows a pattern tied to the halvings.

Next: [Hacks and collapses](08-hacks-and-collapses.md)
