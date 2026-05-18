#  Task 155: Continuously log CPU, memory, and disk usage every 10 seconds.

import psutil
import time
import logging

# Set up logging directly to a file
logging.basicConfig(
    filename="system_metrics.log", 
    level=logging.INFO, 
    format="%(asctime)s - %(message)s"
)

def log_system_usage():
    print("Logging system metrics to system_metrics.log. Press Ctrl+C to stop.")
    try:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent
            
            log_message = f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"
            
            logging.info(log_message)
            print(f"Logged: {log_message}")
            
            time.sleep(10)
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    log_system_usage()

print(f" \n Python 30 days Series - Day 21 : Task 155 \n")
print(f" \n Day 21 : Logging, Monitoring, and Alerts \n")
print(f" \n Have a good one! \n " + "-"*40)
