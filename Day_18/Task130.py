# Task 130: Monitor a directory and log create, delete, and modify events.

import os
import time

def monitor_directory(directory):
    print(f"Monitoring {directory}...")
    seen_files = set(os.listdir(directory))
    
    while True:
        time.sleep(2)
        current_files = set(os.listdir(directory))
        
        added = current_files - seen_files
        removed = seen_files - current_files
        
        for file in added:
            print(f"Created: {file}")
        for file in removed:
            print(f"Deleted: {file}")
            
        seen_files = current_files

        print(" \n Python 30 days Series - Day 18 Task 130 \n"                                               )
        print(" \n Day 18 : Advanced File Automation \n"                                         )
        print(" \n Have a good one! \n "                          + "-"*40)
