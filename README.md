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
