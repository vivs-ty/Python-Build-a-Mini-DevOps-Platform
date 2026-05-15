# Task 133: Create timestamped backups of a directory.

import shutil
import time

def create_backup(directory_to_backup):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"backup_{timestamp}"
    
    shutil.make_archive(backup_name, 'zip', directory_to_backup)
    print(f"Backup created: {backup_name}.zip")