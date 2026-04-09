# Multi department data aggregation
import numpy as np

# Branch data
branch_a = np.array([[10, 20],
                     [30, 40]])

branch_b = np.array([[5, 15],
                     [25, 35]])

# Combine matrices (element-wise addition)
combined_matrix = branch_a + branch_b

# Calculate total employees
total_employees = np.sum(combined_matrix)

# Print results
print("Combined Matrix:\n", combined_matrix)
print("Total Employees:", total_employees)
