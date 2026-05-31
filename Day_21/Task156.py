#  Task 156: Trigger a console alert when CPU usage exceeds a threshold.

import psutil
import time

def monitor_cpu_usage(threshold=80.0):
    print(f"Monitoring CPU usage (Threshold: {threshold}%)...")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            
            if cpu_usage > threshold:
                print(f"ALERT: CPU usage is high at {cpu_usage}%!")
            else:
                print(f"CPU usage normal: {cpu_usage}%")
                
            time.sleep(5)
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    # Using a low threshold for demonstration purposes so it triggers
    monitor_cpu_usage(threshold=5.0)

print(" \n Python 30 days Series - Day 21 : Task 156 \n"                                                 )
print(" \n Day 21 : Logging, Monitoring, and Alerts \n"                                                )
print(" \n Have a good one! \n "                          + "-"*40)
