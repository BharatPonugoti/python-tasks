#Employee Salary System (Simple Inheritance)#
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def display(self):
        print(self.name, self.salary)

m = Manager("John", 50000)
m.display()