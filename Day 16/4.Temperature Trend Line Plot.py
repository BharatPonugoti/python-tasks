# Temperature Trend Line Plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
temps = np.array([28, 30, 32, 31, 29])

# 1. Convert to Pandas Series
temp_series = pd.Series(temps)

# 2. Plot line graph
plt.plot(temp_series, marker='o')

# 3. Add title and grid
plt.title("Daily Temperature Trend")
plt.grid()

# Show plot
plt.show()