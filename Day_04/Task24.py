# Task 24: Build a password strength checker based on length, uppercase letters, digits, and special characters.

import string

def check_password_strength(password):
    if len(password) < 8:
        return 0 # Fail fast if it's too short
        
    # Using sets means we only need to pass over the password once conceptually
    pwd_set = set(password)
    
    strength = 1 # Already passed length check
    if any(c.isupper() for c in pwd_set): strength += 1
    if any(c.isdigit() for c in pwd_set): strength += 1
    # string.punctuation covers ALL standard special characters securely
    if any(c in string.punctuation for c in pwd_set): strength += 1
        
    return strength

input_password = input("Enter a password to check its strength: ").strip()
strength = check_password_strength(input_password)

# A tuple is slightly more memory efficient than a dictionary here
strength_levels = ("Very Weak", "Weak", "Moderate", "Strong", "Very Strong")

print(f"Password strength: {strength_levels[strength]}")
print(" \n Python 30 days Series - Day 4 Task 24 \n"                                             )
print(" \n Day 4: Strings \n"                      )
print(" \n Have a good one! \n "                          + "-"*40)