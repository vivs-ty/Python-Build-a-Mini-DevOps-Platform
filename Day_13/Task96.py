# Task 96: Monitor a process and restart it if it stops. 
import psutil
import time

def monitor_process(process_name, restart_command):
    while True:
        try:
            # Find the process by name
            process = None
            for p in psutil.process_iter(['pid', 'name']):
                if p.info['name'] == process_name:
                    process = p
                    break

            if not process or not process.is_running():
                print(f"Process '{process_name}' is not running. Restarting...")
                # Restart the process (replace with actual restart command)
                # os.system(restart_command)
                time.sleep(5)  # Wait before checking again
            else:
                time.sleep(1)  # Check every second
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(5)  # Wait before checking again
            