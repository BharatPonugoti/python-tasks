# Data Alignment Issue in Series Addition
import pandas as pd

S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])

# Add both Series
result = S1 + S2
print("Result with NaN:")
print(result)