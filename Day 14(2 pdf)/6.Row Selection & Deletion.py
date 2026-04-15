# Row Selection & Deletion
import pandas as pd

df = pd.DataFrame({
    "A": [10, 20, 30],
    "B": [5, 15, 25]
}, index=["x", "y", "z"])

# Select row with index "y"
row_y = df.loc["y"]
print("Row y:")
print(row_y)

# Delete row "x"
df = df.drop("x")

print("\nUpdated DataFrame:")
print(df)