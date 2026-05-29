# Task 196: Rotate secrets periodically and update them in the system.

import os
import secrets

def read_secret_from_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return f.read().strip()
    return None

def write_secret_to_file(filepath, secret):
    with open(filepath, 'w') as f:
        f.write(secret)

def rotate_secret(filepath):
    print("Starting secret rotation process...")

    current_secret = read_secret_from_file(filepath)
    if current_secret:
        # We slice the string [:5] just to safely print a preview of the secret
        print(f"Current secret found: {current_secret[:5]}... (truncated)")
    else:
        print("No existing secret found.")

    # Generate a new highly secure 32-byte hexadecimal token
    new_secret = secrets.token_hex(32)
    write_secret_to_file(filepath, new_secret)

    print(f"New secret generated and saved: {new_secret[:5]}... (truncated)")
    print("Secret rotation complete. Systems must now use the new secret.")

if __name__ == "__main__":
    config_file = "app_secret.key"

    print("--- First Run (Creating Secret) ---")
    rotate_secret(config_file)

    print("\n--- Second Run (Rotating Secret) ---")
    rotate_secret(config_file)

    print("\nPython 30 days Series - Day 29 : Task 196")
    print("Day 29 : Security and Secrets Management")
    print("Have a good one!\n" + "-"*40)
    