# Task 113: Use multiprocessing for CPU-bound tasks and compare runtime with a single-threaded version.
import multiprocessing
import time    

if __name__ == "__main__":
    # Example CPU-bound task
    def cpu_bound_task(n):
        total = 0
        for _ in range(n):
            total += _ ** 2
        return total

    # Single-threaded version
    start_time = time.time()
    result_single = cpu_bound_task(1000000)
    single_thread_time = time.time() - start_time

    # Multiprocessing version
    start_time = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(cpu_bound_task, [1000000 // multiprocessing.cpu_count()] * multiprocessing.cpu_count())
    multi_thread_time = time.time() - start_time

    print(f"Single-threaded time: {single_thread_time}")
    print(f"Multiprocessing time: {multi_thread_time}")
