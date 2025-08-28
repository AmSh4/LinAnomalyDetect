import matplotlib.pyplot as plt
import os

def plot_metrics(df, output_dir):
    plt.figure(figsize=(12, 6))
    plt.plot(df['timestamp'], df['cpu_percent'], label='CPU %')
    plt.plot(df['timestamp'], df['mem_used'] / 1e9, label='Mem Used (GB)')
    plt.legend()
    plt.title('System Metrics')
    plt.savefig(os.path.join(output_dir, 'metrics.png'))
    plt.close()

def plot_anomalies(df, anomalies, output_dir):
    plt.figure(figsize=(12, 6))
    plt.plot(df['timestamp'], df['cpu_percent'], label='CPU %')
    anomaly_times = df['timestamp'][anomalies['anomaly']]
    anomaly_values = df['cpu_percent'][anomalies['anomaly']]
    plt.scatter(anomaly_times, anomaly_values, color='red', label='Anomalies')
    plt.legend()
    plt.title('Anomalies in CPU Usage')
    plt.savefig(os.path.join(output_dir, 'anomalies.png'))
    plt.close()