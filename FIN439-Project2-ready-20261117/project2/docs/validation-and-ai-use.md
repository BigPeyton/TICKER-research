# Validation and AI use

Prepared November 17, 2026; updated with Luke's returned cold-run note and Peyton's reported 10-to-30-bps trading-cost experiment. Prediction/results are recorded below. Peyton confirmed that he wrote the prediction before testing but did not commit it to GitHub first; that required step remains unmet. Original experiment exports still need to be linked. The code explanation and independent app startup remain unresolved.

## Data, controls, and reproducibility

See the [data card](data-card.md) for sources, October 22 price-download dates, September 30 analysis boundary, the prior Lab 17 signal evidence, transformations, and limitations. The app uses bundled data and no credentials. `python run.py --report` regenerates visible output, including code/input hashes. The output, app and memo use the same defaults and the same calculation engine.

Equal weight and inverse volatility are the required transparent baselines; a 60% ACWI / 40% VTC benchmark is also displayed. The 5-point grid minimizes estimated volatility subject to the net objective, SGOV reserve, long-only/full-investment rule, and illustrative turnover cap. Each portfolio has individual rule results and a full-mandate FAIL because unresolved risk and operational/data requirements prevent clearance. Annualized volatility is not a maximum-loss rule.

## Checks executed November 17, 2026

`python -m unittest discover -s tests -v` passed **14 tests** on Python 3.13.15 with Streamlit 1.66.0. This is assistant-run development validation, not a partner cold run.

The one-command launcher was also run in a newly created project `.venv`. The sandbox initially blocked package-network access; after network permission, the pinned dependency installed successfully and the server started at `http://127.0.0.1:8502`. Its health endpoint returned HTTP 200 / `ok`, and all 14 tests passed again using that fresh environment. See the [captured check output](../outputs/development-checks.txt) and [installed package versions](../outputs/tested-environment.txt). The native browser was minimized and unavailable to the UI tool, so no independent visual-browser pass is claimed.

A separate source reconstruction check matched **all 244 monthly prices and their dates** against the last daily adjusted-price observation of each month in the four archived Yahoo responses.

The checks cover independently calculated two-asset covariance math and the course's 6.8% benchmark return; the previous Lab 15 75/25 result; all 1,771 unique 5-point allocations; exact asset order; missing months and nonfinite data; the 36-return window; future-vintage and wrong-unit rejection; one-way turnover and cost conversion; inclusive limits and infeasible scenarios; distinction between numeric and full-mandate verdicts; all four archived raw-data hashes; and a Streamlit interaction that changes costs and then reaches infeasibility.

The default candidate returns 5.51% net with 3.81% volatility and 75% reserve. Equal weight and inverse volatility fail the return hurdle. The benchmark fails reserve and illustrative turnover. All fail full clearance for the stated unresolved requirements. See [exact output](../outputs/results.json) and [readable output](../outputs/results.md).

## Predefined engineering stresses

| Change from default | Unchanged portfolio | Reoptimized result |
|---|---|---|
| ACWI annual estimate −2 percentage points | Net falls to 5.01%; return FAIL | 65% SGOV / 35% ACWI; net 5.65%, volatility 5.28% |
| Last 36 monthly returns | Net 7.60%; modeled rules PASS | 85% SGOV / 15% ACWI; net 5.90%, volatility 1.76% |
| Additional annual cost 100 bps | Net falls to 4.76%; return FAIL | 65% SGOV / 35% ACWI; net 5.60%, volatility 5.28% |
| SGOV reserve minimum 80% | 75% reserve fails | No feasible grid allocation |
| Combined equity −2 pp, cost 100 bps, reserve 80% | Net 4.26%; return and reserve FAIL | No feasible grid allocation |

These were designed and run with AI assistance. They do **not** qualify as the required human-authored, precommitted experiment. Reoptimization must not be described as the original weights surviving. The reversal rule is to withdraw a failing candidate, and reject a scenario with no feasible grid allocation; live use also requires all full-mandate gaps to be resolved.

## Partner cold run — returned note

Luke's [unchanged returned note](luke-cold-run.md) reports Windows/Python 3.13.15 and `python run.py` failing to resolve `pypi.org`. Retrying reproduced that failure. `python run.py --report` confirmed the decision 36 seconds after the first launch attempt; time spent reading the README was not measured.

Peyton later supplied a running browser app. Luke changed the reserve minimum from 3% to 80% and observed scenario rejection with no feasible grid allocation; full-mandate FAIL remained. He restored 3% and saw the 5.51% net estimate and paper-pilot decision. The 7-second browser check excludes startup; its launch command and commit were unverified. This supports an assisted control check, not a successful independent installation, and is not the required precommitted human prediction.

