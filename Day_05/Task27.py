# Task 27: Sort a list in ascending order without using sort().

input_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
for i in range(len(input_list)):
    for j in range(0, len(input_list) - i - 1):
        if input_list[j] > input_list[j + 1]:
            input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]

print(f"Sorted list: {input_list}")
print(f" \n Python 30 days Series - Day 5 Task 27 \n")
print(f" \n Day 5: Lists, Sets, and Dictionaries \n")
print(f" \n Have a good one! \n")
