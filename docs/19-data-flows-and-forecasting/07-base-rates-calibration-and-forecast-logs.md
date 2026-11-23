# Base rates, calibration and forecast logs

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">DATA</span>

After this lesson you can start a forecast from a base rate, state a view as a probability, score a set of forecasts with the Brier score, and read a calibration plot.

Before this: [The trade journal](../04-psychology-journal-and-paper-trading/04-the-trade-journal.md), and [basic probability](https://faiyaz-svg.github.io/MathFromTheGroundUp/02-middle-school/07-statistics-and-probability/02-basic-probability/) in the math book. You need: a calculator, and Python if you try the code box.

## The idea

Will Stock A gap up after its next earnings report? A trader says "probably". That word cannot be checked. A trader who says "60%" can be scored after the event, and again after fifty events.

Start with the base rate. The **base rate** is how often the event happens in a set of similar past cases (the reference class). Suppose that in a made-up record of 40 earnings reports from similar stocks, 18 gapped up at the open. The base rate is 18 / 40 = 45%. That is your starting forecast. You then move it up or down for reasons you can name, and you write the reasons down. The common error is skipping this step and starting from the story about the company. The math book's lesson on [conditional probability and Bayes](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/07-probability/02-conditional-probability-and-bayes/) shows how evidence should shift a starting probability.

A **probability forecast** is a number from 0 to 1 (or 0% to 100%) for an event that will resolve yes or no. A **forecast log** is a file where you record each forecast before the event, then the outcome after.

## How it works

### Scoring forecasts

The **Brier score** measures the average squared gap between each forecast and what happened:

\[ B = \frac{1}{N} \sum_{i=1}^{N} (f_i - o_i)^2 \]

- \(N\) is the number of forecasts.
- \(f_i\) is the forecast probability for event \(i\), between 0 and 1.
- \(o_i\) is the outcome: 1 if the event happened, 0 if not.
- \(B\) runs from 0 (perfect) to 1 (always certain and wrong). Lower is better.

Always forecasting 50% scores 0.25, whatever happens, so 0.25 is a reference line. Some sources, including tournaments on geopolitical questions, add the squared error for both outcomes, which doubles the score and gives a range of 0 to 2. Compare scores only inside one definition.

<div class="example" markdown>

### Worked example: three forecasts by hand

1. You forecast 0.8 for an event that happens: (0.8 - 1)^2 = 0.04.
2. You forecast 0.3 for an event that does not happen: (0.3 - 0)^2 = 0.09.
3. You forecast 0.9 for an event that does not happen: (0.9 - 0)^2 = 0.81.
4. Brier score: (0.04 + 0.09 + 0.81) / 3 = 0.3133.

The score is worse than 0.25, the always-50% line, because of one confident miss. The figure shows why: the penalty grows with the square of the miss.

</div>

![Brier penalty against forecast probability for an event that happens and one that does not, with three example forecasts marked](../assets/figures/19-data-flows-and-forecasting/brier-penalty-dark.svg#only-dark)
![Brier penalty against forecast probability for an event that happens and one that does not, with three example forecasts marked](../assets/figures/19-data-flows-and-forecasting/brier-penalty-light.svg#only-light)

### Calibration

A forecaster is **calibrated** when events given 70% happen about 70% of the time. To check, group the forecasts into buckets and compare each bucket's average forecast with the share that happened. A **calibration plot** puts the average forecast on the horizontal axis and the share that happened on the vertical axis. Points on the diagonal mean good calibration. Points below it on the right mean overconfidence: the "likely" events happen less often than you said.

The file [forecast-log.csv](../assets/data/forecast-log.csv) holds 60 made-up forecasts about made-up stocks, with columns date, question, forecast and outcome. It is invented for teaching.

<div class="example" markdown>

### Worked example: scoring the 60-forecast log

1. Yes rate: 28 of the 60 events happened, so 28 / 60 = 46.7%.
2. Brier score: 0.2295.
3. The always-50% line is 0.25, and a forecaster who always said the 46.7% base rate would score 0.4667 x 0.5333 = 0.2489. So the log beats both, narrowly: 1 - 0.2295 / 0.2489 = 0.078, about 8% better than the base rate.
4. Buckets, by forecast:

| Forecast range | Forecasts | Average forecast | Share that happened |
|---|---|---|---|
| 0.0 to 0.25 | 14 | 0.14 | 0.14 |
| 0.25 to 0.5 | 11 | 0.34 | 0.36 |
| 0.5 to 0.75 | 17 | 0.65 | 0.65 |
| 0.75 to 1.0 | 18 | 0.85 | 0.61 |

The first three buckets are close to the diagonal. In the top bucket, 85% forecasts came true 61% of the time (11 of 18). With 18 forecasts the share has a standard error of about 0.11, so the gap of 0.24 is about two standard errors: probably overconfidence, but a small sample.

</div>

![Calibration plot of 60 made-up forecasts: four buckets close to the diagonal except the highest bucket, where 0.85 forecasts happened 61 percent of the time](../assets/figures/19-data-flows-and-forecasting/calibration-dark.svg#only-dark)
![Calibration plot of 60 made-up forecasts: four buckets close to the diagonal except the highest bucket, where 0.85 forecasts happened 61 percent of the time](../assets/figures/19-data-flows-and-forecasting/calibration-light.svg#only-light)

The plot shows the same table. The point at the far right sits well below the dashed line.

### What research found

The Good Judgment Project entered a US government forecasting tournament on geopolitical questions, scored by the Brier score. Mellers and co-authors ([Psychological Science, 2014](https://www.psychologicalscience.org/journals/psychological-science/0956797614524255/)) report that three things improved accuracy: probability training (including use of reference classes), teaming, and tracking (placing top performers together in elite teams). Tetlock and Gardner's book *Superforecasting* (2015) describes the top 2% of forecasters, called superforecasters. These findings are about geopolitical questions, and they do not say that the same habits give an edge in markets. They do support the habits this lesson teaches: start from a base rate, give a number, score it, and update.

## In code

The snippet reads the log and prints its Brier score and a calibration table. Download the file from the link above and keep it in the same folder.

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

log = pd.read_csv("forecast-log.csv")
brier = ((log["forecast"] - log["outcome"]) ** 2).mean()
print(round(brier, 4))

log["bucket"] = pd.cut(log["forecast"], [0, 0.25, 0.5, 0.75, 1.0])
table = log.groupby("bucket", observed=True).agg(
    n=("outcome", "size"), avg_forecast=("forecast", "mean"), happened=("outcome", "mean")
)
print(table.round(3))
```

</details>

## Common mistakes

- Forecasting after you know the answer, or editing a forecast. Write the number and the date first and never change the row.
- Judging skill from a few forecasts. Twenty forecasts say little. Wait for 50 or more.
- Using only "50%" to stay safe. It scores 0.25 every time, so it never improves.

## Try it

1\. In a made-up record, 27 of 60 similar events happened. What is the base rate?

<details class="solution" markdown>
<summary>Answer</summary>

27 / 60 = 45.0%.

</details>

2\. You forecast 0.6 for an event that happens and 0.6 for one that does not. Brier score for the two?

<details class="solution" markdown>
<summary>Answer</summary>

(0.6 - 1)^2 = 0.16 and (0.6 - 0)^2 = 0.36. The mean is (0.16 + 0.36) / 2 = 0.26.

</details>

3\. A bucket of 20 forecasts averages 0.70, and 12 of the events happened. Is that calibrated?

<details class="solution" markdown>
<summary>Answer</summary>

The share that happened is 12 / 20 = 0.60 against a forecast of 0.70. The standard error is about sqrt(0.6 x 0.4 / 20) = 0.11, so the gap of 0.10 is under one standard error. It is consistent with good calibration, and the sample is too small to say more.

</details>

4\. A forecaster says 100% for an event and it does not happen. What is the penalty, and why do some people avoid 100%?

<details class="solution" markdown>
<summary>Answer</summary>

(1.0 - 0)^2 = 1.00, the worst possible penalty for one forecast. A single miss at 100% costs as much as many good forecasts save.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Create a forecast log with columns date, question, forecast, outcome. Write five yes or no questions about the next two weeks, each with a base rate and a forecast. |
| 3 | Score any five older forecasts you can resolve now, using the Brier formula. |
| 2 | Add a line to your [trade journal](../practice/trade-journal.md) notes: when you will review the log (for example, the first Sunday of each month). |

</div>

## Key terms

- **Base rate**: how often an event happens in a set of similar past cases.
- **Reference class**: the set of similar past cases used for a base rate.
- **Probability forecast**: a number from 0 to 1 for an event that resolves yes or no.
- **Forecast log**: a record of forecasts, made before the event, with their outcomes.
- **Brier score**: the average squared gap between forecasts and outcomes, where lower is better.
- **Calibrated**: events forecast at a given probability happen about that often.
- **Calibration plot**: a chart of average forecast against the share that happened.

Next: [Prediction markets](08-prediction-markets.md)
