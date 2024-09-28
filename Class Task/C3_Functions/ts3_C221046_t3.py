
# Task 3-

# Define a funtion that accepts a list as parameter
def work_in_list(num_list):
    largest = lowest = num_list[0]  #set the default value of largest and lowest variable to the first element
    sum = 0  # declaring variable to store the summation
    for num in num_list: #iterate through the list 
        sum += num       #Add the element to the sum 
        #Greedily update the largest and lowest number
        if( largest < num ):
            largest = num
        if(lowest > num):
            lowest = num
    average = sum/(len(num_list)) # calculate the average sum of the numbers
    #Print the outputs
    print(f"The largest number of the list is {largest}")
    print(f"The lowest number of the list is {lowest}")
    print(f"The average of the numbers of the list is {average}")

#Declaring an empty list initially
list_of_num =[]

# Take input for the size of the list
size = int(input("Enter the size of the list : "))
# take input for the elements of the list and append elements to the list
for i in range(size):
    temp = int(input(f"Enter the {i + 1}th number: "))
    list_of_num.append(temp)

# Call the function and pass the list as parameter
work_in_list(list_of_num)
