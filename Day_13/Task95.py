# Task 95: Warn when disk usage exceeds 80 percent.
import psutil

def check_disk_usage(threshold=80):
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > threshold:
        print(f"Warning: Disk usage is at {disk_usage.percent:.2f}%")

# Example usage:
# check_disk_usage(80)