#Write a Python program that generates 20 random numbers between 1 and 200 using the random module and store them in a list. Then using the math module, compute and display: ● Maximum value ● Minimum value ● Square root of the maximum number ● Logarithm of the minimum number#
import random
import math

numbers = [random.randint(1, 200) for _ in range(20)]

max_val = max(numbers)
min_val = min(numbers)

print("Numbers:", numbers)
print("Maximum value:", max_val)
print("Minimum value:", min_val)
print("Square root of maximum:", math.sqrt(max_val))
print("Logarithm of minimum:", math.log(min_val))
