I used OpenAI Codex to help adapt my earlier lab code, build and revise the app, check calculations and primary sources, and draft documentation and recording guides. The analysis and decision are mine to review, explain, and defend.

This is an educational project for a fictional university scholarship fund, not investment advice.

# Decision memo — paper pilot; 0% live allocation

Updated November 23, 2026 after the readiness revision. Analysis cutoff: September 30, 2026. Adjusted prices were downloaded October 22; this is an estimate reconstruction, not a point-in-time performance backtest.

**Recommendation:** authorize a paper research pilot; allocate **0% live** until client policy, operations and evidence of suitability are cleared. Use **75% SGOV / 25% ACWI** as the default paper portfolio: **5.57% estimated annual net return and 3.81% annualized volatility**. Feasible individual stresses select **65–85% SGOV / 15–35% ACWI**, with no SCHR/VTC. This is a sensitivity range, not a confidence interval or a live trading band.

**Committee ask:** review the proposed 6% annualized-volatility ceiling and breach response; define acceptable loss and approve a complete risk policy; verify actual holdings, annual turnover, fund eligibility and liquidity. Permit only paper research pending those decisions. Withdraw a failing candidate and reject an infeasible scenario rather than relaxing the mandate.

## Mandate and method

The fictional $10 million scholarship fund pays $75,000 quarterly, seeks CPI + 3% net over rolling five-year periods, and has a ten-year horizon. Assumed inflation of 2.5% gives a **5.50% annual planning hurdle**. Twelve months of payouts require a $300,000 **3% reserve**, modeled as SGOV. Universe: SGOV, SCHR, VTC, ACWI. Benchmark: 60% ACWI / 40% VTC.

The portfolio is fully invested and long-only, with no direct borrowing or derivatives. At least 90% must be liquid within five days; the 8% company limit has documented exemptions; annual turnover above 25% needs approval. Modeled turnover uses the earlier 75/25 paper proposal, not verified actual holdings or cumulative annual trading.

The revised model enforces a **proposed 6% annualized-volatility ceiling**, calculated from monthly sample covariance × 12. This round research parameter was chosen after earlier results were available; it is not a client approval, calibrated safety threshold or maximum-loss guarantee. A breach suspends the candidate and requires review. See the [risk policy](risk-policy.md).

The search selects the least volatile feasible portfolio on a five-percentage-point grid. It uses 60 monthly returns, arithmetic annual means, 25 bps annual additional cost and 10 bps × one-way turnover, charged once. A dated September 16 Federal Reserve announcement supplies the **3.75% target lower bound** used to cap SGOV's annual mean. The cap is nonbinding at defaults and binding in the 36-return window. Both official source documents are archived and verified; predictive validity remains unproven.

## Results and validation

| Default portfolio | Net estimate | Volatility | Modeled verdict |
|---|---:|---:|---|
| Equal weight | 3.55% | 6.55% | FAIL: return, turnover, risk |
| Inverse volatility | 3.17% | 1.33% | FAIL: return |
| 60/40 benchmark | 6.90% | 11.63% | FAIL: reserve, turnover, risk |
| Constrained 75/25 | **5.57%** | **3.81%** | PASS |

**All fail full-mandate clearance.** The default's return margin is only about 0.07 percentage point. Arithmetic estimates and passing tests do not establish forecast accuracy or the rolling five-year real objective.

Peyton's original [AI-off experiment](student-experiment.md) remains unchanged: on its earlier model, cost 25→35 bps shifted 75/25 to 70/30, with net estimates 5.51%→5.83% and volatility 3.81%→4.54%. Its prediction preceded the changed run. The later source/risk revision is AI-assisted development work, not a new locked experiment. In the current model, the same cost scenario yields 70/30 at **5.89%**; unchanged 75/25 weights yield **5.47%**, below the hurdle. More equity, not higher fees, explains the higher selected return.

Current stresses: equity estimate −2 pp leaves original weights at 5.07%; reoptimization selects 65/35 at 5.70% net and 5.28% volatility. Cost 100 bps leaves original weights at 4.82%; 65/35 gives 5.65%. The 36-return window selects 85/15 at 6.00% net and 1.76% volatility. An 80% reserve, combined adverse scenario, 3% risk ceiling, or 35-bps cost with a 4% ceiling is infeasible. Reoptimization does not establish that the original portfolio survived.

## Monitoring and reversal

Review quarterly with payouts and whenever inputs are updated: reserve dollars, net estimate, volatility against the ceiling, source integrity/timing, stress sensitivity, liquidity and cumulative turnover. Breach: withdraw the candidate, suspend new paper allocations, record and investigate the failure, then seek explicit policy review before restarting. Never raise the ceiling automatically. This static-data app is not a live monitor.

Client loss-policy approval, operational evidence, forecast validity and rolling five-year performance remain unresolved. Those limitations keep the recommendation at zero live allocation.

Evidence: [visible output](../outputs/results.md), [validation/AI use](validation-and-ai-use.md), [data card](data-card.md), [revision reconciliation](readiness-revision.md), and [original mandate](prior-evidence/lab13_portfolio_mandate.md). Final student review and recordings remain pending.
