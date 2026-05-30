# Task 198: Build a simple role-based access control system.

class RBACSystem:
    def __init__(self):
        self.roles = {}  # Maps role_name to a set of permissions
        self.users = {}  # Maps username to a role_name

    def add_role(self, role_name, permissions):
        self.roles[role_name] = set(permissions)
        print(f"Role '{role_name}' created with permissions: {permissions}")

    def assign_user_role(self, username, role_name):
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        self.users[username] = role_name
        print(f"User '{username}' assigned to role '{role_name}'.")

    def has_permission(self, username, permission):
        role_name = self.users.get(username)
        if not role_name:
            return False
        return permission in self.roles.get(role_name, set())

if __name__ == "__main__":
    access_control = RBACSystem()

    # Define roles and their permissions
    access_control.add_role("Admin", ["read", "write", "delete"])
    access_control.add_role("Editor", ["read", "write"])
    access_control.add_role("Viewer", ["read"])

    # Assign users
    print("\nAssigning users...")
    access_control.assign_user_role("alice", "Admin")
    access_control.assign_user_role("bob", "Viewer")

    # Test access
    print("\nTesting Access Controls:")
    users_to_test = ["alice", "bob"]
    action = "delete"

    for user in users_to_test:
        if access_control.has_permission(user, action):
            print(f"GRANT: {user} is allowed to {action}.")
        else:
            print(f"DENY: {user} is NOT allowed to {action}.")

    print("\nPython 30 days Series - Day 30 : Task 198")
    print("Day 30 : Security Review and Compliance")
    print("Have a good one!\n" + "-"*40)
    