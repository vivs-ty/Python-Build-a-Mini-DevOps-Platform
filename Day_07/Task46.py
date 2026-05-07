# Task 46: Write only unique lines from a file into a new file.

from pathlib import Path

src_file = input("Enter the source file: ").strip()
dst_file = input("Enter the destination file: ").strip()

if Path(src_file).is_file():
    seen_lines = set()
    
    with open(src_file, "r", encoding="utf-8") as src, \
         open(dst_file, "w", encoding="utf-8") as dst:
        
        for line in src:
            if line not in seen_lines:
                dst.write(line)
                seen_lines.add(line)
                
    print(" Unique lines copied successfully.")
else:
    print(" Source file not found.")

print(f" \n Python 30 days Series - Day 7 Task 46 \n")
print(f" \n Day 7: File Handling \n")
print(f" \n Have a good one! \n " + "-"*40)
