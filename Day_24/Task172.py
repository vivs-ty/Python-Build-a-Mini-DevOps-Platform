# Task 172: Fetch logs from a specific pod and save them locally.

import subprocess

def fetch_pod_logs(pod_name, output_file):
    try:
        result = subprocess.run(
            ["kubectl", "logs", pod_name],
            check=True,
            capture_output=True,
            text=True
        )
        
        with open(output_file, 'w') as f:
            f.write(result.stdout)
            
        print(f"Logs from pod '{pod_name}' successfully saved to '{output_file}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error fetching logs from pod '{pod_name}': {e.stderr}")

if __name__ == "__main__":
    # Ensure you replace "my_nginx_pod" with an actual running pod name before executing
    fetch_pod_logs("my_nginx_pod", "pod_logs.txt")
    
    print("\nPython 30 days Series - Day 24 : Task 172")
    print("Day 24 : Deployment and Kubernetes Basics")
    print("Have a good one!\n" + "-"*40)
    