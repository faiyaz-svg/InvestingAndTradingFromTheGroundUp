# Writing style

These rules apply to every page in `docs/`. The reader is a 4th-year computer science student with an economics minor, living in Toronto. They have done some active trading and want to go further:
- long-term investing
- swing and day trading
- reading company financials and economic data
- options, futures and crypto
- a possible career in finance

They trade US stocks from Canadian accounts at Wealthsimple and Interactive Brokers (TFSA, RRSP or FHSA, a cash account and a margin account), in USD or CAD. They study about 30 minutes a day.

They know programming, basic statistics and some economics. They do not know finance jargon: every term (bid, spread, delta, accrual, duration) is explained the first time it appears. Don't talk down to them.

The goal of each page is that the reader can do or understand something new by the end of it, can check it with numbers, and knows where it fails.

## Voice

- Talk to the reader as "you" in instructions ("Work out the position size"). Use "we" when working through something together ("We want the loss at the stop to be 1% of the account").
- Plain and direct. Terms use the standard names a broker, the CFA curriculum, the SEC or the CRA would use, so the reader can follow other sources later.
- Active voice, present tense, plain verbs.
- Be modest and exact. No hype about strategies, indicators, assets or tools. Say what a method does, what the numbers are, and when it stops working.
- No buy or sell calls. Never say a real stock, ETF or coin is a good or bad buy. Trade examples use made-up stocks (see the conventions table).
- Canadian spelling in English: colour, centre, practise (verb) and practice (noun), cheque, licence (noun). US names keep their spelling (Federal Reserve, Labor Department, Defense).

## How to explain

