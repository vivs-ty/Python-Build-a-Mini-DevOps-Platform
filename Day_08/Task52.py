# Task 52: Demonstrate method overriding in child classes.

class Server:
    def __init__(self, hostname: str):
        self.hostname = hostname

    def get_status(self) -> str:
        return f"Server '{self.hostname}' is running."

class LinuxServer(Server):
    # Overriding the parent's get_status method
    def get_status(self) -> str:
        return f" Linux Server '{self.hostname}' is accessible via SSH."

class WindowsServer(Server):
    # Overriding the parent's get_status method
    def get_status(self) -> str:
        return f" Windows Server '{self.hostname}' is accessible via RDP."

# Demonstration
generic = Server("base-node")
linux = LinuxServer("db-node")
windows = WindowsServer("exchange-node")

print(generic.get_status())
print(linux.get_status())
print(windows.get_status())
print(f" \n Python 30 days Series - Day 8 Task 52 \n")
print(f" \n Day 8: OOPs \n")
print(f" \n Have a good one! \n")
