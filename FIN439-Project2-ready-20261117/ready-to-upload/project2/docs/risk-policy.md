# Proposed paper-research risk policy

Dated November 23, 2026, after the original student experiment. This is an AI-assisted, analyst-proposed extension of the fictional scholarship-fund mandate. It is not an actual committee approval, an inferred client preference, or a change to the historical prediction.

## Measure and ceiling

Use annualized standard deviation of monthly total returns: square root of `w' × (12 × monthly sample covariance) × w`. At the default 60-return window, a candidate must have **estimated annualized volatility at or below 6.00%**, as well as meet return, reserve, long-only and modeled turnover constraints. The 36-return scenario recomputes the same measure on that shorter sample. Equality passes, subject only to a numerical tolerance of 1e-12 in decimal units.

The 6% value is a round, illustrative research budget chosen after earlier model results were available. It is not statistically calibrated, independently precommitted, or demonstrated to be appropriate for the fund. The analyst proposes it for committee review, rather than choosing whichever limit makes a scenario pass. The estimate-comparison app allows explicit sensitivity changes, and records the chosen ceiling in every export.

For scale, 6% of the fictional $10 million fund is $600,000 of annual standard-deviation exposure. This is neither an expected dollar loss nor a worst-case bound. A volatility ceiling cannot guarantee the original case's loss promise or establish scholarship-payment safety. Tail losses, correlations, costs and liquidity can change.

## Enforcement and breach response

The solver excludes every candidate above the selected ceiling. Each baseline displays its own risk PASS/FAIL. A scenario with no feasible candidate is rejected; the app never relaxes the risk budget automatically.

On a breach, withdraw the paper candidate, suspend new paper allocations, record the breached rule and inputs, verify data and the calculation, and refer any policy change for explicit review. Restart only after the corrected or newly authorized scenario passes all modeled rules. A replacement is a new candidate, not proof the old allocation survived. Live allocation stays zero until client risk policy and the other unresolved requirements are approved and verified.

Review quarterly with scholarship payouts, and at each new data/input update in the model. These are manual review requirements; the static-data app is not a live market monitor or an automated trading system.

## Sensitivity and verification

With the revised dated-policy signal, at 25 bps cost a 3% ceiling is infeasible, while 4%, 5%, 6% and 8% select 75% SGOV / 25% ACWI. At 35 bps cost, 3% and 4% are infeasible; 5%, 6% and 8% select 70% SGOV / 30% ACWI. This shows that feasibility depends on the risk budget; a higher return target cannot silently override it.

Tests cover an exact boundary, a breach just below the candidate's volatility, invalid limits, a cost/risk conflict, and app rejection/recovery. Independent enumeration applies the ceiling to every candidate. See [revision results](../outputs/readiness-revision-results.json) and [independent audit](../outputs/readiness-audit.json).
