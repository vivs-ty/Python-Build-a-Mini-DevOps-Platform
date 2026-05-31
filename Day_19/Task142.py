# Task 142: Automate an application deployment by executing remote commands.

import paramiko

def deploy_application(hostname, username, password):
    commands = [
        "cd /var/www/myapp && git pull",
        "cd /var/www/myapp && pip install -r requirements.txt",
        "sudo systemctl restart myapp"
    ]

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(hostname, username=username, password=password)
        
        for cmd in commands:
            print(f"Executing: {cmd}")
            stdin, stdout, stderr = client.exec_command(cmd)
            
            # Wait for the command to finish and get the exit status
            exit_status = stdout.channel.recv_exit_status()
            
            if exit_status == 0:
                print("Success.")
            else:
                print(f"Error executing '{cmd}': {stderr.read().decode()}")
                break # Stop deployment if a step fails
                
    except Exception as e:
        print(f"Deployment failed: {e}")
    finally:
        client.close()

print(" \n Python 30 days Series - Day 19 Task 142 \n"                                               )
print(" \n Day 19 : SSH Automation \n"                               )
print(" \n Have a good one! \n "                          + "-"*40)
