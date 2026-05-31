# Task 49: Create a Server class with hostname, IP address, CPU cores, and memory.

class Server:
    # Defining attributes (Task 50 will formally introduce the constructor)
    hostname: str = "Unknown"
    ip_address: str = "0.0.0.0"
    cpu_cores: int = 0
    memory_gb: int = 0

# Demonstration
my_server = Server()
my_server.hostname = "web-node-01"
my_server.ip_address = "192.168.1.10"

print(f"Created Server: {my_server.hostname} at {my_server.ip_address}")
print(" \n Python 30 days Series - Day 8 Task 49 \n"                                             )
print(" \n Day 8: OOPs \n"                   )
print(" \n Have a good one! \n "                          + "-"*40)
