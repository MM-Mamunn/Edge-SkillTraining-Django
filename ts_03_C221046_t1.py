# define a recursive funtion to calculate factorial
# A recursive function must have a base case and the recursive call must have to shrink towards the base case

# Define a recursive funtion named "fact" that accept a parameter as an argument
# The  base case is n == 0
def fact(num):
    # Checking the base case
    if not num:
        return 1
    #Calling the function itself to make necessary calculation
    return num * fact(num - 1)

#Take an integer inputs
number = int(input("Insert an integer input: "))

#Call the fact funtion and pass the taken input (number) and print it
print(fact(number))