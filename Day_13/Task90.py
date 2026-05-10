# Task 90: Find and terminate a process by name.
import psutil

def terminate_process_by_name(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            print(f"Found process: {proc.info['name']}, PID: {proc.info['pid']}")
            proc.terminate()
            print(f"Terminated process: {proc.info['name']}")

# Example usage:
# terminate_process_by_name("notepad.exe")