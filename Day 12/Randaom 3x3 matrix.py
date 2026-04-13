#Random 3×3 Matrix and Filter > 25
import numpy as np

matrix = np.random.randint(0, 51, (3, 3))

print("Matrix:\n", matrix)

filtered = matrix[matrix > 25]

print("Values Greater Than 25:", filtered)