# Task 57: Read a JSON configuration file and print all key-value pairs.

import json
from pathlib import Path
from typing import Any

def read_config(file_path: str | Path) -> dict[str, Any] | None:
    path = Path(file_path)
    if not path.is_file():
        print(f" Error: Configuration file '{path}' not found.")
        return None
        
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError as e:
        print(f" Error: Invalid JSON format. {e}")
        return None

# --- Demonstration ---
dummy_config = Path("dummy_config.json")
dummy_config.write_text('{"host": "localhost", "port": 8080, "debug": true}', encoding="utf-8")

config = read_config(dummy_config)
if config:
    print(" Configuration Loaded:")
    for key, value in config.items():
        print(f"  - {key}: {value}")

print(" \n Python 30 days Series - Day 9 Task 57 \n"                                             )
print(" \n Day 9: JSON, CSV, and Configuration \n"                                           )
print(" \n Have a good one! \n "                          + "-"*40)
