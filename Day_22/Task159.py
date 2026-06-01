# Task 159: Monitor a log file in real-time and report specific keywords.

import os
import time

def monitor_logs(log_file, keywords):
    if not os.path.exists(log_file):
        print(f"Log file {log_file} does not exist.")
        return

    try:
        with open(log_file, 'r') as f:
            f.seek(0, os.SEEK_END)  # Move to the end of the file
            
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                    
                for keyword in keywords:
                    if keyword.lower() in line.lower():
                        print(f"[{keyword}] {line.strip()}")
                        
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
    except Exception as e:
        print(f"Error monitoring log: {e}")

if __name__ == "__main__":
    log_file = 'app.log'
    keywords = ['ERROR', 'FAILED', 'CRITICAL']
    
    print(f"Monitoring {log_file} for keywords: {keywords}. Press Ctrl+C to stop.")
    monitor_logs(log_file, keywords)
    
    print("\nPython 30 days Series - Day 22 : Task 159")
    print("Day 22 : Logs, Reports, and Container Basics")
    print("Have a good one!\n" + "-"*40)
