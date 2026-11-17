I used OpenAI Codex to help adapt my earlier lab code, build the web app, test calculations, and draft documentation. The analysis and decision are mine to review, explain, and defend.

This is an educational project for a fictional university scholarship fund, not investment advice.

# Decision memo — paper pilot only

**Draft for Peyton's review and ownership; prepared November 17, 2026.** Input boundary: September 30, 2026. Prices were downloaded October 22, so this is a reconstruction, not proof of a strategy executable at that historical boundary.

**Recommendation:** pilot the process on paper; allocate **0% live** until the committee resolves its risk policy and the operational/data gaps. Use **75% SGOV / 25% ACWI** as the base paper allocation, with zero SCHR and VTC. Across the individually feasible engineering scenarios, selected paper weights range from **65–85% SGOV and 15–35% ACWI**. This is an observed sensitivity range, not a live trading band or confidence interval. The reserve and combined stresses have no feasible grid candidate.

**Committee ask:** authorize the paper research exercise, define acceptable loss and a breach response, supply actual holdings/annual turnover, and verify fund eligibility and source evidence before considering live capital. Reverse the paper allocation when it fails a modeled requirement; reject the scenario if no feasible allocation remains on the grid. Do not solve a failure by silently changing the mandate.

## Mandate and evidence

The fictional fund has $10 million, pays $75,000 quarterly, and seeks CPI + 3% net annually over rolling five-year periods with a ten-year horizon. Assumed inflation of 2.5% gives an annual model hurdle of 5.50%. Twelve months of payouts require $300,000, or 3%, in the reserve sleeve. The model includes SGOV, SCHR, VTC, and ACWI. Only SGOV is treated as reserve-eligible; the benchmark is 60% ACWI / 40% VTC.

The fund is long-only with no direct borrowing or derivatives, at least 90% five-day liquidity, and an 8% company limit with the documented exemptions. Annual turnover above 25% requires committee approval. The model uses Lab 15's proposed 75/25 allocation as an illustrative turnover reference, not confirmed holdings. Its single-rebalance calculation cannot establish actual annual turnover compliance. No numeric loss limit was provided, so full-mandate clearance remains **FAIL** for every portfolio.

Estimates use 60 monthly adjusted-price returns (October 2021–September 2026), annualized arithmetic means, and sample covariance. Net returns subtract an illustrative 25 bps annual operating/advisory cost and 10 bps per dollar of one-way rebalance turnover. The prior Lab 17 record identifies August FEDFUNDS of 3.63% as available in the September 30 vintage; the model caps SGOV's annual mean at that policy-rate proxy. This is an unvalidated modeling choice, not an observed Treasury yield. The raw vintage could not be retrieved again; the prior checked summary is preserved and clearly labeled.

## Results and decision limits

| Portfolio | Annual net estimate | Annualized volatility | Reserve | Modeled verdict |
|---|---:|---:|---:|---|
| Equal weight | 3.53% | 6.55% | 25.00% | FAIL: return and illustrative turnover |
| Inverse volatility | 3.10% | 1.33% | 84.20% | FAIL: return |
| Benchmark 60% ACWI / 40% VTC | 6.90% | 11.63% | 0.00% | FAIL: reserve and illustrative turnover |
| Constrained 75% SGOV / 25% ACWI | **5.51%** | **3.81%** | **75.00%** | PASS numeric model; FAIL full clearance |

The selected portfolio meets the modeled net hurdle by only about **0.01 percentage point**. That margin does not support confidence in the return forecast. It is the lowest-volatility feasible allocation on a 5-point grid; a continuous optimizer could find different weights. Volatility is not a loss guarantee, and a first-year estimate cannot demonstrate rolling five-year CPI + 3% performance.

Lowering ACWI's mean by two percentage points reduces the unchanged portfolio's net estimate to **5.01%**. Reoptimizing selects 65% SGOV / 35% ACWI, with **5.65%** net and **5.28%** volatility. Increasing annual additional cost to 100 bps reduces the unchanged portfolio to **4.76%**; reoptimization selects the same 65/35 weights at **5.60%** net. With only the latest 36 returns, the optimizer instead selects 85% SGOV / 15% ACWI at **5.90%** net and **1.76%** volatility. A minimum 80% SGOV reserve makes the return hurdle infeasible on this grid. The original weights therefore do not survive all stresses; a feasible replacement is not evidence that the original recommendation was robust.

## Monitoring and reversal

At quarterly payout reviews, check reserve dollars against the next twelve months of scholarships; net estimates against the hurdle; price completeness and release timing; estimated volatility and stress sensitivity; actual liquidity and cumulative annual turnover. Rebalance annually or with a documented committee exception. Stop using a candidate when its modeled rules fail or timing evidence becomes unreliable. No live allocation is permitted while risk policy, real holdings, fund permissions, liquidity, or raw-vintage evidence remain unresolved.

Evidence: [executed output](../outputs/results.md), [data card](data-card.md), [validation and AI use](validation-and-ai-use.md), and the [original Lab 13 mandate](prior-evidence/lab13_portfolio_mandate.md). Student sign-off and the independent Lab 20 exercise remain pending.
