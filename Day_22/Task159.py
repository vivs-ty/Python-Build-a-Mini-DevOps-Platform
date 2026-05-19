# Task 159: Monitor application logs and trigger alerts for keywords like ERROR or FAILED.
import time
def monitor_logs(log_file, keywords):
    with open(log_file, 'r') as f:
        f.seek(0, os.SEEK_END)  # Move to the end of the file
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)  # Sleep briefly to avoid busy waiting
                continue
            for keyword in keywords:
                if keyword in line:
                    print(f"ALERT: Found '{keyword}' in log: {line.strip()}")
if __name__ == "__main__":
    log_file = 'application.log'  # Example log file
    keywords = ['ERROR', 'FAILED']
    print(f"Monitoring {log_file} for keywords: {keywords}")
    monitor_logs(log_file, keywords)
print(f" \n Python 30 days Series - Day 22 : Task 159 \n")
print(f" \n Day 22 : Logs, Reports, and Container Basics \n")
print(f" \n Have a good one! \n " + "-"*40)
