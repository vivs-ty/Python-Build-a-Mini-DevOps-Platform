# Task 80: Create a regex-based log filtering tool.

import re
from pathlib import Path
from typing import Iterator

class RegexLogFilter:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def filter_logs(self, regex_pattern: str) -> Iterator[str]:
        """Yields lines from the log file that match the given regex pattern."""
        if not self.file_path.exists():
            print(f"❌ File '{self.file_path}' not found.")
            return

        compiled_pattern = re.compile(regex_pattern, re.IGNORECASE)

        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                # search() looks for a match anywhere in the string
                if compiled_pattern.search(line):
                    yield line.strip()

# --- Demonstration ---
log_tool = RegexLogFilter("server_logs.txt")

print("🚨 Filtering for WARNING or ERROR logs:")
# Regex to match lines containing either ERROR or WARNING
for match in log_tool.filter_logs(r'\b(ERROR|WARNING)\b'):
    print(f" -> {match}")

print("\n🧑‍💻 Filtering for 'alice' activity:")
for match in log_tool.filter_logs(r'alice\.smith'):
    print(f" -> {match}")

print("\nPython 30 days Series - Day 11 Task 80\nHave a good one!\n" + "-"*40)
