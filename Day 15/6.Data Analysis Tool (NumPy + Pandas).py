# Data Analysis Tool (NumPy + Pandas)
import numpy as np
import pandas as pd

# Generate marks
marks = np.random.randint(30, 100, 10)

# Convert to DataFrame
df = pd.DataFrame({"Marks": marks})

# Filter passing students (>= 50)
passing = df[df["Marks"] >= 50]

# Calculate mean
mean_marks = np.mean(df["Marks"])

print("All Marks:\n", df)

print("\nPassing Students:")
for index, row in passing.iterrows():
    print(f"Student {index}: {row['Marks']}")

print("\nMean Marks:", mean_marks)