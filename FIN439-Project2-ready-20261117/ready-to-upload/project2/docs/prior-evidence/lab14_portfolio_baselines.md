# Lab 14 - Portfolio Baselines

## Question and inputs

What does each simple portfolio earn and risk, and does any meet the Meridian mandate?

Inputs are the course-authored annual training values, not market estimates.
The objective is 6.5%: estimated CPI of 2.5% plus 4%. Bills and the 10-year
Treasury count toward the 3% eligible-reserve minimum.

Source: [Lab 14 instructions](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-09/lab-14-portfolio-baselines.md).

## Files and commands

- [portfolio.py](portfolio.py): reusable calculations using the standard library.
- [mandate.py](mandate.py): Lab 13 checker with the benchmark added as candidate E.

```powershell
python portfolio.py
python mandate.py
```

## Results

Weights are in the order bills / 10-year Treasury / IG bonds / global equity.

| Portfolio | Weights (%) | Expected return | Volatility | Eligible reserves | Meets 6.5%? |
|---|---|---|---|---|---|
| Benchmark | 0.0 / 0.0 / 40.0 / 60.0 | 6.80% | 10.46% | 0.0% | Yes |
| Equal weight | 25.0 / 25.0 / 25.0 / 25.0 | 5.20% | 5.21% | 50.0% | No |
| Inverse volatility | 84.3 / 6.0 / 7.0 / 2.6 | 3.77% | 1.05% | 90.3% | No |

Displayed weights are rounded; calculations use unrounded weights.
None meets both the expected-return objective and the reserve requirement.
The benchmark reaches the return objective but has no eligible reserves.
The other two have enough reserves but fall short of the return objective.
These expected returns do not guarantee realized returns or establish that all
mandate provisions, including the unresolved loss rule, are satisfied.

## Validation performed October 20, 2026

- Reran Lab 13: A passes, B fails three rules, C fails one, and D passes
  the implemented rules.
- All three portfolios match the lab's known-answer returns, volatilities,
  and reserve weights.
- Changed IG-equity correlation to 0.50 in both cells of an in-memory copy:
  benchmark volatility rose to 11.00%.
- A correlation of 1.3 was rejected with a clear error.
- An asymmetric correlation table was also rejected.
- Original file correlations remain 0.25.
- Candidate E has 0% reserves and fails only the checker's reserve rule.

These checks were run with AI assistance. I also ran the file myself and
shared the terminal output: the baseline matched, changing both IG-equity
correlations to 0.50 raised benchmark volatility to 11.00%, and 1.3 was
rejected. After restoring 0.25, volatility returned to 10.46%. My mandate
checker output confirmed that candidate E fails only the reserve rule.

## Diversification and hand calculation

Diversification combines exposures that do not move perfectly together.
Correlation below +1 reduces the pair's risk relative to perfect positive
correlation. It does not guarantee that a mix is less volatile than its
least-risky asset or prevent losses.

Benchmark expected return:

`0.40 * 0.05 + 0.60 * 0.08 = 0.068 = 6.80%`

Bond-equity covariance:

`0.25 * 0.06 * 0.16 = 0.0024`

Benchmark variance:

`(0.40**2 * 0.06**2) + (0.60**2 * 0.16**2) + (2 * 0.40 * 0.60 * 0.0024)`

`= 0.000576 + 0.009216 + 0.001152 = 0.010944`

Volatility: `sqrt(0.010944) = 10.46%`.

The nested loops in `portfolio_volatility` include both the bond-equity and
equity-bond terms. Together they supply the factor of 2 in the hand calculation.
Leaving out those terms incorrectly gives 9.90%.

## Reflection

Inverse volatility puts most money in bills because their volatility is only
0.5%. Their reciprocal, 200, is much larger than the other reciprocals.
Normalizing the reciprocals gives bills about 84.3%. This weighting rule does
not target the required return, which is why its expected return is only 3.77%.

I would show the CIO the benchmark portfolio first because it is the only
portfolio that meets the 6.5% expected-return objective, with an expected return
of 6.8%. Although it has the highest volatility at 10.46%, it also has the
highest expected return among these three portfolios. The equal-weight and
inverse-volatility portfolios have lower modeled risk, but neither meets the
required expected return.

The benchmark has no reserve-eligible assets, so it fails the mandatory 3%
reserve requirement. I would use it as a starting point for discussion, then
adjust and retest it to see whether it can meet both the reserve requirement
and the 6.5% expected-return objective.

## Code quiz and partner discussion

**Code quiz:** Does a smaller volatility make `1 / vol` larger or smaller,
and what does that do to the sleeve's weight?

**My answer, given before the explanation:** Smaller volatility makes
`1 / vol` bigger. This gives the sleeve more weight.

**My code explanation:** `sum` adds each pair's weighted covariance to get
portfolio variance. The outer loop selects investment i, and the inner loop
selects investment j, including pairs where an investment is paired with
itself. The negative-variance check allows tiny floating-point rounding errors
but rejects a materially negative variance. `math.sqrt(max(variance, 0))`
converts variance to volatility and prevents a square root of a tiny negative
rounding error.

**Partner's question:** Why does the code use two loops instead of just one?

**My answer:** Portfolio risk depends on both the individual investments and
how they move together. The first loop selects one investment, and the second
compares it with every investment, including itself. This includes all
covariance combinations in total portfolio variance.

**My question to my partner:** Why take the square root of variance at the end?

**Partner's answer:** Variance is measured in squared units. Taking its square
root converts it to standard deviation, which is easier to interpret as
portfolio volatility.

**Partner break test:** I reported that the partner's file also rejected the
invalid correlation of 1.3. Restoration and a successful normal rerun of the
partner's file still need confirmation.

## Final in-class checks

- Confirm that diversification and the benchmark hand calculation have been
  explained to the partner.
- Restore the partner's changed correlations to 0.25 and confirm the normal
  results after the break test.

## Before Lab 15

Streamlit is installed. The remaining preparation is to choose three to six
funds for the student's Project 2 mandate and record their tickers, names and
roles, then prepare five years of monthly adjusted-close prices in `prices.csv`,
with sources and download dates. Fund selection and price collection are not
claimed complete here.
