# AI for market research
<!-- lint-ok: significant (statistical sense) -->

<span class="tag tag-career">Career</span> <span class="tag tag-review">Review</span> <span class="tag tag-part">CAREER</span>

After this lesson you can use a language model to read filings and earnings calls without trusting its numbers, check an AI summary against the filing, and avoid the main traps in testing ideas with a model.

Before this: [Filings and EDGAR](../09-company-financials/01-filings-and-edgar.md), [Earnings season and earnings calls](../09-company-financials/11-earnings-season-and-calls.md) and [Writing a stock pitch](../10-valuation-and-research/09-writing-a-stock-pitch.md). You need: a calculator.

## The idea

You paste a 10-K into a chatbot and ask for a summary. The reply reads well and has numbers in it. One of them is wrong, and nothing in the style of the reply tells you which one. That is the main risk of using a **large language model** (LLM), a program that predicts text from patterns in its training data, for research: it writes fluent text whether or not the content is right.

Used with care, an LLM saves reading time. It is a fast first reader. It is not a source. The filing is the source, and every figure you use must be checked against it.

## How it works

### Good uses

- Summarising a long filing or call transcript to decide what to read closely.
- Pulling a list of items from a document (risk factors, customers named, guidance given) that you then check.
- Extracting figures into a table from the filing text you supplied.
- Explaining a term or an accounting treatment, which you then confirm in a textbook or the filing's notes.
- Drafting code to parse data, which you run and test ([Fundamentals from EDGAR](../20-quant-track-in-python/04-fundamentals-from-edgar.md) shows the data path).
- Listing questions to ask about a company.

### Failure modes

| Failure | What it looks like | Defence |
|---|---|---|
| Made-up numbers | A figure that is not in the filing, or a digit changed | Check each figure in the filing |
| Stale knowledge | Facts from before the model's training cutoff, such as an old rate or a past CEO | Supply the document, and date everything |
| Confident errors | A wrong reading of an accounting term, stated flatly | Ask for the page or quote, and read it |
| Dropped context | A summary that leaves out a note or a one-off item | Read the notes and the reconciliation yourself |
| Look-ahead | A test that uses information from after the event | See below |

### Verifying a summary

1. Give the model the document itself, not a request to recall it, and ask for quotes with page or section.
2. For each number in the summary, find it in the filing and write down where.
3. Recompute every derived figure (growth, margins, ratios) yourself.
4. Check the links between statements ([How the three statements connect](../09-company-financials/05-how-the-statements-connect.md)): a summary that breaks one is wrong somewhere.
5. Keep what you checked in your journal, and mark what you did not.

<div class="example" markdown>

### Worked example: checking an AI summary

An AI summary of Northwind's FY2025 statements says:

1. "Revenue grew 15% to US$1,150 million."
2. "The EBIT margin was 21.4%."
3. "Net income rose 34% to US$165 million."
4. "Cash from operations was US$165 million, the same as net income."
5. "Northwind repaid all of its debt."
6. "Cash fell US$20 million to US$130 million."
7. "It bought back US$100 million of stock."

Check against the statements in part 9:

1. Revenue: 1,150 / 1,000 - 1 = 15.0%. Correct.
2. EBIT is 235 and 235 / 1,150 = 20.4%. The summary says 21.4%, a changed digit. Wrong.
3. 165 / 123 - 1 = 34.1%. Correct.
4. The cash flow statement shows cash from operations of US$205 million, which is 40 more than net income because of D&A and stock-based pay, less working capital. Wrong.
5. Debt was 300 at the start, 25 was repaid, and 275 remains. Wrong.
6. Cash went from 150 to 130. Correct.
7. Share repurchases were 100. Correct.

Four of seven are right and three are wrong. All seven read the same. Without the check, the wrong ones go into your pitch.

</div>

### Testing ideas: look-ahead

**Look-ahead bias** means using information that was not available at the time of the decision. A model trained on text through some date has read what happened next. If you ask it "would you have bought this stock in March 2019 given this report?", it can answer from what it knows about the later outcome, and the answer proves nothing. Better tests use documents dated after the model's training cutoff, remove names and dates from the text, or keep the model's output as a list of features that you then test on data in a fixed time order ([Backtesting concepts and biases](../20-quant-track-in-python/08-backtesting-concepts-and-biases.md)). A model's opinion about a stock is an unscored forecast. Log it as one ([Base rates, calibration and forecast logs](../19-data-flows-and-forecasting/07-base-rates-calibration-and-forecast-logs.md)).

### Privacy

Anything you paste goes to the service's servers, and its terms say what is kept and whether it trains future models. Do not paste account numbers, a SIN, brokerage statements, or tax returns. If you work at a firm, do not paste client data or material non-public information, which means facts about a company that are not public and that a buyer would care about. Public filings are fine. Use the service's data settings and your employer's rules.

## In code

The code recomputes the checks in the example from the statement numbers.

<details class="code" markdown>
<summary>In code</summary>

