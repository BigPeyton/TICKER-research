I used OpenAI Codex to help adapt my earlier lab code, build the web app, test calculations, and draft documentation and recording guides. The analysis and decision are mine to review, explain, and defend.

This is an educational project for a fictional university scholarship fund, not investment advice.

# Decision memo — paper pilot; 0% live allocation

Updated November 23, 2026. Analysis boundary: September 30, 2026. Prices were downloaded October 22; this is a reconstruction, not a historical point-in-time return backtest. Final student review of this revised memo remains part of submission preparation.

**Recommendation:** authorize a paper research pilot, with **0% live allocation** until the committee resolves the missing risk policy and data/operational checks. Use **75% SGOV / 25% ACWI** as the default paper portfolio. Individually feasible engineering scenarios selected **65–85% SGOV / 15–35% ACWI**, with no SCHR or VTC. This is a sensitivity range, not a confidence interval or live trading band.

**Committee ask:** permit the paper exercise; define acceptable loss, a numerical risk limit and breach response; supply actual holdings and annual turnover; and verify fund eligibility, liquidity and historical signal evidence before considering live capital. Withdraw a failing candidate. Reject a scenario with no feasible grid allocation rather than silently relaxing the mandate.

## Mandate and method

The fictional $10 million scholarship fund pays $75,000 quarterly and seeks CPI + 3% net over rolling five-year periods, with a ten-year horizon. Assumed inflation of 2.5% gives a **5.50% annual planning hurdle**. Twelve months of payouts require $300,000, a **3% reserve**, modeled as SGOV only. The universe is SGOV, SCHR, VTC and ACWI; the benchmark is 60% ACWI / 40% VTC.

The mandate is fully invested and long-only, with no direct borrowing or derivatives, at least 90% five-day liquidity, and an 8% company limit with documented exemptions. Annual turnover above 25% requires approval. Modeled turnover is one-way change from the prior 75/25 paper proposal, not verified holdings or cumulative annual trading. The mandate lacks an approved numerical loss/risk limit; volatility is measured but is not tested against an approved ceiling.

The model uses 60 monthly adjusted-price returns, arithmetic means multiplied by twelve, and sample covariance multiplied by twelve. It selects the least volatile feasible allocation on a five-percentage-point grid. Costs are 25 bps annually plus 10 bps times modeled one-way turnover, charged once for the proposed rebalance. These are illustrative additional costs, not verified fee quotes.

SGOV's annual mean is capped at the prior Lab 17 FEDFUNDS observation of 3.63%, recorded for the September 30 vintage. The raw vintage remains unavailable. This policy-rate proxy is an unvalidated heuristic, not an observed ETF return or Treasury yield forecast. See the [data card](data-card.md).

## Results and changed-input evidence

| Portfolio at defaults | Net annual estimate | Annualized volatility | SGOV reserve | Modeled verdict |
|---|---:|---:|---:|---|
| Equal weight | 3.53% | 6.55% | 25.00% | FAIL: return and turnover |
| Inverse volatility | 3.10% | 1.33% | 84.20% | FAIL: return |
| 60% ACWI / 40% VTC benchmark | 6.90% | 11.63% | 0.00% | FAIL: reserve and turnover |
| Constrained 75% SGOV / 25% ACWI | **5.51%** | **3.81%** | **75.00%** | PASS numerical rules |

**All portfolios fail full-mandate clearance.** The default exceeds the modeled hurdle by only about 0.01 percentage point. A first-year arithmetic estimate does not demonstrate rolling five-year real returns, forecast accuracy, or a maximum-loss guarantee.

In Peyton's [precommitted student experiment](student-experiment.md), increasing additional annual cost from **25 to 35 bps** left the original weights with **5.41%** estimated net return, below the hurdle. Reoptimization selected **70% SGOV / 30% ACWI**, with **5.83% net return, 4.54% volatility and 5% modeled turnover**. The higher selected estimate reflects greater equity exposure, not a benefit from higher fees. The prediction matched; numerical PASS, full-mandate FAIL and the paper-only decision remained. Peyton confirmed writing the prediction, executing the run and writing his observations with AI closed. Code/data hashes match across the exports.

Other stresses expose fragility: ACWI's mean minus two percentage points leaves the original portfolio at 5.01% net; reoptimization selects 65/35 at 5.65% net and 5.28% volatility. At 100 bps annual cost, the original falls to 4.76%; 65/35 gives 5.60%. The 36-return window selects 85/15 at 5.90% net and 1.76% volatility. An 80% SGOV reserve requirement and the combined stress have no feasible grid candidate. Reoptimization does not mean the original weights survived.

## Monitoring and reversal

At quarterly payout reviews, check the next twelve months' reserve dollars, net estimate against the objective, source completeness and timing, volatility and stress sensitivity, actual liquidity and cumulative annual turnover. Rebalance annually or by documented exception. Stop using a candidate when a modeled requirement fails or timing evidence becomes unreliable. Restrict the present work to paper research because source and mandate gaps remain; it is not cleared for reliance with live capital.

Evidence: [visible output](../outputs/results.md), [validation and AI use](validation-and-ai-use.md), [student experiment](student-experiment.md), [data card](data-card.md), and [original mandate](prior-evidence/lab13_portfolio_mandate.md). Peyton confirmed the partner task and Lab 20 submission. Those do not establish final Project 2 submission or resolve the model's limitations.
