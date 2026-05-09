# Task 86: Build a CLI with subcommands such as create-user, delete-user, and list-users.

import argparse

# --- Mock Business Logic Functions ---
def create_user(args: argparse.Namespace) -> None:
    print(f" User '{args.username}' created with role: {args.role}")

def delete_user(args: argparse.Namespace) -> None:
    print(f" User '{args.username}' has been deleted.")

def list_users(args: argparse.Namespace) -> None:
    print(" Listing all active users... (Mock Data)")

# --- CLI Setup ---
def main() -> None:
    parser = argparse.ArgumentParser(description="User Management CLI")
    subparsers = parser.add_subparsers(title="commands", dest="command", required=True)

    # Subcommand: create
    parser_create = subparsers.add_parser("create", help="Create a new user")
    parser_create.add_argument("username", help="The new user's username")
    parser_create.add_argument("--role", default="Standard", help="User role")
    parser_create.set_defaults(func=create_user) # Binds the function!

    # Subcommand: delete
    parser_delete = subparsers.add_parser("delete", help="Delete a user")
    parser_delete.add_argument("username", help="The username to delete")
    parser_delete.set_defaults(func=delete_user)

    # Subcommand: list
    parser_list = subparsers.add_parser("list", help="List all users")
    parser_list.set_defaults(func=list_users)

    # Parse and execute
    args = parser.parse_args()
    args.func(args) # Magically calls the correct function based on the subcommand

if __name__ == "__main__":
    main()

print(f" \n Python 30 days Series - Day 12 Task 86 \n")
print(f" \n Day 12: CLI Tools with argparse \n")
print(f" \n Have a good one! \n " + "-"*40)
