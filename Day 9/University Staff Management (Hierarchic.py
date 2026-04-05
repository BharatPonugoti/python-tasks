#University Staff Management (Hierarchical Inheritance)#
class Staff:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Professor(Staff):
    def show(self):
        print("Professor:", self.name, self.id)

class LabAssistant(Staff):
    def show(self):
        print("LabAssistant:", self.name, self.id)

class Administrator(Staff):
    def show(self):
        print("Administrator:", self.name, self.id)

p = Professor("Ravi", 1)
l = LabAssistant("Sita", 2)
a = Administrator("Kiran", 3)

p.show()
l.show()
a.show()