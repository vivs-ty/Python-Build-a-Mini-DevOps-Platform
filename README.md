---

#  Python for DevOps — 30 Day Challenge
---

## 🟢 DAY 1 — Input, Output, Variables (6 Challenges)

### 1. Write a Python script that prints a welcome message for a DevOps engineer. The message should include the current system date and time using Python’s built-in libraries.

---

### 2. Create a program that asks the user to input their name and their current job role. The program should then display a formatted greeting message such as:
``` "Hello <name>, you are working as a <role>. Welcome to DevOps automation." ```

---

### 3. Write a Python script that takes two numbers as input from the user and prints their sum, difference, multiplication, and division. Handle invalid numeric inputs gracefully.

---

### 4. Create a program that swaps two variables entered by the user without using a third variable. Print the values before and after swapping.

---

### 5. Write a script that takes temperature in Celsius as input and converts it into Fahrenheit. Display the result with proper formatting up to 2 decimal places.

---

### 6. Build a simple command-line calculator that asks the user to input two numbers and an operator (+, -, *, /). Based on the operator, perform the corresponding operation and print the result.

---

## 🟢 DAY 2 — Conditional Logic (6 Challenges)

### 7. Write a Python program that takes a number as input and determines whether it is even or odd. Ensure that invalid inputs are handled properly.

---

### 8. Create a script that accepts a number and determines whether it is positive, negative, or zero. Print a clear message describing the result.

---

### 9. Write a program that takes three numbers from the user and prints the largest among them. Do not use built-in max() function.

---

### 10. Build a simple login system where a predefined username and password are stored in the script. Ask the user to enter credentials and validate them. Print success or failure messages accordingly.

---

### 11. Write a Python script to check whether a given year is a leap year or not based on standard leap year rules.

---

### 12. Create a grading system where the user enters marks (0–100), and the program assigns grades:

* A: 90–100
* B: 75–89
* C: 50–74
* Fail: below 50

---

## 🟢 DAY 3 — Loops (6 Challenges)

### 13. Write a Python script that prints numbers from 1 to 100 using a loop. Modify it to skip numbers divisible by 3.

---

### 14. Create a program that generates a multiplication table for a number entered by the user, up to 10 multiples.

---

### 15. Write a script to calculate the factorial of a number using a loop. Ensure that negative numbers are handled properly.

---

### 16. Generate the Fibonacci sequence up to N terms, where N is provided by the user.

---

### 17. Write a program that counts the number of digits in a given integer input by the user.

---

### 18. Create a script that calculates the sum of all numbers between two given numbers (inclusive).

---

## 🟢 DAY 4 — Strings (6 Challenges)

### 19. Write a Python program that reverses a string entered by the user without using built-in reverse functions.

---

### 20. Create a script to check whether a given string is a palindrome (reads same forward and backward).

---

### 21. Write a program that counts the number of vowels and consonants in a string.

---

### 22. Create a script that removes duplicate characters from a string while preserving the order of characters.

---

### 23. Write a Python program that calculates the frequency of each character in a string and prints the result in dictionary format.

---

### 24. Build a password strength checker that evaluates a password based on:

* Length (minimum 8 characters)
* Presence of uppercase letters
* Presence of digits
* Presence of special characters

---

## 🟢 DAY 5 — Lists, Sets, Dictionaries (8 Challenges)

### 25. Write a Python script that removes duplicate elements from a list provided by the user.

---

### 26. Create a program that finds the second largest number in a list without using built-in sorting functions.

---

### 27. Write a script to sort a list of numbers in ascending order without using the built-in sort() method.

---

### 28. Create a program that merges two lists and removes duplicate values from the combined list.

---

### 29. Write a script that counts the frequency of each element in a list and stores the result in a dictionary.

---

### 30. Build a simple phonebook application using a dictionary where users can:

* Add a contact
* Search a contact
* Delete a contact

---

### 31. Write a Python program that converts a list of tuples into a dictionary.

---

### 32. Create a script that finds the intersection and union of two sets provided by the user.

---


## 🟢 DAY 6 — Functions & Error Handling (8 Challenges)

### 33. Write a Python program that defines reusable functions for basic mathematical operations such as addition, subtraction, multiplication, and division. The program should call these functions based on user input and handle invalid inputs gracefully.

