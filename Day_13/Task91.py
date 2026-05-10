# Task 91: Print CPU and memory usage every 5 seconds.


import psutil

def monitor_system(cycles: int = 3) -> None:
    print("📊 Starting System Monitor (Press Ctrl+C to stop)...")
    
    try:
        for _ in range(cycles): # Limited to 3 for testing. Use 'while True' for infinite.
            # interval=5 blocks execution for 5 seconds while it measures
            cpu_percent = psutil.cpu_percent(interval=5)
            memory_info = psutil.virtual_memory()
            
            print(f"⚙️ CPU Usage:    {cpu_percent:>5.1f}%")
            print(f"🧠 Memory Usage: {memory_info.percent:>5.1f}% ({memory_info.used / (1024**3):.1f} GB used)")
            print("-" * 30)
            
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped.")

monitor_system()
print("\nPython 30 days Series - Day 13 Task 91\nHave a good one!\n" + "-"*40)