# Task 38: Define a custom InvalidAgeError and raise it when age is below 18.

class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    return True

# Example usage
try:
    check_age(15)  # This will raise the custom exception
except InvalidAgeError as e:
    print(e)
print(f" \n Python 30 days Series - Day 6 Task 38 \n")
print(f" \n Day 6: Functions and Error Handling \n")
print(f" \n Have a good one! \n")
