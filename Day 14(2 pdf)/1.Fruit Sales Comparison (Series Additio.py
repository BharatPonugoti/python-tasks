# Fruit Sales Comparison (Series Addition)
import pandas as pd

S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"])
S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"])

# Add both series
total_series = S1 + S2
print("Combined Sales:")
print(total_series)

# Total sales of all fruits
total_sales = total_series.sum()
print("\nTotal Sales:", total_sales)
