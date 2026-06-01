# Task 172: Fetch logs from a specific pod and save them locally.

import subprocess
import os

def fetch_pod_logs(pod_name, output_file=None):
    """Fetch logs from a Kubernetes pod and save them locally.
    
    Args:
        pod_name: Name of the pod to fetch logs from
        output_file: Path to save the logs (default: pod_name_logs.txt)
    """
    if not output_file:
        output_file = f"{pod_name}_logs.txt"
        
    try:
        # Verify pod exists before fetching logs
        check_result = subprocess.run(
            ["kubectl", "get", "pod", pod_name],
            capture_output=True,
            text=True
        )
        
        if check_result.returncode != 0:
            print(f"Error: Pod '{pod_name}' not found: {check_result.stderr}")
            return False
        
        # Fetch logs
        result = subprocess.run(
            ["kubectl", "logs", pod_name],
            check=True,
            capture_output=True,
            text=True
        )
        
        # Write logs to file
        try:
            os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)
            with open(output_file, 'w') as f:
                f.write(result.stdout)
                
            print(f"Logs from pod '{pod_name}' successfully saved to '{output_file}'.")
            return True
        except IOError as io_error:
            print(f"Error writing logs to file '{output_file}': {io_error}")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"Error fetching logs from pod '{pod_name}': {e.stderr}")
        return False

if __name__ == "__main__":
    # Ensure you replace "my_nginx_pod" with an actual running pod name before executing
    fetch_pod_logs("my_nginx_pod", "pod_logs.txt")
    
    print(" \n Python 30 days Series - Day 24 : Task 172 \n")
    print(" \n Day 24: Deployment and Kubernetes Basics \n")
    print(" \n Have a good one! " + "-"*40)
    