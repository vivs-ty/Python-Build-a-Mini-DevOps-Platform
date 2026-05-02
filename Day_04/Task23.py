# Task 23: Count the frequency of each character in a string.

from collections import Counter

input_string = input("Enter a string to count character frequency: ").strip()

# Counter does all the looping and dictionary management in C under the hood
frequency = Counter(input_string)

print("Character frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")
print(f" \n Python 30 days Series - Day 4 Task 23 \n")
print(f" \n Day 4: Strings \n")
print(f" \n Have a good one! \n")
