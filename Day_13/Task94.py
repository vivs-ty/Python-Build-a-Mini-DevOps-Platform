# Task 94: Alert the user when CPU usage exceeds a threshold.

import psutil
import logging

# Configure basic logging for alerts
logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s")

def check_cpu_usage(threshold: float = 80.0) -> None:
    print(f"📊 Checking CPU usage (Threshold: {threshold}%)...")
    
    # interval=1 ensures we get the average usage over 1 second, not just an instant snapshot
    cpu_percent = psutil.cpu_percent(interval=1)
    
    if cpu_percent > threshold:
        alert_msg = f"HIGH CPU: Usage is at {cpu_percent}%!"
        logging.warning(alert_msg)
        print(f"🚨 ALERT: {alert_msg}")
    else:
        print(f"✅ CPU is healthy at {cpu_percent}%.")

# --- Demonstration ---
# I am passing a low threshold (5.0%) just so you can see the alert trigger when you test it!
check_cpu_usage(threshold=5.0) 

print("\nPython 30 days Series - Day 13 Task 94\nHave a good one!\n" + "-"*40)