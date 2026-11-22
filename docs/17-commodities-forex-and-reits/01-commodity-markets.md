# Commodity markets

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">CMDTY</span>

After this lesson you can name the three groups of commodities, say who trades them and why, read a benchmark quote for oil and gold, and work out what a hedge locks in.

Before this: [What futures are](../14-futures/01-what-futures-are.md), [Margin, leverage and mark to market](../14-futures/02-margin-leverage-and-mark-to-market.md). You need: a calculator.

## The idea

An oil company pumps 100,000 barrels a month and sells them at whatever the price is on the day. If oil is US$70 a barrel, that is US$7.0 million. If oil falls to US$60, it is US$6.0 million, and the company still owes the same wages and loan payments. The company would like to know its price in advance. An airline sits on the other side of the same problem: fuel is a large cost, and a higher price hurts it.

A **commodity** is a raw material that is interchangeable from one seller to the next: a barrel of a given grade of oil, an ounce of gold of a given purity, a bushel of a given grade of corn. Because one unit is the same as any other, buyers care mainly about the price, and the price is set in a market. Commodities fall into three groups.

| Group | Examples | What drives the price most |
|---|---|---|
| Energy | Crude oil, natural gas, gasoline, heating oil | Production, inventories, weather, the economy |
| Metals | Gold, silver, copper, aluminum | Industrial demand (copper), investor demand (gold), mine supply |
| Agriculture | Corn, wheat, soybeans, coffee, live cattle | Weather, harvests, exports |

Commodity prices are quoted in a fixed unit and a currency, nearly always US dollars: US$ per barrel for oil, US$ per troy ounce for gold. A **troy ounce** is a unit used for precious metals, about 31.1 grams. 

## Who trades them

Three groups trade commodity futures, and each wants something different.

A **hedger** has a business exposed to the price and uses futures to reduce the risk: the oil producer who fears a fall, the airline that fears a rise, the farmer who wants to fix a price before harvest. (Part 2 defined a hedge as a position that offsets a risk: [Currency risk on US stocks](../02-accounts-currency-and-taxes/05-currency-risk-on-us-stocks.md).) A **speculator** has no use for the commodity and takes the other side of the risk, hoping to profit from price changes. Speculators also supply the trading volume that lets a hedger get in and out quickly. A third group, **arbitrageurs and index funds**, trade the gap between related prices or hold commodity baskets for investors.

<div class="example" markdown>

### Worked example: a producer's hedge

Producer A will sell 100,000 barrels next month. Today the contract for that month trades at US$70.00 per barrel. One contract covers 1,000 barrels (the WTI contract size on CME, as of 2026, see below), so Producer A sells 100 contracts.

Next month, oil has fallen to US$60.00.

1. Physical sale: 100,000 x 60.00 = US$6,000,000.
2. Futures: Producer A sold at 70.00 and buys back at 60.00, a gain of 10.00 per barrel, so 100,000 x 10.00 = US$1,000,000.
3. Total: US$7,000,000, which is US$70.00 per barrel.

If oil had risen to US$80.00, the physical sale brings US$8,000,000, the futures lose US$1,000,000, and the total is again US$7,000,000. The hedge removed the risk of a fall and also the chance of a rise. It locks in a price. (Basis, the gap between the local price and the futures price, makes a real hedge a little less exact.)

</div>

## Benchmarks and exchanges

A **benchmark** is the reference price that other prices are quoted against. Two crude oils are the main ones.

