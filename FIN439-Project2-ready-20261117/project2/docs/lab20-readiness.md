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

- Code block/commit explained: PENDING.
- Luke's question: PENDING.
- Peyton's own answer: PENDING.
- Lines needing further study after the exchange: PENDING.

## Fix one thing and rerun

- First failure from Luke's run: dependency installation could not resolve `pypi.org`.
- Change prepared in response: README now names this error, explains that setup failed before app startup, documents the offline fallback's limits, and specifies what constitutes an independent rerun. This is a documentation improvement, not a demonstrated DNS repair. No source-code change was made.
- Pushed fix commit: PENDING upload of this README/documentation update.
- Luke's reported retry: same DNS failure; offline report still worked. Later supplied-app control check worked, with startup command and commit unverified.
- Rerun after the documentation update: PENDING. Independent first-time web-app startup remains unresolved; do not mark this a clean run or “no fix needed.”

The stray `1` corrected during development occurred before Luke's independent run. Do not use that as a substitute for this step.

## Decision line — draft for Peyton to review

**Pilot the process on paper, with 0% live allocation; withdraw a failing paper allocation when return, reserve, turnover or source checks fail, and require a resolved risk policy plus operational/data clearance before considering live capital.**

Peyton's final line / confirmation: PENDING.

## Reflect — Peyton explains to Luke

1. What the cold run revealed that I had missed: PENDING after the run.
2. What I will not change before the deadline: PENDING student choice.

## Individual checkout

- Partner's cold-run note: RECEIVED and preserved unchanged; startup limitation documented.
- Changed-input prediction and result: REPORTED by Peyton for trading cost 10 → 30 bps. Pre-run GitHub commit: NOT COMPLETED; Peyton confirmed predicting before testing but not committing first. Original experiment exports: PENDING.
- Fix pushed and rerun, or independently clean run recorded: README improvement prepared; push and independent rerun PENDING.
- Student-owned decision line and reversal condition: PENDING review.
- Original project folder: published and verified. Updated readiness/validation/README and Luke's returned note: PENDING publication.

Submit individually. The [lab](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-13/lab-20-project2-readiness.md) allows truthful unresolved items; it does not approve Project 2. Check the separate Project 2 manifest for videos and final submission items.