In response, the README now documents this exact setup error and distinguishes the offline fallback from the interactive app. This documentation improvement is prepared locally; its publication and a partner rerun after the update are pending. No application-source fix or resolved DNS problem is claimed. The [readiness record](lab20-readiness.md) preserves the remaining gaps.

## Locked Changed-Input Record

**Status: prediction and results supplied by Peyton; prediction written before testing, but not committed to GitHub before testing.** Peyton explicitly confirmed this sequence. The lab's pre-run commit-and-push requirement was not completed. Uploading this record afterward does not retroactively satisfy that requirement. Original experiment exports still need to be attached. No commit, run timestamp, or independently captured output is invented here. Codex formatted the supplied account afterward.

### Before the run — Peyton's supplied prediction

- **Control changed:** Trading cost per turnover.
- **Original value:** 10 basis points.
- **New value:** 30 basis points.
- **Other controls:** All other controls remained at their defaults.

**Predictions saved before testing, as reported by Peyton:**

- **Estimated net return:** Stay the same because the selected portfolio has 0% modeled turnover, so the higher trading cost would still be multiplied by zero.
- **Volatility:** Stay the same because I expected the same portfolio and asset weights to remain selected.
- **Asset weights:** Stay the same at 75% SGOV and 25% ACWI, with 0% SCHR and VTC. Increasing trading costs should not make competing allocations more attractive.
- **Recommendation/mandate verdict:** Stay the same—“PILOT ON PAPER; 0% live allocation,” modeled numeric rules PASS, and full mandate FAIL. Changing trading costs would not resolve the outstanding mandate issues.

**Reason for my predictions:** The default portfolio already had the lowest estimated volatility among eligible allocations and required no turnover. Raising trading costs should leave this portfolio unaffected while making portfolios requiring trading less attractive.

### After the run — actual results reported by Peyton

| Measure | Before: 10 bps | After: 30 bps | Prediction matched? |
|---|---|---|---|
| Estimated annual net return | 5.51% | 5.51% | Yes |
| Annualized volatility | 3.81% | 3.81% | Yes |
| Asset weights | 75% SGOV, 25% ACWI; 0% SCHR and VTC | Unchanged | Yes |
| Recommendation | Paper pilot; 0% live allocation | Unchanged | Yes |
| Modeled numeric rules | PASS | PASS | Yes |
| Full mandate | FAIL | FAIL | Yes |

**What I learned:** All four predictions matched the results. A higher trading-cost assumption does not automatically reduce net return; it depends on how much trading the portfolio requires. Because modeled turnover stayed at 0%, the higher cost had no effect on the selected portfolio. The full mandate still failed because its unresolved requirements remained.

**Ending app state:** The control was left at 30 basis points after testing. This reports the interactive state; it does not change the source-code default of 10 basis points or the saved default output.

### Timing and evidence to attach

| Required evidence | Status |
|---|---|
| Prediction date/time and time zone | Not supplied |
| Immutable GitHub prediction commit, pushed before the run | NOT COMPLETED. Peyton confirmed that he made and saved the prediction before testing but did not put it on GitHub first. The prediction and reported results are retained; this missing required step is disclosed. |
| Run date/time and code commit used | Not supplied |
| Before and after JSON exports from this experiment | Not yet located; the existing 25-to-50-bps annual-cost exports belong to the separate AI-assisted experiment |
| Result commit | Pending publication |

The supplied explanation is consistent with the model's cost formula: trading-cost rate multiplied by zero turnover contributes zero drag. The exact zero-turnover candidate remains feasible and keeps its volatility; increasing nonnegative trading costs cannot add new feasible competitors when all other settings and data are fixed. This reasoning supports the reported unchanged result but does not replace the original outputs or establish when the prediction was committed.

## Prospective cost experiment (AI-assisted)

This prediction was drafted and entered with Codex assistance before running this specific 25-to-50-bps experiment. It does not establish completion of the separate AI-off requirement.

- Control: Additional annual cost (bps), 25 -> 50 bps; all other controls at defaults.
- Prediction: For unchanged weights, estimated annual net return will fall by 0.25 percentage points, from approximately 5.51% to 5.26%. Volatility, reserve and turnover for those unchanged weights will stay the same. The original 75% SGOV / 25% ACWI portfolio should fail the 5.50% net objective.
- Expected decision: The app may select different weights to meet the objective; if no feasible allocation exists it will reject the scenario. Full-mandate clearance should remain FAIL and live allocation should remain 0%.
- Timing: November 17, 2026, America/Indianapolis. The GitHub commit timestamp will establish publication before this experiment.
- Status: Prediction only; this experiment has not yet been run. Results and the immutable prediction commit link will be appended afterward.


