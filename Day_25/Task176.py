# Task 176: Watch cluster health continuously and report anomalies.

import subprocess
import time

def watch_cluster_health(interval=10):
    while True:
        try:
            result = subprocess.run(
                ["kubectl", "get", "nodes"],
                check=True,
                capture_output=True,
                text=True
            )
            print("Cluster health status:\n")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error checking cluster health: {e.stderr}")
        
        time.sleep(interval)

if __name__ == "__main__":
    watch_cluster_health()
    
    print("\nPython 30 days Series - Day 25 : Task 176")
    print("Day 25 : Kubernetes and Cloud Storage")
    print("Have a good one!\n" + "-"*40)
    