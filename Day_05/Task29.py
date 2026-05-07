# Task 29: Count the frequency of each list element and store the result in a dictionary.

from collections import Counter

input_list = input("Enter elements separated by spaces: ").split()
# Counter does all the heavy lifting instantly
frequency_dict = dict(Counter(input_list))

print(f"Frequency of each element: {frequency_dict}")
print(f" \n Python 30 days Series - Day 5 Task 29 \n")
print(f" \n Day 5: Lists, Sets, and Dictionaries \n")
print(f" \n Have a good one! \n " + "-"*40)
