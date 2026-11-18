# Video preparation — prompts, not transcripts

No videos have been recorded by this workflow. Do not label these prompts as verbatim transcripts. Record on YouTube, enable transcripts, correct substantive errors, then save or link the actual transcripts in this repository.

Open **each** video with two student-reviewed statements:

> I used OpenAI Codex to help adapt my earlier lab code, build the app, test calculations, and draft documentation. The analysis and decision are mine.

> This is an educational project for a fictional scholarship fund, not investment advice.

## Video 1 — how the system and thinking changed (maximum 3:00)

- Describe the progression from Lab 13 mandate, Lab 14 baselines, Lab 15 sensitivity, and Lab 17 timing evidence to the app.
- Show one AI output that you actually checked. The 6.8% known-answer benchmark or the stray input-list bug are available examples; explain your own check, not merely that the assistant ran tests.
- Explain why an estimated numeric PASS became a paper-only recommendation with full-mandate FAIL.
- Describe one important uncertainty and how it affected your decision.

## Video 2 — code walkthrough (maximum 5:00)

- Show the actual frozen code and explain `evaluate()` in `model.py`, following the weighted-return and covariance functions in `portfolio.py`.
- Explain decimal versus percentage/basis-point units, asset order, cost deduction and turnover reference.
- Show how the search rejects infeasible weights and picks the minimum-volatility feasible grid allocation.
- Explain the signal vintage restriction and the missing raw-vintage limitation.
- State what the code cannot establish: loss guarantees, rolling five-year real return, real holdings/turnover, or complete liquidity compliance.

## Video 3 — committee presentation (maximum 5:00)

**Open with the app already running live**, and give the two required statements while showing it.

- State the mandate, 5.50% model hurdle and the paper-only / 0% live decision.
- Show default weights, 5.51% net estimate, 3.81% volatility, reserve and both verdict levels.
- Compare the two baselines and explain their failed rules.
- Move a control and distinguish changed inputs, fixed-portfolio stress results, and reoptimized weights.
- Give the paper sensitivity range, unresolved requirements, monitoring/reversal triggers, and precise committee ask.

Use the final results after any code changes. Ensure every spoken number agrees with the frozen app, memo and visible output. Supply YouTube URLs, actual durations, timestamp indices and transcript files in the manifest.
