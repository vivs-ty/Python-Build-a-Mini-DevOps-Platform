# Task 194: Store passwords securely with hashing.
#
# Required dependencies: pip install bcrypt

import bcrypt

def hash_password(plain_text_password, rounds=12):
    """Hash a password using bcrypt with configurable rounds.
    
    Args:
        plain_text_password: The password to hash
        rounds: Number of rounds for bcrypt (default: 12, recommended: 12-14)
    """
    # bcrypt automatically generates a secure random salt and hashes the password
    salt = bcrypt.gensalt(rounds=rounds)
    hashed = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
    return hashed

def check_password(plain_text_password, hashed_password):
    """Check if the provided password matches the securely stored hash.
    
    Args:
        plain_text_password: The password to check
        hashed_password: The stored hash to compare against
        
    Returns:
        True if password matches, False otherwise
    """
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)

if __name__ == "__main__":
    password = "super_secret_password_123"

    print("Hashing password with bcrypt (rounds=12)...")
    hashed_pw = hash_password(password)
    print(f"Hashed Password (Store this in the database): {hashed_pw}")

    print("\nVerifying correct password login attempt...")
    is_correct = check_password("super_secret_password_123", hashed_pw)
    print(f"Login successful: {is_correct}")

    print("\nVerifying wrong password login attempt...")
    is_wrong = check_password("wrong_password", hashed_pw)
    print(f"Login successful: {is_wrong}")

    print(" \n Python 30 days Series - Day 29 : Task 194 \n")
    print(" \n Day 29: Security and Secrets Management \n")
    print(" \n Have a good one! " + "-"*40)
    