---

### 34. Create a function that accepts a list of numbers and returns the maximum, minimum, and average values. Do not use built-in functions like `max()` or `min()`.

---

### 35. Write a Python function that takes a number as input and returns its factorial using recursion. Ensure proper error handling for negative numbers.

---

### 36. Create a function that takes a filename as input and safely reads the file content. If the file does not exist, handle the exception and print a meaningful error message instead of crashing.

---

### 37. Write a program that asks the user for two numbers and performs division. Use exception handling to manage division by zero and invalid inputs.

---

### 38. Define a custom exception called `InvalidAgeError`. Write a program that asks the user for their age and raises this exception if the age is below 18.

---

### 39. Create a function that accepts variable-length arguments (`*args`) and calculates the sum and average of all numbers passed to it.

---

### 40. Build a command-line utility that uses functions to perform different operations (e.g., add user, delete user, list users). The user should select options via menu input.

---

## 🟡 DAY 7 — File Handling Deep Dive (8 Challenges)

### 41. Write a Python script that reads a text file and prints the total number of lines, words, and characters present in the file.

---

### 42. Create a program that reads a log file and prints only the lines that contain the word "ERROR".

---

### 43. Write a script that copies the contents of one file into another file. Ensure that the destination file is created if it does not exist.

---

### 44. Create a program that appends user activity logs (with timestamp) into a file every time the script is executed.

---

### 45. Write a Python script that reads a file and counts how many times a specific word (entered by the user) appears in it.

---

### 46. Create a script that reads a file line by line and writes only unique lines into a new file.

---

### 47. Write a program that merges multiple text files into a single file.

---

### 48. Build a simple log analyzer that reads a log file and categorizes entries into INFO, WARNING, and ERROR counts.

---

## 🟡 DAY 8 — Object-Oriented Programming (8 Challenges)

### 49. Create a class called `Server` with attributes such as hostname, IP address, CPU cores, and memory. Add a method to display server details.

---

### 50. Enhance the `Server` class by adding a constructor that initializes all attributes during object creation.

---

### 51. Create two subclasses called `LinuxServer` and `WindowsServer` that inherit from the `Server` class. Add OS-specific attributes and methods.

---

### 52.

Demonstrate method overriding by redefining a method in the child classes that behaves differently from the parent class.

---

### 53. Implement encapsulation by making certain attributes private and providing getter and setter methods.

---

### 54. Create a class called `UserManager` that manages a list of users with operations such as add, delete, and list users.

---

### 55. Write a Python program to simulate a bank system using classes, where users can deposit, withdraw, and check balance.

---

### 56. Create a class that tracks the number of objects created using a class variable and prints the count.

---

## 🟡 DAY 9 — JSON, CSV, Config Management (8 Challenges)

### 57. Write a Python script that reads a JSON configuration file and prints all key-value pairs.

---

### 58. Modify the JSON file by updating a value and writing the updated content back to the file.

---

### 59. Create a program that converts a CSV file into a JSON file.

---

### 60. Write a script that reads a CSV file and calculates summary statistics such as total rows and average values for numeric columns.

---

### 61. Build a configuration loader that reads settings from a JSON file and applies them to your program.

---

### 62. Write a Python script that validates whether a JSON file is properly formatted. If not, display the error.

---

### 63. Create a script that merges multiple JSON files into a single file.

---

### 64. Build a tool that reads environment-specific configuration files (e.g., dev.json, prod.json) and loads the correct configuration based on user input.

---

## 🟡 DAY 10 — OS Interaction & Environment (8 Challenges)

### 65. Write a Python script that prints all environment variables available in the system.

---

### 66. Create a program that reads a specific environment variable and prints its value. If it does not exist, print an appropriate message.

---

### 67. Write a script that lists all files and directories in the current working directory.

---

### 68. Create a program that creates a directory structure (e.g., logs/, data/, backup/) if it does not already exist.

---

### 69. Write a Python script that deletes files older than a certain number of days from a directory.

---

### 70. Create a disk usage analyzer that calculates the total size of files in a directory.

---

### 71. Write a script that monitors a directory and prints a message whenever a new file is added.

---

### 72. Build a backup automation tool that copies files from one directory to another and logs the operation.


---


## 🟡 DAY 11 — Regular Expressions (Regex for Logs & Validation) (8 Challenges)

