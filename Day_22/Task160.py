# Task 160: Simulate centralized logging by collecting logs from multiple services.

import os

def collect_logs(log_files):
    collected_logs = []
    
    for log_file in log_files:
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                collected_logs.extend(f.readlines())
        else:
            print(f"Warning: {log_file} does not exist.")
            
    return collected_logs

if __name__ == "__main__":
    log_files = ['service1.log', 'service2.log', 'service3.log']
    
    all_logs = collect_logs(log_files)
    
    print("Collected Logs:")
    for log in all_logs:
        print(log.strip())
        
    print("\nPython 30 days Series - Day 22 : Task 160")
    print("Day 22 : Logs, Reports, and Container Basics")
    print("Have a good one!\n" + "-"*40)
    