# Student Score Processor
import math

# List of tuples
data = [("A", 60), ("B", 45), ("C", 75), ("D", 30)]

# Convert to dictionary
students = dict(data)

# Find students scoring above 50
print("Students scoring above 50:")
total = 0
count = 0

for name, marks in students.items():
    total += marks
    count += 1
    if marks > 50:
        print(name, marks)

# Calculate average using math
average = total / count
print("Average Marks:", average)

# Store results in file
with open("students.txt", "w") as f:
    f.write(f"Average Marks: {average}\n")
    for name, marks in students.items():
        f.write(f"{name}: {marks}\n")