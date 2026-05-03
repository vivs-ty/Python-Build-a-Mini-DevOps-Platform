# Task 35: Write a recursive factorial function with error handling for negative values.

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
try:
    print(factorial(5))  # Example usage
    print(factorial(-3))  # This will raise an error
except ValueError as e:
    print(e)
print(f" \n Python 30 days Series - Day 6 Task 35 \n")
print(f" \n Day 6: Functions and Error Handling \n")
print(f" \n Have a good one! \n")
