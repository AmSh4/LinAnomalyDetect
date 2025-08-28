import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(df):
    # Select numerical features
    features = ['cpu_percent', 'mem_used', 'mem_free', 'disk_used', 'disk_free', 'net_sent', 'net_recv']
    data = df[features].values
    # Handle NaNs
    data = np.nan_to_num(data)
    # Normalize
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data)
    return data_scaled