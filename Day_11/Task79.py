# Task 79: Mask sensitive data such as email addresses in a file.

import re
from pathlib import Path

def mask_emails_in_file(input_file: str, output_file: str) -> None:
    in_path = Path(input_file)
    if not in_path.exists(): return

    # Group 1: The very first character of the email
    # Group 2: The '@' symbol and everything after it
    pattern = re.compile(r'\b([A-Za-z0-9])[A-Za-z0-9._%+-]*(@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7})\b')

    with open(in_path, "r", encoding="utf-8") as src, \
         open(output_file, "w", encoding="utf-8") as dst:
        
        for line in src:
            # \1 represents Group 1. \2 represents Group 2.
            masked_line = pattern.sub(r'\1***\2', line)
            dst.write(masked_line)

    print(f"✅ Masked logs saved to {output_file}")
    print("\nPreview of masked file:")
    print(Path(output_file).read_text()[:250] + "...\n") # Print a snippet

mask_emails_in_file("server_logs.txt", "masked_logs.txt")
print("Python 30 days Series - Day 11 Task 79\nHave a good one!\n" + "-"*40)
