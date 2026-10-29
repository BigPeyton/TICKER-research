"""FIN 439 Lab 17: compare live FRED data with an ALFRED vintage."""
from datetime import date
from io import StringIO
import re

import pandas as pd
import requests
import streamlit as st


SERIES = {
    "BAA": "Moody's Baa corporate bond yield",
    "FEDFUNDS": "Federal funds rate",
    "DGS10": "10-year Treasury yield",
    "MORTGAGE30US": "30-year mortgage rate",
}


def read_csv_response(response):
    """Parse either provider's date/value columns; dots are missing values."""
    response.raise_for_status()
    frame = pd.read_csv(StringIO(response.text), na_values=["."])
    if len(frame.columns) != 2:
        raise ValueError("Expected a date column and one series column.")
    frame.columns = ["Date", "Value"]
    frame["Date"] = pd.to_datetime(frame["Date"], errors="raise")
    frame["Value"] = pd.to_numeric(frame["Value"], errors="raise")
    return frame.dropna().set_index("Date").sort_index()["Value"]


@st.cache_data(ttl=3600, show_spinner=False)
def download_today(series_id, download_date):
    """One public FRED request per series; date also separates daily caches."""
    response = requests.get(
        "https://fred.stlouisfed.org/graph/fredgraph.csv",
        params={"id": series_id}, timeout=45,
    )
    return read_csv_response(response)


@st.cache_data(ttl=3600, show_spinner=False)
def download_asof(series_id, vintage_date, download_date):
    """Ask ALFRED for the values actually available on the chosen date."""
    response = requests.get(
        "https://alfred.stlouisfed.org/graph/alfredgraph.csv",
        params={"id": series_id, "vintage_date": vintage_date.isoformat()},
        timeout=45,
    )
    return read_csv_response(response)


def compare_series(series_id, current, historical):
    """Compare all downloaded observations, independent of the chart start."""
    last_known = historical.index.max() if not historical.empty else None
    shared = current.index.intersection(historical.index)
    revisions = int(((current.loc[shared] - historical.loc[shared]).abs() > 1e-9).sum())
    return {
        "Series": f"https://fred.stlouisfed.org/series/{series_id}",
        "Last date known then": last_known.date().isoformat() if last_known is not None else None,
        "Value known then": float(historical.iloc[-1]) if not historical.empty else None,
        "Last date today": current.index[-1].date().isoformat() if not current.empty else None,
        "Value today": float(current.iloc[-1]) if not current.empty else None,
        "Later observations": int((current.index > last_known).sum()) if last_known is not None else len(current),
        "Revised observations": revisions,
    }


def main():
    st.set_page_config(page_title="Point-in-Time Rates", layout="wide")
    today = date.today()
    st.title("Point-in-Time Rates")
    st.caption(
        f"Data from FRED and ALFRED, Federal Reserve Bank of St. Louis, downloaded {today}; "
        "built with AI help, a learning demonstration, not investment advice."
    )
    chosen = st.sidebar.multiselect(
        "Interest rate series", list(SERIES), default=list(SERIES),
        format_func=lambda key: f"{key} — {SERIES[key]}",
    )
    extra = st.sidebar.text_input("Add a FRED series ID", placeholder="e.g. PAYEMS").strip().upper()
    start = st.sidebar.date_input("Chart start date", value=date(2020, 1, 1), min_value=date(1776, 1, 1), max_value=today)
    vintage = st.sidebar.date_input("As known on", value=today, min_value=date(1776, 1, 1), max_value=today)
    if extra:
        if re.fullmatch(r"[A-Z0-9_]+", extra):
            chosen = list(dict.fromkeys(chosen + [extra]))
        else:
            st.sidebar.error("Enter a series ID using letters, numbers, or underscores.")
    rows = []
    for series_id in chosen:
        st.subheader(f"{series_id} — {SERIES.get(series_id, 'Additional series')}")
        try:
            with st.spinner(f"Loading {series_id}..."):
                current = download_today(series_id, today)
                historical = download_asof(series_id, vintage, today)
            row = compare_series(series_id, current, historical)
            rows.append(row)
            visible = current.loc[pd.Timestamp(start):]
            if visible.empty:
                st.info("No observations in the chart's date range.")
            else:
                st.line_chart(visible.rename(series_id))
            st.caption(f"Last measurement available as known on {vintage}: "
                       f"{row['Last date known then'] or 'No observations available'}. "
                       "Dates identify the period measured, not the publication date.")
        except (requests.RequestException, ValueError, pd.errors.ParserError) as exc:
            st.error(f"Could not load {series_id}: {exc}")
    st.subheader("What was known then versus today")
    st.caption("Counts use the full downloaded history. Later observations are nonmissing values "
               "after the last measurement known then. Revisions compare dates present in both downloads.")
    if rows:
        st.dataframe(pd.DataFrame(rows), hide_index=True, width="stretch", column_config={
            "Series": st.column_config.LinkColumn("Series", display_text=r"https://fred\.stlouisfed\.org/series/(.*)"),
        })
    elif not chosen:
        st.info("Select a series or enter a FRED ID to begin.")


if __name__ == "__main__":
    main()
