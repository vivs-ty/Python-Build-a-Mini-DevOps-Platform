# Task 71: Monitor a directory and print a message when a new file is added.

import time
from pathlib import Path

def monitor_directory(directory: str, poll_interval: int = 2) -> None:
    target_dir = Path(directory)
    
    if not target_dir.is_dir():
        print(f"❌ Error: '{directory}' not found.")
        return

    print(f"👀 Monitoring '{target_dir.resolve()}' for new files...")
    print("Press Ctrl+C to stop.\n")

    # Capture the initial state of the directory
    previous_files = set(target_dir.iterdir())

    try:
        while True:
            time.sleep(poll_interval)
            current_files = set(target_dir.iterdir())
            
            # Set math: Find items in 'current' that are NOT in 'previous'
            new_files = current_files - previous_files
            
            for file in new_files:
                print(f"✨ NEW ITEM DETECTED: {file.name}")
                
            # Update the state for the next loop
            previous_files = current_files
            
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user.")

# --- Demonstration ---
# Uncomment the line below to run the infinite loop. 
# Open another terminal and create a file in the same directory to see it trigger!

# monitor_directory(".", poll_interval=2)

print("\nPython 30 days Series - Day 10 Task 71\nHave a good one!\n" + "-"*40)