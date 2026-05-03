# Task 36: Create a safe file reader that handles missing files cleanly.

def safe_file_reader(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
# Example usage
safe_file_reader('existing_file.txt')  # Replace with an actual file path to test
safe_file_reader('non_existing_file.txt')  # This will trigger the error handling
print(f" \n Python 30 days Series - Day 6 Task 36 \n")
print(f" \n Day 6: Functions and Error Handling \n")
print(f" \n Have a good one! \n")
