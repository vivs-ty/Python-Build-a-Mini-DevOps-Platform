# Task 30: Build a simple phonebook with add, search, and delete operations.

class Phonebook:
    def __init__(self):
        self.contacts = {} # The dictionary is now tied to the instance

    def add(self, name, number):
        self.contacts[name] = number
        print(f" Added: {name} -> {number}")

    def search(self, name):
        # .get() avoids KeyError and returns a default string if not found
        result = self.contacts.get(name, f" {name} not found.")
        print(result)

    def delete(self, name):
        # .pop() removes the key and returns its value, or a default if missing
        result = self.contacts.pop(name, None)
        if result:
            print(f" Deleted: {name}")
        else:
            print(f" {name} not found.")

# Usage
my_phonebook = Phonebook()
# Example interaction (hardcoded to avoid an infinite while-loop blocking execution here)
my_phonebook.add("Alice", "555-0100")
my_phonebook.search("Alice")
my_phonebook.delete("Bob")
print(f" \n Python 30 days Series - Day 5 Task 30 \n")
print(f" \n Day 5: Lists, Sets, and Dictionaries \n")
print(f" \n Have a good one! \n")
