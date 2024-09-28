# Task 05: Multiplication table of a given number and skip the multiple of 3

# Take input of an integer number
num = int(input("Enter an integer number: "))

# Iterate from 1 to 10 using a for loop and range()
for i in range(1, 11):
    #skip when i == 3
    if i == 3:
        continue
    print(f"{num} * {i} = {num * i}")
