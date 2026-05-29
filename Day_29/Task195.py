# Task 195: Read secrets from environment variables instead of hardcoding them.

import os
class SecretReader:
    def get_secret(self, secret_name):
        # Read a secret from environment variables
        return os.getenv(secret_name)
    
# Example usage
if __name__ == "__main__":
    secret_reader = SecretReader()
    secret_name = "MY_SECRET_KEY"
    
    # Set an environment variable for demonstration purposes
    os.environ[secret_name] = "ThisIsASecretValue"
    
    secret_value = secret_reader.get_secret(secret_name)
    print(f"Secret Value: {secret_value}")
    # Clean up the environment variable    
    del os.environ[secret_name]
    