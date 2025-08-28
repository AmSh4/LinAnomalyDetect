import unittest
import numpy as np
import pandas as pd
from src.preprocessor import preprocess_data

class TestPreprocessor(unittest.TestCase):
    def test_preprocess_data(self):
        df = pd.DataFrame({
            'cpu_percent': [50, 60],
            'mem_used': [1000, 2000],
            'mem_free': [3000, 4000],
            'disk_used': [5000, 6000],
            'disk_free': [7000, 8000],
            'net_sent': [9000, 10000],
            'net_recv': [11000, 12000],
        })
        data = preprocess_data(df)
        self.assertEqual(data.shape, (2, 7))
        self.assertTrue(np.all(data >= 0) and np.all(data <= 1))

if __name__ == '__main__':
    unittest.main()