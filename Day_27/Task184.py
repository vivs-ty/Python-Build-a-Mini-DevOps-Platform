# Task 184: Simulate auto-scaling based on CPU usage.

import time
import random

def simulate_auto_scaling(min_instances=1, max_instances=5, scale_up_threshold=80, scale_down_threshold=30):
    current_instances = 2
    print(f"Starting auto-scaling simulation with {current_instances} instances.")
    
    try:
        # Loop 5 times for simulation purposes. In production, use 'while True'.
        for _ in range(5):
            cpu_usage = random.randint(10, 100)
            print(f"Current CPU Usage: {cpu_usage}%")
            
            if cpu_usage > scale_up_threshold and current_instances < max_instances:
                current_instances += 1
                print(f"High CPU detected! Scaling UP. Current instances: {current_instances}")
            elif cpu_usage < scale_down_threshold and current_instances > min_instances:
                current_instances -= 1
                print(f"Low CPU detected. Scaling DOWN. Current instances: {current_instances}")
            else:
                print(f"CPU stable. No scaling required. Current instances: {current_instances}")
            
            print("-" * 40)
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\nSimulation stopped.")

if __name__ == "__main__":
    simulate_auto_scaling()
    
    print("\nPython 30 days Series - Day 27 : Task 184")
    print("Day 27 : Cloud Tagging and CI/CD Basics")
    print("Have a good one!\n" + "-"*40)
    