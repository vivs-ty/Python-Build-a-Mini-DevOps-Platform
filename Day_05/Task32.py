# Task 32: Find the union and intersection of two sets.

set1 = set(input("Enter first set of elements: ").split())
set2 = set(input("Enter second set of elements: ").split())

# The Pythonic Set Operators:
union = set1 | set2          # Equivalent to set1.union(set2)
intersection = set1 & set2   # Equivalent to set1.intersection(set2)
difference = set1 - set2     # Elements in set1 but not set2
sym_diff = set1 ^ set2       # Elements in either set, but not both

print(f"Union (Merged without duplicates): {list(union)}")
print(f"Intersection: {list(intersection)}")
print(f" \n Python 30 days Series - Day 5 Task 32 \n")
print(f" \n Day 5: Lists, Sets, and Dictionaries \n")
print(f" \n Have a good one! \n")
