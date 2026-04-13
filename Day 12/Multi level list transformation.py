#  Multi level list transformation
data = [[1, 2, 3], [4, 5], [6]]

# Flatten the list
flat = [num for sublist in data for num in sublist]

# Squares of only even numbers
result = [num**2 for num in flat if num % 2 == 0]

print("Flattened List:", flat)
print("Even Squares:", result)