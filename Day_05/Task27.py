# Task 27: Sort a list in ascending order without using sort().

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    # List comprehensions make this incredibly readable
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

input_list = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print(f"Sorted list: {quicksort(input_list)}")
print(f" \n Python 30 days Series - Day 5 Task 27 \n")
print(f" \n Day 5: Lists, Sets, and Dictionaries \n")
print(f" \n Have a good one! \n")