### 73. Write a Python script that reads a text file and extracts all email addresses using regular expressions. Print the list of unique emails.

---

### 74. Create a program that validates whether a given string is a valid IPv4 address using regex. The program should reject invalid formats like "999.300.1.1".

---

### 75. Write a script that parses a log file and extracts all timestamps in the format `YYYY-MM-DD HH:MM:SS`.

---

### 76. Create a program that reads a log file and extracts all IP addresses along with the number of times each IP appears.

---

### 77. Write a Python script that identifies all URLs present in a given text file and prints them.

---

### 78. Build a password validator using regex that enforces:

* Minimum 8 characters
* At least one uppercase letter
* At least one number
* At least one special character

---

### 79. Write a script that replaces all occurrences of sensitive data (like email addresses) in a file with masked values (e.g., `user@example.com → u***@example.com`).

---

### 80. Create a log filtering tool that uses regex patterns provided by the user to extract matching lines from a log file.

---

## 🟡 DAY 12 — CLI Tools with `argparse` (DevOps Tooling Mindset) (8 Challenges)

### 81. Write a Python script that uses `argparse` to accept a filename as an argument and prints its content.

---

### 82. Create a CLI tool that accepts two numbers and an operation (`add`, `sub`, `mul`, `div`) as command-line arguments and performs the operation.

---

### 83. Build a command-line log analyzer that accepts a log file path and a log level (INFO, ERROR, WARNING) as arguments and filters logs accordingly.

---

### 84. Write a CLI tool that accepts a directory path and lists all files larger than a specified size.

---

### 85. Create a script that takes multiple filenames as arguments and merges their contents into a single output file.

---

### 86. Build a CLI tool with multiple subcommands such as:

* `create-user`
* `delete-user`
* `list-users`

Each subcommand should perform its respective function.

---

### 87. Write a script that supports flags like `--verbose` and `--dry-run` to simulate execution without making actual changes.

---

### 88. Create a CLI utility that takes a URL as input and returns the HTTP status code along with response time.

---

## 🟡 DAY 13 — Process & System Monitoring (8 Challenges)

### 89. Write a Python script that lists all running processes on the system along with their process IDs.

---

### 90. Create a program that finds and terminates a process by its name. Handle cases where the process does not exist.

---

### 91. Build a system monitoring tool that prints CPU and memory usage every 5 seconds.

---

### 92. Write a script that identifies the top 5 processes consuming the most memory.

---

### 93. Create a program that logs system performance (CPU, memory, disk usage) into a file periodically.

---

### 94. Write a Python script that alerts the user if CPU usage exceeds a certain threshold.

---

### 95. Build a tool that checks disk usage and sends a warning if usage exceeds 80%.

---

### 96. Create a script that monitors a specific process and restarts it if it stops running.

---

## 🟡 DAY 14 — Networking & API Handling (8 Challenges)

### 97. Write a Python script that checks whether a given website is reachable by sending an HTTP request.

---

### 98. Create a program that fetches data from a public API and displays selected fields in a readable format.

---

### 99. Write a script that retrieves the HTTP status code and headers of a given URL.

---

### 100. Build a program that downloads data from an API and saves it as a JSON file.

---

### 101. Create a script that retries an API request up to 3 times if it fails due to network issues.

---

### 102. Write a Python program that measures the response time of an API and logs it.

---

### 103. Build a tool that fetches weather or system data from an API and displays it in a formatted table.

---

### 104. Create a script that monitors an API endpoint and sends an alert if the response status is not 200.

---

## 🟠 DAY 15 — Multithreading (Parallel DevOps Tasks) (8 Challenges)

### 105. Write a Python program that runs multiple functions concurrently using threads and prints their execution order.

---

### 106. Create a script that downloads multiple files simultaneously using multithreading.

---

### 107. Write a program that compares execution time between single-threaded and multi-threaded approaches.

---

### 108. Build a log processing system where multiple threads process different parts of a log file in parallel.

---

### 109. Create a script that monitors multiple servers concurrently by pinging them in parallel threads.

---

### 110. Write a Python program that uses a thread pool to execute tasks efficiently.

---

### 111. Build a system that processes a queue of tasks using multiple worker threads.

---

### 112. Create a script that performs parallel API requests and aggregates the results.

