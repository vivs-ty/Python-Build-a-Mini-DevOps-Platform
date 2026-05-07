# Task 69: Delete files older than a given number of days.

import time
from pathlib import Path

def cleanup_old_files(directory: str, days_old: int, dry_run: bool = True) -> None:
    target_dir = Path(directory)
    if not target_dir.is_dir():
        print(f" Error: Directory '{directory}' not found.")
        return

    # Calculate the cutoff timestamp (Current time - X days in seconds)
    cutoff_time = time.time() - (days_old * 86400)
    deleted_count = 0

    print(f"🧹 Scanning '{target_dir}' for files older than {days_old} days...")
    if dry_run:
        print(" DRY RUN ACTIVE - No files will actually be deleted.\n")

    for file_path in target_dir.rglob("*"): # rglob("*") searches recursively
        if file_path.is_file():
            file_mod_time = file_path.stat().st_mtime
            
            if file_mod_time < cutoff_time:
                try:
                    if not dry_run:
                        file_path.unlink() # This permanently deletes the file
                    print(f"   {'[WOULD DELETE]' if dry_run else '[DELETED]'} {file_path.name}")
                    deleted_count += 1
                except Exception as e:
                    print(f"   Failed to delete {file_path.name}: {e}")

    print(f"\n Total files {'flagged for deletion' if dry_run else 'deleted'}: {deleted_count}")

# --- Demonstration ---
# We will use dry_run=True so it doesn't accidentally delete your hard work!
cleanup_old_files(".", days_old=30, dry_run=True)

print(f" \n Python 30 days Series - Day 10 Task 69 \n")
print(f" \n Day 10: OS Interaction and Environment \n")
print(f" \n Have a good one! \n " + "-"*40)
