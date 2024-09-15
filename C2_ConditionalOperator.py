# Task - 2 : Check marks and output the grade according to the marks

#Take a number input for the marks
marks = float(input("Enter Marks: "))

#check the marks is valid or not
if 0 <= marks <= 100:
    #Check weather pass or fail
    
    #pass 
    if marks >= 50:
        if marks <= 59:
            print("Grade: C")
        elif marks <= 69:
            print("Grade: B")
        else :
            print("Grade: A")
    #fail
    else :
        print("Fail")
#wrong input
else:
    print("Wrong Input.Input is out of range (0 - 100)")

#Task 03 : print first 10 natural numbers

#iterate from 0 to 10 via for loop using range function
for i in range(1,11):
    print(i)

# Task 04: Multiplication table of a given number

# Take input of an integer number
num = int(input("Enter an integer number: "))

# Iterate from 1 to 10 using a for loop and range()
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")


# Task 05: Multiplication table of a given number and skip the multiple of 3

# Take input of an integer number
num = int(input("Enter an integer number: "))

# Iterate from 1 to 10 using a for loop and range()
for i in range(1, 11):
    #skip when i == 3
    if i == 3:
        continue
    print(f"{num} * {i} = {num * i}")
