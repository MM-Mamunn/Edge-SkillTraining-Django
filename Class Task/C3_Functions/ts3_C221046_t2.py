
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

# Alternative - Recommended
# import the functions from the module
from myCustomModule import calculate_circle_area, celsius_to_fahrenheit

# Take input for celsius
celsius = float(input("Enter temperature in Celsius: "))

# Call the custom module to convert it to fareinheit
fareinheit = celsius_to_fahrenheit(celsius)

print(f"The equivalent fahreinheit of celsius {celsius} is {fareinheit}")

# Take input for radius of a circle
radius = float(input("Enter Radius of a circle: "))
# Call the custom module to calculate the area of the circle
area = calculate_circle_area(radius)

print(f"The area of a circle with radius {radius} is {area}")
