# Task 74: Validate an IPv4 address with regex.

import re

def is_valid_ipv4(ip: str) -> bool:
    # Strict IPv4 Validation:
    # 25[0-5]       = 250-255
    # 2[0-4][0-9]   = 200-249
    # 1[0-9][0-9]   = 100-199
    # [1-9][0-9]    = 10-99
    # [0-9]         = 0-9
    octet = r'(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])'
    
    # ^ and $ ensure the ENTIRE string matches, not just a substring
    pattern = re.compile(rf'^{octet}\.{octet}\.{octet}\.{octet}$')
    
    # fullmatch() is strictly better than match() or search() for validation
    return bool(pattern.fullmatch(ip))

# --- Demonstration ---
test_ips = ["192.168.1.1", "10.0.0.255", "256.100.50.0", "1.1.1.01"]

print(" IPv4 Validation:")
for ip in test_ips:
    status = " Valid" if is_valid_ipv4(ip) else " Invalid"
    print(f" {status}: {ip}")

print(f" \n Python 30 days Series - Day 11 Task 74 \n")
print(f" \n Day 11: Regular Expressions \n")
print(f" \n Have a good one! \n " + "-"*40)
