# Task 170: Monitor pod health and restart failed pods.

import subprocess

def monitor_and_restart_pods():
    try:
        # Get pods and their status phases
        result = subprocess.run(
            ["kubectl", "get", "pods", "--no-headers", "-o", "custom-columns=:metadata.name,:status.phase"],
            check=True,
            capture_output=True,
            text=True
        )
        
        lines = result.stdout.strip().split('\n')
        for line in lines:
            if not line.strip():
                continue
                
            parts = line.split()
            pod_name = parts[0]
            status = parts[1]
            
            # Check for common failure states
            if status in ["Failed", "CrashLoopBackOff", "Error"]:
                print(f"Pod {pod_name} is in state {status}. Deleting to force restart...")
                subprocess.run(["kubectl", "delete", "pod", pod_name])
            else:
                print(f"Pod {pod_name} is healthy ({status}).")
                
    except subprocess.CalledProcessError as e:
        print(f"Error monitoring pod health: {e.stderr}")

if __name__ == "__main__":
    monitor_and_restart_pods()
    
    print("\nPython 30 days Series - Day 24 : Task 170")
    print("Day 24 : Deployment and Kubernetes Basics")
    print("Have a good one!\n" + "-"*40)
    