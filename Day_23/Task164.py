# Task 164: Pull a Docker image and run it with specified parameters.

import subprocess

def pull_and_run_docker_image(image_name, container_name, ports=None):
    try:
        # Pull the Docker image
        print(f"Pulling Docker image: {image_name}")
        pull_result = subprocess.run(['docker', 'pull', image_name], capture_output=True, text=True)
        
        if pull_result.returncode != 0:
            print(f"Failed to pull image: {pull_result.stderr}")
            return
        
        print(f"Successfully pulled image: {image_name}")
        
        # Prepare the run command
        run_command = ['docker', 'run', '-d', '--name', container_name]
        
        if ports:
            for host_port, container_port in ports.items():
                run_command.extend(['-p', f"{host_port}:{container_port}"])
        
        run_command.append(image_name)
        
        # Run the Docker container
        print(f"Running container: {container_name} from image: {image_name}")
        run_result = subprocess.run(run_command, capture_output=True, text=True)
        
        if run_result.returncode == 0:
            print(f"Container '{container_name}' is running successfully.")
        else:
            print(f"Failed to run container: {run_result.stderr}")
            
    except FileNotFoundError:
        print("Error: Docker is not installed or not added to your system PATH.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    image_name = "nginx:latest"  # Example image
    container_name = "my_nginx_container"
    ports = {8080: 80}  # Map host port 8080 to container port 80
    
    pull_and_run_docker_image(image_name, container_name, ports)
    
    print("\nPython 30 days Series - Day 23 : Task 164")
    print("Day 23 : Docker Automation")
    print("Have a good one!\n" + "-"*40)