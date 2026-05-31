# Task 11: Check whether a year is a leap year.

year = int(input("Enter a Year: ").strip())
if ( year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0 ):
    print(f"Entered year {year} is a Leap Year")
else:
    print(f"Entered year {year} is not a Leap Year")

print(" \n Python 30 days Series - Day 2 Task 11 \n"                                             )
print(" \n Day 2: Conditional Logic \n"                                )
print(" \n Have a good one! \n "                          + "-"*40)
