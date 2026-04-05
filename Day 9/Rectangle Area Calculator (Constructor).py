#Rectangle Area Calculator (Constructor)#
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)

r = Rectangle(5, 3)
r.area()