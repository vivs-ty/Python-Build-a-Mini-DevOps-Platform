# Task 191: Trigger pipelines automatically on version control changes.

import subprocess
import time

def get_latest_commit():
    result = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    return None

def monitor_repository(interval=5):
    last_commit = get_latest_commit()
    
    if not last_commit:
        print("Error: Not inside a Git repository. Cannot monitor.")
        return

    print(f"Monitoring repository for changes every {interval} seconds. Press Ctrl+C to stop.")
    print(f"Current commit: {last_commit}")

    try:
        # Using a limited loop for simulation. Use 'while True' for real monitoring.
        for _ in range(5):
            time.sleep(interval)
            current_commit = get_latest_commit()
            
            if current_commit and current_commit != last_commit:
                print(f"\nNew commit detected: {current_commit}")
                print("Triggering pipeline...")
                # Insert pipeline trigger logic here
                last_commit = current_commit
            else:
                print("No changes detected.")
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    monitor_repository()
    
    print("\nPython 30 days Series - Day 28 : Task 191")
    print("Day 28 : CI/CD Automation")
    print("Have a good one!\n" + "-"*40)
    