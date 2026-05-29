# Task 195: Read secrets from environment variables instead of hardcoding them.

import os

def connect_to_database():
    # Read from environment variables
    # os.getenv safely returns None if the variable doesn't exist
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    if not db_user or not db_password:
        print("Error: Database credentials are missing in environment variables.")
        print("Please set DB_USER and DB_PASSWORD before running the application.")
        return

    print(f"Successfully retrieved credentials for user: {db_user}")
    print("Connecting to database using secured password... (Success)")

if __name__ == "__main__":
    # Simulating the environment variables being set by your Operating System
    # In reality, you would set these in your terminal or a .env file
    os.environ["DB_USER"] = "admin_user"
    os.environ["DB_PASSWORD"] = "secure_db_pass_999"

    connect_to_database()

    print("\nPython 30 days Series - Day 29 : Task 195")
    print("Day 29 : Security and Secrets Management")
    print("Have a good one!\n" + "-"*40)
    