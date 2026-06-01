# Task 184: Simulate auto-scaling based on CPU usage.

import time
import random

def simulate_auto_scaling(min_instances=1, max_instances=5, scale_up_threshold=80, scale_down_threshold=30, iterations=5):
    """Simulate auto-scaling based on CPU usage.
    
    Args:
        min_instances: Minimum number of instances to maintain
        max_instances: Maximum number of instances to scale to
        scale_up_threshold: CPU percentage above which to scale up (default: 80%)
        scale_down_threshold: CPU percentage below which to scale down (default: 30%)
        iterations: Number of iterations for simulation (set to None for infinite loop)
    """
    current_instances = max(min_instances, 2)  # Start with at least min_instances
    print(f"Starting auto-scaling simulation with {current_instances} instances.")
    print(f"Config: min={min_instances}, max={max_instances}, scale_up_at={scale_up_threshold}%, scale_down_at={scale_down_threshold}%\n")
    
    try:
        iteration_count = 0
        while True:
            if iterations and iteration_count >= iterations:
                print(f"\nSimulation completed after {iterations} iterations.")
                break
                
            iteration_count += 1
            cpu_usage = random.randint(10, 100)
            print(f"Iteration {iteration_count}: CPU Usage: {cpu_usage}%")
            
            if cpu_usage > scale_up_threshold and current_instances < max_instances:
                current_instances += 1
                print(f"  → High CPU detected! Scaling UP. Current instances: {current_instances}")
            elif cpu_usage < scale_down_threshold and current_instances > min_instances:
                current_instances -= 1
                print(f"  → Low CPU detected. Scaling DOWN. Current instances: {current_instances}")
            else:
                print(f"  → CPU stable. No scaling required. Current instances: {current_instances}")
            
            print("-" * 50)
            time.sleep(2)
             
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")

if __name__ == "__main__":
    simulate_auto_scaling(iterations=5)
    
    print("\nPython 30 days Series - Day 27 : Task 184")
    print("Day 27 : Cloud Tagging and CI/CD Basics")
    print("Have a good one!\n" + "-"*40)
    