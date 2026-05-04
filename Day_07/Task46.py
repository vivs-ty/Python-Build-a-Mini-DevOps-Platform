# Task 46: Write only unique lines from a file into a new file.

import os
select_file = input("Enter the filename: ")
destination_file = input("Enter the destination file name: ").strip()

with open(select_file, "r") as src:
    lines = src.readlines()

unique_lines = list(set(lines))

with open(destination_file, "w") as dst:
    dst.writelines(unique_lines)
    