# Task 62: Validate whether a JSON file is properly formatted.

import json
from pathlib import Path

def validate_json(file_path: str) -> bool:
    path = Path(file_path)
    if not path.is_file():
        print(" File not found.")
        return False
        
    try:
        with open(path, "r", encoding="utf-8") as f:
            json.load(f)
        print(" JSON format is completely valid.")
        return True
    except json.JSONDecodeError as e:
        # Master touch: Exposing the exact location of the syntax error
        print(f" Invalid JSON syntax on Line {e.lineno}, Column {e.colno}: {e.msg}")
        return False

# --- Demonstration ---
Path("bad_syntax.json").write_text('{"name": "Alice", "role": Admin}', encoding="utf-8") # Missing quotes around Admin
validate_json("bad_syntax.json")

print(f" \n Python 30 days Series - Day 9 Task 62 \n")
print(f" \n Day 9: JSON, CSV, and Configuration \n")
print(f" \n Have a good one! \n")