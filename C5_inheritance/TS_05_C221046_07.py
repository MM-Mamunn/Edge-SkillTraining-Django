# Interface segregations (ISP) ( SOLID -> I)

# in vehicle some are drivable and some are flyable, there is note that is both.
# So it is not logical that drive and fly contains in the same parent class like the following code 

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
    
# So it is logical to build spearate parent class
# Some vehicle are driveable and some are flyable
#  This is interface segregations (ISP)
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
