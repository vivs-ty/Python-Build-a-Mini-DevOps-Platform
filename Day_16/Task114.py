# Task 114: Split a large log file into chunks and count ERROR entries in parallel.

import concurrent.futures
from pathlib import Path
import re

# Setup a dummy massive log file
test_file = Path("massive_parallel_log.txt")
log_data = "INFO Boot\nERROR Timeout\nWARNING High CPU\nINFO Ok\nERROR DB crash\n" * 500_000
test_file.write_text(log_data)

def count_errors_in_chunk(chunk: list[str]) -> int:
    """Worker function executed in isolated processes."""
    pattern = re.compile(r'^ERROR')
    return sum(1 for line in chunk if pattern.match(line))

def main() -> None:
    print(f" Reading {test_file.name} into memory...")
    
    with open(test_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    num_processes = 4
    chunk_size = len(lines) // num_processes
    chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]
    
    print(f" Distributing {len(lines):,} lines across {num_processes} processes...")
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        # Map automatically passes each chunk to a separate core
        results = executor.map(count_errors_in_chunk, chunks)
        
    total_errors = sum(results)
    print(f" Analysis complete! Found {total_errors:,} ERROR entries.")

if __name__ == "__main__":
    main()
    print(f" \n Python 30 days Series - Day 16 Task 114 \n")
    print(f" \n Day 16 : Multiprocessing \n")
    print(f" \n Have a good one! \n " + "-"*40)
