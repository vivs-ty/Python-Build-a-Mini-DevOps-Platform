# Task 193: Encrypt and decrypt sensitive data with a secure algorithm.

import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
class SecretManager:
    def __init__(self, key):
        self.key = key.encode('utf-8')  # Ensure the key is bytes

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        return base64.b64encode(ct_bytes).decode('utf-8'), iv

    def decrypt(self, ciphertext, iv):
        ct_bytes = base64.b64decode(ciphertext)
        iv_bytes = base64.b64decode(iv)
        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv_bytes)
        plaintext = unpad(cipher.decrypt(ct_bytes), AES.block_size)
        return plaintext.decode('utf-8')
    
# Example usage
if __name__ == "__main__":
    secret_manager = SecretManager(key='ThisIsASecretKey')  # Key must be 16, 24, or 32 bytes long
    secret = "MySensitiveData"
    
    encrypted_secret, iv = secret_manager.encrypt(secret)
    print(f"Encrypted: {encrypted_secret}, IV: {iv}")
    
    decrypted_secret = secret_manager.decrypt(encrypted_secret, iv)
    print(f"Decrypted: {decrypted_secret}")

    print("Encryption and decryption successful:", secret == decrypted_secret)
    print("Encryption and decryption failed:", secret != decrypted_secret)
    