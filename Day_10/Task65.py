# Task 65: Print all environment variables.

import os

def print_environment_variables() -> None:
    print(" Current Environment Variables:\n" + "="*40)
    
    # Sort keys alphabetically for readability
    for key in sorted(os.environ):
        value = os.environ[key]
        # Security best practice: mask sensitive data in logs/console
        if any(secret in key.lower() for secret in ['key', 'token', 'password', 'secret']):
            value = "******** [REDACTED]"
            
        print(f"{key}: {value}")

# --- Demonstration ---
print_environment_variables()

print("Environment Variable" + "-"*40)
print(f" \n Python 30 days Series - Day 10 Task 65 \n")
print(f" \n Day 10: OS Interaction and Environment \n")
print(f" \n Have a good one! \n")