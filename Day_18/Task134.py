# Task 134: Synchronize two directories like a small rsync tool.

import os
import shutil

def sync_directories(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
        
    for file in os.listdir(source):
        src_file = os.path.join(source, file)
        dest_file = os.path.join(destination, file)
        
        if os.path.isfile(src_file) and not os.path.exists(dest_file):
            shutil.copy2(src_file, dest_file)
            print(f"Copied {file} to destination")
        elif os.path.isfile(src_file) and os.path.exists(dest_file):
            if os.path.getmtime(src_file) > os.path.getmtime(dest_file):
                shutil.copy2(src_file, dest_file)
                print(f"Updated {file} in destination")
    print(f" \n Python 30 days Series - Day 18 Task 134 \n")
    print(f" \n Day 18 : Advanced File Automation \n")
    print(f" \n Have a good one! \n " + "-"*40)
    