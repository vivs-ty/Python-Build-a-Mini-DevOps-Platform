# Task 173: Check CPU and memory usage for Kubernetes pods.

import subprocess
def check_pod_resources():
    try:
        result = subprocess.run(
            ["kubectl", "top", "pods"],
            check=True,
            capture_output=True,
            text=True
        )
        print("CPU and Memory usage for Kubernetes pods:\n")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error checking pod resources: {e.stderr}")
if __name__ == "__main__":
    check_pod_resources()
    
    print("\nPython 30 days Series - Day 25 : Task 173")
    print("Day 25 : Kubernetes and Cloud Storage")
    print("Have a good one!\n" + "-"*40)
    