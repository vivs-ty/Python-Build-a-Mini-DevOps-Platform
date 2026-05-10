#Task 89: List all running processes with their process IDs.


import psutil

def list_processes(limit: int = 15) -> None:
    print(f"{'PID':<10} | {'Process Name':<25}")
    print("-" * 40)
    
    count = 0
    # process_iter is safer when we yield only specific attributes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            print(f"{proc.info['pid']:<10} | {proc.info['name']:<25}")
            count += 1
            if count >= limit: # Limit output so we don't flood the console
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass  # Silently skip processes we don't have permission to read

list_processes()
print(f" \n Python 30 days Series - Day 13 Task 89\n")
print(f" \n Day 13 : Process and System Monitoring \n")
print(f" \n Have a good one! \n " + "-"*40)
