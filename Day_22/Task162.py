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
            print(f"Failed to list containers: {result.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    list_docker_containers()
print(f" \n Python 30 days Series - Day 22 : Task 162 \n")
print(f" \n Day 22 : Logs, Reports, and Container Basics \n")
print(f" \n Have a good one! \n " + "-"*40)
