# Task 7
# List by comprehensive funtions
list = [ x  for x in  range(1,51) if x % 2 == 0]
# multiply via lambda functions
multiply = lambda lists : [ i * 3 for i in lists]
print(multiply(list))