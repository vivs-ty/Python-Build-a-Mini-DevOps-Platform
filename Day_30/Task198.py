# Task 198: Build a simple role-based access control system.

import json
class RBAC:
    def __init__(self):
        self.roles = {}
        self.users = {}

    def add_role(self, role_name, permissions):
        self.roles[role_name] = permissions

    def add_user(self, username, role_name):
        if role_name in self.roles:
            self.users[username] = role_name
        else:
            print(f"Role {role_name} does not exist.")

    def check_permission(self, username, permission):
        role_name = self.users.get(username)
        if role_name:
            return permission in self.roles.get(role_name, [])
        return False

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            json.dump({'roles': self.roles, 'users': self.users}, file)

    def load_from_file(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            self.roles = data.get('roles', {})
            self.users = data.get('users', {})
if __name__ == "__main__":
    rbac = RBAC()
    rbac.add_role('admin', ['read', 'write', 'delete'])
    rbac.add_role('user', ['read'])
    rbac.add_user('alice', 'admin')
    rbac.add_user('bob', 'user')

    print(rbac.check_permission('alice', 'delete'))  # True
    print(rbac.check_permission('bob', 'delete'))    # False

    rbac.save_to_file('rbac_data.json')
    new_rbac = RBAC()
    new_rbac.load_from_file('rbac_data.json')
    print(new_rbac.check_permission('alice', 'delete'))  # True
    print(new_rbac.check_permission('bob', 'delete'))    # False
    