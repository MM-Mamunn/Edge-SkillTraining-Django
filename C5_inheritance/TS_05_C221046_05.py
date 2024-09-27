# open close principle - open to extend , close for modification
# raise defines that each child of parent (Shape) must have the "area" method define,otherwise will show an error

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement this method.")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
# Now you want to add a new shape of square , you can extend the shape

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
square = Square(5)
print(square.area())

# if you dont implement area() in child it will show an error as the parent method contains the template to raise an error if its not implemented