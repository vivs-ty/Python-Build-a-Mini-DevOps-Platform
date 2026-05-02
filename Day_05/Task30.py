# Task 30: Build a simple phonebook with add, search, and delete operations.

phonebook = {}
def add_contact(name, number):
    phonebook[name] = number
    print(f"Contact {name} added with number {number}.")

def search_contact(name):
    if name in phonebook:
        print(f"Contact {name} found with number {phonebook[name]}.")
    else:
        print(f"Contact {name} not found.")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")
while True:
    action = input("Choose an action: add, search, delete, or exit: ").lower()
    if action == "add":
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        add_contact(name, number)
    elif action == "search":
        name = input("Enter contact name to search: ")
        search_contact(name)
    elif action == "delete":
        name = input("Enter contact name to delete: ")
        delete_contact(name)
    elif action == "exit":
        print("Exiting phonebook. Goodbye!")
        break
    else:
        print("Invalid action. Please choose add, search, delete, or exit.")
print(f" \n Python 30 days Series - Day 5 Task 30 \n")
print(f" \n Day 5: Lists, Sets, and Dictionaries \n")
print(f" \n Have a good one! \n")
