#Task 89: List all running processes with their process IDs.
import psutil

for proc in psutil.process_iter(['pid', 'name']):
    print(f"Process: {proc.info['name']}, PID: {proc.info['pid']}")