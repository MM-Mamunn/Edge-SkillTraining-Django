# Task 3 - S of SOLID (of OOP)

# Create classes with single resposibility
class Fuel_Efficiency_Calculation:
    def __init__(self,miles,fuel):#Constructor to initialize variable
        self.miles =miles
        self.fuel =fuel
    def __str__(self):
        return f"{self.miles/self.fuel}"


class Car:
    def __init__(self,model):
        self.model = model
    def drive(self):
        print (f"{self.model} is being driven.")
    def __str__(self):
        return f"Car({self.model})"

# create object of the classes
car_object = Car("G class")
Effciency = Fuel_Efficiency_Calculation(100,3)

print(car_object)
print(Effciency)