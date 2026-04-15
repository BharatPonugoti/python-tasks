# Combine NumPy Arrays into DataFrame
import numpy as np
import pandas as pd

names = np.array(["A", "B", "C"])
marks = np.array([80, 90, 70])

# Create DataFrame
df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

print("Original DataFrame:")
print(df)

# Filter students with marks > 75
filtered_df = df[df["Marks"] > 75]

print("\nStudents with Marks > 75:")
print(filtered_df)