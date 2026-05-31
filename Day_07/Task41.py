# Task 41: Count lines, words, and characters in a text file.

from pathlib import Path

file_path = input("Enter the filename: ").strip()

if not Path(file_path).is_file():
    print(" File not found.")
else:
    line_count = word_count = char_count = 0
    
    # Explicit encoding is a best practice for text files
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file: # Lazy iteration (O(1) memory)
            line_count += 1
            word_count += len(line.split())
            char_count += len(line)

    print(f"Lines: {line_count}\nWords: {word_count}\nCharacters: {char_count}")

print(" \n Python 30 days Series - Day 7 Task 41 \n"                                             )
print(" \n Day 7: File Handling \n"                            )
print(" \n Have a good one! \n "                          + "-"*40)
