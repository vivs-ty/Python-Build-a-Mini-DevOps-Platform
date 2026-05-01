# Task 22: Remove duplicate characters from a string while preserving order.

input_string = input("Enter a string to remove duplicate characters: ").strip()
seen = set()
result = ""

for char in input_string:
    if char not in seen:
        seen.add(char)
        result += char

print(f"String after removing duplicates: {result}")
print(f" \n Python 30 days Series - Day 4 Task 22 \n")
print(f" \n Day 4: Strings \n")
print(f" \n Have a good one! \n")
