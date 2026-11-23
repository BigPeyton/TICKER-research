# Student-operated Locked Changed-Input Record

**Status: prediction commit and supplied before/after results verified November 23, 2026. Peyton's predicted allocation change, higher volatility, and unchanged paper-only recommendation matched. Peyton confirmed that he performed the run and wrote his observations with AI closed. The three output JSONs are published and verified in the evidence commit linked below.**

Template prepared November 23, 2026. Codex filled in the known project details, then inserted Peyton's supplied prediction and reasoning verbatim and extracted the stated control and values. After Peyton reported the run, Codex checked the supplied JSON exports and appended his observations and explanation. This preparation date is not the prediction timestamp. Codex did not operate the 35-basis-point app run; its post-run checks compared the supplied exports, source hashes, and arithmetic.

## Project details

- Author: Peyton Dow
- Project: FIN 43900 Project 2 — Scholarship-fund investment application
- App/code snapshot: `661364945c533d03343afb7a9e817c220479f5a0`
- GitHub project path: `FIN439-Project2-ready-20261117/ready-to-upload/project2`
- Time zone for the record: America/Indianapolis (EST, UTC−05:00 in November)
- Local app address reported opened by Peyton: `http://127.0.0.1:8501`

## Documented baseline settings — verify in the app before the experiment

These are the documented defaults, not a record of newly observed controls. Change only the selected experimental control after committing the prediction; keep the others fixed.

| Control | Baseline value |
|---|---|
| Annual net objective | 5.50% |
| Minimum SGOV reserve | 3% |
| Additional annual cost | 25 basis points |
| Trading cost per turnover | 10 basis points |
| Illustrative turnover limit | 25% |
| ACWI annual estimate adjustment | 0 percentage points |
| Use last 36 monthly returns | Unchecked |

## Before the run — Peyton's supplied prediction

Prediction date, time, and time zone: November 23, 2026, 2:00 p.m. EST (America/Indianapolis; UTC−05:00), supplied by Peyton. The eventual GitHub commit timestamp will separately establish publication time.

Input/control chosen: Additional annual cost.

Original value and units: 25 basis points annually.

New value and units: 35 basis points annually.

Other controls held fixed (planned protocol): Annual net objective 5.50%; minimum SGOV reserve 3%; trading cost per turnover 10 basis points; illustrative turnover limit 25%; ACWI annual estimate adjustment 0 percentage points; last 36 monthly returns unchecked. Verify these settings before the run.

### Original wording — preserved verbatim

Prediction (untested). If the additional annual cost rises from 25 to 35 basis points, I expect the model to shift the paper portfolio from 75% SGOV / 25% ACWI to 70% SGOV / 30% ACWI. I expect the new mix to clear the 5.50% net return objective with volatility above 3.81%. The decision would still be a paper pilot with 0% live allocation because the loss limit and operational checks remain unresolved.

Reasoning. The extra 10 basis points would lower the current mix’s estimated net return from 5.51% to 5.41%, so it would miss the objective. The model considers allocations in five-percentage-point steps, and I expect one more step into ACWI to cover that shortfall.

AI-off authorship confirmation: Peyton explicitly stated, "i didnt use ai," when supplying the prediction date and time. This is his authorship attestation, not independent observation. Codex prepared the template and inserted his supplied prediction and reasoning verbatim afterward.

## Commit evidence — record after publishing the prediction, before testing

Prediction commit URL: https://github.com/BigPeyton/TICKER-research/commit/53d284a2f3a23b846f2bfe3bfdd9bb320c57d00b

GitHub commit timestamp: November 23, 2026, 2:05:47 p.m. EST (2026-11-23T19:05:47Z). The uploaded file matched the prepared local file byte for byte when verified. This timestamp establishes publication; compare it with the actual run/export timestamps after execution.

Pre-run status: Peyton labeled the supplied prediction "untested." Codex verified the prediction commit before providing the run instructions and did not execute the 35-basis-point scenario. The changed-scenario JSON was generated after that commit, as recorded below.

## After the run — Peyton's supplied observations and verified exports

Run date and time zone: November 23, 2026, America/Indianapolis (EST).

Actual run operator: Peyton. On November 23, 2026, Peyton explicitly confirmed that he performed the run and wrote his observations with AI closed. This is his attestation; Codex verified the supplied files afterward, and file timestamps do not independently establish AI-off execution.

App/code version: all eight code/configuration/data hashes in both exports match one another and the reviewed source snapshot `661364945c533d03343afb7a9e817c220479f5a0`. Prediction commit `53d284a2f3a23b846f2bfe3bfdd9bb320c57d00b` added the prediction document; it did not change the tested model.

