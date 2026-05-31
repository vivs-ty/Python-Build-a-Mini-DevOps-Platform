# Task 72: Build a backup tool that copies files and logs the operation.

import shutil
import logging
from datetime import datetime
from pathlib import Path

# Configure the backup logger
logging.basicConfig(
    filename='backup_operations.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def create_backup(source_dir: str, backup_base_dir: str) -> None:
    src = Path(source_dir)
    backup_base = Path(backup_base_dir)

    if not src.is_dir():
        logging.error(f"Source directory '{source_dir}' does not exist.")
        print(" Backup failed. Check logs.")
        return

    # Create a unique timestamped folder for this specific backup run
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = backup_base / f"backup_{src.name}_{timestamp}"

    try:
        logging.info(f"Starting backup: '{src}' -> '{dest}'")
        print(f" Copying files to {dest}...")
        
        # shutil.copytree copies an entire directory tree recursively
        shutil.copytree(src, dest)
        
        logging.info("Backup completed successfully.")
        print(" Backup successful!")
        
    except Exception as e:
        logging.error(f"Backup failed: {e}")
        print(" Backup encountered an error. Check logs.")

# --- Demonstration ---
# We will create a dummy source directory to back up safely
Path("my_important_data").mkdir(exist_ok=True)
Path("my_important_data/file.txt").write_text("Crucial data here.")

# Run the backup tool
create_backup("my_important_data", "backup_vault")

print(" \n Python 30 days Series - Day 10 Task 72 \n"                                              )
print(" \n Day 10: OS Interaction and Environment \n"                                              )
print(" \n Have a good one! \n "                          + "-"*40)