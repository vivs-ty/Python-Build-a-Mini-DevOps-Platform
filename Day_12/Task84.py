# Task 84: List files larger than a specified size in a directory.


import argparse
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser(description="Find large files in a directory.")
    
    parser.add_argument("directory", type=str, help="Directory to scan")
    parser.add_argument(
        "-s", "--size", 
        type=int, 
        required=True, # Forces the user to provide this flag
        help="Minimum file size in Megabytes (MB)"
    )

    args = parser.parse_args()
    target_dir = Path(args.directory)
    min_bytes = args.size * 1024 * 1024

    if not target_dir.is_dir():
        print(f"❌ '{args.directory}' is not a valid directory.")
        return

    print(f"🔍 Scanning for files larger than {args.size}MB...")
    found = False
    
    for file_path in target_dir.rglob("*"):
        if file_path.is_file() and file_path.stat().st_size >= min_bytes:
            size_mb = file_path.stat().st_size / (1024 * 1024)
            print(f" - {file_path.name} ({size_mb:.2f} MB)")
            found = True
            
    if not found:
        print("No files found matching that criteria.")

if __name__ == "__main__":
    main()

print(f" \n Python 30 days Series - Day 12 Task 84 \n")
print(f" \n Day 12: CLI Tools with argparse \n")
print(f" \n Have a good one! \n " + "-"*40)
