# Task 96: Monitor a process and restart it if it stops. 

import time
import subprocess

def keep_alive(command: list[str], check_interval: int = 3) -> None:
    """
    command: The terminal command as a list (e.g., ['python', 'my_script.py'])
    """
    print(f" Starting Keep-Alive monitor for: {' '.join(command)}")
    
    try:
        # Launch the process directly so we own its PID
        process = subprocess.Popen(command)
        
        while True:
            # .poll() returns None if the process is still running
            if process.poll() is not None:
                print(" Process crashed or stopped! Restarting...")
                process = subprocess.Popen(command)
                
            time.sleep(check_interval)
            
    except KeyboardInterrupt:
        print("\n Monitor stopped by user. Terminating child process...")
        process.terminate()

# Example Usage (This will launch a simple ping command and keep it alive):
# Keep-alive is commented out to prevent infinite looping in the test run.

# keep_alive(["ping", "8.8.8.8"]) # Windows
# keep_alive(["ping", "-c", "4", "8.8.8.8"]) # Mac/Linux

print(" \n Python 30 days Series - Day 13 Task 96\n"                                             )
print(" \n Day 13 : Process and System Monitoring \n"                                              )
print(" \n Have a good one! \n "                          + "-"*40)
