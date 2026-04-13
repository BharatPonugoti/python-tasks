#Random Dataset Normalization + Filtering
import numpy as np

# Generate 8 random float values between 0 and 1
data = np.random.rand(8)

print("Original Data:", data)

# Normalize (scale to 0–100)
normalized = data * 100

# Filter values greater than 50
filtered = normalized[normalized > 50]

# Sort filtered values
sorted_values = np.sort(filtered)

print("Normalized Data:", normalized)
print("Filtered (>50):", filtered)
print("Sorted Filtered Values:", sorted_values)