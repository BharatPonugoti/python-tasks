# Random Number Analyzer
import random

# Generate 10 random numbers
numbers = [random.randint(1, 20) for _ in range(10)]

print("Generated Numbers:", numbers)

even = 0
odd = 0

# Count even and odd
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even count:", even)
print("Odd count:", odd)

# Remove duplicates using set
unique_numbers = set(numbers)
print("Unique Numbers:", unique_numbers)