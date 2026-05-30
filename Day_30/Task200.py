# Task 200: Create a compliance checker for rules such as no plaintext passwords and proper permissions.

import os
import re

def check_compliance(file_path):
    compliance_issues = []
    
    # Check for plaintext passwords
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if re.search(r'(password|secret|api_key|token)\s*=\s*["\'].*?["\']', line, re.IGNORECASE):
                compliance_issues.append(f"Plaintext secret found in {file_path} at line {line_number}: {line.strip()}")
    
    # Check for proper permissions (example: no world-writable files)
    if os.path.isfile(file_path) and os.stat(file_path).st_mode & 0o002:
        compliance_issues.append(f"File {file_path} is world-writable.")
    
    return compliance_issues

if __name__ == "__main__":
    directory_to_check = input("Enter the directory to check for compliance: ")
    all_issues = []
    
    for root, dirs, files in os.walk(directory_to_check):
        for filename in files:
            if filename.endswith(('.py', '.js', '.java', '.cpp')):
                file_path = os.path.join(root, filename)
                issues = check_compliance(file_path)
                all_issues.extend(issues)
    
    if all_issues:
        print("Compliance issues found:")
        for issue in all_issues:
            print(issue)
    else:
        print("No compliance issues found.")
        