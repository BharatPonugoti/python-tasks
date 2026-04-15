# Student Marks Analysis (NumPy → Pandas)
import numpy as np
import pandas as pd

arr = np.array([
    [80, 90],
    [70, 60],
    [85, 95]
])

# Convert to DataFrame
df = pd.DataFrame(arr, columns=["Math", "Science"])

# Add Total column
df["Total"] = df["Math"] + df["Science"]

# Find student with highest total
top_student = df.loc[df["Total"].idxmax()]

print("DataFrame:\n", df)
print("\nTop student:\n", top_student)