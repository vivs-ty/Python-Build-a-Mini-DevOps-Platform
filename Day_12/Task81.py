# Task 81: Use argparse to accept a filename and print its content.

import argparse
from pathlib import Path

def main() -> None:
    # 1. Initialize the parser
    parser = argparse.ArgumentParser(
        description="A professional CLI tool to print file contents."
    )
    
    # 2. Add arguments
    parser.add_argument("filename", type=str, help="The path to the file you want to read")

    # 3. Parse the arguments
    args = parser.parse_args()
    
    # 4. Business logic
    file_path = Path(args.filename)
    if file_path.is_file():
        print(f" Contents of {file_path.name}:\n" + "-"*30)
        print(file_path.read_text(encoding="utf-8"))
    else:
        print(f" Error: File '{file_path}' does not exist.")

if __name__ == "__main__":
    main()

print(f" \n Python 30 days Series - Day 12 Task 81 \n")
print(f" \n Day 12: CLI Tools with argparse \n")
print(f" \n Have a good one! \n " + "-"*40)
