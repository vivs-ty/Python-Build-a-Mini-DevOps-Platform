# Task 78: Build a regex-based password validator.

import re

def validate_password(password: str) -> bool:
    """
    Validates a password based on strict security rules:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character
    """
    pattern = re.compile(
        r'^'
        r'(?=.*[A-Z])'       # Lookahead: At least one uppercase
        r'(?=.*[a-z])'       # Lookahead: At least one lowercase
        r'(?=.*\d)'          # Lookahead: At least one digit
        r'(?=.*[@$!%*?&#])'  # Lookahead: At least one special char
        r'[A-Za-z\d@$!%*?&#]{8,}' # Consume 8 or more valid characters
        r'$'
    )
    return bool(pattern.fullmatch(password))

# --- Demonstration ---
test_passwords = ["weakpass", "NoSpecial123", "Short1!", "SuperSecureP@ssw0rd!"]

print(" Password Validation:")
for pwd in test_passwords:
    status = " Strong" if validate_password(pwd) else " Weak  "
    print(f" {status}: {pwd}")

print(" \n Python 30 days Series - Day 11 Task 78 \n"                                              )
print(" \n Day 11: Regular Expressions \n"                                   )
print(" \n Have a good one! \n "                          + "-"*40)
