# Task 40: Build a menu-driven utility with actions like add user, delete user, and list users.

class UserManager:
    def __init__(self):
        self.users = set() 

    def add(self):
        if user := input("Enter user name: ").strip(): 
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
    match input(menu).strip(): # Structural Pattern Matching
        case "1": manager.add()
        case "2": manager.delete()
        case "3": manager.list_all()
        case "4": 
            print("Exiting...")
            break
        case _: 
            print("Invalid choice.")
print(f" \n Python 30 days Series - Day 6 Task 40 \n")
print(f" \n Day 6: Functions and Error Handling \n")
print(f" \n Have a good one! \n")
