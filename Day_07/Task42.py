# Task 42: Read a log file and print only the lines that contain ERROR.

log_file = 'application.log'
with open(log_file, 'r') as file:
    for line in file:
        if 'ERROR' in line:
            print(line.strip())