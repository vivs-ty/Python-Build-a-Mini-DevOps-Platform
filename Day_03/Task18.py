# Task 18: Calculate the sum of all numbers between two values, inclusive.

def sum_between(a, b):
    if a > b:
        a, b = b, a  # Swap to ensure a is the smaller number
    total_sum = sum(range(a, b + 1))
    return total_sum   
print(f" \n Python 30 days Series - Day 3 Task 18 \n") 
print(f" \n Have a good one! \n")
