# Task 194: Store passwords securely with hashing.

import bcrypt

def hash_password(plain_text_password):
    # bcrypt automatically generates a secure random salt and hashes the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
    return hashed

def check_password(plain_text_password, hashed_password):
    # Check if the provided password matches the securely stored hash
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)

if __name__ == "__main__":
    password = "super_secret_password_123"

    print("Hashing password...")
    hashed_pw = hash_password(password)
    print(f"Hashed Password (Store this in the database): {hashed_pw}")

    print("\nVerifying correct password login attempt...")
    is_correct = check_password("super_secret_password_123", hashed_pw)
    print(f"Login successful: {is_correct}")

    print("\nVerifying wrong password login attempt...")
    is_wrong = check_password("wrong_password", hashed_pw)
    print(f"Login successful: {is_wrong}")

    print("\nPython 30 days Series - Day 29 : Task 194")
    print("Day 29 : Security and Secrets Management")
    print("Have a good one!\n" + "-"*40)
    