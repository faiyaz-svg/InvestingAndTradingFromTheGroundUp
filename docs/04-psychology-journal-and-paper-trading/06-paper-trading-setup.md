# Setting up paper trading

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">MIND</span>

After this lesson you can open a paper trading account, set rules that make its results closer to a live account, and adjust a paper fill for the slippage and fees you would have paid.

Before this: [Reviewing your trades](05-reviewing-your-trades.md), and [Order types](../01-how-markets-work/05-order-types.md). You need: a calculator and a free account at one of the platforms below.

## The idea

**Paper trading** means placing trades in a simulator with fake money, at real prices. It costs nothing, and it lets you practise your plan, your checklist and your journal before a mistake costs money.

It has limits you should know first. In a simulator nobody else's order is competing with yours, and your fear of loss is weak. A paper account also fills orders more kindly than a live market. IBKR says its simulated fills come from the top of the book with no deep book access, and that stop and other complex order types are always simulated, so they may behave differently than in a live account ([IBKR, about paper trading accounts](https://www.ibkrguides.com/clientportal/aboutpapertradingaccounts.htm), as of 2026).

So paper trading proves that you can follow a plan. It does not prove that the plan makes money, and it does not show how you will feel with real money at risk. The rest of this lesson makes it as close to live as it can be.

## How it works

### Where to paper trade

