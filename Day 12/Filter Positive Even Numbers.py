# Filter Positive Even Numbers
import numpy as np

arr = np.array([-5, 10, 15, -2, 20, 25, 30])

result = arr[(arr > 0) & (arr % 2 == 0)]

print("Filtered (Positive Even Numbers):", result)