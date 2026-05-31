# Task 120: Benchmark threading versus multiprocessing for CPU-intensive work.

import time
import concurrent.futures

def cpu_intensive_task(num: int) -> int:
    """A mathematically heavy operation."""
    return sum(i * i for i in range(num))

def main() -> None:
    workload = [10_000_000] * 4 # 4 massive tasks
    print(" Benchmarking CPU-Intensive Workload...\n")

    # 1. Sequential (Base line)
    start = time.perf_counter()
    [cpu_intensive_task(n) for n in workload]
    seq_time = time.perf_counter() - start
    print(f" Sequential:      {seq_time:.2f} seconds")

    # 2. Threading (Will be roughly the same or SLOWER than sequential due to the GIL)
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        list(executor.map(cpu_intensive_task, workload))
    thread_time = time.perf_counter() - start
    print(f" Threading:       {thread_time:.2f} seconds (Blocked by GIL!)")

    # 3. Multiprocessing (Will be significantly faster, dividing work across cores)
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        list(executor.map(cpu_intensive_task, workload))
    process_time = time.perf_counter() - start
    print(f" Multiprocessing: {process_time:.2f} seconds (True Parallelism!)")

if __name__ == "__main__":
    main()
    print(" \n Python 30 days Series - Day 16 Task 120 \n"                                               )
    print(" \n Day 16 : Multiprocessing \n"                                )
    print(" \n Have a good one! \n "                          + "-"*40)
    