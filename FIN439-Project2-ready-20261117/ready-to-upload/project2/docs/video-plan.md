# Revised video preparation — drafts, not transcripts

Prepared with OpenAI Codex on November 23 after the risk/source repair. Review and personalize every claim. These scripts are not evidence of recorded videos.

## Before recording

Refresh/restart the app to load the revised source. Defaults: objective 5.50%; reserve 3%; annual cost 25 bps; trading cost 10 bps; turnover limit 25%; **proposed annual volatility ceiling 6%**; ACWI adjustment 0 pp; last 36 returns off. Confirm **75/25, 5.57% net, 3.81% volatility**. A 5.51% display indicates the old model.

Use clear audio and a small webcam unless an approved accommodation applies. Speak both disclosures in each recording. Video 3's first frame must show the app running. Open the README, memo, student experiment, revision comparison, data card, risk policy and code. Search code by function name; previous line numbers changed.

**Do not mix versions:** original AI-off experiment = 5.51%→5.83%; revised model = 5.57%→5.89%. The original evidence remains unchanged. A current demonstration is a later illustration, not a new first run.

## Video 1 — Evolution and a checked AI output

Maximum **3:00**, aim 2:40. Suggested title: `FIN 439 Project 2 — How My System Changed and What I Checked`.

| Planned time | Screen |
|---|---|
| 0:00–0:20 | README; disclosures |
| 0:20–0:55 | Memo; numerical pass versus live clearance |
| 0:55–1:45 | Original prediction commit and experiment table |
| 1:45–2:40 | Revision comparison, risk policy and dated source |

### Suggested narration

I used OpenAI Codex to help build and revise the app, check calculations and primary sources, and draft documentation and recording guides. The analysis and decision are mine. This is an educational project for a fictional scholarship fund, not investment advice.

My project combines the earlier mandate, portfolio, stress and data-timing labs. My thinking changed from finding weights that pass numerical checks to deciding whether the committee could rely on the process. A return target alone does not establish acceptable risk.

One AI-assisted output I checked was the response to costs. With AI closed, I predicted that increasing annual cost from 25 to 35 basis points would make the original 75/25 portfolio miss the 5.50% hurdle and shift the search to 70% SGOV and 30% ACWI. I committed that prediction before running the change.

Here are the original results: net estimates moved from 5.51% to 5.83%, and volatility from 3.81% to 4.54%. The original weights would have earned 5.41% at the higher cost. My prediction matched. The higher selected return came from more equity exposure, not higher fees. That supports the calculation for this case, not forecast accuracy.

A later review found no enforced numerical risk ceiling and a signal supported only by a lab transcription. I accepted an AI-assisted repair with qualifications. The current model enforces a proposed 6% volatility ceiling and archives the Federal Reserve's September 16 announcement. Its target lower bound replaces the earlier effective-rate transcription; it is a different measure.

The revision changes current net estimates to 5.57% and 5.89%, with the same allocation choices. The original experiment files remain untouched. I distinguish these versions instead of claiming the old results came from revised code.

I retained a paper-only recommendation and zero live allocation. The ceiling is a research proposal, not committee approval or a loss guarantee, and the rate cap is not a validated forecast. Better evidence strengthens the research without proving suitability for live capital.

## Video 2 — Code, source checks and risk enforcement

Maximum **5:00**, aim 4:30. Suggested title: `FIN 439 Project 2 — Code, Data Timing and Risk Validation`.

| Planned time | Screen / action |
|---|---|
| 0:00–0:20 | Repository; disclosures |
| 0:20–0:55 | README command, `run.py`, file map |
| 0:55–1:45 | `signal_record()` and dated source/metadata |
| 1:45–2:45 | `estimates()`, `evaluate()`, `allocations()`, `solve()` |
| 2:45–3:50 | App: cost 35, ceiling 4 → reject; restore ceiling 6 and cost 25 |
| 3:50–4:30 | Current tests/audit; historical versus current results |

Show the actual code while explaining it; a README-only or interface-only video is insufficient.

### Suggested narration

I used OpenAI Codex to help build and revise the app, check calculations and primary sources, and draft documentation and recording guides. The analysis and decision are mine. This is an educational project for a fictional scholarship fund, not investment advice.

A user runs `python run.py` from this project folder. It creates an environment, installs the pinned dependency and starts Streamlit. First setup needs internet; calculations then use bundled data. The report is readable without execution.

`app.py` passes eight controls to the model. `portfolio.py` derives 60 returns from 61 monthly prices, and multiplies monthly means and sample covariance by twelve. Rates and weights are decimals internally.

Here is `signal_record()`. The signal is the 3.75% target lower bound announced September 16 at 2 p.m. Eastern, effective September 17, before our September 30 cutoff. The code checks units, dates, target values, hashes and supporting text in both archived Federal Reserve documents. Unsupported timing, inconsistent rates or a changed source file stop calculation.

`estimates()` caps SGOV's historical mean at that rate. The cap is nonbinding at defaults but binds in the 36-return window. It is a heuristic, not an ETF yield or validated forecast. Prices downloaded after the boundary do not establish a point-in-time performance backtest.

