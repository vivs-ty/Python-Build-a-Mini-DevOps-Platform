# Task 43: Copy the contents of one file into another file.

import shutil
from pathlib import Path

src = input("Enter source file: ").strip()
dst = input("Enter destination file: ").strip()

if Path(src).is_file():
    # copy2 copies the file data AND the metadata (timestamps, permissions)
    shutil.copy2(src, dst)
    print(f" Successfully copied {src} to {dst}")
else:
    print(" Source file does not exist.")

print(f" \n Python 30 days Series - Day 7 Task 43 \n")
print(f" \n Day 7: File Handling \n")
print(f" \n Have a good one! \n " + "-"*40)
