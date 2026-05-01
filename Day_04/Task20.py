# Task 20: Check whether a string is a palindrome.

val = input("Enter a string to check if it's a palindrome: ").strip()
normalized_val = val.replace(" ", "").lower()
if normalized_val == normalized_val[::-1]:
    print(f"The string '{val}' is a palindrome.")
else:
    print(f"The string '{val}' is not a palindrome.")
print(f" \n Python 30 days Series - Day 4 Task 20 \n")
print(f" \n Day 4: Strings \n")
print(f" \n Have a good one! \n")