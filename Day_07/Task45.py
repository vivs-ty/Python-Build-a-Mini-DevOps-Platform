# Task 45: Count how many times a specific word appears in a file.


import os
select_file = input("Enter the filename: ")
target_word = input("Enter the word to count: ")

with open(select_file, "r") as file:
    content = file.read()

word_count = content.count(target_word)
print(f"The word '{target_word}' appears {word_count} times in the file.")
