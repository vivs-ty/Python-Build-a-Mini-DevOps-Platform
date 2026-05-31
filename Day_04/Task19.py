# Task 19: Reverse a string without using built-in reverse helpers.

input_string = input("Enter a string to reverse: ").strip()

# Using a list and join is much more memory-efficient than string concatenation
chars = []
for char in input_string:
    chars.insert(0, char) # Or append and then reverse the list
reversed_string = "".join(chars)

# Note: The absolute most "Pythonic" way is slicing: reversed_string = input_string[::-1]
print(f"Reversed string: {reversed_string}")

print(" \n Python 30 days Series - Day 4 Task 19 \n"                                             ) 
print(" \n Day 4: Strings \n"                      )
print(" \n Have a good one! \n "                          + "-"*40)