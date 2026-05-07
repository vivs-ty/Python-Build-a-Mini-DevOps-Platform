# Task 47: Merge multiple text files into one file.

import shutil
from pathlib import Path

file_names = input("Enter files to merge (space-separated): ").split()
destination = input("Enter destination file: ").strip()

with open(destination, "wb") as dst: # 'wb' is write-binary (faster for raw copying)
    for name in file_names:
        if Path(name).is_file():
            with open(name, "rb") as src:
                shutil.copyfileobj(src, dst) # Highly optimized stream copying
                dst.write(b"\n") # Ensure a newline between files
        else:
            print(f" Skipped missing file: {name}")

print(f" Merged into {destination}.")
print(f" \n Python 30 days Series - Day 7 Task 47 \n")
print(f" \n Day 7: File Handling \n")
print(f" \n Have a good one! \n " + "-"*40)