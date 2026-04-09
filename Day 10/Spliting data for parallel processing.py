# Splitinf data for parallel processing
import numpy as np

# Given data
data = [5, 10, 15, 20, 25, 30]

# Convert to NumPy array
data_array = np.array(data)

# Split into 3 equal parts
split_data = np.array_split(data_array, 3)

# Print result
print("Split Data:")
for i, part in enumerate(split_data):
    print(f"Part {i+1}:", part)