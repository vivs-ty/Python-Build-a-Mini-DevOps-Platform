# Task 28: Merge two lists and remove duplicate values.

list1 = input("Enter the first list of elements separated by spaces: ").split()
list2 = input("Enter the second list of elements separated by spaces: ").split()
merged_list = list1 + list2
result = list(dict.fromkeys(merged_list))
print(f"Merged list without duplicates: {result}")
print(f" \n Python 30 days Series - Day 5 Task 28 \n")
print(f" \n Day 5: Lists, Sets, and Dictionaries \n")
print(f" \n Have a good one! \n")
