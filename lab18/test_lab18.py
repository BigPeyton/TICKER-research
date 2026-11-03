"""Known-answer, extraction-edge, and Streamlit interaction tests. No live downloads needed."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("buffett", ROOT / "buffett-investing/scripts/buffett.py")
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)

def saved(ticker):
    return json.loads((ROOT / f"{ticker}_report.json").read_text(encoding="utf-8"))

class Lab18Tests(unittest.TestCase):
    def test_cost_known_answers(self):
        expected = [
            ("2022-08-28", 226954,5844,7392,3891,20642,"28.3%",3501),
            ("2023-09-03", 242290,6292,11068,4323,25058,"25.1%",6745),
            ("2024-09-01", 254453,7367,11339,4710,23622,"31.2%",6629),
            ("2025-08-31", 275235,8099,13335,5498,29164,"27.8%",7837),
            ("2026-08-30", 303154,9226,15817,6435,35803,"25.8%",9382),
        ]
        report = saved("COST")
        self.assertEqual(len(report["rows"]), 5)
        for row, answer in zip(report["rows"], expected):
            actual = [row["fiscal_year_end"]]
            for field in b.LABELS:
                actual.append(b.display(field,row[field]["value"]) if field == "roe" else row[field]["value"]/1_000_000)
            self.assertEqual(tuple(actual), answer)
        self.assertEqual(list(report["checks"].values()), ["pass"]*3)

    def test_jpm_gaps(self):
        report = saved("JPM")
        for row in report["rows"]:
            self.assertIsNone(row["capital_spending"]["value"])
            self.assertIsNone(row["owner_earnings"]["value"])
        self.assertEqual(list(report["checks"].values()), ["fail","not known","not known"])

    def test_memos_and_deliberate_error(self):
        for ticker in ("COST","JPM"):
            memo = (ROOT/f"{ticker}_memo.md").read_text(encoding="utf-8-sig")
            self.assertEqual(b.unsupported_numbers(memo, saved(ticker)), [])
        bad = b.unsupported_numbers("ROE is 40.0%.", saved("COST"))
        self.assertEqual(bad, [{"number":"40.0%","line":1}])
        self.assertTrue(b.unsupported_numbers("Owner earnings -9,382", saved("COST")))
        self.assertTrue(b.unsupported_numbers("ROE 9382%", saved("COST")))

    def test_annual_latest_and_fallback(self):
        def f(value, filed, start="2025-01-01", form="10-K"):
            return {"start": start,"end":"2025-12-31","filed":filed,"form":form,"val":value,"accn":filed}
        fixture = {"facts":{"us-gaap":{
            "Revenues":{"units":{"USD":[f(10,"2026-01-01"),f(12,"2027-01-01"),f(999,"2028-01-01","2025-10-01"),f(888,"2029-01-01",form="10-Q")]}},
            "PaymentsToAcquireProductiveAssets":{"units":{"USD":[f(4,"2026-01-01")]}},
        }}}
        self.assertEqual(b.pick_fact(fixture,"revenue","2025-12-31")["value"],12)
        self.assertEqual(b.pick_fact(fixture,"capital_spending","2025-12-31")["value"],4)
        self.assertIsNone(b.pick_fact(fixture,"equity","2025-12-31")["value"])
        # Preferred tag wins over fallback.
        fixture["facts"]["us-gaap"]["RevenueFromContractWithCustomerExcludingAssessedTax"]={"units":{"USD":[f(13,"2026-01-01")]}}
        self.assertEqual(b.pick_fact(fixture,"revenue","2025-12-31")["value"],13)
        self.assertTrue(b.annual(f(1,"2026-01-01","2024-12-27")))

    def test_nonpositive_equity_and_missing_year(self):
        company = json.loads((ROOT/"data/COST_facts.json").read_text(encoding="utf-8"))
        for equity in (0,-1):
            altered=copy.deepcopy(company)
            for fact in altered["facts"]["us-gaap"]["StockholdersEquity"]["units"]["USD"]:
                if fact.get("end")=="2026-08-30":
                    fact["val"]=equity
            self.assertIsNone(b.year_row(altered,"2026-08-30")["roe"]["value"])
        self.assertEqual(set(b.checks(saved("COST")["rows"][:4]).values()),{"not known"})
        missing=copy.deepcopy(saved("COST")["rows"])
        missing[2]["owner_earnings"]["value"]=None
        self.assertEqual(list(b.checks(missing).values())[1:],["not known","not known"])

    def test_streamlit_interactions(self):
        app=AppTest.from_file(str(ROOT/"buffett_app.py")).run(timeout=30)
        self.assertEqual(len(app.exception),0)
        self.assertEqual(len(app.error),0)
        self.assertEqual(len(app.success),1)
        memo=app.text_area[0].value
        app.text_area[0].set_value(memo+"\nROE is 40.0%.").run()
        self.assertEqual(len(app.exception),0)
        self.assertIn("40.0%",app.error[0].value)
        app.sidebar.text_input[0].set_value("JPM").run()
        self.assertEqual(len(app.exception),0)
        self.assertEqual(len(app.error),0)
        self.assertIn("not found",app.dataframe[0].value.to_string())
        app.sidebar.text_input[0].set_value("../bad").run()
        self.assertEqual(len(app.exception),0)
        self.assertIn("valid ticker",app.error[0].value)

if __name__=="__main__":
    unittest.main(verbosity=2)
