# Post-experiment readiness revision — November 23, 2026

Peyton requested fixes after reviewing the course's mandate/risk-limit and point-in-time-signal requirements. OpenAI Codex implemented and checked this revision. It follows the original experiment and is not an AI-off student experiment or evidence of committee approval.

## What changed

1. Added an explicit, enforced **6% proposed annualized-volatility ceiling**, an adjustable scenario control, baseline risk verdicts and a stop/review response. See [policy and rationale](risk-policy.md).
2. Replaced the unarchived 3.63% monthly FEDFUNDS transcription in the current model with the **3.75% target lower bound** in the Federal Reserve's September 16 dated announcement, effective September 17. Archived both official HTML documents, publication/effective dates, retrieval times and hashes. Verified their rate and timing text. See [data card](data-card.md).
3. Recomputed visible output, added risk conflicts, extended the tests and reconciled the written and recording materials.

The original ALFRED source was not recovered. Repeated downloads timed out; an alternate Federal Reserve H.15 historical route also failed. This repair uses a different, independently retrievable dated primary source, and does not claim to authenticate the old transcription.

## Version reconciliation

| Measure | Original student experiment model | Current revised model |
|---|---|---|
| Signal | Prior Lab 17 FEDFUNDS transcription, 3.63% | Dated FOMC target lower bound, 3.75% |
| Numerical volatility ceiling | None | Proposed 6%, with stop/review response |
| Default allocation | 75% SGOV / 25% ACWI | Same |
| Default annual net estimate | 5.51% | **5.57%** |
| Default annualized volatility | 3.81% | Same |
| 35-bps selected allocation | 70% SGOV / 30% ACWI | Same |
| 35-bps selected net estimate | 5.83% | **5.89%** |
| 35-bps selected volatility / turnover | 4.54% / 5% | Same |
| Original 75/25 weights at 35 bps | 5.41% net | **5.47% net** |
| Live recommendation | 0%, paper only | Same |

The new target cap is above the 60-return SGOV mean (about 3.715%), so the cap no longer reduces that default mean. The resulting net-return changes are explained by the source/model revision, not by edits to historical evidence. The 6% ceiling excludes high-risk baseline portfolios while retaining the default and cost-experiment weight choices.

## Verification and preserved ownership evidence

- All **18 tests passed**, including two app interaction checks, timing/units/value rejection, corrupted-source rejection, exact risk-boundary behavior and infeasible cost/risk combinations.
- Independent arithmetic reconciled **244 monthly prices and eight scenarios**. See [audit](../outputs/readiness-audit.json).
- At 25 bps, a 3% ceiling is infeasible; at 35 bps, a 4% ceiling is infeasible. Explicitly relaxing to 5% restores a 35-bps candidate. The model never changes the ceiling by itself. Full 3%, 4%, 5%, 6%, 8% sensitivity is in [revision results](../outputs/readiness-revision-results.json).
- The original prediction commit, student-experiment document, two supplied scenario exports, comparison JSON, prior turnover record and Luke's note are unchanged. They remain tied to their original code snapshot, not this revised source.
- The original student experiment remains the locked-record evidence. A live video demonstration of the revised code is a later illustration and must be described that way. No replacement AI-off prediction or run is claimed.

This revision fixes a missing modeled risk constraint and supplies traceable dated signal evidence. It does **not** establish real-client approval, a loss guarantee, investment suitability, point-in-time adjusted-price performance, or a proven forecast. Actual videos, corrected transcripts and final submission are still pending.
