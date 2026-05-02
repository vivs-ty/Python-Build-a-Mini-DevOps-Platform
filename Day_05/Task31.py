# Task 31: Convert a list of tuples into a dictionary.

input_list = input("Enter a list of tuples (key, value) separated by spaces: ").split()
tuple_list = [tuple(item.split(',')) for item in input_list]
result_dict = dict(tuple_list)
print(f"Converted dictionary: {result_dict}")
print(f" \n Python 30 days Series - Day 5 Task 31 \n")
print(f" \n Day 5: Lists, Sets, and Dictionaries \n")
print(f" \n Have a good one! \n")
