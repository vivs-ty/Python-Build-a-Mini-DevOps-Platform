# Task 94: Alert the user when CPU usage exceeds a threshold.

import psutil
import logging

def system_health_check(cpu_threshold: float = 80.0, disk_threshold: float = 80.0) -> None:
    print("🩺 Running System Health Check...")
    
    # Check CPU
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > cpu_threshold:
        logging.warning(f"HIGH CPU: {cpu_percent}% exceeds limit of {cpu_threshold}%")
        print(f"🚨 ALERT: CPU usage critical at {cpu_percent}%!")
    else:
        print(f"✅ CPU healthy ({cpu_percent}%)")

    # Check Disk
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > disk_threshold:
        logging.warning(f"HIGH DISK: {disk_usage.percent}% exceeds limit of {disk_threshold}%")
        print(f"🚨 ALERT: Disk space critical at {disk_usage.percent}%!")
    else:
        print(f"✅ Disk healthy ({disk_usage.percent}%)")

system_health_check(cpu_threshold=50.0) # Lowered threshold to trigger test
print("\nPython 30 days Series - Day 13 Task 94 & 95\nHave a good one!\n" + "-"*40)
