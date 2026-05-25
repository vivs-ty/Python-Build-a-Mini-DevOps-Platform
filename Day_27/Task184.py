# Task 184: Simulate auto-scaling based on CPU usage.

import random

# Simulate CPU usage for a set of instances
instances = [
    {"id": 1, "name": "Instance-1", "cpu_usage": random.uniform(0, 100)},
    {"id": 2, "name": "Instance-2", "cpu_usage": random.uniform(0, 100)},
    {"id": 3, "name": "Instance-3", "cpu_usage": random.uniform(0, 100)},
]

# Function to determine if auto-scaling is needed
def should_scale_up(instances_list, threshold=80):
    return any(instance["cpu_usage"] > threshold for instance in instances_list)

# Example usage
if should_scale_up(instances):
    print("Auto-scaling triggered: CPU usage is high.")
else:
    print("No auto-scaling needed: CPU usage is within limits.")
    