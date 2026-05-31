# Task 138: Run the same SSH command on multiple servers.

import paramiko

def run_on_multiple_servers(servers, username, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for host in servers:
        try:
            client.connect(host, username=username, password=password)
            stdin, stdout, stderr = client.exec_command(command)
            
            print(f"--- Output from {host} ---")
            print(stdout.read().decode().strip())
        except Exception as e:
            print(f"Failed to connect to {host}: {e}")
        finally:
            client.close()

print(" \n Python 30 days Series - Day 19 Task 138 \n"                                               )
print(" \n Day 19 : SSH Automation \n"                               )
print(" \n Have a good one! \n "                          + "-"*40)

# Example usage:
# server_list = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
# run_on_multiple_servers(server_list, "admin", "secretpass", "df -h")