# Task 135: Watch a config file and reload settings on change.

import os
import time

def watch_config(filepath):
    last_modified = os.path.getmtime(filepath)
    print(f"Watching {filepath}...")
    
    while True:
        time.sleep(2)
        current_modified = os.path.getmtime(filepath)
        
        if current_modified != last_modified:
            print("Config file changed! Reloading settings...")
            # You would put your file reading logic here
            last_modified = current_modified