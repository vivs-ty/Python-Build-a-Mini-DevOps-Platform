# Task 47: Merge multiple text files into one file.


import os

num_files = int(input("Enter the number of files to merge: ")).strip()
file_names = []
for _ in range(num_files):
    file_name = input("Enter the filename: ")
    file_names.append(file_name)
destination_file = input("Enter the destination file name: ").strip()
with open(destination_file, "w") as dst:
    for file_name in file_names:
        with open(file_name, "r") as src:
            dst.write(src.read() + "\n")
print(f"Files {', '.join(file_names)} have been merged into {destination_file}.")
