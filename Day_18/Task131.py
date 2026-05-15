# Task 131: Build a file organizer that moves files by file type.

import os
import shutil

def organize_files(directory):
    for file in os.listdir(directory):
        filepath = os.path.join(directory, file)
        
        if os.path.isfile(filepath):
            extension = file.split('.')[-1]
            target_folder = os.path.join(directory, extension)
            
            if not os.path.exists(target_folder):
                os.mkdir(target_folder)
                
            shutil.move(filepath, os.path.join(target_folder, file))
            print(f"Moved {file} to {extension} folder")
    print(f" \n Python 30 days Series - Day 18 Task 131 \n")
    print(f" \n Day 18 : Advanced File Automation \n")
    print(f" \n Have a good one! \n " + "-"*40)
