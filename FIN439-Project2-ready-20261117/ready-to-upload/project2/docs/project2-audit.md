# Project 2 readiness audit — revised November 23, 2026

The earlier audit identified a missing modeled risk ceiling and weak signal-source evidence. The [readiness revision](readiness-revision.md) addresses both without changing the original student experiment.

| Course requirement | Current evidence |
|---|---|
| Runnable Python web app | `run.py`, pinned dependencies, README; two Streamlit interaction tests pass |
| Mandate, risk measure and limits | Original fictional mandate plus proposed 6% annualized-volatility ceiling, enforced and stress tested; client approval remains a separate limitation |
| Two baselines and constrained portfolio | Equal weight, inverse volatility and selected portfolio, with individual failed rules; 60/40 comparator also supplied |
| One point-in-time signal and data card | Dated Sep 16 Federal Reserve statement and implementation note archived and checked, effective Sep 17 before Sep 30 cutoff |
| Stresses and stopping condition | Eight scenarios, including binding risk conflicts; reject infeasible scenarios and stop/review breaches |
| Locked Changed-Input Record | Original AI-off student prediction and run on the prior model preserved unchanged and included in validation |
| Recommendation, range and triggers | Paper pilot, 0% live; 65–85% SGOV sensitivity range; explicit monitoring and reversal |
| Opening disclosures | README, memo and revised video scripts include named AI/ownership and education statements |

Verification: 18 tests pass; independent arithmetic reconciles 244 prices and all eight scenarios. See [audit results](../outputs/readiness-audit.json), [test log](../outputs/readiness-tests.txt) and [current visible results](../outputs/results.md). The default is now 5.57% net; historical student results remain 5.51%/5.83%. This distinction must be maintained in videos.

Remaining: student review/understanding, three actual videos, corrected transcripts, actual manifest metadata/timestamps, final snapshot/access check, Brightspace deadline check and final submission receipt. Luke's task and Lab 20 are completed per Peyton. No final submission is claimed.

The proposal is not decision-ready for live capital: client risk-policy approval, liquidity/eligibility, actual holdings/annual turnover, forecast validity and rolling-five-year objective evidence remain unresolved. An honest paper-only/reject-live decision is the intended scope; no grade guarantee is made.