**WTI** (West Texas Intermediate) is the US benchmark. Its futures trade on NYMEX, one of the exchanges owned by CME Group. A contract is 1,000 barrels, quoted in US$ per barrel ([CME Group, WTI futures specifications](https://www.cmegroup.com/markets/energy/wti-crude-oil-futures.contractSpecs.html), as of 2026). One dollar of price move is worth US$1,000 per contract.

**Brent** is the international benchmark, priced from North Sea crude. Brent futures trade on ICE Futures Europe, also with a size of 1,000 barrels per contract and a price in US$ per barrel, and the final settlement is tied to the ICE Brent Index ([ICE, Brent futures specifications](https://www.ice.com/products/219/specs), as of 2026). Brent and WTI usually differ by a few dollars, and the gap itself moves.

Gold futures trade on COMEX, also part of CME Group ([CME Group, gold futures](https://www.cmegroup.com/markets/metals/precious/gold.html), as of 2026; read the page for the contract size, because CME lists several sizes). The gold price quoted in the news is usually the front futures contract or the "spot" price, the price for immediate delivery, which is set among large dealers. Grains such as corn and wheat trade on CBOT, another CME Group exchange. Which contracts your own broker offers differs by account, and Part 14 covers futures access ([Futures in Canada](../14-futures/07-futures-in-canada.md)).

A futures contract on a commodity can end in **physical delivery** (the seller delivers the barrels or the metal) or in cash settlement. Most traders close the position before that date, a point lesson 3 returns to ([Commodity ETFs and roll costs](03-commodity-etfs-and-roll-costs.md)). Prices of different expiry months make up a curve, which [Contango, backwardation and basis](../14-futures/05-contango-backwardation-and-basis.md) explains.

## How commodities differ from stocks

A stock gives you a claim on future profits, so Part 10 can value it from cash flows. A barrel of oil has no cash flow. Its price is set by supply, demand and the cost of storing it, which is why the carry formula in Part 14 includes storage costs and a convenience yield. A commodity has no earnings report, but it has its own calendar: inventory reports, production decisions and weather. Part 10 covered the proved reserves and breakeven price that producers report ([Comparables and industry KPIs](../10-valuation-and-research/07-comparables-and-industry-kpis.md)).

<div class="canada" markdown>

### For Canadians

Canada is a large oil producer, and the oil and gas sector is a big part of the TSX, so oil moves Canadian stocks and, as lesson 5 shows, the Canadian dollar ([What moves currencies](05-what-moves-currencies.md)). The WTI and Brent prices above are in US dollars. A Canadian refinery or airline often pays in CAD, so the USD/CAD exchange rate is part of its price.

</div>

## Common mistakes

- Reading a futures price as the price of the physical good today. The front contract and the spot price can differ, and later contracts differ again.
- Treating a hedge as a way to make money. It fixes a price. A producer that hedges at US$70 gives up the gain if oil goes to US$80.
- Mixing barrels and contracts. One WTI contract is 1,000 barrels, so a US$1 move is US$1,000 per contract, not US$1.

## Try it

1\. A refinery will sell 50,000 barrels of product next month and sells 50 WTI contracts at US$72.00 to hedge. Next month the price is US$65.50. What price per barrel does the hedge lock in, ignoring basis?

<details class="solution" markdown>
<summary>Answer</summary>

Futures gain = (72.00 - 65.50) x 50,000 = US$325,000. Physical sale = 65.50 x 50,000 = US$3,275,000. Total = US$3,600,000, which is 3,600,000 / 50,000 = US$72.00 per barrel.

</details>

2\. An airline buys 20 WTI contracts at US$74.00 to fix its fuel cost. Oil rises to US$80.00 at expiry. What is the futures gain, and why is it not a profit?

<details class="solution" markdown>
<summary>Answer</summary>

Gain = (80.00 - 74.00) x 1,000 x 20 = US$120,000. The airline pays US$6.00 per barrel more for the physical fuel, so the gain only offsets the higher cost and the net price stays near US$74.00.

</details>

3\. Which group (hedger or speculator) is each? (a) A wheat farmer sells futures before planting. (b) A trader buys oil futures because she expects a cold winter and has no use for oil.

<details class="solution" markdown>
<summary>Answer</summary>

(a) A hedger, because the farmer has the physical exposure. (b) A speculator, because she has no business exposure to oil and takes price risk for a possible profit.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Open the [CME Group WTI specifications](https://www.cmegroup.com/markets/energy/wti-crude-oil-futures.contractSpecs.html) and write down the contract size, the tick size and the tick value in dollars. |
| 3 | Find today's gold and WTI prices on your broker's quote page. Write each with its unit and currency. |
| 2 | Write one sentence on which hedger would gain most from a 10% rise in oil, and which would lose. |

</div>

## Key terms

- **Commodity**: a raw material that is interchangeable from one seller to the next.
- **Troy ounce**: the unit for precious metals, about 31.1 grams.
- **Hedger**: a trader with a business exposure to the price who trades futures to reduce risk.
- **Speculator**: a trader who takes price risk for a possible profit and has no use for the commodity.
- **Benchmark**: the reference price against which other prices are quoted.
- **WTI**: West Texas Intermediate, the US crude benchmark, traded on NYMEX.
- **Brent**: the international crude benchmark, traded on ICE Futures Europe.
- **NYMEX and COMEX**: CME Group exchanges for energy and for metals.
- **Spot price**: the price for immediate delivery.
- **Physical delivery**: settling a contract by handing over the actual commodity.

Next: [What moves oil and gold](02-what-moves-oil-and-gold.md)