Baseline controls: Peyton reported that the baseline matched the starting assumptions. The baseline JSON independently matches all seven documented settings above.

Before output: [scenario-2026-11-23T185925.230308_0000.json](../outputs/scenario-2026-11-23T185925.230308_0000.json). Copied unchanged from Peyton's `Downloads/Portfolio_Scenarios` folder into the project outputs. Published in evidence commit `6ef7f9521bf0fd2a128ed317517646fe65913d94`.

After output: [scenario-2026-11-23T190910.590247_0000.json](../outputs/scenario-2026-11-23T190910.590247_0000.json). Copied unchanged from the same folder. Published in evidence commit `6ef7f9521bf0fd2a128ed317517646fe65913d94`.

Only `annual_cost_bps` changed, from `25.0` to `35.0`; the other six settings and all eight exported source hashes are identical. See the [machine-readable comparison](../outputs/student-cost-experiment-comparison.json), including exact results and file hashes.

### Timing — generation versus download

| Event | November 23, 2026, EST | Evidence |
|---|---|---|
| Baseline JSON generated | 1:59:25.230308 p.m. | Embedded `exported_at_utc`: `2026-11-23T18:59:25.230308+00:00` |
| Prediction written | 2:00 p.m. | Peyton's supplied timestamp |
| Prediction committed | 2:05:47 p.m. | Verified GitHub commit |
| Baseline downloaded | 2:08:59 p.m. | Peyton's reported download time |
| Changed-scenario JSON generated | 2:09:10.590247 p.m. | Embedded `exported_at_utc`: `2026-11-23T19:09:10.590247+00:00` |
| Changed scenario downloaded | 2:09:31 p.m. | Peyton's reported download time |

The app prepares the JSON payload during rendering, before the user clicks its download button. The baseline payload predates the prediction commit; the changed-scenario payload follows it. Neither JSON timestamp is represented as a verified download-click time, and no assertion is made that both payloads were generated after the prediction commit.

| Measure | Before: 25 bps | After: 35 bps | Did the prediction match? |
|---|---|---|---|
| Estimated annual net return | 5.51% | 5.83% | Yes: selected mix clears the 5.50% objective |
| Annualized volatility | 3.81% | 4.54% | Yes: higher than 3.81% |
| Portfolio weights | 75% SGOV / 25% ACWI; 0% SCHR/VTC | 70% SGOV / 30% ACWI; 0% SCHR/VTC | Yes |
| Modeled turnover | 0.00% | 5.00% | Consistent with the predicted five-point allocation shift |
| Recommendation | Paper pilot; 0% live allocation | Paper pilot; 0% live allocation | Yes |
| Modeled numerical rules | PASS | PASS | Consistent with the predicted feasible selection |
| Full-mandate verdict | FAIL | FAIL | Consistent with the predicted unresolved requirements |

### Peyton's explanation — preserved verbatim

The prediction matched. The baseline matched the starting assumptions, and the two downloaded JSONs confirm that only Additional annual cost changed. Raising it from 25 to 35 bps shifted 5% of the portfolio from SGOV to ACWI.

At 35 bps, the original allocation would have earned an estimated 5.41% net, below the 5.50% objective. Moving five percentage points into ACWI brought the estimate to 5.83% and increased volatility, as predicted. The unresolved loss limit and operational checks kept the recommendation at 0% live allocation.

### Post-run verification and publication

Codex checked the saved export values and cost arithmetic on November 23. The original weights at 35 bps give 5.407828508750429% net; the selected replacement gives 5.828394210500515% net and 4.544438430015182% volatility. These are consistent with Peyton's rounded observations. The replacement's 5% modeled turnover adds 0.5 basis point in trading cost, making total cost drag 35.5 basis points. The higher selected net estimate reflects changed weights; it does not mean higher fees improve the original portfolio's return.

Material AI assistance after the run: read the supplied JSONs, compare controls and source hashes, verify arithmetic and timing against the previously verified prediction commit, preserve the original downloads, prepare the comparison JSON, and format Peyton's supplied observations. No new app execution was used for these checks. The source evidence and unresolved mandate limitations remain unchanged.

Result/evidence commit URL: [6ef7f9521bf0fd2a128ed317517646fe65913d94](https://github.com/BigPeyton/TICKER-research/commit/6ef7f9521bf0fd2a128ed317517646fe65913d94). Both original scenario exports and the comparison JSON were verified against their local copies using Git blob hashes. This document is the subsequent result-record update. The comparison JSON preserves its pre-publication preparation status; this publication note supersedes that status.
