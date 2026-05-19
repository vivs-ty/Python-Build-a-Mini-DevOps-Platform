# Task 158: Aggregate logs from multiple files and generate a summary report.

import os

def aggregate_logs(log_files):
    # Pre-define the keys we want to track
    log_summary = {'ERROR': 0, 'FAILED': 0}
    
    for log_file in log_files:
        if not os.path.exists(log_file):
            continue
            
        with open(log_file, 'r') as f:
            for line in f:
                if 'ERROR' in line:
                    log_summary['ERROR'] += 1
                elif 'FAILED' in line:
                    log_summary['FAILED'] += 1
                    
    return log_summary

if __name__ == "__main__":
    log_files = ['app1.log', 'app2.log', 'app3.log']
    
    summary = aggregate_logs(log_files)
    
    print("Log Summary Report:")
    for key, count in summary.items():
        print(f"{key}: {count}")
        
    print("\nPython 30 days Series - Day 22 : Task 158")
    print("Day 22 : Logs, Reports, and Container Basics")
    print("Have a good one!\n" + "-"*40)
    