# Lab 20 — Peyton's Project 2 readiness record

**Status: Luke's returned cold-run note received; independent app startup unresolved.** The note reports a package-installation DNS failure, a successful offline report, and a later assisted browser control check. It does not establish a clean independent web-app launch. Luke's separate code was already cold-run by Peyton and returned, as reported by Peyton.

Question: Could a committee member who has never met me reach my decision from this repository, and does the decision survive one changed input?

## Repository and visible result

- Repository / project-folder URL: [published Project 2 folder](https://github.com/BigPeyton/TICKER-research/tree/main/FIN439-Project2-ready-20261117/project2). Its 30 app/data/documentation/test files were verified against the tested local package before this returned-note update. This updated record and README still need to be uploaded.
- [README](../README.md), [executed output](../outputs/results.md), [decision memo](decision-memo.md), [validation and locked record](validation-and-ai-use.md).
- App startup command: `python run.py`, from the folder containing `run.py`.
- Development result: 14 checks pass; separate from the partner cold run below.

## Luke's cold run — returned observations

Source: [Luke's original returned note](luke-cold-run.md), copied unchanged from `lab20-readiness (2).md`. The table below summarizes his report; it does not add an independently verified startup or an inferred commit.

| Field | Partner's observation |
|---|---|
| Reviewer and date/time | Luke; November 17, 2026. Time of day not recorded. |
| Exact repository commit tested | Not recorded. The later running app's commit and successful launch command were not verified. |
| OS / Python version | Windows; Python 3.13.15. |
| Exact command run | `python run.py` from a fresh `project2` copy; offline fallback `python run.py --report`. |
| First failure, or explicitly “none” | `Failed to resolve 'pypi.org' ([Errno 11001] getaddrinfo failed)`; dependency installation failed and launcher exited with code 1. |
| Elapsed time from starting README to decision | Reading time was not measured. Offline report confirmed the decision 36 seconds after the first launch command. Later browser control check took 7 seconds from the loaded app, excluding Peyton's startup time. |
| Location of visible result | README; `outputs/results.md`; later, app decision heading and full-mandate alert at `http://127.0.0.1:8503/`. |
| Control moved and resulting mandate verdict | Minimum SGOV reserve 3% → 80%, other defaults unchanged: REJECT scenario / no feasible grid allocation. Full mandate remained FAIL. |
| Restored defaults | Reserve restored to 3%: PILOT ON PAPER; 0% live allocation; modeled PASS; net estimate 5.51%; full mandate FAIL. |

The initial startup retry hit the same DNS error. The later browser control check used the app Peyton supplied, so it is recorded as assisted. The infeasible 80% reserve scenario is a model verdict, not an application crash. It is also not Peyton's required prospective changed-input prediction.

## Changed input — predicted first

Peyton supplied a trading-cost-per-turnover experiment, 10 → 30 bps, with all other controls at defaults. He reports saving his prediction before testing: unchanged 5.51% net return, 3.81% volatility, 75% SGOV / 25% ACWI, paper-only recommendation, numeric PASS and full-mandate FAIL. The reported actual results matched. His explanation is zero modeled turnover, which makes the higher trading-cost multiplier contribute zero drag. The control was left at 30 bps. See the [prediction and result record](validation-and-ai-use.md#locked-changed-input-record).

Peyton confirmed that he wrote the prediction before testing but did not commit it to GitHub first. The pre-run GitHub commit requirement was not completed; this report preserves the prediction and reported results while disclosing that gap. Original experiment exports still need to be attached. The earlier AI-assisted 25 → 50 bps annual-cost experiment is preserved separately.

- Prediction commit: NOT COMPLETED before testing, as confirmed by Peyton. The prediction was written before testing but was not uploaded to GitHub first.
- Before/after output links: PENDING.
- Result commit: PENDING.

## Explain the code — six minutes with AI closed

Open `model.py` at `evaluate()`: it produces gross return, turnover, cost drag, net return, volatility, and the numeric mandate verdict. Follow its call to `expected_return()` in `portfolio.py` if needed. Explain the actual lines to Luke, then answer a question from the code. This is the student's live explanation, not an AI-written substitute.

- Written walkthrough supplied: `model.py`, `evaluate()`, lines 101–132. The exact commit used for a live explanation was not supplied.
- Live explanation to Luke with AI closed: confirmed by Peyton. Exact elapsed duration was not recorded.
- Luke's question, as supplied by Peyton: Why can a portfolio pass the modeled rules but still fail the full mandate?
- Peyton's supplied answer: The modeled rules check numerical requirements, such as net return, reserve weight, and turnover. Other requirements still need human verification, so the code always sets full_mandate_verdict to "FAIL — not cleared for live use", even if every modeled rule passes.
- Lines needing further study after the exchange: no additional lines identified in Peyton's supplied response.

**Summary of Peyton's supplied written walkthrough (formatted afterward by Codex):** The function accepts the portfolio name, weights, estimates and settings; validates weights; computes gross return, turnover, costs, net return and covariance-based volatility; checks measurable rules; lists unresolved requirements; and returns a dictionary with numeric results and verdicts. Peyton explained basis-point conversion and asset-order alignment, identified the hardcoded fully-invested/long-only flag, noted the absence of a volatility-limit test, and distinguished numeric PASS from the always-FAIL full-mandate verdict. His gross-return and cost examples calculate correctly.

**Helper details checked during review:** `checked_weights()` converts weights to floats and checks exactly four finite, nonnegative weights summing to one within `TOL = 1e-12`; it does not infer the asset identities from the numbers. `turnover()` is half the sum of absolute weight changes from the illustrative 75% SGOV / 25% ACWI reference. The returned weight dictionary contains all four named assets, including zero weights, rather than the two-key illustrative dictionary in the supplied explanation. The unavailable raw historical evidence specifically concerns the FEDFUNDS vintage; archived Yahoo price responses are bundled. These clarifications are assistant feedback, not a claimed partner question or live student answer.

## Fix one thing and rerun

- First failure from Luke's run: dependency installation could not resolve `pypi.org`.
- Change prepared in response: README now names this error, explains that setup failed before app startup, documents the offline fallback's limits, and specifies what constitutes an independent rerun. This is a documentation improvement, not a demonstrated DNS repair. No source-code change was made.
- Documentation upload: [f497adc026d98c4ad4dd987d3ed8ac8caf44c624](https://github.com/BigPeyton/TICKER-research/commit/f497adc026d98c4ad4dd987d3ed8ac8caf44c624) placed the updated package inside the existing project folder, creating a nested duplicate. The intended project-folder README still needs the update; this is not a verified independent startup fix.
- Luke's reported retry: same DNS failure; offline report still worked. Later supplied-app control check worked, with startup command and commit unverified.
- Rerun after the documentation update: PENDING. Independent first-time web-app startup remains unresolved; do not mark this a clean run or “no fix needed.”

The stray `1` corrected during development occurred before Luke's independent run. Do not use that as a substitute for this step.

## Decision line — Peyton's confirmed recommendation

**Decision category: pilot for analysis; 0% live allocation.**

Peyton's own statement: “I recommend using the app for analysis, but not live investing. I would reverse that decision once the unresolved requirements are verified and approved and the portfolio passes all required checks.”

## Reflect — Peyton's supplied responses

1. **What the cold run revealed:** “It showed me that passing the modeled checks does not mean the portfolio meets the full mandate. I had focused on the numerical results and overlooked the unresolved requirements.”
2. **What I will not change before the deadline:** “I will avoid changing the calculations, default settings, decision rules, or app layout before the deadline, except to fix a critical error.”

## Individual checkout

- Partner's cold-run note: RECEIVED and preserved unchanged; startup limitation documented.
- Changed-input prediction and result: REPORTED by Peyton for trading cost 10 → 30 bps. Pre-run GitHub commit: NOT COMPLETED; Peyton confirmed predicting before testing but not committing first. Original experiment exports: PENDING.
- Fix pushed and rerun, or independently clean run recorded: documentation update uploaded in a nested duplicate; intended-folder README update and successful independent startup remain unresolved.
- Code explanation: Peyton confirmed explaining the code to Luke with AI closed; supplied question and answer recorded above.
- Student-owned decision line and reversal condition: CONFIRMED above.
- Reflection and freeze statement: SUPPLIED above.
- Original project folder: published and verified. Nested duplicate contains an earlier documentation update. These merged readiness/validation records and the original partner note still need publication in the intended `docs` folder.

Submit individually. The [lab](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-13/lab-20-project2-readiness.md) allows truthful unresolved items; it does not approve Project 2. Check the separate Project 2 manifest for videos and final submission items.
