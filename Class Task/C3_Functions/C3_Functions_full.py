# # Task1 : define a recursive funtion to calculate factorial
# # A recursive function must have a base case and the recursive call must have to shrink towards the base case

# # Define a recursive funtion named "fact" that accept a parameter as an argument
# # The  base case is n == 0
# def fact(num):
#     # Checking the base case
#     if not num:
#         return 1
#     #Calling the function itself to make necessary calculation
#     return num * fact(num - 1)

# #Take an integer inputs
# number = int(input("Insert an integer input: "))

# #Call the fact funtion and pass the taken input (number) and print it
# print(fact(number))


# Task 2 : Make a custom module ,import it and use it 
# Import the module to use
# import myCustomModule

# # Take input for celsius
# celsius = float(input("Enter temperature in Celsius: "))

# # Call the custom module to convert it to fareinheit
# fareinheit = myCustomModule.celsius_to_fahrenheit(celsius)

# print(f"The equivalent fahreinheit of celsius {celsius} is {fareinheit}")

# # Take input for radius of a circle
# radius = float(input("Enter Radius of a circle: "))
# # Call the custom module to calculate the area of the circle
# area = myCustomModule.calculate_circle_area(radius)

# print(f"The area of a circle with radius {radius} is {area}")

#Alternative - Recommended
# import the functions from the module
# from myCustomModule import calculate_circle_area, celsius_to_fahrenheit

# # Take input for celsius
# celsius = float(input("Enter temperature in Celsius: "))

# # Call the custom module to convert it to fareinheit
# fareinheit = celsius_to_fahrenheit(celsius)

# print(f"The equivalent fahreinheit of celsius {celsius} is {fareinheit}")

# # Take input for radius of a circle
# radius = float(input("Enter Radius of a circle: "))
# # Call the custom module to calculate the area of the circle
# area = calculate_circle_area(radius)

# print(f"The area of a circle with radius {radius} is {area}")

# Task 3-

# Define a funtion that accepts a list as parameter
# def work_in_list(num_list):
#     largest = lowest = num_list[0]  #set the default value of largest and lowest variable to the first element
#     sum = 0  # declaring variable to store the summation
#     for num in num_list: #iterate through the list 
#         sum += num       #Add the element to the sum 
#         #Greedily update the largest and lowest number
#         if( largest < num ):
#             largest = num
#         if(lowest > num):
#             lowest = num
#     average = sum/(len(num_list)) # calculate the average sum of the numbers
#     #Print the outputs
#     print(f"The largest number of the list is {largest}")
#     print(f"The lowest number of the list is {lowest}")
#     print(f"The average of the numbers of the list is {average}")

# #Declaring an empty list initially
# list_of_num =[]

# # Take input for the size of the list
# size = int(input("Enter the size of the list : "))
# # take input for the elements of the list and append elements to the list
# for i in range(size):
#     temp = int(input(f"Enter the {i + 1}th number: "))
#     list_of_num.append(temp)

# # Call the function and pass the list as parameter
# work_in_list(list_of_num)


# Task 4 -

# def sum_of_tuples(tup):
#     sum = 0
#     for i in tup:
#         sum += i
#     return sum

# def change_first_element(tup,num):
#     list = []
#     for i in tup:
#         list.append(i)
#     list[0] = num
#     tup = tuple(list)
#     return tup

# # taking a tuple 
# tup = (2, 3, 4, 5, 6)

# print(sum_of_tuples(tup))

# # change the first element of the tuple via 100
# tup = change_first_element(tup,100)
# print(tup)

# # Task 5
# # Declare two set
# set1 = {"Mamun","Seyam","Rayhan"}
# set2 = {"Rayhan","Rafi","Nahian"}

# union_set = set1 | set2
# intersection = set1 & set2
# diff = (set1 - set2) | (set2 - set1)
# print(f"The students in both sets are {intersection}")
# print(f"The students in one sets are {diff}")


# task 6
# def operations_on_dict(dict):
#     best = -100
#     worst = 102
#     loser = ""
#     topper = ""
#     Totall_score = 0
#     for key, value in dict.items():
#         Totall_score += value
#         if( best < value):
#             topper = key
#             best = value
#         if( worst > value):
#             worst = value
#             loser = key
#     print(f"Average score {Totall_score/len(dict)}")
#     print(f"Highest {topper}")
#     print(f"Lowest {loser}")

# score = {}
# score = dict()
# score["Mamun"] = 40
# score["Rayhan"] = 92
# score["Rafi"] = 95
# operations_on_dict(score)



# Task 7
# List by comprehensive funtions
# list = [ x  for x in  range(1,51) if x % 2 == 0]
# # multiply via lambda functions
# multiply = lambda lists : [ i * 3 for i in lists]
# print(multiply(list))