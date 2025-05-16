import pandas as pd
import time

def stream_sensor_data(path, delay=1):
    df = pd.read_csv(path)
    for _, row in df.iterrows():
        yield row.to_dict()
        time.sleep(delay)  # Simulate delay for real-time streaming
