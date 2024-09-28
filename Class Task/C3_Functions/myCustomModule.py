# import math library to use PI
import math

# Module for coverting celsius to fahreinheit,That accept a celcius variable and returns the equivalent fahreinheit
def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32  # Converts Celsius to Fahrenheit by formula
  return fahrenheit

# Module for calculating area,That accepts a radius and returns the area of the circle
def calculate_circle_area(radius):
  area = math.pi * radius * radius  # Calculates the area of a circle given its radius
  return area