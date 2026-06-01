# Task 196: Rotate secrets periodically and update them in the system.

import os
import secrets

def read_secret_from_file(filepath):
    """Safely read a secret from a file."""
    try:
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return f.read().strip()
        return None
    except IOError as e:
        print(f"Error reading secret file: {e}")
        return None

def write_secret_to_file(filepath, secret):
    """Safely write a secret to a file with restricted permissions."""
    try:
        # Create file with restricted permissions (0o600 = rw-------)
        # This ensures only the owner can read/write
        fd = os.open(filepath, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(fd, 'w') as f:
            f.write(secret)
        print(f"Secret successfully written to {filepath}")
        return True
    except IOError as e:
        print(f"Error writing secret file: {e}")
        return False

def rotate_secret(filepath='app_secret.key'):
    """Rotate and update the secret.
    
    Args:
        filepath: Path to the secret file (default: app_secret.key)
    """
    print("Starting secret rotation process...")

    current_secret = read_secret_from_file(filepath)
    if current_secret:
        # We slice the string [:5] just to safely print a preview of the secret
        print(f"Current secret found: {current_secret[:5]}... (truncated)")
    else:
        print("No existing secret found.")

    # Generate a new highly secure 32-byte hexadecimal token
    new_secret = secrets.token_hex(32)
    
    if write_secret_to_file(filepath, new_secret):
        print(f"New secret generated and saved: {new_secret[:5]}... (truncated)")
        print("Secret rotation complete. Systems must now use the new secret.")
        return True
    else:
        print("Failed to rotate secret due to file write error.")
        return False

if __name__ == "__main__":
    config_file = "app_secret.key"

    print("--- First Run (Creating Secret) ---")
    rotate_secret(config_file)

    print("\n--- Second Run (Rotating Secret) ---")
    rotate_secret(config_file)

    # Clean up for demonstration
    if os.path.exists(config_file):
        os.remove(config_file)
        print(f"\nCleanup: Removed {config_file}")

    print(" \n Python 30 days Series - Day 29 : Task 196 \n")
    print(" \n Day 29: Security and Secrets Management \n")
    print(" \n Have a good one! " + "-"*40)
    