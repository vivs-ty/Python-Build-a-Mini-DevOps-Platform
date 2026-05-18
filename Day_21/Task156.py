#  Task 156: Trigger a console alert when CPU usage exceeds a threshold.

import psutil
import time
def monitor_cpu_usage(threshold=80):
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > threshold:
            print(f"ALERT: CPU usage is at {cpu_usage}%!")
        time.sleep(5)

if __name__ == "__main__":
    monitor_cpu_usage(threshold=80)
    