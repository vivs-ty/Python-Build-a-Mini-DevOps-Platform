#  Task 155: Continuously log CPU, memory, and disk usage every 10 seconds.

import psutil
import time
def log_system_usage():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_info = psutil.disk_usage('/')
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_info.percent}%")
        print(f"Disk Usage: {disk_info.percent}%")
        print("-" * 30)
        time.sleep(10)
if __name__ == "__main__":
    log_system_usage()
    