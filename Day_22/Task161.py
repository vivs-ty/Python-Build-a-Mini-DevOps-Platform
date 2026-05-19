# Task 161: Run a Docker container through Python and verify that it started successfully.

import subprocess
def run_docker_container(image_name):
    try:
        # Run the Docker container
        result = subprocess.run(['docker', 'run', '-d', image_name], capture_output=True, text=True)
        if result.returncode == 0:
            container_id = result.stdout.strip()
            print(f"Container started successfully with ID: {container_id}")
            return container_id
        else:
            print(f"Failed to start container: {result.stderr}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
if __name__ == "__main__":
    image_name = 'hello-world'  # Example Docker image
    run_docker_container(image_name)
print(f" \n Python 30 days Series - Day 22 : Task 161 \n")
print(f" \n Day 22 : Logs, Reports, and Container Basics \n")
print(f" \n Have a good one! \n " + "-"*40)
