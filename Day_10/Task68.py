# Task 68: Create a directory structure such as logs, data, and backup if it does not exist.

from pathlib import Path

def setup_project_directories(base_path: str, subdirs: list[str]) -> None:
    base = Path(base_path)
    
    print(f"🏗️ Setting up workspace in '{base.resolve()}'...")
    
    for subdir in subdirs:
        dir_path = base / subdir # Pathlib allows using '/' to join paths!
        
        try:
            # exist_ok=True prevents crashes if it already exists
            # parents=True creates intermediate parent folders if needed
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"   Directory ready: {dir_path}")
        except PermissionError:
            print(f"   Permission denied: Cannot create {dir_path}")
        except Exception as e:
            print(f"   Unexpected error creating {dir_path}: {e}")

# --- Demonstration ---
folders_to_create = ["logs", "data/raw", "data/processed", "backup"]
setup_project_directories("./my_workspace", folders_to_create)

print(f" \n Python 30 days Series - Day 10 Task 68 \n")
print(f" \n Day 10: OS Interaction and Environment \n")
print(f" \n Have a good one! \n")
