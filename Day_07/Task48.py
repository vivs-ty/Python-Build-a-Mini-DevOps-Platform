# Task 48: Build a log analyzer that counts INFO, WARNING, and ERROR entries.

import re
from collections import Counter
from pathlib import Path

log_file = input("Enter the log filename: ").strip()

if Path(log_file).is_file():
    counts = Counter()
    
    # Looks for exact matches of INFO, WARNING, or ERROR
    pattern = re.compile(r'\b(INFO|WARNING|ERROR)\b')
    
    with open(log_file, "r", encoding="utf-8") as file:
        for line in file:
            match = pattern.search(line)
            if match:
                # Add the matched word to our Counter
                counts[match.group(1)] += 1
                
    print(" Log Analysis:")
    for log_level, count in counts.most_common():
        print(f"{log_level}: {count}")
else:
    print(" File not found.")

print(f" \n Python 30 days Series - Day 7 Task 48 \n")
print(f" \n Day 7: File Handling \n")
print(f" \n Have a good one! \n " + "-"*40)