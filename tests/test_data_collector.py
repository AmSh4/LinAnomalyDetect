import unittest
from src.data_collector import collect_metrics
import os
import pandas as pd

class TestDataCollector(unittest.TestCase):
    def test_collect_metrics(self):
        output_file = 'test_metrics.csv'
        collect_metrics(duration=2, interval=1, output_file=output_file)
        self.assertTrue(os.path.exists(output_file))
        df = pd.read_csv(output_file)
        self.assertGreater(len(df), 0)
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()