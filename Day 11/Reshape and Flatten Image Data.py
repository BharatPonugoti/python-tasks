#Reshape and Flatten Image Data
import numpy as np

# Example image data (2D)
image = np.array([[1, 2, 3],
                  [4, 5, 6]])

# Reshape (e.g., to 3x2)
reshaped_image = image.reshape(3, 2)

# Flatten to 1D
flattened_image = image.flatten()

print("Original:\n", image)
print("Reshaped:\n", reshaped_image)
print("Flattened:", flattened_image)