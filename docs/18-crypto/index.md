# Part 18: Crypto

Bitcoin, Ethereum and stablecoins, buying crypto in Canada, crypto ETFs, perps and the risks.

Before this part: Parts 2, 3 and 14.

<!-- lessons:start -->
## Lessons

1. [What bitcoin is](01-what-bitcoin-is.md) (idea)
2. [Blockchains, keys and wallets](02-blockchains-keys-and-wallets.md) (idea)
3. [Ethereum, stablecoins and DeFi](03-ethereum-stablecoins-and-defi.md) (idea)
4. [Buying crypto in Canada](04-buying-crypto-in-canada.md) (canada)
5. [Crypto ETFs](05-crypto-etfs.md) (idea)
6. [Crypto market structure: perps, funding and liquidations](06-crypto-market-structure.md) (idea)
7. [On-chain data and crypto cycles](07-on-chain-data-and-cycles.md) (data)
8. [Hacks and collapses](08-hacks-and-collapses.md) (case study)
9. [Crypto taxes and position sizing](09-crypto-taxes-and-sizing.md) (canada, review)

<!-- lessons:end -->

## Cheat sheet

Rules and dates are as of 2026. Prices in examples are made up.

| Item | Formula or rule |
|---|---|
| Proof of work | \( p = 2^{-k} \), expected guesses \( 2^{k} \) for \(k\) leading zero bits |
| Bitcoin supply | \( 210{,}000 \times (50 + 25 + 12.5 + \dots) \) approaches 21 million BTC |
| Block subsidy | 3.125 BTC after the April 20, 2024 (UTC) halving (144 blocks a day, 450 BTC a day) |
| Ethereum fee | gas used x (base fee + tip), a plain transfer uses 21,000 gas |
| Constant-product pool | \( x \times y = k \) |
| DeFi liquidation value | loan / threshold |
| Round-trip cost | \( 1 - (1 - f)^2 \) for a cost \(f\) per trade |
| Fund fee drag | \( V_n = V_0 (1 - m)^n \) |
| Funding payment | notional x rate, longs pay when the rate is positive |
| Long liquidation price | \( E (1 - 1/L) / (1 - m) \) |
| MVRV | market cap / realized cap |
| Crypto sizing | stop = entry - k x ATR, units = floor(risk / (entry - stop)) |

Rules and checklists:

- Whoever holds the private key controls the coins. An exchange balance is a claim on the exchange.
- Never type a seed phrase into a website. Keep a backup that survives a fire, in a different place from the wallet.
- A stablecoin is a claim on reserves or on a rule. Ask what backs it and who audits it.
- Check the platform's legal entity on the OSC's registered crypto asset trading platforms page before you send money.
- Platforms that apply the OSC limit: a net acquisition cost of C$30,000 over the preceding 12 months for non-eligible investors on assets other than the specified ones (Bitcoin, Ether, Bitcoin Cash, Litecoin and certain stablecoins). Confirm on the OSC's own notice.
- A spot ETF holds coins in a fund, trades in exchange hours and cannot be withdrawn as coins.
- A liquidation price comes before your stop in a leveraged trade. Put the stop first.
- Four halving cycles are too few to test a pattern.
- CRA: a sale, a coin-to-coin trade, a payment in crypto and a gift are dispositions. Wallet-to-wallet transfers between your own wallets are not.
- Keep records for six years: date and time, coin and amount, CAD value, other party, wallet addresses.
- Size a coin with the same method as a stock. The wide ATR makes the position small.

