# Task 162: List all running and stopped Docker containers.

import subprocess

def list_docker_containers():
    try:
        # List all Docker containers (both running and stopped)
        result = subprocess.run(['docker', 'ps', '-a'], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Docker Containers:")
            print(result.stdout)
        else:
            stderr = result.stderr.strip()
            if stderr:
                print(f"Failed to list containers: {stderr}")
            else:
                print("Failed to list containers: Unknown error")
            
    except FileNotFoundError:
        print("Error: Docker is not installed or not added to your system PATH.")
    except subprocess.TimeoutExpired:
        print("Error: Docker command timed out.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_docker_containers()
    
    print(" \n Python 30 days Series - Day 22 : Task 162 \n")
    print(" \n Day 22: Logs, Reports, and Container Basics \n")
    print(" \n Have a good one! " + "-"*40)
    