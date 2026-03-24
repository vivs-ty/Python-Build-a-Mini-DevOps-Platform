# Task 9: Find the largest of three numbers without using `max()`.

number_1 = int(input("Enter First Number coming in your mind: ").strip())
number_2 = int(input("Enter Second Number coming in your mind: ").strip())
number_3 = int(input("Enter Third Number coming in your mind: ").strip())
if number_1 >= number_2 and number_1 >= number_3:
    print(f"Entered number {number_1} is the largest")
elif number_2 >= number_1 and number_2 >= number_3:
    print(f"Entered number {number_2} is the largest")
else:
    print(f"Entered number {number_3} is the largest")

print(f" \n Python 30 days Series - Day 2 Task 9 \n")
print(f" \n Have a good one! ")
