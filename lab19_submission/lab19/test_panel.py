import copy
import json
import unittest
from unittest.mock import patch
from streamlit.testing.v1 import AppTest
import panel as p

def report(ticker, growth_threshold=10.0):
    facts = json.loads((p.ROOT/f'data/{ticker}_facts.json').read_text(encoding='utf-8-sig'))
    meta = json.loads((p.ROOT/f'data/{ticker}_facts.meta.json').read_text(encoding='utf-8-sig'))
    return p.build_report(facts,ticker,meta,growth_threshold)

class PanelTests(unittest.TestCase):
    def test_cost_known_answers(self):
        r=report('COST')
        self.assertEqual([p.display('current_ratio',v['current_ratio']['value']) for v in r['rows']],['1.02','1.07','0.97','1.03','1.06'])
        self.assertEqual([p.display('liabilities_equity',v['liabilities_equity']['value']) for v in r['rows']],['2.11','1.75','1.96','1.64','1.49'])
        self.assertEqual(list(r['checks'].values()),['pass']*3)
        self.assertEqual(list(p.burry_checks(r['rows']).values()),['pass']*2)

    def test_apple_actual_failure_year(self):
        r=report('AAPL')
        self.assertEqual(list(r['checks'].values()),['pass']*3)
        self.assertEqual(list(p.burry_checks(r['rows']).values()),['fail']*2)
        self.assertEqual([v['fiscal_year_end'] for v in r['rows'] if v['operating_cash_flow']['value'] < v['net_income']['value']],['2025-09-27'])

    def test_missing_and_zero_denominators(self):
        r=report('JPM')
        self.assertTrue(all(v['owner_earnings']['value'] is None and v['current_ratio']['value'] is None for v in r['rows']))
        for d in [None,0,-1]:
            self.assertIsNone(p.ratio(100,d))
        rows=copy.deepcopy(report('COST')['rows'])
        rows[0]['operating_cash_flow']['value']=None
        self.assertEqual(list(p.burry_checks(rows).values())[0],'not known')
        self.assertEqual(list(p.burry_checks(rows[:4]).values())[0],'not known')

    def test_all_saved_memos(self):
        for ticker in ('COST','AAPL','JPM'):
            r=report(ticker)
            for who,threshold in [('Buffett',10),('Burry',10),('Wood',10),('Wood',5)]:
                memo=p.memo_path(ticker,who,threshold).read_text(encoding='utf-8-sig')
                self.assertEqual(p.unsupported_numbers(memo,r),[],(ticker,who))
                self.assertTrue(p.unsupported_numbers(memo+'\nROE is 40.0%.',r))

    def test_app_and_each_memo_checker(self):
        with patch.object(p,'load_report',side_effect=lambda ticker,**kw: report(ticker,kw.get('growth_threshold',10))):
            app=AppTest.from_file(str(p.ROOT/'panel_app.py')).run(timeout=30)
            self.assertEqual(len(app.exception),0)
            self.assertEqual(len(app.text_area),3)
            self.assertEqual(len(app.success),3)
            self.assertEqual(len(app.warning),0)
            app.sidebar.selectbox[0].set_value(5.0).run()
            self.assertIn('relaxed',app.text_area[1].value)
            self.assertEqual(app.dataframe[1].value.iloc[3]['Result'],'pass')
            app.sidebar.selectbox[0].set_value(10.0).run()
            self.assertEqual(app.dataframe[1].value.iloc[3]['Result'],'fail')
            for i in range(3):
                original=app.text_area[i].value
                app.text_area[i].set_value(original+'\nROE is 40.0%.').run()
                self.assertTrue(any('40.0%' in x.value for x in app.error))
                app.text_area[i].set_value(original).run()
            app.sidebar.text_input[0].set_value('AAPL').run()
            self.assertEqual(len(app.exception),0)
            app.sidebar.text_input[0].set_value('JPM').run()
            self.assertIn('not found',app.dataframe[0].value.to_string())

    def test_wood_probes_and_gaps(self):
        cost=report('COST')
        self.assertAlmostEqual(cost['revenue_cagr'],7.50,places=2)
        self.assertEqual(list(p.wood_checks(cost['rows']).values()),['fail','not known','not known'])
        self.assertEqual(list(p.wood_checks(cost['rows'],5).values()),['pass','not known','not known'])
        apple=report('AAPL')
        self.assertEqual(list(p.wood_checks(apple['rows']).values()),['fail','pass','pass'])
        self.assertEqual(list(p.wood_checks(apple['rows'],5).values()),['fail','pass','pass'])
        self.assertEqual(p.display('research_intensity',apple['rows'][-1]['research_intensity']['value']),'9.56%')
        rows=copy.deepcopy(apple['rows'])
        rows[2]['research_intensity']['value']=None
        self.assertEqual(list(p.wood_checks(rows).values())[-1],'not known')
        rows[0]['revenue']['value']=0
        self.assertIsNone(p.revenue_cagr(rows))

    def test_research_extraction_excludes_quarters(self):
        facts={'facts':{'us-gaap':{'ResearchAndDevelopmentExpense':{'units':{'USD':[
            {'form':'10-K','start':'2025-01-01','end':'2025-12-31','filed':'2026-01-01','val':10},
            {'form':'10-K','start':'2025-01-01','end':'2025-12-31','filed':'2026-02-01','val':12},
            {'form':'10-K','start':'2025-10-01','end':'2025-12-31','filed':'2026-03-01','val':999}
        ]}}}}}
        self.assertEqual(p.research_fact(facts,'2025-12-31')['value'],12)
        self.assertIsNone(p.research_fact(facts,'2024-12-31')['value'])

if __name__=='__main__':
    unittest.main(verbosity=2)
