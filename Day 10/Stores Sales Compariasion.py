# Stores Sales Compariasion
import numpy as np

# Sales data
store_a = [200, 250, 300]
store_b = [180, 270, 310]

# Convert to NumPy arrays
array_a = np.array(store_a)
array_b = np.array(store_b)

# Find daily difference (Store A - Store B)
difference = array_a - array_b

# Print result
print("Daily Sales Difference:", difference)