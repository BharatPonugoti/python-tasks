# Data processing pipe line.
import numpy as np

# Given data
data = [12, 7, 25, 3, 18, 10]

# Step 1: Convert to NumPy array
data_array = np.array(data)

# Step 2: Sort the array
sorted_array = np.sort(data_array)

# Step 3: Split into two equal parts
split_arrays = np.array_split(sorted_array, 2)

# Step 4: Calculate sum of each part
sum_part1 = np.sum(split_arrays[0])
sum_part2 = np.sum(split_arrays[1])

# Print results
print("Sorted Array:", sorted_array)
print("First Half:", split_arrays[0])
print("Second Half:", split_arrays[1])
print("Sum of First Half:", sum_part1)
print("Sum of Second Half:", sum_part2)