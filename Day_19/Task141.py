# Task 141: Check remote disk usage over SSH.

import paramiko

def check_disk_usage(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(hostname, username=username, password=password)
        # Run the disk free command in human-readable format
        stdin, stdout, stderr = client.exec_command("df -h /")
        
        print(f"Disk Usage on {hostname}:")
        print(stdout.read().decode())
    except Exception as e:
        print(f"Failed to check disk usage: {e}")
    finally:
        client.close()

print(f" \n Python 30 days Series - Day 19 Task 141 \n")
print(f" \n Day 19 : SSH Automation \n")
print(f" \n Have a good one! \n " + "-"*40)

# Example usage:
# check_disk_usage("192.168.1.10", "admin", "secretpass")