import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from run_monthly_trend_review import previous_calendar_month  # noqa: E402


class MonthlyTrendReviewTests(unittest.TestCase):
    def test_previous_calendar_month(self):
        first, last = previous_calendar_month(date(2026, 9, 20))
        self.assertEqual(date(2026, 8, 1), first)
        self.assertEqual(date(2026, 8, 31), last)

        jan_first, jan_last = previous_calendar_month(date(2026, 1, 15))
        self.assertEqual(date(2025, 12, 1), jan_first)
        self.assertEqual(date(2025, 12, 31), jan_last)


if __name__ == "__main__":
    unittest.main()
