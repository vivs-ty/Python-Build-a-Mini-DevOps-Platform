# Task 158: Aggregate logs from multiple files and generate a summary report.
import os
def aggregate_logs(log_files):
    log_summary = {}
    for log_file in log_files:
        with open(log_file, 'r') as f:
            for line in f:
                if 'ERROR' in line:
                    log_summary.setdefault('ERROR', 0)
                    log_summary['ERROR'] += 1
                elif 'FAILED' in line:
                    log_summary.setdefault('FAILED', 0)
                    log_summary['FAILED'] += 1
    return log_summary
if __name__ == "__main__":
    log_files = ['app1.log', 'app2.log', 'app3.log']  # Example log files
    summary = aggregate_logs(log_files)
    print("Log Summary Report:")
    for key, count in summary.items():
        print(f"{key}: {count}")
print(f" \n Python 30 days Series - Day 22 : Task 158 \n")
print(f" \n Day 22 : Logs, Reports, and Container Basics \n")
print(f" \n Have a good one! \n " + "-"*40)
