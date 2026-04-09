# Temperature monitoring system
import numpy as np

# Temperature data
day1 = [30, 32, 31]
day2 = [29, 33, 34]

# Create 2D NumPy array
temp_array = np.array([day1, day2])

# Print the array
print("Temperature Array:\n", temp_array)

# Find total temperature
total_temp = np.sum(temp_array)
print("Total Temperature:", total_temp)