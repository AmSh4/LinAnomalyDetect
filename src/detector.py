import torch
import numpy as np
import pandas as pd

def detect_anomalies(model, data, threshold):
    data_tensor = torch.tensor(data, dtype=torch.float32)
    with torch.no_grad():
        reconstructed = model(data_tensor)
    errors = np.mean((data - reconstructed.numpy())**2, axis=1)
    anomalies = pd.DataFrame({'error': errors})
    anomalies['anomaly'] = anomalies['error'] > threshold
    return anomalies