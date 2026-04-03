#Employee Salary Management#
highest_salary = 0
highest_employee = ""
try:
    with open("employees.txt", "r") as file:
        print("Employee Details:\n")
        
        for line in file:
            name, salary = line.split()
            salary = int(salary)
            
            print(f"Name: {name}, Salary: {salary}")
            
            # Check for highest salary
            if salary > highest_salary:
                highest_salary = salary
                highest_employee = name

    # Display highest salary employee
    if highest_employee:
        print(f"\nHighest Salary: {highest_salary} (Employee: {highest_employee})")
    else:
        print("\nNo employee records found.")

except FileNotFoundError:
    print("Error: employees.txt file not found.")

# Append a new employee record
print("\nAdd a new employee record:")

name = input("Enter employee name: ")
salary = input("Enter employee salary: ")

with open("employees.txt", "a") as file:
    file.write(name + " " + salary + "\n")

print("New employee record added successfully.")