#Import random file to use the functions necessary to generate a random number
import random

#Generate a random integer number between 1 to 100
random_number = random.randint(1, 100)

#Success flag
success = False

#Iterate through 1 to 7 via for loop to simulate the 7 attempth
for i in range(1, 8):
    print("Attempt number :",i);
    #Take the integer input
    chose = int(input(f"Enter an integer : "))
    
    #Check weather the taken  integer is in range(1 - 100) or not
    if  chose > 100 or chose < 1:
        #Chosen number is out of range
        print("You have chosen a number out of the range (1 - 100)")
        #Continue to next iteration as the input is out of range
        continue

    #This is a valid input as we have skip the continue statement
    #Check the chosen number match with the desired number or not
    if(chose == random_number):
        print("Success!! You've guessed the correct number")
        #Success flag set to true that indicates success and break the loop as the answer in found
        success = True
        break;
    else :
        #The chosen number is not matched, Suggestion is given 
        if chose > random_number:
            print("You have chosen a too high number")
        else :
            print("You have chosen a too low number")

#If success flag is false it indicates the program did not encountred  a success, thus it is a fail and show the correct number
if success == False:
    print("Fail!The correct number is ",random_number)