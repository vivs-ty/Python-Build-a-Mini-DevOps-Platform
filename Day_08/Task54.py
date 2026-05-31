# Task 54: Create a UserManager class with add, delete, and list operations.

class UserManager:
    def __init__(self):
        self._users: dict[str, str] = {} # Encapsulated dictionary

    def add(self, username: str, role: str = "Standard") -> None:
        if username in self._users:
            print(f" User '{username}' already exists.")
        else:
            self._users[username] = role
            print(f" User '{username}' added as {role}.")

    def delete(self, username: str) -> None:
        if self._users.pop(username, None):
            print(f" User '{username}' deleted.")
        else:
            print(f" User '{username}' not found.")

    def list_all(self) -> None:
        print(f"\n Total Users: {len(self._users)}")
        for user, role in self._users.items():
            print(f" - {user} [{role}]")

# Demonstration
manager = UserManager()
manager.add("alice", "Admin")
manager.add("bob")
manager.add("bob") # Should warn
manager.list_all()
manager.delete("bob")
print(" \n Python 30 days Series - Day 8 Task 54 \n"                                             )
print(" \n Day 8: OOPs \n"                   )
print(" \n Have a good one! \n "                          + "-"*40)
