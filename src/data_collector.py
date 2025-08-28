import time
import psutil
import pandas as pd
import logging

def collect_metrics(duration=60, interval=1, output_file='metrics.csv'):
    data = []
    start_time = time.time()
    while time.time() - start_time < duration:
        cpu_percent = psutil.cpu_percent()
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        net = psutil.net_io_counters()
        metrics = {
            'timestamp': time.time(),
            'cpu_percent': cpu_percent,
            'mem_total': mem.total,
            'mem_used': mem.used,
            'mem_free': mem.free,
            'disk_total': disk.total,
            'disk_used': disk.used,
            'disk_free': disk.free,
            'net_sent': net.bytes_sent,
            'net_recv': net.bytes_recv,
        }
        data.append(metrics)
        time.sleep(interval)
    
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    logging.info(f"Data collected and saved to {output_file}")