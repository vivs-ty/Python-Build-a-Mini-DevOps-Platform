# Task 170: Monitor pod health and restart failed pods.

import subprocess

def monitor_pod_health():
    try:
        result = subprocess.run(
            ["kubectl", "get", "pods"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("Pod Health Status:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error monitoring pod health: {e.stderr}")

if __name__ == "__main__":
    monitor_pod_health()
    
    print("\nPython 30 days Series - Day 24 : Task 170")
    print("Day 24 : Deployment and Kubernetes Basics")
    print("Have a good one!\n" + "-"*40)
    