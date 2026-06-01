# Task 158: Aggregate logs from multiple files and generate a summary report.

import os

def aggregate_logs(log_files, keywords=None):
    if keywords is None:
        keywords = ['ERROR', 'FAILED']
    
    # Dynamically create the summary dictionary based on provided keywords
    log_summary = {keyword: 0 for keyword in keywords}
    
    for log_file in log_files:
        if not os.path.exists(log_file):
            continue
            
        with open(log_file, 'r') as f:
            for line in f:
                for keyword in keywords:
                    if keyword in line:
                        log_summary[keyword] += 1
                    
    return log_summary

if __name__ == "__main__":
    log_files = ['app1.log', 'app2.log', 'app3.log']
    
    summary = aggregate_logs(log_files)
    
    print("Log Summary Report:")
    for key, count in summary.items():
        print(f"{key}: {count}")
        
    print(" \n Python 30 days Series - Day 22 : Task 158 \n")
    print(" \n Day 22: Logs, Reports, and Container Basics \n")
    print(" \n Have a good one! " + "-"*40)
    