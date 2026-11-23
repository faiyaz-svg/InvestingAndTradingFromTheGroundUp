# Crypto ETFs

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">CRYPTO</span>

After this lesson you can say what a spot bitcoin or ether ETF holds, work out how its fee compares with the cost of holding coins yourself, and name what you give up and what you gain by owning the fund.

Before this: [Buying crypto in Canada](04-buying-crypto-in-canada.md), [How ETFs work](../13-etfs-portfolios-and-factors/01-how-etfs-work.md). You need: a calculator.

## The idea

You want exposure to a coin's price but not the work of keys, wallets and platform checks. A **spot crypto ETF** is a fund whose shares trade on a stock exchange like any other ETF and whose assets are the coins themselves, held by a custodian. You buy shares in your brokerage account in a few clicks, in the same app and statement as your stocks.

The first one came from Canada. The Toronto Stock Exchange listed Purpose Bitcoin ETF on February 18, 2021, and described it as the world's first bitcoin ETF ([TSX announcement](https://www.tsx.com/en/news?id=814), as of 2026). Ether ETFs followed on the TSX in April 2021 (press report: [The Block](https://theblock.co/news/ecosystems/2021-04-20-ether-etf-purpose-ci-evolve-begin-trading-canada-102379)).

In the United States, the SEC approved the listing and trading of several spot bitcoin exchange-traded products on January 10, 2024. The agency's chair said the approval did not endorse bitcoin or the products' custody arrangements, and that investors should be cautious about the risks ([SEC statement](https://www.sec.gov/newsroom/speeches-statements/gensler-statement-spot-bitcoin-011023)). Spot ether ETFs began trading in the US on July 23, 2024, after the SEC declared the funds' registration statements effective on July 22. One fund's SEC filing states both dates ([21Shares Core Ethereum ETF, Form 10-Q, Note 10](https://www.sec.gov/Archives/edgar/data/1992508/000121390024073379/ea0211501-10q_21shares.htm)).

## How it works

### What you own and what you do not

When you hold the ETF you own shares of a fund, not coins. The fund owns the coins, and a custodian holds the keys. The comparison with holding coins yourself:

| | Spot crypto ETF | Coins at a platform | Coins in self-custody |
|---|---|---|---|
| What you own | Fund shares | A claim on the platform | The keys and coins |
| Where you buy | Brokerage account | Crypto platform | Any platform, then withdraw |
| Ongoing cost | Management fee, built into the price | Spread and fee per trade | Network fee when you move coins |
| Trading hours | Exchange hours only | 24 hours, 7 days | 24 hours, 7 days |
| Can you move coins out | No | Yes | Yes |
| Counterparty risk | The fund's custodian and sponsor | The platform | None from a company, plus your own mistakes |

The ETF gives you no way to send coins to a person or use them in DeFi (lesson 3). It does remove the risk of your own key mistakes, and it adds the risk of the fund's custodian.

Two more differences matter for a trader. The ETF trades only when its exchange is open (lesson 6 covers the 24/7 market), so the coin can move while the fund is shut and the fund opens with a gap. And the fund's share price can differ a little from the value of its coins. The value of the coins less costs, per share, is the **net asset value** (NAV). The gap between the market price and the NAV is a **premium** when the price is higher and a **discount** when it is lower.

### The fee

The **management fee** is a yearly percentage of the fund's assets. It is taken from the fund, so the number of coins behind each share falls a little each day. You never see a bill.

\[ V_n = V_0 \, (1 - m)^n \]

- \(V_0\) is the starting value of your holding, in dollars.
- \(m\) is the yearly fee as a fraction (0.4% is 0.004).
- \(n\) is the number of years.
- \(V_n\) is the value after \(n\) years if the coin's price is unchanged.

<div class="example" markdown>

### Worked example: fund fee against platform costs

Fund A is a made-up spot ETF with a 0.40% yearly fee. You invest C$10,000. Assume the coin's price does not change and ignore the broker's commission. The alternative is buying coins at a platform with a 0.9% cost per trade (lesson 4's example), selling at the end.

1. Fund A after 1 year: 10,000 x 0.996 = C$9,960.00.
2. Fund A after 5 years: 10,000 x 0.996^5 = C$9,801.59.
3. Platform after a round trip: 10,000 x 0.991 x 0.991 = C$9,820.81, whatever the holding time.
4. Break-even: 0.996^n = 0.991^2 gives n = 4.5 years (ln 0.982081 / ln 0.996 = 4.51). Hold shorter and the fund is cheaper. Hold longer and the platform is cheaper, ignoring storage costs and the network fee.

The calculation leaves out the spread when you buy or sell the ETF and any premium or discount. Look up each fund's current fee on its own page.

</div>

### What a fund cannot do

A fund tracks the coin's price, so it moves with the coin. It does not remove the coin's volatility (lesson 9 sizes it). It also does not protect you from the sponsor's mistakes. The SEC statement above is explicit that approval was not an endorsement of the custody arrangements.

<div class="canada" markdown>

### For Canadians

A Canadian-listed fund trades in CAD or USD units on the TSX, and a US-listed fund trades in USD. Part 2 covers the conversion cost on US-listed holdings ([USD or CAD, and currency conversion fees](../02-accounts-currency-and-taxes/03-usd-vs-cad-and-fx-fees.md)). Gains from selling fund units in a non-registered account are capital gains or business income on the usual terms (lesson 9). Whether a given fund is allowed in a TFSA, RRSP or FHSA is a question for the fund's prospectus and your broker, so check it before you buy. Look up each fund's fee and holdings on the issuer's page. Fees change, so the lesson quotes none.

</div>

## Common mistakes

- Comparing only management fees. Add the spread, the premium or discount, and the exchange-hours gap.
- Treating the fund as safer because it is regulated. The coin's price risk is unchanged, and the custodian is a new risk.
- Assuming every fund holds coins. Some hold futures contracts instead, which bring the roll costs from part 14 ([Contango, backwardation and basis](../14-futures/05-contango-backwardation-and-basis.md)). Read the fund's holdings.

## Try it

1\. Fund A has a 0.25% fee. What is C$20,000 worth after 3 years if the coin's price is unchanged?

<details class="solution" markdown>
<summary>Answer</summary>

20,000 x 0.9975^3 = C$19,850.37.

</details>

2\. The fund's NAV is C$40.00 per share and it trades at C$40.30. Is that a premium or a discount, and how large?

<details class="solution" markdown>
<summary>Answer</summary>

A premium: (40.30 - 40.00) / 40.00 = 0.75%.

</details>

3\. The coin rises 3% overnight while the exchange is closed. Where does Fund A open, assuming it tracks NAV?

<details class="solution" markdown>
<summary>Answer</summary>

About 3% higher than its last close. The coin traded all night, so the fund opens with a gap that reflects it.

</details>

4\. What two things does a spot ETF let you avoid compared with self-custody, and what one thing does it stop you doing?

<details class="solution" markdown>
<summary>Answer</summary>

You avoid key management and the network fee for moving coins. You cannot withdraw coins or use them in DeFi.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Open one Canadian-listed and one US-listed spot bitcoin or ether ETF page. Write each fee, the custodian's name and whether it holds coins or futures. |
| 3 | Find the premium or discount to NAV for one of them. Compute it as a percentage. |
| 2 | In your [trade journal](../practice/trade-journal.md), note which way of owning crypto fits your plan and why. |

</div>

## Key terms

- **Spot crypto ETF**: an exchange-traded fund that holds the coins themselves.
- **Custodian**: the company that holds a fund's coins and keys.
- **Management fee**: the yearly percentage of assets the fund takes to run itself.
- **Net asset value (NAV)**: the value of the fund's assets less costs, per share.
- **Premium**: the market price of a share above its NAV.
- **Discount**: the market price of a share below its NAV.

Next: [Crypto market structure: perps, funding and liquidations](06-crypto-market-structure.md)
