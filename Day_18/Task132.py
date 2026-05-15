# Task 132: Compress old log files and delete files older than a threshold.

import os
import time
import zipfile

def compress_old_logs(directory, days_old=7):
    cutoff_time = time.time() - (days_old * 86400)
    
    with zipfile.ZipFile('old_logs_archive.zip', 'w') as zipf:
        for file in os.listdir(directory):
            if file.endswith('.log'):
                filepath = os.path.join(directory, file)
                
                if os.path.getmtime(filepath) < cutoff_time:
                    zipf.write(filepath, file)
                    os.remove(filepath)
                    print(f"Archived and deleted: {file}")