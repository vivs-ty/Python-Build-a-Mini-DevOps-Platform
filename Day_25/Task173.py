# Task 173: Check CPU and memory usage for Kubernetes pods.

import subprocess

def check_pod_resources():
    """Check CPU and memory usage for Kubernetes pods.
    
    Note: This command requires metrics-server to be installed in your Kubernetes cluster.
    Install it with: kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
    """
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
        stderr = e.stderr.strip() if e.stderr else "Unknown error"
        if "metrics not available" in stderr.lower() or "no metrics" in stderr.lower():
            print("Error: metrics-server is not installed in your Kubernetes cluster.")
            print("Install it with: kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml")
        else:
            print(f"Error checking pod resources: {stderr}")

if __name__ == "__main__":
    check_pod_resources()
    
    print(" \n Python 30 days Series - Day 25 : Task 173 \n")
    print(" \n Day 25: Kubernetes Operations and Cloud Basics \n")
    print(" \n Have a good one! " + "-"*40)
    