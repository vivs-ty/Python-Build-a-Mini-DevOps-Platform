# Task 48: Build a log analyzer that counts INFO, WARNING, and ERROR entries.

import os

log_file = input("Enter the log filename: ").strip()
info_count = 0
warning_count = 0
error_count = 0
