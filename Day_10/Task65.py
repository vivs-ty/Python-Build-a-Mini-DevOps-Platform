# Task 65: Print all environment variables.

import os

def print_environment_variables() -> None:
    print("🌐 Current Environment Variables:\n" + "="*40)
    
    # Sort keys alphabetically for readability
    for key in sorted(os.environ):
        value = os.environ[key]
        # Security best practice: mask sensitive data in logs/console
        if any(secret in key.lower() for secret in ['key', 'token', 'password', 'secret']):
            value = "******** [REDACTED]"
            
        print(f"{key}: {value}")

# --- Demonstration ---
print_environment_variables()

print("\nPython 30 days Series - Day 10 Task 65\nHave a good one!\n" + "-"*40)