# Task 26: Find the second largest number in a list without sorting.

import heapq

def get_second_largest(numbers):
    # Edge case handling: Need at least 2 unique numbers
    unique_nums = set(numbers)
    if len(unique_nums) < 2:
        return None
        
    # heapq.nlargest is highly optimized in C for finding top K elements
    return heapq.nlargest(2, unique_nums)[-1]

# Using a list comprehension for input parsing is clean
input_list = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
second_largest = get_second_largest(input_list)

print(f"Second largest number: {second_largest}")
print(f" \n Python 30 days Series - Day 5 Task 26 \n")
print(f" \n Day 5: Lists, Sets, and Dictionaries \n")
print(f" \n Have a good one! \n")
