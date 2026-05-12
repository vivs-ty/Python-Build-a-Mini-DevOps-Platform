# Task 108: Process different parts of a log file in parallel threads.

# Task 108: Master Version
import concurrent.futures
from pathlib import Path
import re

# 1. Setup a dummy log file for the test
log_content = "INFO Start\nERROR Disk full\nINFO Ok\nWARNING Slow\nERROR Auth fail\nINFO Stop\n" * 1000
test_file = Path("massive_log.txt")
test_file.write_text(log_content)

def process_chunk(chunk: list[str]) -> int:
    """A worker function that counts ERRORs in its assigned chunk of lines."""
    error_pattern = re.compile(r'^ERROR')
    return sum(1 for line in chunk if error_pattern.search(line))

def main() -> None:
    print(f"📂 Reading log file '{test_file.name}'...")
    
    # Read all lines into memory (for massive files, use a file generator)
    with open(test_file, "r") as f:
        lines = f.readlines()
        
    # Split the lines into 4 chunks
    num_chunks = 4
    chunk_size = len(lines) // num_chunks
    chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]
    
    total_errors = 0
    print(f"🚀 Processing {len(lines)} lines across {num_chunks} parallel threads...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_chunks) as executor:
        # Submit the chunks to the threads
        results = executor.map(process_chunk, chunks)
        
        # Aggregate the results
        total_errors = sum(results)
        
    print(f"✅ Log analysis complete! Found {total_errors} total errors.")

if __name__ == "__main__":
    main()
    print("\nPython 30 days Series - Day 15 Task 108\nHave a good one!\n" + "-"*40)