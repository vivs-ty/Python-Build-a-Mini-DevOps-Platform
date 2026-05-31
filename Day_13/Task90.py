# Task 90: Find and terminate a process by name.

import psutil

def terminate_process_by_name(process_name: str) -> None:
    killed_count = 0
    
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'].lower() == process_name.lower():
                print(f" Found '{process_name}' (PID: {proc.info['pid']}). Terminating...")
                proc.terminate() # Asks the process to close nicely
                proc.wait(timeout=3) # Wait up to 3 seconds for it to close
                killed_count += 1
                
        except psutil.TimeoutExpired:
            print(f" Process {proc.info['pid']} did not terminate. Forcing kill...")
            proc.kill() # Forcefully terminates
            killed_count += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if killed_count == 0:
        print(f" No process named '{process_name}' found.")
    else:
        print(f" Successfully terminated {killed_count} instance(s) of '{process_name}'.")

# Example: terminate_process_by_name("notepad.exe")
print(" \n Python 30 days Series - Day 13 Task 90\n"                                             )
print(" \n Day 13 : Process and System Monitoring \n"                                              )
print(" \n Have a good one! \n "                          + "-"*40)
