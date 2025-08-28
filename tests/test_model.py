import unittest
import numpy as np
from src.model import Autoencoder, train_autoencoder, save_model, load_model
import torch
import os

class TestModel(unittest.TestCase):
    def setUp(self):
        self.config = {
            'input_dim': 7,
            'hidden_dim': 16,
            'epochs': 1,
            'batch_size': 2,
            'learning_rate': 0.001
        }
        self.data = np.random.rand(4, 7)

    def test_train_autoencoder(self):
        model = train_autoencoder(self.data, self.config)
        self.assertIsInstance(model, Autoencoder)

    def test_save_load_model(self):
        model = Autoencoder(self.config['input_dim'], self.config['hidden_dim'])
        save_model(model, 'test_model.pth')
        loaded_model = load_model('test_model.pth', self.config['input_dim'], self.config['hidden_dim'])
        self.assertIsInstance(loaded_model, Autoencoder)
        os.remove('test_model.pth')

if __name__ == '__main__':
    unittest.main()