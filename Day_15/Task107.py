# Task 107: Compare execution time between single-threaded and multi-threaded code.

import time
import concurrent.futures

def simulated_io_task(task_id: int) -> str:
    """Simulates a task that waits for network or disk (I/O bound)."""
    time.sleep(1) # Wait 1 second
    return f"Task {task_id} done"

def run_single_threaded(tasks: list[int]) -> float:
    start_time = time.perf_counter()
    for t in tasks:
        simulated_io_task(t)
    return time.perf_counter() - start_time

def run_multi_threaded(tasks: list[int]) -> float:
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(tasks)) as executor:
        # map() acts like the standard map(), but executes in parallel threads
        list(executor.map(simulated_io_task, tasks))
    return time.perf_counter() - start_time

def main() -> None:
    tasks = list(range(1, 6)) # 5 tasks, each takes 1 second
    
    print("⏳ Running Single-threaded (Sequential)...")
    single_time = run_single_threaded(tasks)
    print(f"   -> Took {single_time:.2f} seconds\n")
    
    print("⚡ Running Multi-threaded (Concurrent)...")
    multi_time = run_multi_threaded(tasks)
    print(f"   -> Took {multi_time:.2f} seconds\n")
    
    print(f"🏆 Multithreading was {single_time / multi_time:.1f}x faster!")

if __name__ == "__main__":
    main()

    print(" \n Python 30 days Series - Day 15 Task 107 \n"                                               )
    print(" \n Day 15 : Multithreading \n"                               )
    print(" \n Have a good one! \n "                          + "-"*40)
