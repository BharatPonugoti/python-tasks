# Two Sensor Readings
import numpy as np

# Sensor readings
sensor1 = [10, 20, 30]
sensor2 = [40, 50, 60]

# Convert to NumPy arrays
array1 = np.array(sensor1)
array2 = np.array(sensor2)

# Concatenate arrays
combined_array = np.concatenate((array1, array2))

# Print result
print("Combined Sensor Readings:", combined_array)