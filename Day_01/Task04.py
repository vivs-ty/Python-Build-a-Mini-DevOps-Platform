# Task 4: Swap two user-provided variables without using a third variable.

first_var = input("Enter the first variable : ").strip()
second_var = input("Enter the second variable : ").strip()

print(f" \n You have entered : \n First Variable : {first_var} \n Second Variable : {second_var} \n This is before swapping the variables. \n")
print(f" \n Swapping the variables... \n")
first_var, second_var = second_var, first_var
print(f" \n After swapping the variables : \n First Variable : {first_var} \n Second Variable : {second_var} \n")
print(f" \n Python 30 days Series - Day 1 Task 4 \n")
print(f" \n Have a good one! ")
