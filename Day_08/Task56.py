# Task 56: Track the number of created objects with a class variable.

class Server:
    # Class variable: shared among all Server objects
    total_servers_created = 0

    def __init__(self, hostname: str):
        self.hostname = hostname
        # Increment the class variable every time a new instance is initialized
        Server.total_servers_created += 1
        print(f"Booted {self.hostname}. Total fleet size: {Server.total_servers_created}")

# Demonstration
print("Tracking server deployments:")
server1 = Server("web-01")
server2 = Server("db-01")
server3 = Server("cache-01")

print(f"\nFinal count accessed directly from class: {Server.total_servers_created}")
print(f" \n Python 30 days Series - Day 8 Task 56 \n")
print(f" \n Day 8: OOPs \n")
print(f" \n Have a good one! \n")