`evaluate()` subtracts annual cost and trading cost times one-way turnover from weighted gross return. Basis points are divided by ten thousand. Turnover is half the absolute changes from paper reference weights. Volatility is the square root of weighted annual covariance.

The rule set checks return, reserve, turnover and the proposed volatility ceiling. `allocations()` generates 1,771 five-point combinations. `solve()` keeps the least volatile candidate passing every modeled rule. Full clearance remains blocked by client-policy and operational requirements.

Here is a test of the risk constraint. At 35 bps and a 6% ceiling, the app selects 70/30 with 4.54% volatility. Tightening the ceiling to 4% rejects the scenario: the original weights miss return and the replacement exceeds risk. The model does not loosen the limit automatically. I restore 6%, then cost to 25 bps.

All 18 tests passed, including source tampering, future dates, exact risk boundaries and app recovery. Independent arithmetic reconciled 244 prices and eight scenarios. My locked experiment remains on its original model version; the revision table explains changed estimates. These checks support implementation and evidence consistency, not a loss guarantee or forecast validity.

## Video 3 — Committee recommendation with the live app

Maximum **5:00**, aim 4:35. Suggested title: `FIN 439 Project 2 — Scholarship-Fund Paper-Pilot Recommendation`.

**The first frame must show the app running at revised defaults.** This demonstration is later than the original experiment and uses the revised model's numbers.

| Planned time | Screen / action |
|---|---|
| 0:00–0:20 | Running app; disclosures |
| 0:20–1:05 | Recommendation, client and default metrics |
| 1:05–1:40 | Baselines and failed rules |
| 1:40–2:40 | Cost 25→35; ceiling 6→4 → reject; restore ceiling 6 and cost 25 |
| 2:40–3:25 | Stress table, sensitivity range and source card |
| 3:25–4:35 | Limitations, monitoring, breach response and committee ask |

### Suggested narration

I used OpenAI Codex to help build and revise the app, check calculations and primary sources, and draft documentation and recording guides. The analysis and decision are mine. This is an educational project for a fictional scholarship fund, not investment advice.

I recommend a paper research pilot and zero live allocation. This running app evaluates a ten-million-dollar scholarship fund paying seventy-five thousand dollars quarterly. It seeks inflation plus three percent net over rolling five-year periods. Assumed inflation of 2.5% gives a 5.50% annual planning hurdle. Twelve months of payouts require a three-percent reserve.

The current default is 75% SGOV and 25% ACWI, with 5.57% estimated annual net return and 3.81% volatility. It passes the modeled rules, including a proposed 6% volatility ceiling. That is a research assumption for review, not an approved client tolerance or maximum-loss guarantee. Full clearance remains FAIL.

Equal weight fails return, turnover and risk. Inverse volatility fails return. The benchmark fails reserve, turnover and risk. A modeled pass still needs operational verification and client-policy approval.

Increasing annual cost from 25 to 35 basis points lowers the original weights' net estimate to 5.47%, below the target. The model selects 70/30 with 5.89% net, 4.54% volatility and 5% turnover. This is the revised model. My original precommitted experiment used the earlier signal and reported 5.51% to 5.83%; that evidence remains preserved.

Now I tighten the volatility ceiling to 4%. The replacement breaches risk while the original misses return, so this scenario is rejected. The app does not silently relax the ceiling. I restore 6% and return cost to 25 bps.

Feasible stresses select 65% to 85% SGOV, with the rest in ACWI. That is a sensitivity range, not a live trading band. An 80% reserve, the combined adverse case and a 3% risk ceiling are infeasible. A replacement does not prove the original portfolio survived.

The policy signal comes from archived Federal Reserve documents published before our cutoff. Its return-cap use remains unvalidated. Later-downloaded prices do not establish historical tradability. Client loss policy, actual holdings and annual turnover, fund eligibility and liquidity need review.

At quarterly payouts and input updates, monitor reserves, net return, volatility, source timing, liquidity and turnover. A breach withdraws the candidate, suspends new paper allocations and requires recorded investigation and review before restarting. This static app is not a live monitor.

My committee ask is to authorize paper research, review the proposed risk policy and assign the remaining verification work. Keep live capital at zero until evidence and approvals support a different decision.

## After recording

Upload three separate YouTube videos as **Unlisted or Public**, never Private. Keep transcripts enabled. Correct material finance terms, tickers, attribution and numbers. Save actual corrected transcripts as `docs/transcript-video-1.txt`, `docs/transcript-video-2.txt` and `docs/transcript-video-3.txt`. Do not submit these scripts as transcripts.

Enter actual titles, URLs, durations and evidence timestamps in [submission-manifest.md](submission-manifest.md). Verify access without owner credentials. Reconcile current figures and original experiment figures to their respective versions. Attach final memo and validation Markdown files to Brightspace; save the receipt. Planned times are not actual evidence timestamps.

Sources: [Project 2 brief](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md), [checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md), [submission architecture](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/PROJECT-SUBMISSION-ARCHITECTURE.md).
