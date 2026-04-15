# Accessing Specific Data (Indexing)
import pandas as pd

S = pd.Series([100, 200, 300, 400], index=["A", "B", "C", "D"])

# Access B and D
subset = S[["B", "D"]]

print("Subset (B and D):")
print(subset)