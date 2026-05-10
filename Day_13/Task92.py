# Task 92: Identify the top 5 memory-consuming processes.
import psutil

def get_top_memory_processes(n=5):
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            memory_info = proc.info['memory_info']
            processes.append((proc.info['name'], proc.info['pid'], memory_info.rss))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    # Sort by memory usage and return the top n
    processes.sort(key=lambda x: x[2], reverse=True)
    return processes[:n]

# Example usage:
# top_processes = get_top_memory_processes(5)
# for name, pid, memory in top_processes:
#     print(f"Process: {name}, PID: {pid}, Memory Usage: {memory}")
