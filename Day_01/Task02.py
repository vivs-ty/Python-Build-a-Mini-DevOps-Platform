# Task 2: Ask the user for their name and current role, then print a formatted greeting.

name = input("What is your Name ? ").strip().title()
com = input("What is your organization name ? ").strip().upper()
dom = input("What is your domain ?").strip().upper()
rol = input("What is your role ? ").strip()
des = input("What is your designation ? ").strip()            

article = "an" if rol[0].lower() in "aeiou" else "a"

print(f" \n Hello {name}, \n Nice to meet you in person!")
print(f" \n I see you are working in {com}, Company and you are in {dom}, domain. \n ")
print(f" \n Your are working at {des} level in {article} {rol} role. \n")
print(f" \n Welcome to the World of DevOps Engineers! \n")
print(f" \n Python 30 days Series - Day 1 Task 2 \n")
print(f" \n Day 1: Input, Output, and Variables \n")
print(f" \n Have a good one! " + "-"*40)