| Platform | How to start | Check before relying on it |
|---|---|---|
| IBKR paper account | In Client Portal: Settings, Account Configuration, Paper Trading Account. Paper accounts start with US$1,000,000 of simulated equity ([IBKR Campus](https://www.interactivebrokers.com/campus/glossary-terms/paper-trading-account/), as of 2026). You can choose to share real-time market data from your live account with it ([IBKR](https://www.ibkrguides.com/clientportal/papertradingaccount.htm)). | The fill rules above. Live data in the paper account depends on your live account's data subscriptions and the share setting. |
| TradingView paper trading | In Supercharts, click Trade, pick Paper Trading from the broker list, then Connect. TradingView says it is available to all users and uses simulated money ([TradingView help](https://www.tradingview.com/support/solutions/43000516466-paper-trading-main-functionality/), as of 2026). | Which plan features (alerts, indicators per chart) your plan includes. |
| Wealthsimple | Wealthsimple's public pages did not list a paper trading mode when this was checked in 2026. Check the app and its help centre before you assume it has one. | Whether it exists at all. |

You can also paper trade by hand: write each trade in the journal with the entry, stop and target, and fill it from a chart. The journal then is the account.

### Rules that make paper realistic

1. Size by your real account. IBKR paper starts at US$1,000,000, but your real account may be US$25,000. Use the position-sizing formula with the real number ([Position sizing with fixed fractional risk](../03-risk-and-position-sizing/04-fixed-fractional-sizing.md)), not the paper balance.
2. Add costs. Take fees from your real broker's schedule, and add slippage to each fill (below).
3. Count a limit order as filled only if the price trades through it. A buy limit at 49.95 is filled if the stock trades at 49.94 or lower, not if it only touches 49.95.
4. Run one setup at a time, so the results mean something (lesson 5).
5. Journal every trade, both stages, before you click.
6. Keep your daily loss limit and cooling-off rule. Breaking them on paper trains you to break them live.

```chart
data: 04-psychology-journal-and-paper-trading/paper-fill.json
title: Stock A, daily: a limit order that only touched
level: 49.95 | Buy limit 49.95
marker: 2026-05-18 | below | Low 49.95
range: 2026-05-04 to 2026-05-26
caption: On May 18 Stock A fell to a low of 49.95 and closed at 50.50. A paper account may fill a buy limit at 49.95 on the touch, but live orders resting at 49.95 would sit in a queue, and the price never traded below it.
```

### Adjusting a paper fill for slippage and fees

**Slippage** is the gap between the price you expected and the price you got ([Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md)). On a paper fill, move the price against you by a set amount. For a liquid stock a few cents is reasonable. For a thin stock use more. Pick the number from the stock's usual spread (Bid, ask and the order book, [lesson 4 of part 1](../01-how-markets-work/04-bid-ask-and-the-order-book.md)).

<div class="example" markdown>

### Worked example: paper against realistic

Account US$25,000, risk 1% = US$250. Stock A: planned entry 50.00, stop 48.50, exit at the target, 53.00, 166 shares. The simulator fills at the exact prices.

Paper result: P/L = (53.00 - 50.00) x 166 = US$498.00. Risk = (50.00 - 48.50) x 166 = US$249.00. R = 498.00 / 249.00 = 2.00.

Realistic result with slippage of US$0.05 per share each way and US$2.00 in fees:

1. Entry = 50.00 + 0.05 = 50.05. Exit = 53.00 - 0.05 = 52.95.
2. P/L = (52.95 - 50.05) x 166 - 2.00 = 481.40 - 2.00 = US$479.40.
3. Risk = (50.05 - 48.50) x 166 = US$257.30.
4. R = 479.40 / 257.30 = 1.86.

The gap, 2.00R against 1.86R, is the cost the simulator hid. It is larger for tighter stops, smaller accounts and thinner stocks.

</div>

<div class="canada" markdown>

### For Canadians

A paper account moves no money, so it shows no currency conversion cost. If you would trade US stocks from a CAD balance, add your broker's conversion fee to the journal for each trade ([USD or CAD, and currency conversion fees](../02-accounts-currency-and-taxes/03-usd-vs-cad-and-fx-fees.md)). Paper trades also have no tax effect, so you cannot test the superficial loss rule or account choices with them.

</div>

## Common mistakes

- Using the simulator's huge balance for sizing. A 1% risk of US$1,000,000 teaches you nothing about 1% of your own account.
- Skipping the journal because the money is fake. The journal is the point of the exercise.
- Counting every touch as a fill. The more fills the simulator gives you, the more your paper results will beat live ones.

## Try it

1\. Your real account is US$20,000 and your risk is 1%. Your IBKR paper account shows US$1,000,000. Stock A: entry 40.00, stop 38.00. How many shares do you paper trade?

<details class="solution" markdown>
<summary>Answer</summary>

Use the real account. Risk = 1% of 20,000 = US$200. Risk per share = 2.00. Shares = 200 / 2.00 = 100. A 1% risk on the paper balance would give 5,000 shares, a size you would never trade.

</details>

2\. A buy limit is at 49.95. The day's low is 49.95. Does the trade-through rule count it as filled? What if the low was 49.93?

<details class="solution" markdown>
<summary>Answer</summary>

At a low of 49.95, no: the price touched the limit but did not trade through it. At a low of 49.93, yes: the price traded below the limit by 0.02.

</details>

3\. Entry 20.00, stop 19.00, target 23.00, 200 shares. Slippage of 0.04 each way, fees US$2.00. What is the realistic R?

<details class="solution" markdown>
<summary>Answer</summary>

Entry = 20.04, exit = 22.96. P/L = (22.96 - 20.04) x 200 - 2.00 = 584.00 - 2.00 = US$582.00. Risk = (20.04 - 19.00) x 200 = US$208.00. R = 582.00 / 208.00 = 2.80. The paper R is (3.00 x 200) / (1.00 x 200) = 3.00.

</details>

4\. Name two things a paper account cannot teach you.

<details class="solution" markdown>
<summary>Answer</summary>

How it feels to hold a losing position with real money (the biases of lesson 1 are weaker without a real loss), and how real fills behave when the market moves fast or your order sits in a queue. Taxes and currency costs are also missing.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 6 | Open an IBKR paper account (request it in Client Portal) or connect TradingView paper trading. Write the date and the starting balance in your journal. |
| 4 | Write your realism rules: the account size you will size from, your slippage per share, your fee per trade, and your fill rule for limit orders. |

</div>

## Key terms

- **Paper trading**: placing trades in a simulator with fake money at real prices.
- **Simulated fill**: an order execution created by the simulator, not by a real exchange.
- **Trade-through rule**: counting a limit order as filled only if the price trades beyond it.
- **Realism rules**: the size, cost and fill rules you add so paper results are closer to live ones.

Next: [From paper to live trading](07-from-paper-to-live.md)
