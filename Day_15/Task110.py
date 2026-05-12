# Task 110: Use a thread pool to execute tasks efficiently.

import concurrent.futures
import time
import random

def heavy_worker(task_id: int) -> str:
    """Simulates a task with variable execution time."""
    sleep_time = random.uniform(0.5, 2.0)
    time.sleep(sleep_time)
    return f"Task-{task_id} completed in {sleep_time:.2f}s"

def main() -> None:
    print("🏭 Starting Thread Pool Executor...")
    
    # Context manager automatically cleans up threads when finished
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks dynamically
        futures = {executor.submit(heavy_worker, i): i for i in range(1, 6)}
        
        # Process results exactly in the order they finish (Unordered)
        for future in concurrent.futures.as_completed(futures):
            task_id = futures[future]
            try:
                result = future.result()
                print(f" {result}")
            except Exception as e:
                print(f" Task-{task_id} generated an exception: {e}")

if __name__ == "__main__":
    main()
    
    print(f" \n Python 30 days Series - Day 15 Task 110 \n")
    print(f" \n Day 15 : Multithreading \n")
    print(f" \n Have a good one! \n " + "-"*40)