```python
rev0, rev1 = 1000, 1150
ebit, ni0, ni1 = 235, 123, 165
cfo, debt_start, repaid = 205, 300, 25

print(f"revenue growth {rev1 / rev0 - 1:.1%}")
print(f"EBIT margin {ebit / rev1:.1%}")
print(f"net income growth {ni1 / ni0 - 1:.1%}")
print(f"CFO minus net income {cfo - ni1}")
print(f"debt left {debt_start - repaid}")
```

</details>

## Common mistakes

- Trusting a number because the reply is confident and well formatted.
- Asking the model for facts about a company from memory, when you can give it the filing.
- Using the model's view on past events as a test of a strategy.

## Try it

1\. A summary says "diluted EPS was US$2.10" for Northwind's FY2025. Find the number from part 9 and say whether it is right.

<details class="solution" markdown>
<summary>Answer</summary>

Diluted EPS for FY2025 was US$1.61 (165 / 102.5 million diluted shares). So US$2.10 is wrong.

</details>

2\. A summary says gross margin was 42.0%. Check it.

<details class="solution" markdown>
<summary>Answer</summary>

Gross profit is 1,150 - 667 = 483, and 483 / 1,150 = 42.0%. Correct.

</details>

3\. Name two things you must not paste into an online AI service.

<details class="solution" markdown>
<summary>Answer</summary>

Any two of: account numbers, a SIN, brokerage statements, tax returns, client data, material non-public information.

</details>

4\. Why is "ask the model whether a stock was a buy in 2018" a poor test?

<details class="solution" markdown>
<summary>Answer</summary>

The model was trained on text written after 2018 and may know what happened next, so the answer can use the outcome. It is look-ahead bias.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 6 | Take a real 10-K or earnings release from EDGAR. Ask an AI tool for a summary with five numbers, then find each number in the filing and mark it right or wrong. |
| 4 | Write the result in your [journal](../practice/trade-journal.md): how many were right, and which kind of error you found. |

</div>

## Part check

1\. Name the three groups into which most finance jobs fall by whose money it is, and give one example of each.

<details class="solution" markdown>
<summary>Answer</summary>

Sell side (investment banking), buy side (a pension fund) and prop trading (a market maker trading its own capital).

</details>

2\. As of 2026, does the Canadian Securities Course qualify a new candidate for CIRO registration?

<details class="solution" markdown>
<summary>Answer</summary>

No, not for new candidates. Under CIRO's model from January 1, 2026, exams are the requirement. People who enrolled in the old courses by December 31, 2025 had a year to finish. Confirm on CIRO's site.

</details>

3\. A record has 36 trades, a mean of +0.30R and a standard deviation of 1.2R. Find the 95% range for the true mean.

<details class="solution" markdown>
<summary>Answer</summary>

SE = 1.2 / 6 = 0.20R. Range = 0.30 plus or minus 1.96 x 0.20 = 0.30 plus or minus 0.39, so -0.09R to +0.69R.

</details>

4\. A pitch's scenarios give US$30, US$40 and US$55 with probabilities 25%, 50% and 25%. The price is US$45. How far is the price above the expected value?

<details class="solution" markdown>
<summary>Answer</summary>

E = 0.25 x 30 + 0.50 x 40 + 0.25 x 55 = 7.5 + 20 + 13.75 = US$41.25. 45 / 41.25 - 1 = 9.1%.

</details>

5\. Depreciation rises by US$20 at a 25% tax rate. What happens to net income and to cash?

<details class="solution" markdown>
<summary>Answer</summary>

Pretax income falls by 20, tax by 5, so net income falls by 15. Cash from operations changes by -15 + 20 = +5, so cash rises by US$5.

</details>

6\. A market maker quotes 6 bid and 8 ask on the sum of two dice. What is the expected profit per trade against a trader who knows nothing, and why can it be negative against another?

<details class="solution" markdown>
<summary>Answer</summary>

Selling at 8 or buying at 6 against a fair value of 7 earns US$1 per unit. Against a trader who has seen a die, the sum's expected value can be far from 7, so the maker loses on average (adverse selection).

</details>

7\. You test 15 independent ideas at the 5% level and none is real. What is the chance at least one looks significant?

<details class="solution" markdown>
<summary>Answer</summary>

1 - 0.95^15 = 1 - 0.4633 = 53.7%.

</details>

8\. An AI summary gives a growth rate that you recompute and find 3 points lower. What do you do?

<details class="solution" markdown>
<summary>Answer</summary>

Trust the filing, not the summary. Find the figures in the filing, recompute, note the error in your journal, and check the other numbers in that summary more closely.

</details>

## Key terms

- **Large language model (LLM)**: a program that predicts text from patterns in its training data.
- **Training cutoff**: the date after which a model has seen no new text.
- **Look-ahead bias**: using information that was not available at the time of the decision.
- **Material non-public information**: facts about a company that are not public and that a buyer would care about.

Next: [Back to the start](../index.md). The reference pages and the practice tools (chart drills, paper trading and the trade journal) stay useful after the last lesson.
