# Missing Data Handling (NumPy + Pandas)
import numpy as np
import pandas as pd

arr = np.array([10, np.nan, 30, np.nan, 50])

# Convert to Pandas Series
series = pd.Series(arr)

# Calculate mean (ignores NaN by default)
mean_value = series.mean()

# Replace NaN with mean
updated_series = series.fillna(mean_value)

print("Updated Series:")
print(updated_series)