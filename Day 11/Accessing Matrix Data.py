#Accessing Matrix Data
import numpy as np

# Create 2D array (matrix)
marks = np.array([
    [78, 85],
    [90, 88],
    [67, 72]
])

# Access second student's second subject mark
value = marks[1, 1]

print("Second student's second subject mark:", value)