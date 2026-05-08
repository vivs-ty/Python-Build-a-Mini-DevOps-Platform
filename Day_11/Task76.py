# Task 76: Extract IP addresses from a log file and count their frequency.

import re
from collections import Counter
from pathlib import Path

def count_ips_in_log(file_path: str) -> None:
    path = Path(file_path)
    if not path.exists(): return

    # Using the strict octet from Task 74, but with \b boundaries instead of ^$
    octet = r'(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])'
    ip_pattern = re.compile(rf'\b{octet}\.{octet}\.{octet}\.{octet}\b')
    
    ip_counter = Counter()

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            # Find all IPs in the line and add them to the counter
            ip_counter.update(ip_pattern.findall(line))

    print(" IP Address Frequencies:")
    for ip, count in ip_counter.most_common():
        print(f" - {ip}: {count} occurrences")

count_ips_in_log("server_logs.txt")
print(f" \n Python 30 days Series - Day 11 Task 76 \n")
print(f" \n Day 11: Regular Expressions \n")
print(f" \n Have a good one! \n " + "-"*40)
