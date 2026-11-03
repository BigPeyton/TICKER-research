"""Run: python -m streamlit run lab18/buffett_app.py"""
import importlib.util
import json
from pathlib import Path
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
ENGINE = ROOT / "buffett-investing/scripts/buffett.py"
spec = importlib.util.spec_from_file_location("buffett_engine", ENGINE)
engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)

st.set_page_config(page_title="Buffett business screen", layout="wide")
st.title("Buffett business screen")
st.caption("Data from SEC EDGAR; built with AI help, a learning demonstration, not investment advice.")
ticker = st.sidebar.text_input("Ticker", "COST").strip().upper()
refresh = st.sidebar.button("Refresh SEC data")
st.sidebar.caption("Amounts are USD millions. ROE uses year-end equity. Latest filings; not a historical-vintage test.")
try:
    report = engine.load_report(ticker, ROOT, refresh)
except Exception as exc:
    st.error(f"Could not load SEC data: {exc}")
    st.stop()

st.subheader(report["company"])
st.caption(f"Downloaded {report['source']['retrieved_at']}")
table = [{"Fiscal year end": r["fiscal_year_end"], **{engine.LABELS[k]: engine.display(k, r[k]["value"]) for k in engine.LABELS}} for r in report["rows"]]
st.dataframe(pd.DataFrame(table), hide_index=True, width="stretch")
chart = pd.DataFrame([{"Fiscal year end": r["fiscal_year_end"],
                       **{engine.LABELS[k]: None if r[k]["value"] is None else r[k]["value"] / 1_000_000 for k in ("owner_earnings", "net_income")}}
                      for r in report["rows"]]).set_index("Fiscal year end")
st.line_chart(chart, y_label="USD millions")
if any(r["owner_earnings"]["value"] is None for r in report["rows"]):
    st.info("Owner earnings are missing for one or more years; missing observations are not replaced with zero.")
for name, outcome in report["checks"].items():
    st.write(f"**{name}: {outcome}**")
with st.expander("XBRL tags and filing provenance"):
    st.markdown(engine.report_markdown(report).split("## Tags and filing provenance", 1)[1])

st.subheader("Buffett-inspired memo")
memo_path = ROOT / f"{ticker}_memo.md"
memo = memo_path.read_text(encoding="utf-8-sig") if memo_path.exists() else ""
if not memo:
    st.info("No AI memo saved for this ticker yet. Ask Codex to use the Buffett investing skill, then paste the memo here or reload after it is saved.")
memo = st.text_area("Edit the memo to test a number", memo, height=260, key=f"memo_{ticker}")
bad = engine.unsupported_numbers(memo, report)
if bad:
    st.error("Unsupported numbers: " + "; ".join(f"{item['number']} (line {item['line']})" for item in bad))
elif memo.strip():
    st.success("Every numeric token matches a printed table value, fiscal year, or the ROE threshold.")
st.caption("This checks numeric membership, not whether a supported number belongs to the claimed metric. Review units and reasoning too. Edits stay in this session until downloaded.")
signature_path = ROOT / f"{ticker}_memo.meta.json"
if signature_path.exists() and json.loads(signature_path.read_text(encoding="utf-8-sig"))["facts_signature"] != report["facts_signature"]:
    st.warning("SEC facts changed since this memo was written. Ask Codex to review and regenerate it.")
if memo:
    st.markdown(memo)
    st.download_button("Download edited memo", memo, file_name=f"{ticker}_memo.md")
st.download_button("Download facts and checks", engine.report_markdown(report), file_name=f"{ticker}_report.md")

