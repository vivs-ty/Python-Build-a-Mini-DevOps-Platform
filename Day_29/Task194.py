# Task 194: Store passwords securely with hashing.

import bcrypt
class PasswordManager:
    def hash_password(self, password):
        # Hash a password for the first time
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed

    def check_password(self, password, hashed):
        # Check if the provided password matches the hashed password
        return bcrypt.checkpw(password.encode('utf-8'), hashed)
    
# Example usage
if __name__ == "__main__":
    password_manager = PasswordManager()
    password = "MySecurePassword"
    
    hashed_password = password_manager.hash_password(password)
    print(f"Hashed Password: {hashed_password}")
    
    is_correct = password_manager.check_password(password, hashed_password)
    print(f"Password is correct: {is_correct}")
    
    is_incorrect = password_manager.check_password("WrongPassword", hashed_password)
    print(f"Password is incorrect: {is_incorrect}")
    