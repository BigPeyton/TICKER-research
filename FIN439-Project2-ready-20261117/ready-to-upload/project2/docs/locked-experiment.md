# Locked Changed-Input Record — turnover-limit prediction

**Status: prediction only; results not yet recorded.** The GitHub commit containing this prediction must be published before the experiment is run. The prediction date/time below is supplied by Peyton; the actual GitHub commit timestamp separately establishes publication time.

Peyton supplied the prediction below. Codex reviewed its reasoning after receipt and preserved the wording while formatting this document. No run of this changed-input scenario was performed by Codex before preparing this record. The prior experiments and their limitations remain in `validation-and-ai-use.md`.

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

## Commit evidence — complete after publication, before execution

- Immutable prediction commit URL: PENDING publication.
- Confirmation the push preceded the run: PENDING verification.
- AI-off authorship confirmation: to be confirmed by Peyton; no independent verification is claimed.

Preserve the original prediction commit. Do not change the prediction retrospectively to match the results. Append the exact commit link and subsequent results in a later commit.

## After the run — not completed

Download the default scenario, change only the illustrative turnover limit from 25% to 10%, then download the changed scenario. Preserve both unique JSON filenames and their export timestamps. Record the tested code commit separately; file hashes do not replace the pre-run prediction commit.

- Run date/time/time zone:
- Before-output GitHub link:
- After-output GitHub link:
- Code/data hashes identical between exports (or explain differences):

| Measure | Before | After | Prediction matched? |
|---|---|---|---|
| Estimated annual net return | | | |
| Annualized volatility | | | |
| Asset weights | | | |
| Recommendation | | | |
| Modeled rules | | | |
| Full mandate | | | |

- What happened and why:
- Distinguish the effect on unchanged weights from a different reoptimized allocation:
- If the prediction differed, diagnose the discrepancy:
- What this establishes, and what it does not:
- Result commit URL:

Link the completed record from `validation-and-ai-use.md`. Keep the older experiments and their disclosed limitations as historical evidence.
