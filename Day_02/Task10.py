# Task 10: Build a basic login check with a predefined username and password.

username = input("Enter your username: ").strip()
password = input("Enter your password: ").strip()

p_un = "admin"
p_p = "password123"

if username == p_un and password == p_p:
    print("Login successful!")
else:
    print("Invalid username or password.")

print(f" \n Python 30 days Series - Day 2 Task 10 \n")
print(f" \n Have a good one! ")
