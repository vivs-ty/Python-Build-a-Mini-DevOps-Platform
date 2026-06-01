# Task 195: Read secrets from environment variables instead of hardcoding them.

import os

def connect_to_database():
    """Connect to database using credentials from environment variables.
    
    Credentials should be set via:
      - System environment variables
      - .env file (using python-dotenv library)
      - Container secrets (Docker/Kubernetes)
    """
    # Read from environment variables
    # os.getenv safely returns None if the variable doesn't exist
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    if not db_user or not db_password:
        print("Error: Database credentials are missing in environment variables.")
        print("Please set DB_USER and DB_PASSWORD before running the application.")
        print("\nExample:")
        print("  export DB_USER='admin_user'")
        print("  export DB_PASSWORD='secure_db_pass_999'")
        return False

    print(f"Successfully retrieved credentials for user: {db_user}")
    print("Connecting to database using secured password... (Success)")
    return True

if __name__ == "__main__":
    # NOTE: This is ONLY for demonstration purposes in a development/test environment
    # NEVER hardcode credentials in production code
    print("NOTE: For testing purposes only. In production, set environment variables externally:")
    
    os.environ["DB_USER"] = "admin_user"
    os.environ["DB_PASSWORD"] = "secure_db_pass_999"

    connect_to_database()

    print(" \n Python 30 days Series - Day 29 : Task 195 \n")
    print(" \n Day 29: Security and Secrets Management \n")
    print(" \n Have a good one! " + "-"*40)
    