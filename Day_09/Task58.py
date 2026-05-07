# Task 58: Update a value in a JSON file and save it.

import json
from pathlib import Path
from typing import Any

def update_json_key(file_path: str, key: str, new_value: Any) -> None:
    path = Path(file_path)
    
    # Step 1: Read existing data
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(" File missing or invalid. Creating a new configuration.")
        data = {}

    # Step 2: Modify data
    data[key] = new_value

    # Step 3: Write back with formatting
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4) # indent=4 makes it readable!
    
    print(f" Updated '{key}' to {new_value} in {path.name}")

# --- Demonstration ---
# Uses the dummy file from Task 57
update_json_key("dummy_config.json", "port", 9000)

print(f" \n Python 30 days Series - Day 9 Task 58 \n")
print(f" \n Day 9: JSON, CSV, and Configuration \n")
print(f" \n Have a good one! \n " + "-"*40)
