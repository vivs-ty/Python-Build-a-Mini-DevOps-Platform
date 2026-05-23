# Task 175: Delete unused or failed pods automatically.

import subprocess

def delete_unused_pods():
    try:
        # Get the list of pods not in the 'Running' state
        result = subprocess.run(
            ["kubectl", "get", "pods", "--field-selector=status.phase!=Running", "-o", "jsonpath='{.items[*].metadata.name}'"],
            check=True,
            capture_output=True,
            text=True
        )
        
        # Clean up the output string and split into a list
        pod_names = result.stdout.strip().strip("'").split()
        
        if not pod_names:
            print("No unused or failed pods found.")
            return
        
        for pod in pod_names:
            subprocess.run(["kubectl", "delete", "pod", pod], check=True)
            print(f"Deleted pod: {pod}")
            
    except subprocess.CalledProcessError as e:
        print(f"Error deleting pods: {e.stderr}")

if __name__ == "__main__":
    delete_unused_pods()
    
    print("\nPython 30 days Series - Day 25 : Task 175")
    print("Day 25 : Kubernetes Operations and Cloud Basics")
    print("Have a good one!\n" + "-"*40)
    