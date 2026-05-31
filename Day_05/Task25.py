# Task 25: Remove duplicate elements from a list.

input_list = input("Enter elements separated by spaces: ").split()
# If order MATTERS (Python 3.7+):
ordered_result = list(dict.fromkeys(input_list))
# If order DOES NOT matter (Faster and shows intent):
unordered_result = list(set(input_list))
print(f"List after removing duplicates (Ordered): {ordered_result}")
print(" \n Python 30 days Series - Day 5 Task 25 \n"                                             )
print(" \n Day 5: Lists, Sets, and Dictionaries \n"                                            )
print(" \n Have a good one! \n "                          + "-"*40)
