# Task 93: Log CPU, memory, and disk usage into a file periodically.
import psutil
import time

def log_system_usage(filename="system_usage.log", interval=60):
    with open(filename, "a") as f:
        while True:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            disk_usage = psutil.disk_usage('/')

            log_entry = (f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] "
                         f"CPU: {cpu_percent:.2f}%, "
                         f"Memory: {memory_info.percent:.2f}%, "
                         f"Disk: {disk_usage.percent:.2f}%\n")

            f.write(log_entry)
            f.flush()  # Ensure the log is written immediately

            time.sleep(interval)

# Example usage:
# log_system_usage("my_log.log", 60)