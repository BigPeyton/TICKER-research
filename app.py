"""The committee-facing interface. Start with: python run.py"""
from dataclasses import replace
import json
import streamlit as st

from model import (BOUNDARY, NAMES, ROOT, Settings, percent, solve,
                   stress_suite, weight_text)

st.set_page_config(page_title="Scholarship Fund | Project 2", page_icon="🎓", layout="wide")
st.title("Scholarship fund · portfolio readiness")
st.caption("AI-assisted educational research. The student must review and own the analysis and decision. Not investment advice.")
st.write("A fictional $10 million university fund, funding $75,000 in scholarships each quarter. The mandate seeks CPI + 3% net over rolling five-year periods, with a ten-year horizon.")

with st.sidebar:
    st.header("Change an assumption")
    st.caption("Controls are scenarios, not approvals to change the client's mandate.")
    objective = st.number_input("Annual net objective (%)", min_value=0.0, max_value=100.0, value=5.5, step=0.25)
    reserve = st.number_input("Minimum SGOV reserve (%)", min_value=0.0, max_value=100.0, value=3.0, step=1.0)
    annual_cost = st.number_input("Additional annual cost (bps)", min_value=0.0, max_value=2000.0, value=25.0, step=5.0)
    trading_cost = st.number_input("Trading cost per turnover (bps)", min_value=0.0, max_value=2000.0, value=10.0, step=5.0)
    turnover_limit = st.number_input("Illustrative turnover limit (%)", min_value=0.0, max_value=100.0, value=25.0, step=5.0)
    equity_change = st.number_input("ACWI annual estimate adjustment (pp)", min_value=-100.0, max_value=100.0, value=0.0, step=0.25)
    recent = st.checkbox("Use last 36 monthly returns", value=False)
    st.caption("bps = basis points: 25 bps is 0.25%. pp = percentage points. Restore the displayed defaults to reproduce the saved output.")

settings = Settings(objective=objective / 100, reserve_minimum=reserve / 100,
                    annual_cost_bps=annual_cost, trading_cost_bps=trading_cost,
                    turnover_limit=turnover_limit / 100, last_36=recent,
                    equity_change_pp=equity_change)
try:
    result = solve(settings)
except (ValueError, OSError, KeyError) as error:
    st.error(f"Cannot calculate: {error}")
    st.stop()

selected = result["selected"]
st.subheader(result["decision"])
st.warning("Full mandate: FAIL — live use is not cleared. The loss limit is unresolved, operational checks remain, and the historical rate is supported by a prior lab summary rather than a bundled raw vintage.")
if selected:
    metrics = st.columns(4)
    metrics[0].metric("Estimated annual net return", percent(selected["net_return"]))
    metrics[1].metric("Annualized volatility", percent(selected["volatility"]))
    metrics[2].metric("SGOV reserve", percent(selected["reserve"]))
    metrics[3].metric("Illustrative turnover", percent(selected["turnover"]))
    st.write("**Paper candidate:** " + weight_text(selected))
    st.write(f"**Modeled numeric rules: {selected['modeled_verdict']}.** The candidate has the lowest estimated volatility among feasible allocations on a 5-percentage-point grid.")
else:
    st.error("No allocation on the 5-percentage-point grid meets this scenario's modeled return, reserve and turnover rules. This is grid infeasibility, not proof that no continuous allocation exists.")

st.subheader("Compare allocations")
st.dataframe([{
    "Portfolio": p["name"], **{n: f"{100 * p['weights'][n]:.1f}%" for n in NAMES},
    "Net estimate": percent(p["net_return"]), "Volatility": percent(p["volatility"]),
    "Reserve": percent(p["reserve"]), "Turnover": percent(p["turnover"]),
    "Modeled rules": p["modeled_verdict"], "Full mandate": "FAIL: unresolved",
} for p in result["portfolios"]], hide_index=True, width="stretch")
for p in result["portfolios"]:
    with st.expander(f"{p['name']} — see rules and limits"):
        for rule, passed in p["modeled_rules"].items():
            st.write(f"{'PASS' if passed else 'FAIL'} · {rule}")
        st.write("**Unresolved requirements blocking a full pass:**")
        for gap in p["unresolved_rules"]:
            st.write("- " + gap)

with st.expander("Data, signal and calculation assumptions", expanded=False):
    st.write(f"Fixed boundary: {BOUNDARY}; {result['inputs']['months']} monthly returns. Adjusted-price snapshot downloaded October 22, 2026, so this reconstruction is not a historical point-in-time return backtest.")
    st.dataframe([{"Asset": name, "Annual historical mean": percent(old), "Annual estimate used": percent(new)}
                  for name, old, new in zip(NAMES, result['inputs']['historical_returns'], result['inputs']['returns'], strict=True)], hide_index=True)
    st.write("The prior Lab 17 check records August 2026 FEDFUNDS of 3.63% in the September 30 vintage. September's 3.75% was not available at that boundary. The raw vintage could not be retrieved again; this is labeled prior evidence.")
    st.write("Signal rule: cap SGOV's annual mean at 3.63%, a policy-rate proxy. FEDFUNDS is not a Treasury yield or ETF return; this conservative modeling choice has not been validated as a forecasting model.")
    st.write("Net estimate = weighted annual means − annual additional cost − trading cost × one-way turnover. Adjusted fund prices already reflect fund-level expenses; the additional cost represents hypothetical advisory/operating expense. Trading cost is charged once for the proposed rebalance, making this a first-year estimate.")
    st.write("Turnover is half the sum of absolute changes from Lab 15's proposed 75% SGOV / 25% ACWI. These are reference weights, not verified current holdings. Volatility uses sample covariance of monthly returns × 12. It is not a maximum-loss guarantee.")

with st.expander("Predefined stress runs — baseline settings", expanded=False):
    st.caption("These engineering checks always start from the documented defaults. Your current sidebar settings do not alter this table. They do not count as the student-authored locked experiment.")
    stresses = stress_suite()
    st.dataframe([{"Scenario": s["scenario"],
                   "Fixed portfolio net": percent(s['fixed_base_weights']['net_return']),
                   "Fixed rules": s['fixed_base_weights']['modeled_verdict'],
                   "Reoptimized weights": weight_text(s['reoptimized']),
                   "Reoptimized net": percent(s['reoptimized']['net_return']) if s['reoptimized'] else "Infeasible"}
                  for s in stresses], hide_index=True, width="stretch")

st.subheader("Decision and monitoring")
st.write("**Draft committee ask:** authorize a paper-only pilot and resolve the missing risk policy. Live allocation range: **0%** until every unresolved requirement is cleared. The displayed weights apply within the hypothetical paper portfolio; they are not a live allocation instruction.")
st.write(result["stop_condition"])
st.write("Monitor estimated net return against the objective; SGOV dollars against twelve months of payouts; publication dates and source integrity; volatility and stress sensitivity; actual cumulative annual turnover and liquidity. Review quarterly with scholarship payments, and rebalance only at the authorized annual review or by committee exception.")
st.download_button("Download this scenario's result (JSON)", json.dumps(result, indent=2, allow_nan=False), file_name="scenario-result.json", mime="application/json")
st.caption("Before/after experiment: download each scenario, preserve the files, and link them in the locked record after committing your own AI-off prediction. Saved defaults are also readable in outputs/results.md.")
