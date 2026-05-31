# Task 31: Convert a list of tuples into a dictionary.

input_string = input("Enter pairs like 'key,value' separated by spaces: ").split()

# Using a Dictionary Comprehension
try:
    result_dict = {k: v for k, v in (item.split(',') for item in input_string)}
    print(f"Converted dictionary: {result_dict}")
except ValueError:
    print("Invalid format. Please ensure pairs are formatted as 'key,value'.")
print(" \n Python 30 days Series - Day 5 Task 31 \n"                                             )
print(" \n Day 5: Lists, Sets, and Dictionaries \n"                                            )
print(" \n Have a good one! \n "                          + "-"*40)
