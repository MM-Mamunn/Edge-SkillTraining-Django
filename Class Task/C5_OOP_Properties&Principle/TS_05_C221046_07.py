# Interface Segregation (ISP) (SOLID -> I)

# In vehicles, some are drivable and some are flyable, with a note that some are both.
# It is not logical for drive and fly to be contained in the same parent class, as shown in the following code.

# Not recommended
class Vehicle:
    def drive(self):
        pass

    def fly(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Driving on the road.")

    def fly(self):
        raise NotImplementedError("Cars can't fly.")

class Airplane(Vehicle):
    def fly(self):
        print("Flying in the sky.")

    def drive(self):
        raise NotImplementedError("Airplanes can't drive.")
    
# Therefore, it is logical to build separate parent classes.
# Some vehicles are drivable and some are flyable.
# This demonstrates the Interface Segregation Principle (ISP).
class Drivable:
    def drive(self):
        pass

class Flyable:
    def fly(self):
        pass

class Car(Drivable):
    def drive(self):
        print("Driving on the road.")

class Airplane(Flyable):
    def fly(self):
        print("Flying in the sky.")
