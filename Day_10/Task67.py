# Task 67: List all files and directories in the current working directory.

# Task 67: Master Version
from pathlib import Path

def list_directory_contents(target_dir: str = ".") -> None:
    path = Path(target_dir)
    
    if not path.is_dir():
        print(f" Error: {target_dir} is not a valid directory.")
        return

    print(f" Contents of '{path.resolve()}':")
    
    # iterdir() is more modern and efficient than os.listdir()
    directories = []
    files = []
    
    for item in path.iterdir():
        if item.is_dir():
            directories.append(item)
        elif item.is_file():
            files.append(item)

    # Print directories first, then files
    for d in sorted(directories):
        print(f"   {d.name}/")
    for f in sorted(files):
        print(f"   {f.name}")

# --- Demonstration ---
list_directory_contents()

print(f" \n Python 30 days Series - Day 10 Task 67 \n")
print(f" \n Day 10: OS Interaction and Environment \n")
print(f" \n Have a good one! \n")
