# Pump and dumps, finfluencers and signal groups

<span class="tag tag-case">Case study</span> <span class="tag tag-part">HIST</span>

After this lesson you can describe how a pump and dump works with numbers, list the red flags that Canadian and US regulators name, and check a signal group's claimed win rate against its sample size and payoff.

Before this: [Win rate, payoff and expectancy](../03-risk-and-position-sizing/03-win-rate-payoff-and-expectancy.md), [GameStop and meme stocks](05-gamestop-and-meme-stocks.md). You need: a calculator.

## The idea

In a **pump and dump**, people buy a stock, promote it to others to push the price up, and sell their own shares into the buying. The promoters profit because the buyers they attracted pay the higher price. The stocks used are usually small, thinly traded ones, where little buying moves the price.

Social media made promotion cheap. A **finfluencer** is a person who gives opinions or tips about money and investing on social media. A **signal group** is a paid or free chat group, often on Discord, Telegram or WhatsApp, where a leader posts trades to copy. Most finfluencers and groups are not frauds, but the same channels carry the schemes that are, so the skill is checking.

## A US case

On December 14, 2022 the SEC charged eight people over a scheme it said produced about US$100 million in fraudulent profits. The SEC said seven defendants bought stocks and then urged their followers on Twitter and in Discord chatrooms to buy, through price targets or posts about their own positions. They allegedly sold when the price or volume rose, without telling their followers they planned to sell. The seven allegedly had hundreds of thousands of followers, and an eighth person was charged with aiding and abetting ([SEC press release 2022-221](https://www.sec.gov/newsroom/press-releases/2022-221), as of 2026). These are the SEC's allegations; the release describes charges, not findings.

## A Canadian warning

The Canadian Securities Administrators (CSA), the umbrella group of provincial securities regulators, issued an investor alert about a version it calls a **ramp and dump**, republished by the New Brunswick regulator on April 16, 2026 ([FCNB, republishing the CSA alert](https://www.fcnb.ca/en/news-alerts/investor-alert-ramp-and-dump-scams-surge-as-fraudulent-investment-groups-target-unsuspecting), as of 2026). The alert says schemes increasingly use social media and closed group chats, and describes how they work. In outline:

1. Scammers target low-priced or thinly traded stocks.
2. They reach people on social media and build trust, sometimes through friendship or a romantic relationship, then invite them into an investment group on a messaging app.
3. In the group, they pressure members to buy specific stocks, with promises of high returns.
4. The buying drives the price up, and many buyers are group members.
5. The scammers sell at the inflated price, and the stock crashes.
6. Victims who bought high lose heavily.

<div class="example" markdown>

### Worked example: who gets the money

This uses a made-up stock. Stock C trades at US$0.80 on a normal day volume of 300,000 shares.

1. The promoters buy 200,000 shares for 200,000 x 0.80 = US$160,000.
2. Followers buy and the price rises to US$2.40, three times the start. The promoters sell all 200,000 at an average of US$2.10 and receive US$420,000, a profit of US$260,000.
3. Their selling is 200,000 / 300,000 = 67% of a normal day's volume. It pushes the price down, and with no more promotion, it falls back to US$0.70.
4. A follower who bought 100,000 shares at an average of US$2.20 paid US$220,000 and holds shares worth US$70,000, a loss of US$150,000, or 68%.

The promoters' profit and the followers' loss come from the same trades. The group needs the followers to buy before the promoters sell.

</div>

## Red flags

| Red flag | Why it matters |
|---|---|
| An invitation to a private group about one stock | The group's purpose is to get you to buy the same stock |
| A claim of inside information or a special link to the company | Trading on inside information is illegal, and the CSA lists such claims as a red flag |
| A small, unfamiliar stock with a small float, often foreign-based | Little buying moves the price, and there is little public information |
| Pressure to act quickly, around a supposed event | Time pressure stops you from checking |
| Instructions to buy at a set price, quantity and date, then to confirm | Your buying is the product |
| Fake credentials, or impersonating a registered professional or a known firm | Check the person in the registration search (lesson 9) |
| No disclosure of payment or a position in the stock | The adviser's interest may be the opposite of yours |

Most of these come from the CSA alert. A good check is to ask who profits if you buy.

## Checking a signal group's claims

A group may advertise a win rate. Two tests come from part 3.

<div class="example" markdown>

### Worked example: a claimed 80% win rate

A group says it won 16 of its last 20 trades, an 80% win rate.

1. The standard error of a win rate is sqrt(p(1 - p) / n) = sqrt(0.8 x 0.2 / 20) = 0.0894, or 8.9 points.
2. A rough 95% range is the rate plus or minus 1.96 standard errors: 80% plus or minus 17.5 points, so 62.5% to 97.5%.
3. The win rate says nothing about size. If wins average +0.5R and losses average -3R, the expectancy is 0.8 x 0.5 - 0.2 x 3 = 0.40 - 0.60 = -0.20R per trade.

So an 80% win rate on 20 trades is compatible with a 63% true rate, and with a negative expectancy. The questions are the size of the wins and losses, the number of trades, and whether the record is audited ([Win rate, payoff and expectancy](../03-risk-and-position-sizing/03-win-rate-payoff-and-expectancy.md)).

</div>

## What to do

Check before you act (lesson 9 shows how): search the person and firm in the registration search; look for a disclosed payment; look up the stock's float and average volume; and wait a day. If you think you have seen a scheme, report it (lesson 9).

<div class="canada" markdown>

### For Canadians

The OSC has published research on finfluencers' influence on retail investors ([OSC, Social media and retail investing: the rise of finfluencers](https://www.osc.ca/en/investors/investor-research-and-reports/social-media-and-retail-investing-rise-finfluencers), as of 2026), and it runs alerts on its investor pages. The CSA and CIRO published Staff Notice 31-369 in December 2025, which explains how securities law applies to finfluencer activity ([OSC copy](https://www.osc.ca/en/securities-law/instruments-rules-policies/3/31-369/joint-canadian-securities-administrators-and-canadian-investment-regulatory-organization-staff)). Generally, a person or firm that gives advice on securities as a business must be registered in Canada, which is why the registration search in lesson 9 is the first check.

</div>

## Common mistakes

- Judging a group by its screenshots of wins. Screenshots show the wins someone chose to post.
- Treating a rising price as proof. In a pump the price rises because the promoters' followers are buying.
- Believing a friendship or relationship that started online and leads to a stock tip. The CSA lists it as a step in the scheme.

## Try it

1\. Promoters buy 100,000 shares at US$0.50 and sell them at an average of US$1.20. What is their profit?

<details class="solution" markdown>
<summary>Answer</summary>

Cost 100,000 x 0.50 = US$50,000. Proceeds 100,000 x 1.20 = US$120,000. Profit US$70,000.

</details>

2\. A group claims 9 wins in 10 trades. What is the standard error of its win rate?

<details class="solution" markdown>
<summary>Answer</summary>

p = 0.9, n = 10. sqrt(0.9 x 0.1 / 10) = sqrt(0.009) = 0.0949, or 9.5 points.

</details>

3\. A group wins 70% of trades at +1R and loses 30% at -3R. What is the expectancy?

<details class="solution" markdown>
<summary>Answer</summary>

0.7 x 1 - 0.3 x 3 = 0.7 - 0.9 = -0.2R per trade.

</details>

4\. A promoter sells 150,000 shares into a stock that trades 500,000 shares on a normal day. What share of a normal day is that?

<details class="solution" markdown>
<summary>Answer</summary>

150,000 / 500,000 = 30%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Pick a finance account you follow. Write whether it discloses payments or positions, and whether you can find the person or firm in the CSA National Registration Search. |
| 4 | Read the SEC press release 2022-221 (link above) and write the three facts about how the scheme worked. |
| 2 | In your [trade journal](../practice/trade-journal.md), add a rule: no trade from a tip until you have checked the float, average volume and who profits. |

</div>

## Key terms

- **Pump and dump**: buying a stock, promoting it to push the price up, and selling into the buying.
- **Ramp and dump**: the CSA's name for a version run through social media and group chats.
- **Finfluencer**: a person who gives money or investing opinions on social media.
- **Signal group**: a chat group where a leader posts trades to copy.
- **Float**: the shares of a company available to trade.
- **Insider information**: non-public information that could move a price; trading on it is illegal.

Next: [Prop firms and checking registration](09-prop-firms-and-checking-registration.md)
