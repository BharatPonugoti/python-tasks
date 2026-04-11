#Find Indexes of Specific Value
import numpy as np

# Defect codes
codes = np.array([2, 4, 1, 4, 3, 4, 5])

# Find indexes where value is 4
indexes = np.where(codes == 4)

print("Indexes of value 4:", indexes)