# Task 29: Count the frequency of each list element and store the result in a dictionary.

input_list = input("Enter a list of elements separated by spaces: ").split()
frequency_dict = {}
for element in input_list:
    frequency_dict[element] = frequency_dict.get(element, 0) + 1
print(f"Frequency of each element: {frequency_dict}")
print(f" \n Python 30 days Series - Day 5 Task 29 \n")
print(f" \n Day 5: Lists, Sets, and Dictionaries \n")
print(f" \n Have a good one! \n")
