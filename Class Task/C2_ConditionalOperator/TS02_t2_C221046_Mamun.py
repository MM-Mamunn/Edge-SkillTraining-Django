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