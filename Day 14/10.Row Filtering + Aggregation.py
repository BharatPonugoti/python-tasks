# Row Filtering + Aggregation
import numpy as np
import pandas as pd

arr = np.array([
    [100, 200],
    [150, 250],
    [80, 120],
    [300, 400]
])

# Convert to DataFrame
df = pd.DataFrame(arr, columns=["Sales", "Profit"])

print("Original DataFrame:")
print(df)

# Filter rows where Sales > 100
filtered_df = df[df["Sales"] > 100]

print("\nFiltered Data (Sales > 100):")
print(filtered_df)

# Average Profit of filtered rows
avg_profit = filtered_df["Profit"].mean()

print("\nAverage Profit (Filtered):", avg_profit)