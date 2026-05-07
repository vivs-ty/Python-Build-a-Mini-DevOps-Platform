# Task 59: Convert a CSV file into JSON.

import csv
import json
from pathlib import Path

def csv_to_json(csv_path: str, json_path: str) -> None:
    # 1. Read CSV directly into dictionaries
    try:
        with open(csv_path, "r", encoding="utf-8") as csv_file:
            # DictReader maps the header row to dictionary keys
            reader = csv.DictReader(csv_file)
            data = list(reader)
            
        # 2. Write dictionaries out as JSON
        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
            
        print(f" Successfully converted {csv_path} to {json_path}")
    except Exception as e:
        print(f" Conversion failed: {e}")

# --- Demonstration ---
Path("sample.csv").write_text("id,name,role\n1,Alice,Admin\n2,Bob,User", encoding="utf-8")
csv_to_json("sample.csv", "sample_output.json")

print(f" \n Python 30 days Series - Day 9 Task 59 \n")
print(f" \n Day 9: JSON, CSV, and Configuration \n")
print(f" \n Have a good one! \n " + "-"*40)