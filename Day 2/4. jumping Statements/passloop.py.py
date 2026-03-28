#Search for a number in a list#
numbers = [10, 20, 30, 40, 50]
search = int(input("Enter number to search: "))

for num in numbers:
    if num == search:
        print("Number found!")
        break
else:
    print("Number not found")