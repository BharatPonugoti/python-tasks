# Employee Management System (OOP + File + Dict)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        return f"{self.name}: {self.salary}"


employees = {}

n = int(input("Enter number of employees: "))

for _ in range(n):
    name = input("Enter name: ")
    
    try:
        salary = float(input("Enter salary: "))
        emp = Employee(name, salary)
        employees[name] = emp
    except ValueError:
        print("Invalid salary input!")

# Save to file
with open("employees.txt", "w") as f:
    for emp in employees.values():
        f.write(emp.display() + "\n")

# Display all employees
print("\nEmployee List:")
for emp in employees.values():
    print(emp.display())