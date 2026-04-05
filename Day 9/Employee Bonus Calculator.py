#Employee Bonus Calculator (Decorators & OOP)#
def bonus(func):
    def wrapper(self):
        self.salary = self.salary + (0.1 * self.salary)
        func(self)
    return wrapper

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @bonus
    def display(self):
        print(self.name, self.salary)

e = Employee("Bharat", 70000)
e.display()