# Base class representing a generic Vehicle
class Vehicle:
    def __init__(self, model, year, wheels):
        self.model = model  # Model of the vehicle
        self.year = year    # Year of manufacture
        self.wheels = wheels  # Number of wheels

    def display_info(self):
        # Display vehicle information
        print(f"Model: {self.model}, Year: {self.year}, Wheels: {self.wheels}")
    
# Class representing a Car, inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, model, year, doors):
        super().__init__(model, year, wheels=4)  # Cars typically have 4 wheels
        self.doors = doors  # Number of doors in the car

    def special_property(self):
        # Display specific information about the car
        print(f"This is a Car object and the number of doors are {self.doors}")

# Class representing a Bike, inheriting from Vehicle
class Bike(Vehicle):
    def __init__(self, model, year, cornering_angle):
        super().__init__(model, year, wheels=2)  # Bikes typically have 2 wheels
        self.cornering_angle = cornering_angle  # Angle for cornering

    def special_property(self):
        # Display specific information about the bike
        print(f"This is a Bike object and the cornering angle is {self.cornering_angle}")
        
# Creating instances of Vehicle, Car, and Bike
vehicle = Vehicle("C2134", 2020, 8)  # A generic vehicle
car = Car("C12341", "2303", 4)       # A car with 4 doors
bike = Bike("B12341", "2400", 30.06)     # A bike with a cornering angle

# Displaying information about the instances
vehicle.display_info()  # Display info for the generic vehicle
car.special_property()   # Display special property for the car
car.display_info()       # Display info for the car
bike.special_property()  # Display special property for the bike
