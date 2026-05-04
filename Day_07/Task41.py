# Task 41: Count lines, words, and characters in a text file.

select_file = input("Enter the filename: ")

with open(select_file, "r") as file:
    lines = file.readlines()

line_count = len(lines)
word_count = sum(len(line.split()) for line in lines)
char_count = sum(len(line) for line in lines)

print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Characters: {char_count}")
