#Find the largest and smallest element#
numbers = [10, 5, 30, 2, 50]

largest = max(numbers)
smallest = min(numbers)

print("Largest:", largest)
print("Smallest:", smallest)
#Reverse a list#
numbers = [10, 20, 30, 40, 50]

numbers.reverse()
print(numbers)
#Remove duplicate elements#
numbers = [10, 20, 20, 30, 40, 40, 50]

unique_numbers = list(set(numbers))
print(unique_numbers)