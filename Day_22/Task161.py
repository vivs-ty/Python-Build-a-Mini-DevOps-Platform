# Task 161: Run a Docker container through Python and verify that it started successfully.

import subprocess

def run_docker_container(image_name):
    try:
        # Run the Docker container in detached mode (-d)
        result = subprocess.run(['docker', 'run', '-d', image_name], capture_output=True, text=True)
        
        if result.returncode == 0:
            container_id = result.stdout.strip()
            print(f"Container started successfully with ID: {container_id}")
            return container_id
        else:
            print(f"Failed to start container: {result.stderr.strip()}")
            return None
            
    except FileNotFoundError:
        print("Error: Docker is not installed or not added to your system PATH.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    image_name = 'nginx:alpine'
    run_docker_container(image_name)
    
    print("\nPython 30 days Series - Day 22 : Task 161")
    print("Day 22 : Logs, Reports, and Container Basics")
    print("Have a good one!\n" + "-"*40)
    