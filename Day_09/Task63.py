# Task 63: Merge multiple JSON files into one file.

import json
from pathlib import Path

def merge_json_files(output_path: str, *input_paths: str) -> None:
    merged_data = {}
    
    for file_path in input_paths:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    # Using .update() merges keys. Later files overwrite earlier ones.
                    merged_data.update(data)
                else:
                    print(f" Skipping {file_path}: Root must be a JSON Object (dict).")
        except Exception as e:
            print(f" Failed to process {file_path}: {e}")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(merged_data, f, indent=4)
    print(f" Successfully merged files into {output_path}")

# --- Demonstration ---
Path("db_config.json").write_text('{"host": "localhost", "db_port": 5432}', encoding="utf-8")
Path("api_config.json").write_text('{"api_key": "xyz123", "timeout": 60}', encoding="utf-8")

merge_json_files("merged_config.json", "db_config.json", "api_config.json")

