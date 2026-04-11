# Bank Transaction storage
import numpy as np
# Original list of transactions
transactions_list = [1200, 500, 800, 1500]
# Convert list to NumPy array
transactions_array = np.array(transactions_list)
# Print the type of the object
print("Type:", type(transactions_array))

# Verify that it is a NumPy ndarray
print("Is NumPy ndarray?", isinstance(transactions_array, np.ndarray))