# Quant interviews
<!-- lint-ok: significant (statistical sense) -->

<span class="tag tag-career">Career</span> <span class="tag tag-part">CAREER</span>

After this lesson you can name the four kinds of question a quant interview mixes, work an example of each, and plan a preparation routine.

Before this: [Probability and mental math puzzles](06-probability-and-mental-math-puzzles.md). The math book covers the background: [correlation and linear regression](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/08-statistics/04-correlation-and-linear-regression/), [multiple testing and p-hacking](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/08-statistics/07-multiple-testing-and-p-hacking/) and [eigenvalues and eigenvectors](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/06-linear-algebra/08-eigenvalues-and-eigenvectors/). You need from them: the least squares slope, the idea that many tests give false positives, and what an eigenvalue is. Python for the code box.

## The idea

A quant role (lesson 1) usually means a technical interview with statistics, linear algebra, coding and brainteasers. The mix depends on the role: researchers get more statistics, developers more coding, traders more probability and mental math. Firms rarely publish their process, so this lesson makes no claim about any one firm. Read each firm's own careers page for what it says, and treat forum posts as one person's account.

The common thread is this: you state the method, compute carefully and say where the answer could be wrong.

## How it works

### Statistics

Expect to explain, not recite. Typical prompts: what does a p-value mean, what is overfitting, what happens to a regression when two predictors are highly correlated, how do you test whether a strategy works.

<div class="example" markdown>

### Worked example: a regression by hand

Four points: x = 1, 2, 3, 4 and y = 2, 4, 5, 9.

1. Means: \(\bar{x} = 2.5\), \(\bar{y} = 20 / 4 = 5\).
2. \(S_{xy} = \sum (x - \bar{x})(y - \bar{y}) = (-1.5)(-3) + (-0.5)(-1) + (0.5)(0) + (1.5)(4) = 4.5 + 0.5 + 0 + 6 = 11\).
3. \(S_{xx} = \sum (x - \bar{x})^2 = 2.25 + 0.25 + 0.25 + 2.25 = 5\).
4. Slope = 11 / 5 = 2.2. Intercept = 5 - 2.2 x 2.5 = -0.5.

The slope is the covariance divided by the variance of \(x\). Say that in one sentence.

</div>

Multiple testing is a favourite because it is the central risk in finding trading signals. If you test 20 independent ideas at the 5% level and none is real, the chance that at least one looks significant is 1 - 0.95^20 = 1 - 0.3585 = 64.2%.

### Linear algebra

Typical prompts: what is the rank of a matrix, what are eigenvalues, why does PCA use the covariance matrix, when is a matrix invertible.

Example: find the eigenvalues of the matrix with rows (2, 1) and (1, 2). The characteristic equation is \((2 - \lambda)^2 - 1 = 0\), so \(2 - \lambda = \pm 1\) and \(\lambda = 3\) or \(\lambda = 1\). The trace (4) equals the sum of the eigenvalues, and the determinant (3) equals their product. Using the trace and determinant as a check is a good habit.

### Coding

Questions are usually short and ask for correct code with clear reasoning about speed. Say the approach before you write.

Example: given a list of daily portfolio values, return the maximum drawdown (the largest fall from a peak). One pass, keep the running peak, and track the largest percentage fall from it. The time is linear in the list length and the memory is constant.

### Brainteasers

A brainteaser tests structure. Example: 100 doors are closed. In round \(k\) from 1 to 100 you toggle every \(k\)-th door. Which are open at the end? Door \(n\) is toggled once for each divisor of \(n\). Divisors come in pairs, except when \(n\) is a perfect square, so only squares have an odd count. Ten doors are open: 1, 4, 9, 16, 25, 36, 49, 64, 81 and 100.

Another: the expected maximum of two independent uniform numbers on 0 to 1. The chance both are below \(m\) is \(m^2\), so the expected maximum is the integral of \(1 - m^2\) from 0 to 1, which is 1 - 1/3 = 2/3. The minimum is 1/3 by symmetry.

## In code

<details class="code" markdown>
<summary>In code</summary>

```python
def max_drawdown(values):
    peak = values[0]
    worst = 0.0
    for v in values:
        peak = max(peak, v)
        worst = max(worst, (peak - v) / peak)
    return worst

print(round(max_drawdown([100, 120, 90, 110, 80, 130]), 4))

open_doors = [n for n in range(1, 101)
              if sum(1 for k in range(1, n + 1) if n % k == 0) % 2 == 1]
print(open_doors)
```

</details>

### How to prepare

1. Fix your weakest area first, using the list above. Do 3 problems a day in it.
2. Say every answer aloud, with the method before the number.
3. Code in plain Python on paper or a plain editor, without autocomplete, for a few sessions.
4. Review the part 20 lessons on returns, volatility and regression, since those are the data skills a quant role uses.
5. Keep a log of problems you missed and redo them a week later, as in your trade journal.

## Common mistakes

- Memorizing answers. A changed number breaks a memorized answer, and a method survives it.
- Staying silent while thinking. Say what you are trying, even if it fails.
- Giving a number with no check. Test it on a small case.

## Try it

1\. For the regression example, what is the predicted y at x = 5?

<details class="solution" markdown>
<summary>Answer</summary>

-0.5 + 2.2 x 5 = 10.5.

</details>

2\. You test 10 independent ideas at the 5% level, and none is real. What is the chance at least one looks significant?

<details class="solution" markdown>
<summary>Answer</summary>

1 - 0.95^10 = 1 - 0.5987 = 40.1%.

</details>

3\. Run the code. What is the maximum drawdown of 100, 120, 90, 110, 80, 130?

<details class="solution" markdown>
<summary>Answer</summary>

The peak is 120 when the value falls to 80 later, so the fall is (120 - 80) / 120 = 0.3333. The code prints 0.3333, a drawdown of 33.3%.

</details>

4\. The eigenvalues of a matrix with rows (4, 0) and (0, 1)?

<details class="solution" markdown>
<summary>Answer</summary>

A diagonal matrix has its diagonal entries as eigenvalues: 4 and 1.

</details>

5\. Two fair dice: what is the expected maximum?

<details class="solution" markdown>
<summary>Answer</summary>

The maximum is at most \(m\) with probability \((m/6)^2\). Counting, the maximum equals 1 in 1 case, 2 in 3, 3 in 5, 4 in 7, 5 in 9, 6 in 11 out of 36. E = (1 + 6 + 15 + 28 + 45 + 66) / 36 = 161 / 36 = 4.47.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Solve one statistics or linear algebra question aloud, method first. |
| 5 | Write one short function (for example the drawdown above) from memory and test it on a small list. |

</div>

## Key terms

- **Maximum drawdown**: the largest percentage fall from a peak to a later low.
- **Brainteaser**: a short puzzle that tests structure rather than knowledge.
- **Eigenvalue**: a number \(\lambda\) such that a matrix times a vector equals \(\lambda\) times that vector.
- **Multiple testing**: running many tests, which makes a false positive likely.

Next: [AI for market research](08-ai-for-market-research.md)
