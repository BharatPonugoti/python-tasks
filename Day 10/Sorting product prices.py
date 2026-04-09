# Sorting product prices
import numpy as np

# Given prices
prices_list = [499, 299, 799, 199, 599]

# Convert to NumPy array
prices_array = np.array(prices_list)

# Sort prices in ascending order
sorted_prices = np.sort(prices_array)

# Print sorted prices
print("Sorted Prices:", sorted_prices)