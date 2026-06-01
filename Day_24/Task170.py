# Task 170: Monitor pod health and restart failed pods.

import subprocess

def monitor_and_restart_pods():
    try:
        # Get pods and their status phases
        result = subprocess.run(
            ["kubectl", "get", "pods", "--no-headers", "-o", "custom-columns=NAME:metadata.name,STATUS:status.phase"],
            check=True,
            capture_output=True,
            text=True
        )
        
        lines = result.stdout.strip().split('\n')
        for line in lines:
            if not line.strip():
                continue
            
            # Split only on the first whitespace occurrence to handle pod names with spaces
            parts = line.split(None, 1)
            if len(parts) < 2:
                continue
                
            pod_name = parts[0]
            status = parts[1].strip()
            
            # Check for common failure states
            if status in ["Failed", "CrashLoopBackOff", "Error"]:
                print(f"Pod {pod_name} is in state {status}. Deleting to force restart...")
                restart_result = subprocess.run(["kubectl", "delete", "pod", pod_name], capture_output=True, text=True)
                if restart_result.returncode == 0:
                    print(f"Successfully deleted pod {pod_name}.")
                else:
                    print(f"Failed to delete pod {pod_name}: {restart_result.stderr}")
            else:
                print(f"Pod {pod_name} is healthy ({status}).")
                
    except subprocess.CalledProcessError as e:
        print(f"Error monitoring pod health: {e.stderr}")

if __name__ == "__main__":
    monitor_and_restart_pods()
    
    print(" \n Python 30 days Series - Day 24 : Task 170 \n")
    print(" \n Day 24: Deployment and Kubernetes Basics \n")
    print(" \n Have a good one! " + "-"*40)
    