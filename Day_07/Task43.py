# Task 43: Copy the contents of one file into another file.


import shutil

source_file = input("Enter the source file name: ").strip()
destination_file = input("Enter the destination file name: ").strip()

with open(source_file, "r") as src:
    with open(destination_file, "w") as dst:
        dst.write(src.read())