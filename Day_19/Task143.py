# Task 143: Monitor a remote service and restart it if it stops.

import paramiko

def monitor_service(hostname, username, password, service_name):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(hostname, username=username, password=password)

        # Check if the service is active
        stdin, stdout, stderr = client.exec_command(f"systemctl is-active {service_name}")
        status = stdout.read().decode().strip()

        if status != "active":
            print(f"Service '{service_name}' is down. Attempting to restart...")
            client.exec_command(f"sudo systemctl start {service_name}")
            print("Restart command sent.")
        else:
            print(f"Service '{service_name}' is running smoothly.")
            
    except Exception as e:
        print(f"Monitoring failed: {e}")
    finally:
        client.close()

print(f" \n Python 30 days Series - Day 19 Task 143 \n")
print(f" \n Day 19 : SSH Automation \n")
print(f" \n Have a good one! \n " + "-"*40)

# Example usage:
# monitor_service("192.168.1.10", "admin", "secretpass", "nginx")