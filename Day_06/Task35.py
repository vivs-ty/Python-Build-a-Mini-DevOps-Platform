# Task 35: Write a recursive factorial function with error handling for negative values.

from functools import cache

@cache # Memoization prevents redundant recursive calculations
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

try:
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Factorial of 6 (instant): {factorial(6)}") # Uses cached result of 5
    print(factorial(-3))
except ValueError as e:
    print(e)
print(" \n Python 30 days Series - Day 6 Task 35 \n"                                             )
print(" \n Day 6: Functions and Error Handling \n"                                           )
print(" \n Have a good one! \n "                          + "-"*40)
