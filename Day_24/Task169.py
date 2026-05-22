# Task 169: Retrieve and display the status of all Kubernetes pods.

import subprocess

def get_pod_status():
    try:
        result = subprocess.run(
            ["kubectl", "get", "pods"],
            check=True,
            capture_output=True,
            text=True
        )
        print("Pod Status:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving pod status: {e.stderr}")

if __name__ == "__main__":
    get_pod_status()
    
    print("\nPython 30 days Series - Day 24 : Task 169")
    print("Day 24 : Deployment and Kubernetes Basics")
    print("Have a good one!\n" + "-"*40)
    