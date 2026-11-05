"""Lab 18 features extended into a shared-facts investor panel."""
import json
import re
import pandas as pd
import streamlit as st
import panel as p

st.set_page_config(page_title='Legend investor panel', layout='wide')
st.title('Legend investor panel')
st.caption('Data from SEC EDGAR; built with AI help, a learning demonstration, not investment advice.')
st.caption('Buffett · Cathie Wood · Michael Burry | AI simulations, not the investors’ actual opinions.')
ticker = st.sidebar.text_input('Ticker', 'COST').strip().upper()
refresh = st.sidebar.button('Refresh SEC data')
threshold = st.sidebar.selectbox('Wood revenue CAGR threshold (%)', [10.0,5.0])
st.sidebar.caption('Custom Wood proxies: growth, R&D intensity, and increasing R&D intensity. These are our lab design choices.')
st.sidebar.caption('Try COST, AAPL (your ACWI holding), or JPM (missing-data probe). Amounts are USD millions.')
try:
    report = p.load_report(ticker, refresh=refresh,growth_threshold=threshold)
except Exception as exc:
    st.error(f'Could not load SEC data: {exc}')
    st.stop()
st.subheader(report['company'])
st.caption(f"Downloaded {report['source']['retrieved_at']}. Latest filings; not a historical-vintage test.")
st.dataframe(pd.DataFrame([{'Fiscal year end': r['fiscal_year_end'], **{p.LABELS[k]: p.display(k,r[k]['value']) for k in p.LABELS}} for r in report['rows']]), hide_index=True, width='stretch')
chart = pd.DataFrame([{'Fiscal year end': r['fiscal_year_end'], **{p.LABELS[k]: None if r[k]['value'] is None else r[k]['value']/1_000_000 for k in ('net_income','owner_earnings')}} for r in report['rows']]).set_index('Fiscal year end')
st.line_chart(chart, y_label='USD millions')
if any(r['owner_earnings']['value'] is None for r in report['rows']):
    st.info('Missing owner earnings remain missing; no zeros or estimates are substituted.')
st.subheader('Investor checks')
st.write('Revenue CAGR: **' + p.display('revenue_cagr',report['revenue_cagr']) + '**')
st.dataframe(pd.DataFrame([{'Investor': who, 'Check': name, 'Result': value} for who, checks in report['panel_checks'].items() for name,value in checks.items()]), hide_index=True, width='stretch')
st.subheader('Investment memos')
for column, who in zip(st.columns(3), report['panel_checks']):
    with column:
        st.markdown('### ' + who)
        path = p.memo_path(ticker, who,threshold)
        memo = path.read_text(encoding='utf-8-sig') if path.exists() else ''
        if not memo:
            st.info('No reviewed memo saved yet. Ask Codex to apply this investor’s skill to the printed report.')
        memo = st.text_area(f'Edit {who} memo to test a number', memo, height=280, key=f'{ticker}_{who}_{threshold if who == "Wood" else "base"}_{report["facts_signature"]}')
        verdict = re.search(r'\*\*Verdict:\s*(.*?)\*\*', memo)
        st.write('**Verdict:** ' + (verdict.group(1) if verdict else 'not provided'))
        bad = p.unsupported_numbers(memo,report)
        if bad:
            st.error(who + ' unsupported numbers: ' + '; '.join(f"{v['number']} (line {v['line']})" for v in bad))
        elif memo.strip():
            st.success(who + ': all numeric tokens match printed facts or thresholds.')
        meta = path.with_suffix('.meta.json')
        if memo and (not meta.exists() or json.loads(meta.read_text(encoding='utf-8'))['facts_signature'] != report['facts_signature']):
            st.warning('Memo provenance is missing or facts changed. Ask Codex to review it.')
        if memo:
            st.markdown(memo)
            st.download_button(f'Download {who} memo',memo,file_name=path.name)
st.caption('Number matching does not prove correct metric attribution or sound reasoning. Edits remain in this session until downloaded. Memos are saved AI judgments, not generated automatically for new tickers.')
with st.expander('XBRL tags and filing provenance'):
    st.markdown(p.report_markdown(report).split('## Tags and filing provenance',1)[1])
st.download_button('Download facts and checks',p.report_markdown(report),file_name=f'{ticker}_panel.md')
st.download_button('Download report JSON',json.dumps(report,indent=2),file_name=f'{ticker}_panel.json')
