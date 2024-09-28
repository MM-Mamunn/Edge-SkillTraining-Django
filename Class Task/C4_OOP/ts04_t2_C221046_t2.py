# Task 2 - modify a variable
# Declaring class named person that accepts two parameter name and age
class Person:
    def __init__(self,name,age): #constructor that assigns value
        self.name = name
        self.age = age
    def update_age(self,new_age): #update function that updates the age variable by the new variable parameter
        self.age = new_age
    def __str__(self): #returns class as string , to see better
        return f"{self.name} is {self.age} years old"

# Creating two objects of the class person
user1 = Person("Mamun",23)
user2 = Person("Rafi",24)

# Updating user1 age
user1.update_age(25)

print(user1)
print(user2)