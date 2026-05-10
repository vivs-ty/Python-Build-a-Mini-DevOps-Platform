# Task 94: Alert the user when CPU usage exceeds a threshold.
import psutil

def check_cpu_usage(threshold=80):
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > threshold:
        print(f"Alert: CPU usage is at {cpu_percent:.2f}%")

# Example usage:
# check_cpu_usage(80)
