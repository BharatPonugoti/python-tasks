# Data Cleaning + Visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = np.array([100, np.nan, 200, 150, np.nan, 300])

# 1. Convert to Pandas Series
series = pd.Series(data)

# 2. Replace NaN with mean
mean_value = series.mean()
cleaned_series = series.fillna(mean_value)

# 3. Plot graphs

# Line graph of cleaned data
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(cleaned_series, marker='o')
plt.title("Cleaned Data (Line Graph)")

# Bar chart of values > average
filtered = cleaned_series[cleaned_series > mean_value]

plt.subplot(1, 2, 2)
plt.bar(filtered.index.astype(str), filtered.values)
plt.title("Values Above Average")

plt.tight_layout()
plt.show()