# Task 50: Add a constructor to initialize all Server attributes.

class Server:
    def __init__(self, hostname: str, ip_address: str, cpu_cores: int, memory_gb: int):
        # The constructor initializes instance-specific attributes
        self.hostname = hostname
        self.ip_address = ip_address
        self.cpu_cores = cpu_cores
        self.memory_gb = memory_gb

# Demonstration
my_server = Server("api-server", "10.0.0.5", 8, 32)
print(f"Initialized Server: {my_server.hostname} with {my_server.cpu_cores} cores.")