---


## 🟠 DAY 16 — Multiprocessing (CPU-Level Parallelism) (8 Challenges)

### 113. Write a Python program that uses the multiprocessing module to execute multiple CPU-bound tasks (e.g., calculating factorials of large numbers) in parallel. Compare the execution time with a single-threaded version.

---

### 114. Create a script that processes a large log file by splitting it into chunks and using multiple processes to count the number of ERROR entries in parallel.

---

### 115. Write a Python program that uses a process pool to execute a list of tasks (e.g., computing squares of numbers) and collects the results efficiently.

---

### 116. Build a multiprocessing-based file search tool that searches for a keyword across multiple files simultaneously.

---

### 117. Create a program that processes multiple CSV files in parallel and calculates aggregated statistics from all files.

---

### 118. Write a script that demonstrates inter-process communication using queues, where one process produces data and another consumes it.

---

### 119. Build a system that spawns multiple processes to simulate concurrent users accessing a system and logs their activity.

---

### 120. Write a Python script that benchmarks the performance difference between threading and multiprocessing for CPU-intensive tasks.

---

## 🟠 DAY 17 — Decorators (Production-Level Code Patterns) (8 Challenges)

### 121. Write a Python decorator that measures and prints the execution time of any function it wraps.

---

### 122. Create a retry decorator that retries a function up to 3 times if it raises an exception, with a delay between retries.

---

### 123. Build a logging decorator that logs function name, arguments, and return values to a file.

---

### 124. Write a decorator that checks if a user is authorized before executing a function (simulate role-based access).

---

### 125. Create a decorator that caches the result of expensive function calls to improve performance.

---

### 126. Write a decorator that limits how many times a function can be called within a specific time window (basic rate limiting).

---

### 127. Build a decorator that validates input arguments of a function (e.g., ensuring numbers are positive).

---

### 128. Combine multiple decorators (e.g., logging + retry + timing) on a single function and demonstrate their execution order.

---

## 🟠 DAY 18 — Advanced File & Automation Tools (8 Challenges)

### 129. Write a Python script that scans a directory and identifies duplicate files based on file content (not just name).

---

### 130. Create a program that monitors a directory in real-time and logs file creation, deletion, and modification events.

---

### 131. Build a file organizer tool that moves files into folders based on their file type (e.g., images/, documents/, logs/).

---

### 132. Write a script that compresses old log files into archive files and deletes logs older than a specified number of days.

---

### 133. Create a backup system that creates timestamped backups of a directory.

---

### 134. Write a Python program that synchronizes two directories (like a mini rsync tool).

---

### 135. Build a tool that watches a configuration file and reloads settings automatically when the file changes.

---

### 136. Create a script that encrypts and decrypts files using a basic encryption method.

---

## 🔴 DAY 19 — SSH Automation (Real DevOps Work) (8 Challenges)

### 137. Write a Python script using an SSH library to connect to a remote server and execute a command.

---

### 138. Create a program that connects to multiple servers via SSH and runs the same command on all of them.

---

### 139. Build a tool that uploads a file to a remote server using secure file transfer.

---

### 140. Write a script that downloads log files from a remote server and stores them locally.

---

### 141. Create a Python program that checks disk usage on remote servers via SSH and reports the results.

---

### 142. Build an automation tool that deploys an application on a remote server by executing a sequence of commands.

---

### 143. Write a script that monitors a remote service and restarts it if it stops.

---

### 144. Create a program that securely reads SSH credentials from environment variables instead of hardcoding them.

---

## 🔴 DAY 20 — Git & Automation Workflows (8 Challenges)

### 145. Write a Python script that clones a remote Git repository to your local machine.

---

### 146. Create a program that detects changes in a repository and automatically commits them with a message.

---

### 147. Build a tool that pushes local changes to a remote repository after committing.

---

### 148. Write a script that checks the status of a Git repository and prints modified, added, and deleted files.

---

### 149. Create a program that switches branches automatically based on user input.

---

### 150. Build a script that pulls the latest changes from a remote repository and handles merge conflicts gracefully.

---

### 151. Write a Python tool that tags a release version in Git and pushes the tag to the remote repository.

---

### 152. Create a script that integrates Git automation into a CI-like workflow (e.g., commit → test → push).


---
