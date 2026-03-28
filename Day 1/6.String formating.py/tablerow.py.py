#Print a table row#
name = input("Enter name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

print(f"{'Name':<10} {'Age':<5} {'Marks':<10}")
print(f"{name:<10} {age:<5} {marks:<10.2f}")