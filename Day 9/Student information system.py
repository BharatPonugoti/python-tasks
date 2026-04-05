#Student Information System (Class & Object)#
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(self.name, self.roll, self.marks)

s1 = Student("A", 1, 85)
s2 = Student("B", 2, 90)
s3 = Student("C", 3, 78)

s1.display()
s2.display()
s3.display()