# Task 64: Load the correct config file based on an environment like dev or prod.

import os
import json
from pathlib import Path

def get_env_config() -> dict:
    # Look for the 'APP_ENV' variable. If it doesn't exist, default to 'dev'.
    env = os.getenv("APP_ENV", "dev").lower()
    
    # Construct the expected filename dynamically
    config_file = Path(f"config_{env}.json")
    
    if not config_file.is_file():
        print(f" Error: {config_file} is missing for environment '{env}'.")
        return {}
        
    with open(config_file, "r", encoding="utf-8") as f:
        print(f" Operating in '{env.upper()}' environment. Loaded {config_file.name}.")
        return json.load(f)

# --- Demonstration ---
Path("config_dev.json").write_text('{"db": "local_db", "debug": true}', encoding="utf-8")
Path("config_prod.json").write_text('{"db": "cloud_db", "debug": false}', encoding="utf-8")

# Simulate different environments
os.environ["APP_ENV"] = "dev"
print(get_env_config())

os.environ["APP_ENV"] = "prod"
print(get_env_config())

print(f" \n Python 30 days Series - Day 9 Task 64 \n")
print(f" \n Day 9: JSON, CSV, and Configuration \n")
print(f" \n Have a good one! \n")