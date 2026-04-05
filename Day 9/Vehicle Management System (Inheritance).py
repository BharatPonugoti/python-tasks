#Vehicle Management System (Inheritance)#
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class Car(Vehicle):
    def display(self):
        print("Car:", self.brand, self.speed)

class Bike(Vehicle):
    def display(self):
        print("Bike:", self.brand, self.speed)

c = Car("Toyota", 120)
b = Bike("Yamaha", 100)

c.display()
b.display()