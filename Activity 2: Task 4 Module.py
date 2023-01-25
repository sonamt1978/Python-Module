class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Square:
    def __init__(self, sides):
        self.sides = sides
    def area(self):
        return self.sides **2
