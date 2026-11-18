# Project 2 audit and remaining requirements

Audit date: November 17, 2026, America/Indianapolis. UTC evidence timestamps may show November 18. This is an AI-assisted development audit, not a student-authored prediction or independent partner checkout.

## Source and scope

This working copy was downloaded from [source commit 382314e](https://github.com/BigPeyton/TICKER-research/tree/382314e4446d7a0efa1f42756dd8093064a9fe99/FIN439-Project2-ready-20261117/project2). The [baseline manifest](audit-baseline.json) records the 33 downloaded files and their hashes. The duplicate nested upload and generated Python cache files were excluded from this new copy; the existing local package and GitHub repository were not deleted or changed.

The latest published validation and readiness records already contained Peyton's confirmed recommendation, reflection, and AI-off explanation. Earlier README/memo status statements had not caught up. This revision reconciles those statements without claiming that the missing experiment or independent startup occurred.

## Verified model findings

- All **244 monthly adjusted prices and their dates** reconcile to the last available trading observations in the four bundled Yahoo daily responses. Their raw-file hashes match the original metadata. This verifies archive consistency, not external provider authenticity or historical point-in-time availability.
- Independent direct centered cross-products reproduce the annual covariance calculations. Independently calculated net return, volatility, and exhaustive allocation searches agree for all six existing stress cases. The default has 27 feasible grid allocations; the 80% reserve and combined cases have none. See [machine-readable audit results](../outputs/audit-checks.json) and [reproducible audit code](../tools/audit_model.py).
- The default remains **75% SGOV / 25% ACWI**, approximately **5.51% estimated annual net return** and **3.81% annualized volatility**. The model target remains 5.50%. Its narrow margin does not establish predictive reliability.
- Equal weight and inverse volatility remain the two transparent baselines. The 60/40 benchmark is an additional comparator. All show numerical-rule verdicts separately from unresolved full-mandate clearance.
- No calculation, default assumption, decision rule, or app layout was changed. Scenario exports now include a UTC export timestamp, analysis boundary, and code/input hashes. Those identify the local scenario but do not establish GitHub publication or prediction timing.
- The full automated suite contains **15 tests** after adding the export-evidence check. The integration test exercises the existing cost and reserve scenarios; it is not a new student experiment.

## Evidence and mandate limits

The original ALFRED requests, a bounded historical request, and the vintage page all timed out during this audit. The current [FRED source page](https://fred.stlouisfed.org/series/FEDFUNDS) agrees with the recorded July/August 3.63% and September 3.75%, but a current page cannot prove what was available on September 30. The [retrieval record](../data/signal-source.json) preserves this distinction. The raw vintage gap remains open; the prior Lab 17 evidence has not been relabeled as a new download.

The proposed scholarship-fund mandate never specified an approved quantitative loss/risk budget or breach response. Annualized volatility is calculated but not checked against an approved ceiling. Creating a limit merely to obtain PASS would change the mandate without evidence. The committee ask remains to define that policy; live clearance remains FAIL. Actual holdings, annual turnover, liquidity/fund permissions, and rolling five-year real-return compliance also remain unverified.

The additive 2.5% inflation + 3% target is the existing **5.50% planning convention**. The first-year arithmetic return estimate is not a compounded real-return test. A 5-point grid is a transparent restricted search, not proof of a globally optimal continuous allocation.

## Requirement status

| Project 2 requirement | Status and next evidence |
|---|---|
| Runnable Python web app | Launcher and automated interface checks supplied. Audit clean-install evidence is recorded in validation; Luke's independent startup rerun remains separate. |
| Lab 13 mandate, risk measure and limits | Objective, universe, benchmark, reserve and turnover rules documented. Volatility measured; approved loss/risk limit and breach response missing. Keep restriction explicit. |
| Two baselines and constrained portfolio, with verdicts | Implemented and independently reconciled. |
| Point-in-time signal and data card | Prior lab evidence/data card present; raw September 30 ALFRED vintage still missing. Authenticate it before claiming that gap is closed. |
| Estimates/window/cost/constraint stress and stop condition | Implemented; all six cases reconciled, with fixed weights separated from reoptimization. |
| Locked Changed-Input Record | **Not complete.** A new human-authored AI-off prediction must be committed and pushed before its first run. See the [blank workflow](locked-experiment.md). |
| Recommendation, allocation range and monitoring triggers | Paper research pilot; live allocation 0%. Existing scenario range 65–85% SGOV / 15–35% ACWI is a sensitivity range, not a live trading instruction. |
| Opening AI/ownership and education statements | Present in README/memo and video prompts; must be spoken in each actual recording. |

## Remaining sequence

1. Resolve historical signal evidence if the exact vintage becomes accessible. Do not silently substitute the current series. If unresolved, retain the restriction and explain its grading/decision significance.
2. Review and publish this working revision to the intended project folder; record its exact commit. Do not upload `.venv`, `__pycache__`, or the whole parent audit folder inside the existing folder.
3. Peyton closes AI, chooses a fresh input change, writes his own prediction, and commits/pushes it before running it. Then preserve both JSON exports and interpret the result honestly. Neither old experiment substitutes for this step.
4. Luke independently retries a clean setup from the published README and records actual results. Assistant-run installation checks do not replace that evidence.
5. Finish student review, three recordings and actual corrected transcripts, manifest URLs/timestamps/access checks, and the matching Markdown attachments. Brightspace controls the deadline; no submission is claimed.

Source requirements: [Project 2](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md), [student checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md), and [Lab 20](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-13/lab-20-project2-readiness.md). Truthful unresolved items can complete Lab 20; that is not approval of Project 2.
