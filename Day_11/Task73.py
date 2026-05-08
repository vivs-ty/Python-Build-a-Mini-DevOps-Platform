# Task 73: Extract all email addresses from a text file using regex.

import re
from pathlib import Path

def extract_emails(file_path: str) -> set[str]:
    path = Path(file_path)
    if not path.is_file():
        print(" File not found.")
        return set()

    # Pre-compile the pattern. 
    # \b ensures word boundaries. [a-zA-Z0-9._%+-]+ matches the local part.
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
    extracted_emails = set()

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            # .findall() returns a list of all non-overlapping matches in the string
            matches = email_pattern.findall(line)
            extracted_emails.update(matches)
            
    return extracted_emails

print(" Extracted Emails:")
for email in extract_emails("server_logs.txt"):
    print(f" - {email}")
    
print(f" \n Python 30 days Series - Day 11 Task 73 \n")
print(f" \n Day 11: Regular Expressions \n")
print(f" \n Have a good one! \n " + "-"*40)
