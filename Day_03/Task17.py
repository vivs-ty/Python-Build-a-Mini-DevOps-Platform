#  Task 17: Count the number of digits in an integer.

n = int(input("Enter an integer: ").strip())
number = abs(n)
digit_count = 1 if number == 0 else 0
while number > 0:
    digit_count += 1
    number //= 10

print(f"Number of digits in {n} is: {digit_count}")

print(" \n Python 30 days Series - Day 3 Task 17 \n"                                             )
print(" \n Day 3: Loops \n"                    )
print(" \n Have a good one! \n "                          + "-"*40)
