# Task 197: Scan code files for hardcoded secrets and report them.

import os
import re

def scan_for_secrets(directory_path):
    # Dictionary of regex patterns for common secrets
    secret_patterns = {
        "AWS Access Key": r"AKIA[0-9A-Z]{16}",
        "Private Key": r"-----BEGIN (RSA|OPENSSH|DSA|EC|PGP) PRIVATE KEY-----",
        "Hardcoded Password": r"(?i)(password|passwd|secret|api_key)[\s:=]+['\"][^'\"]+['\"]"
    }
    
    findings = []
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Skip common non-code files
            if file.endswith((".pyc", ".png", ".jpg", ".zip")):
                continue
                
            filepath = os.path.join(root, file)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    
                for line_num, line in enumerate(lines, start=1):
                    for secret_type, pattern in secret_patterns.items():
                        if re.search(pattern, line):
                            findings.append({
                                "file": filepath,
                                "line": line_num,
                                "type": secret_type,
                                "content_preview": line.strip()[:40] + "..." 
                            })
            except Exception as e:
                # Silently skip files that cannot be read as utf-8 text
                pass
                
    return findings

if __name__ == "__main__":
    # Create a dummy file with a secret for demonstration
    dummy_file = "test_config.py"
    with open(dummy_file, "w") as f:
        f.write("import os\nAPI_KEY = 'AKIA1234567890ABCDEF'\npassword = 'super_secret'\n")

    print("Scanning directory for secrets...\n")
    results = scan_for_secrets(".")
    
    if results:
        print(f"WARNING: Found {len(results)} potential secrets:")
        for finding in results:
            print(f" - [{finding['type']}] in {finding['file']} at line {finding['line']}")
    else:
        print("Success: No hardcoded secrets found.")

    # Cleanup dummy file
    if os.path.exists(dummy_file):
        os.remove(dummy_file)

    print("\nPython 30 days Series - Day 30 : Task 197")
    print("Day 30 : Security Review and Compliance")
    print("Have a good one!\n" + "-"*40)
    