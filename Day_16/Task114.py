# Task 114: Split a large log file into chunks and count ERROR entries in parallel.
import concurrent.futures
import time

def count_errors_in_chunk(chunk):
    return chunk.count("ERROR")

if __name__ == "__main__":
    # Example log file content
    log_content = "ERROR: Something went wrong\nINFO: Operation completed successfully\nERROR: Another error occurred\nDEBUG: Debug information\n" * 100000

    # Split log into chunks
    chunk_size = len(log_content) // 4
    chunks = [log_content[i:i + chunk_size] for i in range(0, len(log_content), chunk_size)]

    # Single-threaded version
    start_time = time.time()
    total_errors_single = sum(count_errors_in_chunk(chunk) for chunk in chunks)
    single_thread_time = time.time() - start_time

    # Parallel version
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(count_errors_in_chunk, chunks))
    total_errors_parallel = sum(results)
    parallel_time = time.time() - start_time

    print(f"Single-threaded errors: {total_errors_single}")
    print(f"Parallel errors: {total_errors_parallel}")
    print(f"Single-threaded time: {single_thread_time}")
    print(f"Parallel time: {parallel_time}")
    