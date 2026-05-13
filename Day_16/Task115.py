# Task 115: Use a process pool to compute values and collect results.
import concurrent.futures

def compute_value(n):
    return n ** 2

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(compute_value, i) for i in range(10)]
        results = [future.result() for future in futures]
    print(results)