### Observed cost experiment result

Run November 17, 2026, approximately 5:47 PM EST (America/Indianapolis), after the [prediction commit](https://github.com/BigPeyton/TICKER-research/commit/e3963e480406cb0d682ce82fe89c5acb51fd577c) was published. Codex operated the app at http://127.0.0.1:8503/.

| Metric | Before: 25 bps | After: 50 bps |
|---|---|---|
| Selected allocation | 75% SGOV / 25% ACWI | 70% SGOV / 30% ACWI |
| Estimated annual net return | 5.51% | 5.68% |
| Annualized volatility | 3.81% | 4.54% |
| SGOV reserve | 75% | 70% |
| Illustrative turnover | 0% | 5% |
| Selected portfolio modeled rules | PASS | PASS |
| Full-mandate clearance | FAIL | FAIL |
| Decision | PILOT ON PAPER; 0% live allocation | PILOT ON PAPER; 0% live allocation |

The prediction matched the fixed-weight cost effect: the original 75/25 portfolio would fall from approximately 5.51% to 5.26%, a 0.25-percentage-point reduction, below the 5.50% objective. This fixed-weight number is calculated from the saved baseline and extra cost; the app instead displays its reoptimized candidate. It increased ACWI by 5 percentage points, producing a higher selected return and higher volatility. The allocation changed, but the paper-only decision and full-mandate FAIL did not. The original weights did not survive the return rule.

Evidence: [before output](../outputs/cost-before-25bps.json), [after output](../outputs/cost-after-50bps.json), and [immutable output commit](https://github.com/BigPeyton/TICKER-research/commit/c889e79f36152bf2094e559de1d8054622409040). Only annual cost changed; the other app controls remained at their displayed defaults. Annual cost was restored to 25 bps after both downloads. No model or data files were edited during this experiment.

This completes the AI-assisted prediction/commit/run comparison. It does not establish an independent AI-off prediction, a human code explanation, or Peyton's personal confirmation.

## Material AI uses and dispositions

Tool: **OpenAI Codex**, interaction date November 17, 2026. The user identified the session as **Astra, medium** earlier in the conversation; an exact backend model build/version is not exposed in the artifact workflow. Do not claim a more specific model or setting was verified. Python 3.13.15 and Streamlit 1.66.0 are the tested software versions.

| AI contribution | Disposition and check |
|---|---|
| Reused earlier Lab 14/15 calculations | Retained in `portfolio.py`; corrected a stray integer `1` after the equity input tuple that would break baseline iteration; known-answer checks pass |
| Proposed app and constrained search | Implemented; compared against transparent baselines, explicit rules, grid enumeration, and Streamlit interaction checks |
| Added net-cost accounting and SGOV signal cap | Explicit research assumptions, not client approvals; unit/turnover checks pass; predictive validity is not established |
| Suggested missing-mandate handling | Retained: numeric PASS never implies full clearance; missing risk policy and operational/source checks block live use |
| Attempted raw historical-rate retrieval | Failed/timeouts; preserved the student-checked Lab 17 summary instead and disclosed the limitation; no successful new source check claimed |
| Drafted memo, readiness record and video prompts | Prepared for student review; does not establish student agreement, an independent partner run, a human prediction, recorded videos, upload, or submission |

Peyton must review the final interpretation and be able to explain the decision-producing code without AI. The opening ownership statement in the README and memo is a draft until that review occurs.

## Unresolved and not claimed

The original project folder was published and its app/data/documentation/test files verified against the local package. Luke's returned note separately establishes his reported cold-run attempt and assisted browser check; it does not establish a successful independent app launch. An updated folder was uploaded inside the existing project folder, creating a nested duplicate; the main project record still needs these merged updates. No subsequent independent partner startup rerun is recorded. Peyton's trading-cost prediction and results are now reported above. He confirmed predicting before testing, but did not commit to GitHub before testing; that required step remains unmet. Original exports are not yet linked. The six-minute human code explanation, final student-owned decision line, recordings/transcripts, and Brightspace submission remain unrecorded. Raw signal evidence and committee risk/operating approvals remain unresolved. Lab 20 allows truthful unresolved items; that does not establish Project 2 readiness or approval.
