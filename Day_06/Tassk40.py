# Task 40: Build a menu-driven utility with actions like add user, delete user, and list users.

users = []

def add_user():
    user = input("Enter user name: ")
    users.append(user)
    print(f"User added: {user}")

def delete_user():
    user = input("Enter user name to delete: ")
    if user in users:
        users.remove(user)
        print(f"User deleted: {user}")
    else:
        print("User not found.")

def list_users():
    print("Users:")
    for user in users:
        print(f" - {user}")

while True:
    print("\nMenu:")
    print("1. Add User")
    print("2. Delete User")
    print("3. List Users")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        delete_user()
    elif choice == "3":
        list_users()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
print(f" \n Python 30 days Series - Day 6 Task 40 \n")
print(f" \n Day 6: Functions and Error Handling \n")
print(f" \n Have a good one! \n")
