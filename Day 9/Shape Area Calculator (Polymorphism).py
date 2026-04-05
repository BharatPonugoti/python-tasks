#Shape Area Calculator (Polymorphism)#
class Circle:
    def area(self):
        print("Circle Area")

class Rectangle:
    def area(self):
        print("Rectangle Area")

class Triangle:
    def area(self):
        print("Triangle Area")

shapes = [Circle(), Rectangle(), Triangle()]

for s in shapes:
    s.area()