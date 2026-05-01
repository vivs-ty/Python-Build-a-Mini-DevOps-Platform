# Task 10: Build a basic login check with a predefined username and password.

username = input("Enter your username: ").strip()
password = input("Enter your password: ").strip()

PREDEFINED_USERNAME = "admin"
PREDEFINED_PASSWORD = "password123"

if username == PREDEFINED_USERNAME and password == PREDEFINED_PASSWORD:
    print("Login successful!")
else:
    print("Invalid username or password.")

print("Note: Hardcoded credentials are used here for learning only.")

print(f" \n Python 30 days Series - Day 2 Task 10 \n")
print(f" \n Day 2: Conditional Logic \n")
print(f" \n Have a good one! ")
