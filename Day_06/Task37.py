# Task 37: Divide two numbers and handle invalid input and division by zero.

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Invalid input. Please enter numbers."

print(divide(10, 2))  # Example usage
print(divide(10, 0))  # This will trigger the zero division error
print(divide(10, "a"))  # This will trigger the type error
print(f" \n Python 30 days Series - Day 6 Task 37 \n")
print(f" \n Day 6: Functions and Error Handling \n")
print(f" \n Have a good one! \n")
