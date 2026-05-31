# Task 137: Connect to a remote server over SSH and run a command.

import paramiko

def run_ssh_command(hostname, username, password, command):
    client = paramiko.SSHClient()
    # Automatically add the server's host key (avoids the yes/no prompt)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(hostname, username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        
        print(f"Output from {hostname}:")
        print(stdout.read().decode())
    except Exception as e:
        print(f"Connection failed: {e}")
    finally:
        client.close()

print(" \n Python 30 days Series - Day 19 Task 137 \n"                                               )
print(" \n Day 19 : SSH Automation \n"                               )
print(" \n Have a good one! \n "                          + "-"*40)

# Example usage:
# run_ssh_command("192.168.1.10", "admin", "secretpass", "uptime")
