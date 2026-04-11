#Copy vs View Behavior
import numpy as np

# Original array
data = np.array([10, 20, 30, 40])

# Create a copy
copy_data = data.copy()

# Modify original
data[0] = 99

print("Original array:", data)
print("Copied array:", copy_data)