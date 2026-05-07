# Task 70: Calculate the total size of files in a directory.

from pathlib import Path

def format_size(size_in_bytes: int) -> str:
    """Helper function to convert bytes to human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.2f} PB"

def calculate_directory_size(directory: str) -> None:
    target_dir = Path(directory)
    
    if not target_dir.is_dir():
        print(f" Error: '{directory}' is not a valid directory.")
        return

    print(f" Calculating total size of '{target_dir.resolve()}'...")
    
    # Generator expression sums the size of all files recursively
    total_bytes = sum(f.stat().st_size for f in target_dir.rglob('*') if f.is_file())
    
    print(f" Total Size: {format_size(total_bytes)}")

# --- Demonstration ---
calculate_directory_size(".") # Checks current directory

print(f" \n Python 30 days Series - Day 10 Task 70 \n")
print(f" \n Day 10: OS Interaction and Environment \n")
print(f" \n Have a good one! \n")