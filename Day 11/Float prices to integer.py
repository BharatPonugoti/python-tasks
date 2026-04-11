#. Convert Float Prices to Integer
import numpy as np

# Original float array
prices = np.array([10.5, 20.8, 15.3])

# Convert to integer
int_prices = prices.astype(int)

print("Converted prices:", int_prices)