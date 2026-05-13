# Task 117: Process multiple CSV files in parallel and calculate aggregated statistics.

import concurrent.futures
import pandas as pd
def process_csv(file_path):
    df = pd.read_csv(file_path)
    return df['value'].mean(), df['value'].sum()
