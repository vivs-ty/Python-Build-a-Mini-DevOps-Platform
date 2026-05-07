# Task 38: Define a custom InvalidAgeError and raise it when age is below 18.

class InvalidAgeError(Exception):
    def __init__(self, age: int, message: str = "Age must be 18 or older."):
        self.age = age
        self.message = message
        super().__init__(self.message)

def check_age(age: int) -> bool:
    if age < 18:
        raise InvalidAgeError(age)
    return True

try:
    check_age(15)
except InvalidAgeError as e:
    print(f"Error: {e.message} (You entered: {e.age})")
print(f" \n Python 30 days Series - Day 6 Task 38 \n")
print(f" \n Day 6: Functions and Error Handling \n")
print(f" \n Have a good one! \n " + "-"*40)
