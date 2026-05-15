# Task 129: Detect duplicate files by comparing file content.

import hashlib
from collections import defaultdict
from pathlib import Path

def get_file_hash(filepath: Path, chunk_size: int = 8192) -> str:
    """Safely hashes a file in chunks to avoid memory crashes on huge files."""
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicates(directory: str) -> None:
    target_dir = Path(directory)
    if not target_dir.is_dir(): return

    print(f"🔍 Scanning '{target_dir}' for duplicates...")
    
    # Step 1: Group by size (Extremely fast)
    size_dict = defaultdict(list)
    for filepath in target_dir.rglob("*"):
        if filepath.is_file():
            size_dict[filepath.stat().st_size].append(filepath)

    # Step 2: Hash only the files that share a size (Computationally heavy)
    hash_dict = defaultdict(list)
    for size, files in size_dict.items():
        if len(files) > 1: # Only hash if there's a potential duplicate
            for filepath in files:
                file_hash = get_file_hash(filepath)
                hash_dict[file_hash].append(filepath)

    # Step 3: Report
    duplicates_found = False
    for file_hash, files in hash_dict.items():
        if len(files) > 1:
            duplicates_found = True
            print(f"\n⚠️ Found {len(files)} identical files:")
            for f in files:
                print(f"   -> {f}")

    if not duplicates_found:
        print("✅ No duplicates found.")

# --- Demonstration ---
find_duplicates(".")
print("\nPython 30 days Series - Day 18 Task 129\nHave a good one!\n" + "-"*40)