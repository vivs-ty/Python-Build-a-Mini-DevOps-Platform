# Task 100: Download API data and save it as JSON.

import requests
import json
from pathlib import Path

def backup_api_data(api_url: str, output_file: str) -> None:
    print(f"⬇ Downloading data from {api_url}...")
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        out_path = Path(output_file)
        
        # Save to disk with indentation so humans can read it easily
        with open(out_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            
        print(f" Success! Saved {len(data)} records to '{out_path.name}'.")
        
    except requests.exceptions.RequestException as e:
        print(f" Network Error: {e}")
    except json.JSONDecodeError:
        print(" Error: API did not return valid JSON.")

# --- Demonstration ---
backup_api_data("https://jsonplaceholder.typicode.com/posts", "posts_backup.json")

print(" \n Python 30 days Series - Day 14 Task 100\n"                                              )
print(" \n Day 14 : Networking and APIs \n"                                    )
print(" \n Have a good one! \n "                          + "-"*40)
