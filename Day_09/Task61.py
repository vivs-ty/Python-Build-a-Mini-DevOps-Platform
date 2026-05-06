# Task 61: Build a configuration loader that reads settings from JSON.

import json
from pathlib import Path
from typing import Any

class ConfigLoader:
    def __init__(self, config_file: str):
        self.config_file = Path(config_file)
        self._config: dict[str, Any] = {}
        self._load()

    def _load(self) -> None:
        """Private method to load data internally."""
        if self.config_file.is_file():
            with open(self.config_file, "r", encoding="utf-8") as f:
                self._config = json.load(f)
            print(" Configuration loaded into memory.")
        else:
            print(" Config file missing. Using empty defaults.")

    def get(self, key: str, default: Any = None) -> Any:
        """Safely fetch a key with an optional fallback default."""
        return self._config.get(key, default)

# --- Demonstration ---
# Assumes 'dummy_config.json' from Task 57 exists
app_config = ConfigLoader("dummy_config.json")

print(f"Host: {app_config.get('host', '127.0.0.1')}") # Fetches existing key
print(f"Timeout: {app_config.get('timeout', 30)}")    # Falls back to default '30'

print(f" \n Python 30 days Series - Day 9 Task 61 \n")
print(f" \n Day 9: JSON, CSV, and Configuration \n")
print(f" \n Have a good one! \n")