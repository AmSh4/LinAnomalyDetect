import unittest
import numpy as np
from src.model import Autoencoder
from src.detector import detect_anomalies
import torch

class TestDetector(unittest.TestCase):
    def test_detect_anomalies(self):
        input_dim = 7
        hidden_dim = 16
        model = Autoencoder(input_dim, hidden_dim)
        data = np.random.rand(5, input_dim)
        anomalies = detect_anomalies(model, data, 0.1)
        self.assertEqual(len(anomalies), 5)
        self.assertIn('anomaly', anomalies.columns)

if __name__ == '__main__':
    unittest.main()