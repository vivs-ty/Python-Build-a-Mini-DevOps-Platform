# Task 167: Save container logs into a file for analysis.

import docker
from docker.errors import DockerException
def save_container_logs(container_name, log_file):
    try:
        client = docker.from_env()
        container = client.containers.get(container_name)
        
        logs = container.logs().decode('utf-8')
        
        with open(log_file, 'w') as file:
            file.write(logs)
        
        print(f"Logs for container '{container_name}' saved to '{log_file}'.")
        
    except docker.errors.NotFound:
        print(f"Error: Container '{container_name}' not found.")
    except DockerException as e:
        print(f"An error occurred while interacting with Docker: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    save_container_logs("my_nginx_container", "nginx_logs.txt")
    
    print("\nPython 30 days Series - Day 23 : Task 167")
    print("Day 23 : Docker Automation")
    print("Have a good one!\n" + "-"*40)\
    