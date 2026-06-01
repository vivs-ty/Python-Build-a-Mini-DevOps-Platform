# Task 193: Encrypt and decrypt sensitive data with a secure algorithm.
#
# Required dependencies: pip install cryptography

import os
from cryptography.fernet import Fernet, InvalidToken

def generate_and_save_key(key_file='secret.key'):
    """Generate a new encryption key and save it to a file."""
    key = Fernet.generate_key()
    with open(key_file, 'wb') as f:
        f.write(key)
    print(f"New encryption key generated and saved to '{key_file}'")
    return key

def load_key(key_file='secret.key'):
    """Load encryption key from file, or generate a new one if it doesn't exist."""
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            return f.read()
    else:
        return generate_and_save_key(key_file)

def encrypt_data(data, key):
    """Encrypt data using the provided key."""
    try:
        cipher = Fernet(key)
        # Fernet requires data to be in bytes, so we encode the string
        return cipher.encrypt(data.encode())
    except Exception as e:
        print(f"Error encrypting data: {e}")
        return None

def decrypt_data(encrypted_data, key):
    """Decrypt data using the provided key."""
    try:
        cipher = Fernet(key)
        # Decrypt returns bytes, so we decode back to a standard string
        return cipher.decrypt(encrypted_data).decode()
    except InvalidToken:
        print("Error: Invalid encryption key or corrupted data.")
        return None
    except Exception as e:
        print(f"Error decrypting data: {e}")
        return None

if __name__ == "__main__":
    # Load or generate the encryption key
    secret_key = load_key()

    original_message = "My highly confidential data"
    print(f"Original text: {original_message}")

    encrypted_message = encrypt_data(original_message, secret_key)
    if encrypted_message:
        print(f"Encrypted data: {encrypted_message}")

        decrypted_message = decrypt_data(encrypted_message, secret_key)
        if decrypted_message:
            print(f"Decrypted text: {decrypted_message}")

    print(" \n Python 30 days Series - Day 29 : Task 193 \n")
    print(" \n Day 29: Security and Secrets Management \n")
    print(" \n Have a good one! " + "-"*40)
    