# Task 116: Search for a keyword across multiple files using multiprocessing.

import multiprocessing

def search_keyword_in_file(file_path, keyword):
    with open(file_path, 'r') as f:
        return sum(1 for line in f if keyword in line)

if __name__ == "__main__":
    files = ["file1.txt", "file2.txt", "file3.txt"]
    keyword = "ERROR"

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.starmap(search_keyword_in_file, [(file, keyword) for file in files])

    print(f"Keyword '{keyword}' found {sum(results)} times across all files.")