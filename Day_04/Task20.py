# Task 20: Check whether a string is a palindrome.

val = input("Enter a string to check if it's a palindrome: ").strip()

# filter() efficiently extracts only alphanumeric characters
cleaned_chars = list(filter(str.isalnum, val.lower()))
normalized_val = "".join(cleaned_chars)

# Slicing is the fastest way to compare in Python
if normalized_val == normalized_val[::-1]:
    print(f"The string '{val}' is a palindrome.")
else:
    print(f"The string '{val}' is not a palindrome.")
print(" \n Python 30 days Series - Day 4 Task 20 \n"                                             )
print(" \n Day 4: Strings \n"                      )
print(" \n Have a good one! \n "                          + "-"*40)