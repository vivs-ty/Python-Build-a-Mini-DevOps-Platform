# Task 77: Identify all URLs in a text file.

import re
from pathlib import Path

def extract_urls(file_path: str) -> set[str]:
    path = Path(file_path)
    if not path.exists(): return set()

    # https? means the 's' is optional. \S+ matches anything that isn't a space.
    # The trailing [^\s.,;!?] ensures we don't capture ending punctuation as part of the URL.
    url_pattern = re.compile(r'https?://\S+[^\s.,;!?]')
    urls = set()

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            urls.update(url_pattern.findall(line))
            
    return urls

print("🔗 Extracted URLs:")
for url in extract_urls("server_logs.txt"):
    print(f" - {url}")

print("\nPython 30 days Series - Day 11 Task 77\nHave a good one!\n" + "-"*40)
