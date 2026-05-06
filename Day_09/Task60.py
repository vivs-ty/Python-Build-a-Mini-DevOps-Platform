# Task 60: Read a CSV file and calculate summary statistics.

import csv
import statistics
from pathlib import Path

def calculate_csv_stats(csv_path: str, column_name: str) -> None:
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            # Extract the column and convert to floats, ignoring empty rows
            values = [float(row[column_name]) for row in reader if row.get(column_name)]
            
        if not values:
            print(f" No numeric data found in column '{column_name}'.")
            return

        print(f" Statistics for '{column_name}':")
        print(f"  - Count:  {len(values)}")
        print(f"  - Mean:   {statistics.mean(values):.2f}")
        print(f"  - Median: {statistics.median(values):.2f}")
        print(f"  - Max:    {max(values)}")
        print(f"  - Min:    {min(values)}")
            
    except KeyError:
        print(f" Error: Column '{column_name}' not found in CSV.")
    except Exception as e:
        print(f" Error reading file: {e}")

# --- Demonstration ---
Path("data.csv").write_text("user,score\nAlice,85\nBob,92\nCharlie,78\nDiana,95", encoding="utf-8")
calculate_csv_stats("data.csv", "score")

