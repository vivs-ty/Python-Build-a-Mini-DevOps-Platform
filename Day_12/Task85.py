# Task 85: Merge multiple files into a single output file through CLI arguments.

import argparse
import shutil
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser(description="Merge multiple files into one.")
    
    # nargs='+' means "one or more arguments"
    parser.add_argument("input_files", nargs='+', help="List of files to merge")
    parser.add_argument("-o", "--output", required=True, help="Output file name")

    args = parser.parse_args()
    output_path = Path(args.output)

    with open(output_path, "wb") as dst:
        for file_name in args.input_files:
            src_path = Path(file_name)
            if src_path.is_file():
                with open(src_path, "rb") as src:
                    shutil.copyfileobj(src, dst)
                    dst.write(b"\n") # Ensure a newline between files
                print(f"✅ Merged: {src_path.name}")
            else:
                print(f"⚠️ Skipped (Not Found): {file_name}")

    print(f"🎉 Merge complete. Output saved to '{output_path.name}'.")

if __name__ == "__main__":
    main()

print(" \n Python 30 days Series - Day 12 Task 85 \n"                                              )
print(" \n Day 12: CLI Tools with argparse \n"                                       )
print(" \n Have a good one! \n "                          + "-"*40)
