# Task 33: Create reusable functions for addition, subtraction, multiplication, and division.

def add(a: float, b: float) -> float: 
    return a + b

def subtract(a: float, b: float) -> float: 
    return a - b

def multiply(a: float, b: float) -> float: 
    return a * b

def divide(a: float, b: float) -> float: 
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

print(f"Addition (10 + 5): {add(10, 5)}")
print(f"Subtraction (10 - 5): {subtract(10, 5)}")
print(f"Multiplication (10 * 5): {multiply(10, 5)}")
print(f"Division (10 / 5): {divide(10, 5)}")
print(" \n Python 30 days Series - Day 6 Task 33 \n"                                             )
print(" \n Day 6: Functions and Error Handling \n"                                           )
print(" \n Have a good one! \n "                          + "-"*40)
