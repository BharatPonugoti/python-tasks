# Filter Values Using Condition
import numpy as np
import pandas as pd

arr = np.array([10, 25, 30, 15, 40])

# Convert to Series
s = pd.Series(arr)

# Filter values > 20
filtered = s[s > 20]

print("Filtered values:\n", filtered)