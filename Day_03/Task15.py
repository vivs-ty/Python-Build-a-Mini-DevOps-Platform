# Task 15: Calculate the factorial of a number using a loop.

n = int(input("Enter a number to calculate factorial: ").strip())
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial_value = 1
    for i in range(2, n + 1):
        factorial_value *= i
    print(f"Factorial of {n} is: {factorial_value}")

print(f" \n Python 30 days Series - Day 3 Task 15 \n")
print(f" \n Have a good one! \n")
