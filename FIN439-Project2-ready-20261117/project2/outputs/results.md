# Executed results

Run date: 2026-11-17. Fixed input boundary: 2026-09-30.

Reconstruction using later-downloaded prices; NOT a point-in-time return backtest.

**PILOT ON PAPER; 0% live allocation**

Annual target 5.50% net; SGOV reserve minimum 3%; additional annual cost 25 bps; trading cost 10 bps × one-way turnover. Turnover is measured from the illustrative Lab 15 proposal (75% SGOV / 25% ACWI), not actual holdings.

| Portfolio | Weights | Net estimate | Volatility | Reserve | Turnover | Modeled rules | Full mandate |
|---|---|---:|---:|---:|---:|---|---|
| Equal weight | SGOV 25.0%; SCHR 25.0%; VTC 25.0%; ACWI 25.0% | 3.53% | 6.55% | 25.00% | 50.00% | FAIL | FAIL: unresolved |
| Inverse volatility | SGOV 84.2%; SCHR 7.8%; VTC 5.2%; ACWI 2.8% | 3.10% | 1.33% | 84.20% | 22.18% | FAIL | FAIL: unresolved |
| 60% ACWI / 40% VTC benchmark | SGOV 0.0%; SCHR 0.0%; VTC 40.0%; ACWI 60.0% | 6.90% | 11.63% | 0.00% | 75.00% | FAIL | FAIL: unresolved |
| Constrained portfolio | SGOV 75.0%; SCHR 0.0%; VTC 0.0%; ACWI 25.0% | 5.51% | 3.81% | 75.00% | 0.00% | PASS | FAIL: unresolved |

Full-mandate FAIL means compliance has not been established; it is not a prediction of a future loss.

- Equal weight: FAIL — Estimated annual net return meets objective; Illustrative one-way rebalance turnover within limit
- Inverse volatility: FAIL — Estimated annual net return meets objective
- 60% ACWI / 40% VTC benchmark: FAIL — SGOV reserve meets minimum; Illustrative one-way rebalance turnover within limit
- Constrained portfolio: passes the modeled numeric rules; unresolved rules still block live use.

## Stress runs

Fixed weights show whether the original candidate survives; reoptimized results show a different possible allocation. These are engineering tests, not the student's locked changed-input record.

| Scenario | Fixed net | Fixed rules | Reoptimized weights | Reoptimized net | Reoptimized risk |
|---|---:|---|---|---:|---:|
| Base | 5.51% | PASS | SGOV 75.0%; SCHR 0.0%; VTC 0.0%; ACWI 25.0% | 5.51% | 3.81% |
| ACWI estimate -2 percentage points | 5.01% | FAIL | SGOV 65.0%; SCHR 0.0%; VTC 0.0%; ACWI 35.0% | 5.65% | 5.28% |
| Last 36 monthly returns | 7.60% | PASS | SGOV 85.0%; SCHR 0.0%; VTC 0.0%; ACWI 15.0% | 5.90% | 1.76% |
| Annual additional cost 100 bps | 4.76% | FAIL | SGOV 65.0%; SCHR 0.0%; VTC 0.0%; ACWI 35.0% | 5.60% | 5.28% |
| Reserve minimum 80% | 5.51% | FAIL | No feasible grid allocation | N/A | N/A |
| Combined: equity -2 pp; cost 100 bps; reserve 80% | 4.26% | FAIL | No feasible grid allocation | N/A | N/A |

## Unresolved mandate and evidence

- Committee loss tolerance, risk limit and breach response are not approved.
- Five-day redemption capacity and reserve eligibility need operational verification.
- Diversified-fund concentration exemption and fund mandates need confirmation.
- Actual holdings, cumulative annual turnover and rebalance authorization are unknown.
- Historical signal uses a prior student-checked summary; raw vintage is not bundled.
- Annual arithmetic estimates do not demonstrate rolling five-year CPI + 3% net returns.

Signal: August 2026 FEDFUNDS 3.63%, recorded as available in the September 30 vintage by the student's prior Lab 17 check. Raw historical CSV retrieval failed on November 17; no fresh source validation is claimed. The SGOV annual estimate is capped at this policy-rate proxy. This is a modeling heuristic, not a Treasury yield observation.

Stop the paper candidate when its estimated net return or reserve fails, turnover requires unapproved action, or source timing is unverifiable. Do not deploy live before all mandate gaps are resolved.

Exact unrounded results and input/code hashes: [results.json](results.json).
