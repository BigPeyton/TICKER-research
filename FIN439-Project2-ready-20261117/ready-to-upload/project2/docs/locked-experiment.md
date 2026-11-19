# Locked Changed-Input Record — turnover-limit prediction

**Status: pre-run prediction commit verified; assistant-operated results recorded November 19, 2026.** Peyton confirmed on November 19 that he wrote the original prediction with AI closed. This is his authorship attestation. Both result exports are published on GitHub. The prediction date/time below is supplied by Peyton; the actual GitHub commit timestamp separately establishes publication time.

Peyton supplied the prediction below. Codex reviewed its reasoning after receipt and preserved the wording while formatting this document. No run of this changed-input scenario was performed by Codex before preparing the original prediction record. The results below were appended after execution on November 19. The prior experiments and their limitations remain in `validation-and-ai-use.md`.

## Before the run — Peyton's supplied prediction

Author: Peyton Dow

Prediction date/time/time zone: November 17, 2026, 8:40 p.m. EST (America/Indianapolis)

App/code commit being tested: d03607352c856f8dcdc1f77e72c911cff24565e1

Input/control: Illustrative turnover limit

Original value and units: 25%

New value and units: 10%

Other controls held fixed: Annual net objective 5.50%; minimum SGOV reserve 3%; additional annual cost 25 bps; trading cost per turnover 10 bps; ACWI estimate adjustment 0 percentage points; last 36 monthly returns unchecked.

### Expected direction of estimated net return

Stay the same. The selected portfolio has 0% modeled turnover, so it should remain eligible under the tighter limit without changing its return.

### Expected direction of volatility

Stay the same. The current portfolio should remain eligible and retain its position as the lowest-volatility feasible allocation.

### Expected allocation change, or no change

No change. I expect 75% SGOV, 25% ACWI, and 0% SCHR and VTC because the current allocation already meets the new turnover limit.

### Expected recommendation/mandate-verdict effect

Stay the same: PILOT ON PAPER; 0% live allocation, modeled numeric rules PASS, and full mandate FAIL. The tighter turnover limit should not disqualify the current portfolio or resolve the outstanding mandate requirements.

### Reason for these predictions, in your own words

Lowering the turnover limit restricts how much the portfolio can trade. It may eliminate other allocations, but the current portfolio requires no modeled trading. Since it already has the lowest volatility among eligible allocations, narrowing the choices while keeping it eligible should leave the selection and results unchanged.

## Commit evidence

- Immutable prediction commit: [97df60482426668df8c9d3132311759f2d5f6072](https://github.com/BigPeyton/TICKER-research/commit/97df60482426668df8c9d3132311759f2d5f6072).
- GitHub commit timestamp: November 17, 2026, 8:54:32 p.m. EST (2026-11-18T01:54:32Z).
- GitHub was accessed and the prediction and code were verified before this run. The prediction commit precedes both November 19 exports. See [source verification](../outputs/turnover-source-verification.json).
- Tested app/code commit: `d03607352c856f8dcdc1f77e72c911cff24565e1`. Nine local source/configuration/input files matched the immutable GitHub version byte for byte.
- AI-off authorship confirmation: on November 19, after initially expressing uncertainty and receiving a reminder of the requirement, Peyton explicitly confirmed: “I did it with AI closed.” This is a student-supplied attestation, not independent observation. Codex reviewed the submitted prediction before it was committed. The supplied wording above is preserved.

## After the run — November 19, 2026

**Operator and method:** Codex used Streamlit's AppTest to execute the unchanged `app.py` at default settings, then changed its actual turnover-limit number input from 25.0 to 10.0. The exact JSON payload supplied to each app download button was captured. This is an assistant-operated app interaction, not a manual browser download, student-operated run, or partner cold run.

- Run time: November 19, 2026, 4:52:01 p.m. EST (America/Indianapolis).
- Before output: [scenario-2026-11-19T215201.212714_0000.json](../outputs/scenario-2026-11-19T215201.212714_0000.json); exported `2026-11-19T21:52:01.212714+00:00`.
- After output: [scenario-2026-11-19T215201.684920_0000.json](../outputs/scenario-2026-11-19T215201.684920_0000.json); exported `2026-11-19T21:52:01.684920+00:00`.
- All eight code/input hashes in the two app exports are identical. Only `turnover_limit` changed, from `0.25` to `0.10`; all six other controls remained at defaults.
- [Machine-readable comparison and displayed metrics](../outputs/turnover-experiment-comparison.json).

| Measure | Before: 25% limit | After: 10% limit | Prediction matched? |
|---|---|---|---|
| Estimated annual net return | 5.507828508750429% | 5.507828508750429% | Yes |
| Annualized volatility | 3.809658169910532% | 3.809658169910532% | Yes |
| Asset weights | 75% SGOV, 25% ACWI; 0% SCHR/VTC | Same | Yes |
| Modeled one-way turnover | 0% | 0% | Consistent with rationale |
| Recommendation | PILOT ON PAPER; 0% live allocation | Same | Yes |
| Modeled numeric rules | PASS | PASS | Yes |
| Full mandate | FAIL — not cleared for live use | Same | Yes |

**What happened and why (Codex analysis for Peyton to review):** All predicted outcomes matched. The current 75/25 candidate requires no modeled trade relative to the Lab 15 reference weights, so it remains eligible at 10%. Tightening the constraint narrows the eligible set without changing any candidate's estimated return or volatility. Because the previous minimum-volatility candidate remains eligible, the search selects it again.

**Fixed weights versus reoptimization:** The original weights continue to meet the modeled constraints, and rerunning the full constrained search selects those same weights. No different allocation is needed to offset the tighter limit. No prediction discrepancy was observed.

**What this establishes:** This captured app run supports the predicted unchanged result for these inputs, data, and 5-percentage-point grid, with a prediction commit predating execution. It does not verify AI-off authorship, independent startup, forecast accuracy, a maximum-loss limit, actual holdings, cumulative annual turnover, the missing raw signal vintage, or full-mandate clearance. Live allocation remains 0%.

**Publication:** Both timestamped exports, the comparison, and the source-verification record were published in [result evidence commit 83362ec](https://github.com/BigPeyton/TICKER-research/commit/83362eccb27229b71529e5b0e3200a5af0e01d92). This document is a subsequent record update. No course submission is claimed.
