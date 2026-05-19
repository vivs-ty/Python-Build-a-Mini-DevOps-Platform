# Task 159: Monitor application logs and trigger alerts for keywords like ERROR or FAILED.

import time
import os

def monitor_logs(log_file, keywords):
    if not os.path.exists(log_file):
        print(f"Log file {log_file} does not exist.")
        return

    with open(log_file, 'r') as f:
        f.seek(0, os.SEEK_END)  # Move to the end of the file
        
        try:
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)  # Sleep briefly to avoid busy waiting
                    continue
                    
                for keyword in keywords:
                    if keyword in line:
                        print(f"ALERT: Found '{keyword}' in log: {line.strip()}")
        except KeyboardInterrupt:
            print("\nMonitoring stopped.")

if __name__ == "__main__":
    log_file = 'application.log'
    keywords = ['ERROR', 'FAILED']
    
    # Create the file if it doesn't exist so the script doesn't crash
    if not os.path.exists(log_file):
        open(log_file, 'w').close()
        
    print(f"Monitoring {log_file} for keywords: {keywords}. Press Ctrl+C to stop.")
    monitor_logs(log_file, keywords)
    
    print("\nPython 30 days Series - Day 22 : Task 159")
    print("Day 22 : Logs, Reports, and Container Basics")
    print("Have a good one!\n" + "-"*40)
    