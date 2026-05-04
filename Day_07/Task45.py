# Task 45: Count how many times a specific word appears in a file.

import re
from pathlib import Path

file_path = input("Enter the filename: ").strip()
target_word = input("Enter the word to count: ").strip()

if Path(file_path).is_file():
    # re.escape makes sure special characters in the word don't break the regex
    pattern = re.compile(rf"\b{re.escape(target_word)}\b", re.IGNORECASE)
    
    with open(file_path, "r", encoding="utf-8") as file:
        # Count matches line-by-line to save memory
        word_count = sum(len(pattern.findall(line)) for line in file)
        
    print(f"The word '{target_word}' appears {word_count} times.")
else:
    print(" File not found.")

print(f" \n Python 30 days Series - Day 7 Task 45 \n")
print(f" \n Day 7: File Handling \n")
print(f" \n Have a good one! \n")
