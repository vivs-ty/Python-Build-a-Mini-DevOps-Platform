# Task 92: Identify the top 5 memory-consuming processes.

import psutil

def get_top_memory_processes(n: int = 5) -> None:
    processes = []
    
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            # Extract Resident Set Size (RSS) - Actual physical memory used
            rss_memory = proc.info['memory_info'].rss
            processes.append((proc.info['name'], proc.info['pid'], rss_memory))
        except (psutil.NoSuchProcess, psutil.AccessDenied, AttributeError):
            continue

    # Sort by memory descending
    processes.sort(key=lambda x: x[2], reverse=True)
    
    print(f"🏆 Top {n} Memory-Consuming Processes:")
    print(f"{'PID':<10} | {'Memory (MB)':<15} | {'Process Name'}")
    print("-" * 50)
    
    for name, pid, memory_bytes in processes[:n]:
        memory_mb = memory_bytes / (1024 * 1024)
        print(f"{pid:<10} | {memory_mb:<15.2f} | {name}")

get_top_memory_processes()
print("\nPython 30 days Series - Day 13 Task 92\nHave a good one!\n" + "-"*40)
