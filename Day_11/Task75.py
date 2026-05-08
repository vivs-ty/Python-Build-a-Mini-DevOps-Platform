# Task 75: Extract timestamps in YYYY-MM-DD HH:MM:SS format from a log file.

import re
from pathlib import Path

def extract_timestamps(file_path: str) -> list[str]:
    path = Path(file_path)
    if not path.exists(): return []

    # \d{4} matches exactly 4 digits. \b ensures we don't grab partial strings.
    timestamp_pattern = re.compile(r'\b\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\b')
    timestamps = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            timestamps.extend(timestamp_pattern.findall(line))
            
    return timestamps

print(" Extracted Timestamps:")
for ts in extract_timestamps("server_logs.txt"):
    print(f" - {ts}")

print(f" \n Python 30 days Series - Day 11 Task 75 \n")
print(f" \n Day 11: Regular Expressions \n")
print(f" \n Have a good one! \n " + "-"*40)
