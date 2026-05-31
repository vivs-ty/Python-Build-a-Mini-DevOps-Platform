# Task 18: Calculate the sum of all numbers between two values, inclusive.

a = int(input("Enter first number: ").strip())
b = int(input("Enter second number: ").strip())

start = min(a, b)
end = max(a, b)
total_sum = 0
for i in range(start, end + 1):
    total_sum += i

print(f"Sum between {start} and {end} is: {total_sum}")

print(" \n Python 30 days Series - Day 3 Task 18 \n"                                             ) 
print(" \n Day 3: Loops \n"                    )
print(" \n Have a good one! \n "                          + "-"*40)
