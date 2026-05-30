# Task 197: Scan code files for hardcoded secrets and report them.

import os
import re

def scan_for_secrets(file_path):
    secrets_pattern = re.compile(r'(password|secret|api_key|token)\s*=\s*["\'].*?["\']', re.IGNORECASE)
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if secrets_pattern.search(line):
                print(f"Potential secret found in {file_path} at line {line_number}: {line.strip()}")

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(('.py', '.js', '.java', '.cpp')):
                file_path = os.path.join(root, filename)
                scan_for_secrets(file_path)
if __name__ == "__main__":
    directory_to_scan = input("Enter the directory to scan for hardcoded secrets: ")
    scan_directory(directory_to_scan)
    