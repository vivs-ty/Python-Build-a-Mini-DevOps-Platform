# Task 113: Use multiprocessing for CPU-bound tasks and compare runtime with a single-threaded version.

import time
import concurrent.futures
import math

def count_primes(limit: int) -> int:
    """A heavily CPU-bound task."""
    count = 0
    for num in range(2, limit):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count

def main() -> None:
    # 4 large calculations
    tasks = [2_000_000, 2_000_000, 2_000_000, 2_000_000] 
    
    print(" Running sequentially (Single Core)...")
    start = time.perf_counter()
    results_seq = [count_primes(t) for t in tasks]
    duration_seq = time.perf_counter() - start
    print(f"   -> Took {duration_seq:.2f} seconds.")

    print("\n Running with Multiprocessing (Multi-Core)...")
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results_multi = list(executor.map(count_primes, tasks))
    duration_multi = time.perf_counter() - start
    print(f"   -> Took {duration_multi:.2f} seconds.")
    
    print(f"\n Multiprocessing was {duration_seq / duration_multi:.1f}x faster!")

# MUST use this guard for multiprocessing!
if __name__ == "__main__":
    main()
    print(f" \n Python 30 days Series - Day 16 Task 113 \n")
    print(f" \n Day 16 : Multiprocessing \n")
    print(f" \n Have a good one! \n " + "-"*40)
