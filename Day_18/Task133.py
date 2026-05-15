# Task 133: Create timestamped backups of a directory.

import shutil
import time

def create_backup(directory_to_backup):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"backup_{timestamp}"
    
    shutil.make_archive(backup_name, 'zip', directory_to_backup)
    print(f"Backup created: {backup_name}.zip")
    print(f" \n Python 30 days Series - Day 18 Task 133 \n")
    print(f" \n Day 18 : Advanced File Automation \n")
    print(f" \n Have a good one! \n " + "-"*40)