# Task 196: Rotate secrets periodically and update them in the system.

import os
class SecretRotator:
    def rotate_secret(self, secret_name, new_value):
        # Rotate a secret by updating the environment variable
        os.environ[secret_name] = new_value
        return os.getenv(secret_name)
    
# Example usage
if __name__ == "__main__":
    secret_rotator = SecretRotator()
    secret_name = "MY_SECRET_KEY"
    
    # Set an initial secret value
    os.environ[secret_name] = "InitialSecretValue"
    print(f"Old Secret Value: {os.getenv(secret_name)}")
    
    # Rotate the secret with a new value
    new_secret_value = "NewSecretValue"
    updated_secret_value = secret_rotator.rotate_secret(secret_name, new_secret_value)
    print(f"Updated Secret Value: {updated_secret_value}")
    
    # Clean up the environment variable    
    del os.environ[secret_name]
    