# Task 93: Log CPU, memory, and disk usage into a file periodically.


import psutil
import logging

# Configure production-ready logger
logging.basicConfig(
    filename="system_metrics.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def log_system_usage(cycles: int = 2) -> None:
    print(" Logging system metrics... Check 'system_metrics.log'")
    
    for _ in range(cycles): # Replace with 'while True' for continuous logging
        cpu = psutil.cpu_percent(interval=2)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        
        log_message = f"CPU: {cpu:>5.1f}% | Mem: {mem:>5.1f}% | Disk: {disk:>5.1f}%"
        logging.info(log_message)
        print(f"Logged: {log_message}")

log_system_usage()
print(" \n Python 30 days Series - Day 13 Task 93\n"                                             )
print(" \n Day 13 : Process and System Monitoring \n"                                              )
print(" \n Have a good one! \n "                          + "-"*40)
