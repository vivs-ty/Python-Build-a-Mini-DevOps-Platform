# Task 95: Warn when disk usage exceeds 80 percent.

import psutil
import logging

# Configure basic logging for alerts
logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s")

def check_disk_usage(threshold: float = 80.0, path: str = '/') -> None:
    print(f" Checking Disk usage for '{path}' (Threshold: {threshold}%)...")
    
    try:
        disk_usage = psutil.disk_usage(path)
    except FileNotFoundError:
        print(f" Error: The path '{path}' does not exist.")
        return

    # Calculate free space in Gigabytes for better context
    free_gb = disk_usage.free / (1024 ** 3)
    
    if disk_usage.percent > threshold:
        alert_msg = f"HIGH DISK: Usage is at {disk_usage.percent}% (Only {free_gb:.1f} GB free)!"
        logging.warning(alert_msg)
        print(f" WARNING: {alert_msg}")
    else:
        print(f" Disk is healthy at {disk_usage.percent}% ({free_gb:.1f} GB free).")

# --- Demonstration ---
# Checking the root directory ('/' works on Mac/Linux. On Windows, use 'C:\\')
check_disk_usage(threshold=80.0)

print(" \n Python 30 days Series - Day 13 Task 95\n"                                             )
print(" \n Day 13 : Process and System Monitoring \n"                                              )
print(" \n Have a good one! \n "                          + "-"*40)
