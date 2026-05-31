# Task 40: Build a menu-driven utility with actions like add user, delete user, and list users.

class UserManager:
    def __init__(self):
        self.users = set()

    def add(self):
        user = input("Enter user name: ").strip()
        if user:
            self.users.add(user)
            print(f"User added: {user}")

    def delete(self):
        user = input("Enter user name to delete: ").strip()
        try:
            self.users.remove(user)
            print(f"User deleted: {user}")
        except KeyError:
            print("User not found.")

    def list_all(self):
        print("\nUsers:")
        print("\n".join(f" - {u}" for u in self.users) if self.users else " - No users.")

manager = UserManager()
menu = "\nMenu:\n1. Add\n2. Delete\n3. List\n4. Exit\nChoice: "

while True:
    choice = input(menu).strip()
    if choice == "1":
        manager.add()
    elif choice == "2":
        manager.delete()
    elif choice == "3":
        manager.list_all()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")

print(" \n Python 30 days Series - Day 6 Task 40 \n"                                             )
print(" \n Day 6: Functions and Error Handling \n"                                           )
print(" \n Have a good one! \n "                          + "-"*40)
