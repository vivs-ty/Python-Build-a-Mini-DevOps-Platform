# Task 42: Read a log file and print only the lines that contain ERROR.

import re
from pathlib import Path

log_file = Path('application.log')

# Create a dummy file for testing if it doesn't exist
if not log_file.exists():
    log_file.write_text("INFO: System started\nERROR: Disk full\nWARNING: Low memory\nTERROR: Just kidding")

with open(log_file, 'r', encoding='utf-8') as file:
    for line in file:
        # \b ensures we only match the exact word "ERROR"
        if re.search(r'\bERROR\b', line): 
            print(line.strip())

print(f" \n Python 30 days Series - Day 7 Task 42 \n")
print(f" \n Day 7: File Handling \n")
print(f" \n Have a good one! \n " + "-"*40)
