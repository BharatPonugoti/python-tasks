#Write a Python program using the random module to generate 10 random integers#
import random

numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 100))

print("Random Numbers:", numbers)