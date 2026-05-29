# Task 193: Encrypt and decrypt sensitive data with a secure algorithm.

from cryptography.fernet import Fernet

def encrypt_data(data, key):
    cipher = Fernet(key)
    # Fernet requires data to be in bytes, so we encode the string
    return cipher.encrypt(data.encode())

def decrypt_data(encrypted_data, key):
    cipher = Fernet(key)
    # Decrypt returns bytes, so we decode back to a standard string
    return cipher.decrypt(encrypted_data).decode()

if __name__ == "__main__":
    # Generate a secure key (In a real app, you would save this key securely)
    secret_key = Fernet.generate_key()

    original_message = "My highly confidential data"
    print(f"Original text: {original_message}")

    encrypted_message = encrypt_data(original_message, secret_key)
    print(f"Encrypted data: {encrypted_message}")

    decrypted_message = decrypt_data(encrypted_message, secret_key)
    print(f"Decrypted text: {decrypted_message}")

    print("\nPython 30 days Series - Day 29 : Task 193")
    print("Day 29 : Security and Secrets Management")
    print("Have a good one!\n" + "-"*40)
    