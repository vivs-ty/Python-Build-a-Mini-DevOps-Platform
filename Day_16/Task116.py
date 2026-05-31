# Task 116: Search for a keyword across multiple files using multiprocessing.

import concurrent.futures
from pathlib import Path

# Setup dummy files
Path("doc1.txt").write_text("Hello world\nFind the target here.")
Path("doc2.txt").write_text("Nothing to see here.\nMove along.")
Path("doc3.txt").write_text("Another target found on line 2.\nGoodbye.")

def search_file_for_keyword(file_path: Path, keyword: str) -> list[str]:
    """Worker function: Opens the file and returns matching lines."""
    matches = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                if keyword.lower() in line.lower():
                    matches.append(f"[{file_path.name}: Line {line_num}] {line.strip()}")
    except Exception as e:
        matches.append(f"Error reading {file_path.name}: {e}")
    return matches

def main() -> None:
    files_to_search = [Path("doc1.txt"), Path("doc2.txt"), Path("doc3.txt")]
    target_keyword = "target"
    
    print(f" Searching for '{target_keyword}' across {len(files_to_search)} files in parallel...")
    
    all_matches = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # We use a list comprehension to pass the keyword alongside the file path
        futures = [executor.submit(search_file_for_keyword, fp, target_keyword) for fp in files_to_search]
        
        for future in concurrent.futures.as_completed(futures):
            # Extend our master list with the results from the worker
            all_matches.extend(future.result())
            
    print("\n Search Results:")
    for match in all_matches:
        print(f" -> {match}")

if __name__ == "__main__":
    main()
    print(" \n Python 30 days Series - Day 16 Task 116 \n"                                               )
    print(" \n Day 16 : Multiprocessing \n"                                )
    print(" \n Have a good one! \n "                          + "-"*40)
