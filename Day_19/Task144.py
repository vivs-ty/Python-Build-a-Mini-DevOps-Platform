# Task 144: Read SSH credentials from environment variables.

import os
import paramiko

def connect_with_env_vars():
    # Read variables from the operating system environment
    hostname = os.getenv("SSH_HOST", "127.0.0.1")
    username = os.getenv("SSH_USER", "root")
    password = os.getenv("SSH_PASS")

    if not password:
        print("Error: SSH_PASS environment variable is missing.")
        return

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        print(f"Attempting to connect to {hostname} as {username}...")
        client.connect(hostname, username=username, password=password)
        
        stdin, stdout, stderr = client.exec_command("whoami")
        print(f"Connected successfully. Running as: {stdout.read().decode().strip()}")
        
    except paramiko.AuthenticationException:
        print("Authentication failed. Check your credentials.")
    except Exception as e:
        print(f"Connection failed: {e}")
    finally:
        client.close()

# To use this, you must set the environment variables in your terminal first:
# export SSH_HOST="192.168.1.10"
# export SSH_USER="admin"
# export SSH_PASS="secretpass"
# connect_with_env_vars()