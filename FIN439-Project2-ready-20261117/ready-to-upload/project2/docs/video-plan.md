# Project 2 recording guide — drafts, not transcripts

Prepared with OpenAI Codex on November 23, 2026. These are suggested narration and screen cues for Peyton to review, personalize and deliver. They do not claim that a video was recorded. Corrected transcripts must come from the actual recordings; do not submit this guide as a transcript.

## Before recording

1. Keep the app terminal running. Open the app at `http://127.0.0.1:8501`.
2. Restore the defaults before each recording: objective 5.50%; minimum SGOV reserve 3%; annual additional cost 25 bps; trading cost 10 bps; turnover limit 25%; ACWI adjustment 0 pp; last 36 returns unchecked. Confirm 75% SGOV / 25% ACWI, 5.51% net and 3.81% volatility.
3. Open the [current repository](https://github.com/BigPeyton/TICKER-research/tree/main/FIN439-Project2-ready-20261117/ready-to-upload/project2), [student experiment](student-experiment.md), [memo](decision-memo.md), and [validation record](validation-and-ai-use.md) in separate tabs. For Video 2, open `app.py`, `model.py` and `portfolio.py` in your editor.
4. Use screen recording with clear audio and a small webcam view, as required by the submission architecture unless an approved accommodation applies. Make text large enough to read. Record a short practice clip and check sound and framing.
5. Speak the AI/ownership and education statements at the beginning of **each** recording. Video 3 must show the running app from its opening frame.
6. Review the suggested narration against your own understanding. Change wording that does not sound like you; preserve the facts. These are rehearsal targets, not actual evidence timestamps.

## Video 1 — From numerical PASS to a paper-only decision

**Maximum 3:00; aim for 2:30–2:50.** Suggested title: `FIN 439 Project 2 — How My Scholarship-Fund System Changed`.

| Planned time | Screen / action |
|---|---|
| 0:00–0:20 | Show project README; deliver both opening statements. |
| 0:20–0:55 | Show memo and explain the progression from earlier labs to the decision. |
| 0:55–1:55 | Show `student-experiment.md`, its original prediction commit, and the before/after table. Explain one check of AI-assisted model logic. |
| 1:55–2:40 | Show the model's limitations and explain how they restrict the recommendation. |

### Suggested narration

I used OpenAI Codex to help adapt my earlier lab code, build the app, check calculations, and draft documentation and recording guides. The analysis and decision are mine. This is an educational project for a fictional scholarship fund, not investment advice.

My system began with the Lab 13 mandate: a university scholarship fund that needs regular payouts and a return above inflation. The baseline and portfolio labs added allocation comparisons, and the later labs added stress tests and data-timing checks. I brought those pieces into one app that shows both its numerical results and the limits of its recommendation.

My main change in thinking was learning that a numerical PASS is not permission to invest. The default portfolio meets the modeled return, reserve and turnover checks, but the committee has not approved a numerical loss limit, and operational and data checks remain unresolved. That changed my focus from finding attractive weights to explaining whether the process could be relied on.

One AI-assisted output I checked was the model's response to higher annual costs. With AI closed, I predicted that increasing costs from 25 to 35 basis points would make the original 75/25 portfolio miss the 5.50% objective. Ten extra basis points reduce its estimated net return from about 5.51% to 5.41%. I expected the five-point search to shift to 70% SGOV and 30% ACWI, with higher volatility.

I committed that prediction before testing, then ran the change and wrote my observations with AI closed. The downloaded results matched: 70/30, 5.83% estimated net return and 4.54% volatility. The higher selected return came from more equity exposure, not from higher fees. That supports the cost calculation and allocation response for this case; it does not prove forecast accuracy.

I retained the model for paper analysis and kept live allocation at zero. The raw historical rate vintage is still missing, the policy-rate proxy is unvalidated, and the risk policy is incomplete. My recommendation changes only when the evidence and mandate checks support it.

## Video 2 — How the data becomes a portfolio decision

**Maximum 5:00; aim for 4:10–4:40.** Suggested title: `FIN 439 Project 2 — Code, Validation and the Cost Experiment`.

| Planned time | Screen / action |
|---|---|
| 0:00–0:20 | Show the repository and give both opening statements. |
| 0:20–0:55 | Show the README command, `run.py`, the file map and visible output. |
| 0:55–1:35 | Show `estimates()` and `signal_record()` in `model.py`; explain data/units and the signal limitation. |
| 1:35–2:30 | Show `evaluate()` and the return/volatility helpers. Explain the cost formula and two verdicts. |
| 2:30–3:00 | Show `allocations()` and `solve()`; explain five-point enumeration and the feasible minimum. |
| 3:00–4:10 | Show the saved student experiment, before/after values, prediction commit and source hashes. |
| 4:10–4:40 | Show the test evidence and explain a failure case and limitations. |

Useful code locations in the unchanged tested source: `model.py` — `turnover()` line 59, `signal_record()` line 64, `estimates()` line 83, `evaluate()` line 101, `allocations()` line 135, `solve()` line 145, `stress_suite()` line 170, `export_result()` line 197. `portfolio.py` — `expected_return()` line 59, `portfolio_volatility()` line 64, `estimate_from_csv()` line 122. Search by function name if editor line numbers differ.

### Suggested narration

I used OpenAI Codex to help adapt my earlier lab code, build the app, check calculations, and draft documentation and recording guides. The analysis and decision are mine. This is an educational project for a fictional scholarship fund, not investment advice.

This is the submitted project folder. A user runs `python run.py` from the folder containing this README. The launcher creates an isolated environment, installs the pinned dependency, and starts Streamlit. The first setup needs internet; the model then uses bundled data. The visible output is also readable in `outputs/results.md` without running anything.

The interface in `app.py` collects seven controls and passes them to the model. In `estimates()`, the code checks the asset order and data boundary. The price file has 61 monthly prices and 60 returns. Monthly means and covariance are annualized by multiplying by twelve. Returns and weights are decimals internally; the interface converts percentages and percentage points.

The signal gate requires the September 30 vintage and percent units. It caps SGOV's estimated return at the prior lab's 3.63% policy-rate proxy. The date check rejects a later vintage, but it cannot authenticate the transcription. The raw historical download is missing, so this remains a disclosed limitation.

Here is `evaluate()`. It validates weights, calculates weighted gross return, then computes one-way turnover as half the sum of absolute changes from the 75/25 reference. Cost equals annual basis points divided by ten thousand, plus turnover times trading-cost basis points divided by ten thousand. Net return is gross return minus cost. Volatility comes from the weights and covariance matrix.

The numerical checks cover the return objective, reserve and modeled turnover. The full-mandate verdict stays FAIL because the loss policy and other requirements remain unresolved. This separation is deliberate: a numerical pass does not establish full compliance.

`allocations()` enumerates 1,771 combinations in five-percentage-point steps. `solve()` rejects candidates that fail the rules and retains the feasible candidate with the lowest estimated volatility. This is a grid search, not proof of a continuous global optimum.

My saved experiment tests this decision path. I wrote the prediction at 2 p.m. with AI closed; the commit was published at 2:05:47. The changed-scenario payload was generated at 2:09:10. Only annual cost changed, from 25 to 35 basis points, and all eight exported source hashes match.

The original weights would fall to 5.41% net. The search selected 70/30, giving 5.83% net and 4.54% volatility. Five percent turnover adds half a basis point of trading cost. That agrees with my prediction, while full clearance and live allocation remain unchanged.

The development suite passed 15 tests, including asset order, cost units, missing data, source hashes and app interaction. The arithmetic audit also reconciled the archived prices. An 80% reserve requirement produces no feasible grid allocation; the app rejects that scenario. None of these checks establishes a loss guarantee, a valid forecast, or rolling five-year real-return performance.

## Video 3 — Committee recommendation and live demonstration

**Maximum 5:00; aim for 4:00–4:35.** Suggested title: `FIN 439 Project 2 — Scholarship-Fund Committee Recommendation`.

**The first frame must show the app running at the defaults.** Speak the two disclosures while the app is visible. The control change during this recording is a replay of the already-completed experiment, not a new first run.

| Planned time | Screen / action |
|---|---|
| 0:00–0:20 | Running app at defaults; give both statements. |
| 0:20–1:00 | Point to recommendation and default metrics; explain the client and hurdle. |
| 1:00–1:40 | Show comparison table and expand baseline failed rules. |
| 1:40–2:35 | Replay annual cost 25 → 35 bps; point to 70/30, 5.83%, 4.54% and 5% turnover. Restore 25 bps. |
| 2:35–3:20 | Expand predefined stress table; explain the sensitivity range and infeasible reserve case. |
| 3:20–4:35 | Show monitoring/decision panel; explain limitations, reversal conditions and committee ask. |

### Suggested narration

I used OpenAI Codex to help adapt my earlier lab code, build the app, check calculations, and draft documentation and recording guides. The analysis and decision are mine. This is an educational project for a fictional scholarship fund, not investment advice.

My recommendation is to authorize a paper research pilot and allocate zero live capital. This running app evaluates a fictional ten-million-dollar scholarship fund that pays seventy-five thousand dollars each quarter. The mandate seeks inflation plus three percent net over rolling five-year periods. With assumed inflation of 2.5%, the model uses a 5.50% annual hurdle. Twelve months of payouts require a three-percent reserve.

At the defaults, the selected paper portfolio is 75% SGOV and 25% ACWI. Its estimated annual net return is 5.51%, volatility is 3.81%, and reserve is 75%. It passes the numerical rules but fails full-mandate clearance. The margin above the return hurdle is extremely small, and this estimate is not a guarantee.

The app compares this candidate with equal weight and inverse volatility, plus a 60/40 benchmark. Equal weight fails return and turnover. Inverse volatility fails the return hurdle. The benchmark fails the reserve and turnover checks. Every portfolio fails full clearance because the unresolved requirements apply beyond these numerical comparisons.

I will replay my completed cost experiment. Changing only additional annual cost from 25 to 35 basis points makes the original portfolio's net estimate about 5.41%, below the objective. The model instead selects 70% SGOV and 30% ACWI. Its net estimate is 5.83%, volatility is 4.54%, and turnover is 5%. The higher selected return comes with more equity exposure. My prediction was committed before the original run, and the result matched. The decision remains paper-only. I am now restoring the default cost.

The engineering stresses selected paper allocations ranging from 65% to 85% SGOV, with the remainder in ACWI. That is a sensitivity range, not a live trading band. Lower expected equity returns and higher costs can disqualify the original weights. An 80% reserve requirement leaves no feasible allocation on this grid. A replacement portfolio does not mean the original one survived the stress.

The committee still needs an approved loss limit and breach response, actual holdings and annual turnover, fund permissions, liquidity checks, and authenticated historical signal evidence. The code measures volatility but cannot guarantee maximum loss or prove rolling five-year real returns. The policy-rate cap is an unvalidated assumption.

At quarterly payout reviews, monitor reserve dollars, estimated net return, source timing, volatility, stress sensitivity and operational compliance. Withdraw a candidate when a modeled requirement fails, and stop relying on timing evidence that cannot be verified. Do not allocate live capital while these clearance gaps remain.

My committee ask is to approve paper analysis, define the missing risk policy and assign the outstanding verification work. Consider live investment only after the evidence and required checks support that decision.

## After recording — actual submission artifacts

- Save three separate videos. Upload to YouTube as **Unlisted or Public**, never Private; enable captions/transcripts. Public publishing is optional.
- Review the actual spoken wording and correct material transcription errors: SGOV, ACWI, SCHR, VTC, basis points, percentages, dollar amounts, dates, and PASS/FAIL distinctions.
- Save the actual corrected transcripts as `docs/transcript-video-1.txt`, `docs/transcript-video-2.txt`, and `docs/transcript-video-3.txt`. No placeholder transcript files have been created.
- Record actual titles, durations and evidence timestamps in [submission-manifest.md](submission-manifest.md). Replace planned times with the actual moments; do not assume rehearsal windows match the recording.
- Verify that links open without your owner credentials, required disclosures are spoken, Video 3 starts with the running app, and all material figures agree with the memo and output.
- The final student review, video recording and final Brightspace submission are still pending. Nothing in this guide claims they occurred.

Sources: [Project 2 brief](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md), [student checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md), and [submission architecture](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/PROJECT-SUBMISSION-ARCHITECTURE.md).
