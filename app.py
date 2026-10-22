"""Lab 15: a Streamlit interface to portfolio.py."""
import hashlib
import importlib
import io
import streamlit as st
import portfolio

# Reload the engine on every rerun so the lab correlation probe is visible.
engine = importlib.reload(portfolio)
st.set_page_config(page_title="Portfolio Stability", layout="wide")
st.title("Portfolio Stability")
st.caption("Built with AI help, a learning demonstration, not investment advice.")
st.sidebar.header("Mandate")
objective = st.sidebar.number_input("Expected return objective (%)", value=6.5, step=0.1) / 100
minimum = st.sidebar.number_input("Reserve minimum (%)", min_value=0.0, max_value=100.0,
                                 value=3.0, step=1.0) / 100
upload = st.sidebar.file_uploader("Upload prices.csv", type="csv")
recent = st.sidebar.checkbox("Use last 36 months", disabled=upload is None)
st.sidebar.caption("For the proposed scholarship mandate: objective 5.5%, reserve 3%, SGOV eligible.")
try:
    if upload is None:
        names = [row[0] for row in engine.SLEEVES]
        baseline_returns = [row[1] for row in engine.SLEEVES]
        baseline_covariance = engine.build_covariance([row[2] for row in engine.SLEEVES], engine.CORRELATIONS)
        active_returns, active_covariance = baseline_returns, baseline_covariance
        defaults = engine.RESERVE_INDICES
        token = "meridian"
        st.caption("Meridian: course training inputs; these are not market estimates.")
    else:
        raw = upload.getvalue()
        content = raw.decode("utf-8-sig")
        loaded = engine.estimate_from_csv(io.StringIO(content))
        active = engine.estimate_from_csv(io.StringIO(content), last_36=recent)
        names = loaded["names"]
        baseline_returns, baseline_covariance = loaded["returns"], loaded["covariance"]
        active_returns, active_covariance = active["returns"], active["covariance"]
        defaults = tuple(i for i, name in enumerate(names) if name.upper() == "SGOV")
        token = hashlib.sha256(raw).hexdigest()[:16]
        st.caption(f"Historical estimates: {active['months']} monthly returns, "
                   f"prices {active['start']} to {active['end']}. History is not a forecast.")
        if loaded["months"] < 59:
            st.warning("This file has less than five years of monthly price observations. Complete the lab data before submission.")
    st.subheader("Return estimates and reserve eligibility")
    st.caption("Returns are annual percentages. Changing the window resets the return boxes to that window's estimates.")
    edited, eligible = [], []
    for i, name in enumerate(names):
        left, right = st.columns([3, 1])
        edited.append(left.number_input(f"{name} expected return (%)", value=float(active_returns[i] * 100),
                      step=0.1, format="%.4f", key=f"return_{token}_{recent}_{i}") / 100)
        if right.checkbox(f"{name}: reserve-eligible", value=i in defaults, key=f"reserve_{token}_{i}"):
            eligible.append(i)
    baseline = engine.search_portfolio(baseline_returns, baseline_covariance, objective, minimum, eligible)
    current = engine.search_portfolio(edited, active_covariance, objective, minimum, eligible)

    def show_result(title, result):
        st.subheader(title)
        if result is None:
            st.warning("no mix meets the objective")
            return
        st.table({"Asset": names, "Weight (%)": [f"{w*100:.2f}" for w in result["weights"]]})
        st.metric("Expected return", f"{result['return']*100:.2f}%")
        st.metric("Volatility", f"{result['volatility']*100:.2f}%")
        st.metric("Reserve-eligible weight", f"{result['reserve']*100:.2f}%")

    first, second = st.columns(2)
    with first:
        show_result("As loaded (all months for CSV)", baseline)
    with second:
        show_result("Current inputs", current)
    if baseline is not None and current is not None:
        change = max(abs(a-b) for a,b in zip(baseline["weights"], current["weights"])) * 100
        st.metric("Largest weight change (percentage points)", f"{change:.2f}")
    else:
        st.info("Largest weight change unavailable: both runs must have a feasible mix.")
    st.caption("Both columns use the sidebar mandate and the selected reserve assets. Search uses 5-point steps; "
               "lowest risk means lowest among those grid allocations. The app checks the return and reserve rules only.")
except (ValueError, UnicodeError) as error:
    st.error(str(error))
