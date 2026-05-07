# Task 36: Create a safe file reader that handles missing files cleanly.

from pathlib import Path

def safe_file_reader(file_name: str) -> None:
    file_path = Path(file_name)
    if not file_path.exists():
        print(f"Error: The file '{file_path.resolve()}' was not found.")
        return

    try:
        print(file_path.read_text(encoding='utf-8'))
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

safe_file_reader('non_existing_file.txt')
print(f" \n Python 30 days Series - Day 6 Task 36 \n")
print(f" \n Day 6: Functions and Error Handling \n")
print(f" \n Have a good one! \n " + "-"*40)
