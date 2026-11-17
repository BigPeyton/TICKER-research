
# Validation and AI use

Prepared November 17, 2026. Student review and the independent Lab 20 activities are pending.

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

## Locked Changed-Input Record — NOT YET PERFORMED

The lab requires the student to close AI, predict first, and **commit and push before running the chosen change**. Blank fields below are intentional. Do not backdate a prediction or label an already-run engineering test as a prospective prediction.

### Before the run — Peyton writes this with AI closed

| Required field | Student entry |
|---|---|
| One load-bearing input / exact app control | PENDING |
| Old value and units | PENDING |
| New value and units | PENDING |
| Expected direction of decision numbers, and why | PENDING |
| Expected decision / mandate-verdict effect | PENDING |
| Prediction date and time, including time zone | PENDING |
| GitHub immutable commit URL containing this prediction | PENDING — commit and push before the run |

### After the run — preserve the prediction above

| Required field | Student entry |
|---|---|
| Run date and time | PENDING |
| Before output file and GitHub link | PENDING |
| After output file and GitHub link | PENDING |
| Actual return, risk, allocation and mandate-verdict changes | PENDING |
| Did the decision change? | PENDING |
| Why actual matched/differed, or why nothing changed | PENDING |
| Result commit URL | PENDING |

Use the app's JSON download button for the default and changed results. Preserve both files under `outputs/` with distinct names and put their GitHub links here. Freeze the model/data files during the experiment so input effects are not mixed with code changes.

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

The independent cold run, AI-off prediction with prior GitHub commit, six-minute human code explanation, subsequent fix/rerun if necessary, final student decision line, recordings/transcripts, GitHub publication, and Brightspace submission have not been established by these automated checks. Raw signal evidence and committee risk/operating approvals also remain unresolved. Lab 20 allows truthful unresolved items; that does not establish Project 2 readiness or approval.


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
