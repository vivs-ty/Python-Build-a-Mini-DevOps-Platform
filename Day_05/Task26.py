# Task 26: Find the second largest number in a list without sorting.

input_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
first_largest = second_largest = float('-inf')

for num in input_list:
    if num > first_largest:
        second_largest = first_largest
        first_largest = num
    elif num > second_largest and num != first_largest:
        second_largest = num

print(f"Second largest number: {second_largest}")
print(f" \n Python 30 days Series - Day 5 Task 26 \n")
print(f" \n Day 5: Lists, Sets, and Dictionaries \n")
print(f" \n Have a good one! \n")
