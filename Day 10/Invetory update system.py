# Invetory update system
import numpy as np

# Inventory matrix
inventory = np.array([[10, 15],
                      [20, 25]])

# Add 2 to every element
updated_inventory = inventory + 2

# Print updated inventory
print("Updated Inventory:\n", updated_inventory)