1. Start with a situation and numbers, then the idea, then the name, then the formula. A trader meets the problem before the vocabulary.
2. The first time a term appears, say what it means in words, and bold it.
3. Every formula is shown with KaTeX and then explained symbol by symbol in a list, with units. Then a worked example puts real-looking numbers through it.
4. Work examples to the end: the reader should be able to check every number with a calculator. Round only at the end, and say how you rounded.
5. Start from what the reader knows (programming, statistics, the math book's lessons) and link it. Link the math book for background instead of re-teaching it, and say in one line what the reader needs from it.
6. Give a method as numbered steps, then refer to the step numbers.
7. Every exercise has an answer you can check: a number, a level on a chart, a yes or no with a reason.
8. Name a common mistake at the step where it happens, not only in a separate list.
9. Say where a method fails. Every strategy and indicator lesson says when it tends to work, when it does not, and what tests found (with the source), in plain words.
10. Never write "clearly", "obviously", "it is easy", "simply", "just" (as in "just buy the dip") or "trivially". Show the step instead.
11. Keep one idea per paragraph, in 2 to 5 sentences. Aim for about 20 words per sentence on average, never more than about 40, and vary the length.
12. Put labels next to what they label: units next to numbers, the currency next to the amount, the source next to the claim.
13. Leave out decoration. No market lore, quotes from famous investors or history asides that don't teach the skill. History has its own part (21).
14. One term per concept. If the book says "stop-loss order", it doesn't also say "protective stop" except once when introducing the term.

## Book conventions

| Thing | Convention |
|---|---|
| Money | Write the currency whenever both currencies appear on a page, or when it could be unclear: US$1,250.50, C$1,710.25. In a passage that is only about US prices, the first amount says US$ and later ones may use $. Commas for thousands, a period for decimals. Negative amounts with a minus sign: -US$240. |
| Tickers | Plain capitals, no $ sign: SPY, AAPL, BTC. Real tickers appear only for real facts (a filing, an ETF's fee, an index). |
| Trade examples | Use made-up stocks: "Stock A", "Stock B" (or "a US$50 stock"). Never put a real ticker in a hypothetical trade with an entry, stop and target. |
| Times | Eastern Time, which is Toronto's time zone: 9:30 a.m. ET, 4 p.m. ET. Say when a time changes with daylight saving. |
| Dates | March 14, 2026 in prose. YYYY-MM-DD in chart specs and data. |
| Percentages and basis points | 2.5%, a 25 basis point (0.25%) rate cut. Write "percentage points" for a change in a rate: from 4.25% to 4.50% is 0.25 percentage points. |
| Big numbers | US$3.2 billion, 1.4 million shares. Use "billion" and "million" in words, not B or M, except in tables and charts. |
| Formulas | KaTeX: inline `\( ... \)`, display `\[ ... \]`. A plain `$` is always a dollar sign. Name variables with letters a reader can say: \(E\) for entry, \(S\) for stop. |
| Canada | Name the account (TFSA, RRSP, FHSA, cash, margin), the broker (Wealthsimple, IBKR) and the rule (CRA, CIRO) exactly. Canadian rules go in a "For Canadians" box unless the whole lesson is about them. |
| Italics | Only for book and report titles and for a word used as a word ("the word *spread* has two meanings"). Never for emphasis. |
| Code | Python 3, pandas. Variable names in English. Code goes in `python` fences inside an In code box. |

## Facts that change

Fees, tax rules, contribution limits, margin rules, broker features, product specs, release schedules and laws change. Each lesson that uses one:

- takes it from the official source at writing time (SEC, FINRA, CFTC, CME, Cboe, the Federal Reserve, BLS, BEA, Treasury, CRA, CIRO, OSC, the Bank of Canada, the broker's own site), never from memory,
- states the year ("as of 2026"),
- links the source at the point of use.

`RESEARCH.md` in the writers' scratchpad holds facts already checked, with sources. If a fact can't be confirmed, leave it out. Results of studies (for example, how often a pattern works) name the study and link it.

## Data and copyright

- Every explanation, example, exercise and dataset is written or made for the book.
- **Price charts use made-up data.** Real stock and index prices are licensed, so all candlestick and price charts are drawn from the synthetic data in `docs/assets/charts/` (made by `tools/make_charts.py`), and the chart caption says so.
- Real numbers may be quoted in text with a source and date: a company's revenue from its 10-K, a CPI release, a Treasury yield, an ETF's fee.
- Figures with real data use only US public-domain sources: BLS, BEA, Treasury, CFTC and SEC filings. Name the source under the figure.
- No copied charts, screenshots, course material or long quotes. Summarise rules (CRA, SEC, FINRA) in your own words, with a link.
- Lightweight Charts (TradingView, Apache-2.0) draws the interactive charts, and IBM Plex (OFL) is the font. Both are credited on the credits page.

## Markdown that works on the site and in VS Code

The same files are read in VS Code's preview and built into the website (Zensical). These rules keep both working.

### Boxes

Use HTML containers with the `markdown` attribute. Leave a blank line after the opening tag and a blank line before the closing tag, or the content inside won't be processed. `DESIGN.md` shows how each one looks.

```html
<div class="example" markdown>

### Worked example: sizing a swing trade

...

</div>

<div class="note" markdown>

...

</div>

<div class="warning" markdown>

...

</div>

<div class="canada" markdown>

### For Canadians

...

</div>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 10 | ... |

</div>
```

Collapsible answer and code:

```html
<details class="solution" markdown>
<summary>Answer</summary>

...

</details>

<details class="code" markdown>
<summary>In code</summary>

...

</details>
```

Don't use `!!!`, `???` or `===` blocks. They need indented content, which VS Code shows as a raw code block.

### Charts, figures and diagrams

- **Price charts** use a `chart` fence (format in `LESSON_TEMPLATE.md`). The data comes from `tools/charts_src/<folder>.yml`. Run `tools/make_charts.py <folder>` and quote levels and dates from its printed summary, so the text matches the chart exactly.
- **Static figures** (payoff diagrams, yield curves, distributions) are drawn by a script in `tools/figures/<folder>/` with `figstyle.save_pair`. Each figure has a dark and a light file, and the lesson shows both lines:

  ```markdown
  ![Alt text that says what the figure shows](../assets/figures/15-options/long-call-dark.svg#only-dark)
  ![Alt text that says what the figure shows](../assets/figures/15-options/long-call-light.svg#only-light)
  ```

- **Diagrams** (flows, structures, how money or orders move) use a `mermaid` fence with short labels. Prefer `flowchart LR` or `flowchart TD`. Keep a diagram to about 12 boxes.
- Every chart, figure and diagram has a sentence before it that says what to look at.

### Links, headings and numbering

- Link between pages with relative paths to the `.md` file: `[R-multiples](../03-risk-and-position-sizing/02-r-multiples.md)`.
- Link the math and CS books with full URLs: `https://faiyaz-svg.github.io/MathFromTheGroundUp/...` and `https://faiyaz-svg.github.io/CSFromTheGroundUp/...`. Check that the page exists.
- Keep punctuation out of headings that other pages link to, so the anchor stays stable.
- Number exercises as `1\.`, `2\.` (with the escaped dot), because the answer box after each one breaks a Markdown list.

## Patterns to avoid

These are signs of AI-generated text, collected from Wikipedia's "Signs of AI writing" page (including its 2026 updates) and from studies of words that language models overuse (Kobak et al. 2024; Juzek and Ward 2025; Liang et al. 2024). One or two of them can appear by chance in human writing; the problem is when they pile up. Treat them as hard rules here anyway, because the whole book is drafted with AI help and would otherwise drift toward them.

### Words: never use

delve, tapestry, testament, pivotal, underscore (as a verb), intricate, intricacies, meticulous, meticulously, showcase, garner, bolster, interplay, vibrant, multifaceted, realm, groundbreaking, renowned, nestled, seamless, seamlessly, commendable, noteworthy, invaluable, transformative, unparalleled, unveil, harness (as a verb), elucidate, burgeoning, foster, quietly, deep dive, boasts, journey, unlock, elevate, master (as a verb), "key role", "key factor", "key takeaway", "key insight", "key concept".

Book senses are allowed:
- "leverage" in its finance sense (borrowed money or exposure larger than your cash), never as a verb meaning "use"
- "key" in "answer key" or a keyboard key
- "master" in "master account" (a broker term)

### Words: use rarely

crucial, vital, essential, comprehensive, notably, additionally, moreover, furthermore, consequently, ultimately, enhance, valuable, insights, practical, remarkable, nuanced, significant, robust, powerful, modern, rich, lush, best practice (name the practice and the reason instead).

"Significant" is fine in its statistical sense ("statistically significant at the 5% level"); allow it on the page with `<!-- lint-ok: significant (statistical sense) -->`. "Modern portfolio theory" is a name.

### Phrases and patterns: never use

- "serves as", "stands as", "functions as" where "is" works.
- Inflated importance: "plays a crucial role", "is a testament to", "is a cornerstone of", "sets the stage for", "marks a shift".
- A trailing "-ing" clause that adds vague commentary: "..., highlighting the importance of risk", "..., underscoring...", "..., showcasing...".
- Disclaimers inside lessons: "It's important to note that", "It's worth noting", "It is worth mentioning". State the warning directly instead: "Watch out: ...". (The book's one disclaimer lives on the "Not financial advice" page and in the footer.)
- Summary endings: a closing paragraph starting "In summary", "In conclusion", "To sum up" or "Overall,".
- Chatbot lines: "Great question", "Certainly!", "Let's dive in", "Let's unpack this", "I hope this helps", "Let me know".
- Vague attribution: "traders agree", "experts say", "it is widely believed", "studies show" without the study. Name the source or drop the claim.
- Negative parallelism: "not only X but also Y", "it's not X, it's Y", "no X, no Y, just Z". The one exception is correcting a specific mistake: "move the stop to break-even, don't widen it".
- False ranges: "from X to Y" where X and Y are not two ends of one scale. Real ranges are fine: "from 1% to 2% of the account".
- Groups of three used for rhythm. A real list of three things is fine.
- Hedging about sources: "while details are limited", "based on available information".
- Hype: "revolutionize", "game-changing", "supercharge", "magic", "secret", "hack", "holy grail", "foolproof", "guaranteed", "can't lose", "to the moon". Say what the thing does and what it can't do.

### Punctuation and characters

- No em dashes (the long dash character) at all. Use a comma, a colon, parentheses or a new sentence.
- En dashes only in numeric ranges, or write "9 to 16".
- Straight quotes and apostrophes only.
- No emoji, and no unicode bullets. Use Markdown `-` lists.
- Few exclamation marks.

### Formatting

- Headings are in sentence case: "How to size a position", not "How To Size A Position". Proper nouns and acronyms keep their capitals: Canada, Toronto, US, ETF, TFSA, CRA, IBKR, Wealthsimple, Nasdaq, Bollinger. Add a name to the allowlist in `tools/lint.py` when a lesson needs one, instead of lowercasing it.
- A term is bold once, where it is defined, and nowhere else. Don't use bold for emphasis.
- Don't write bullet lists where every item starts with a bold label and a colon, except in `## Key terms`. Use a sentence, a table or a real subheading.
- Each page has one H1 (the title). Don't skip heading levels (H2 straight to H4).
- Don't put `---` lines between sections.
- Use a list for real steps or real collections of items. If prose reads fine, use prose.
- Use tables for real tables of values. A two-row table that should be a sentence should be a sentence.

### Don't over-correct

Wikipedia now also flags the opposite extreme: text that never uses a dash or a semicolon, uses only commas and periods, and keeps every sentence between 8 and 20 words. Write like a good trader explaining a trade to a colleague: plain "is" and "has" sentences, a colon or semicolon or parentheses where they fit, an occasional "usually" or "often", and sentences of different lengths.

## Self-check before a page is committed

1. Run `.venv/Scripts/python tools/lint.py <file or folder>`. It searches for em dashes, curly quotes, emoji and banned words, and checks headings, template sections, the practice minutes, chart fences and figure pairs.
2. Search for "serves as", "stands as", "important to note", "worth noting", "In summary", "In conclusion", "Overall,", "not only", "Let's dive", "simply", "just".
3. Recompute every number in Python, and put the check in `tools/checks/<folder>.py` (see `LESSON_TEMPLATE.md`). Run it.
4. Run `.venv/Scripts/python tools/check_code.py <file or folder>`. Every In code snippet must run.
5. Check that each changing fact has a source link and "as of 2026", that trade examples use made-up stocks, and that no buy or sell call appears.
6. Read the page once from top to bottom for rhythm. If several sentences in a row have the same length and shape, rewrite some of them.
