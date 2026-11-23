"""Optional Streamlit integration checks; run in the installed app environment."""
from pathlib import Path
import unittest
from streamlit.testing.v1 import AppTest


class AppTests(unittest.TestCase):
    def test_defaults_changed_cost_and_infeasibility(self):
        app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / 'app.py')).run(timeout=30)
        self.assertEqual(len(app.exception), 0)
        self.assertEqual(app.metric[0].value, '5.57%')
        controls = {item.label: item for item in app.number_input}
        controls['Additional annual cost (bps)'].set_value(100.0).run(timeout=30)
        self.assertEqual(len(app.exception), 0)
        self.assertEqual(app.metric[0].value, '5.65%')
        self.assertEqual(app.metric[1].value, '5.28%')
        controls = {item.label: item for item in app.number_input}
        controls['Minimum SGOV reserve (%)'].set_value(80.0).run(timeout=30)
        self.assertEqual(len(app.exception), 0)
        self.assertEqual(len(app.metric), 0)
        self.assertTrue(any('No allocation' in message.value for message in app.error))
        self.assertEqual(len(app.get('download_button')), 1)

    def test_risk_control_blocks_and_recovers_candidate(self):
        app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / 'app.py')).run(timeout=30)
        controls = {item.label: item for item in app.number_input}
        controls['Additional annual cost (bps)'].set_value(35.0).run(timeout=30)
        self.assertEqual(app.metric[0].value, '5.89%')
        controls = {item.label: item for item in app.number_input}
        controls['Proposed annual volatility ceiling (%)'].set_value(4.0).run(timeout=30)
        self.assertEqual(len(app.exception), 0)
        self.assertEqual(len(app.metric), 0)
        self.assertTrue(any('No allocation' in item.value for item in app.error))
        controls = {item.label: item for item in app.number_input}
        self.assertEqual(controls['Proposed annual volatility ceiling (%)'].value, 4.0)
        controls['Proposed annual volatility ceiling (%)'].set_value(6.0).run(timeout=30)
        self.assertEqual(app.metric[0].value, '5.89%')


if __name__ == '__main__':
    unittest.main()
