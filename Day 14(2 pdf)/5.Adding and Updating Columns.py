# Adding and Updating Columns
import pandas as pd

df = pd.DataFrame({
    "Price": [100, 200, 300]
})

# Add Discount (10%)
df["Discount"] = df["Price"] * 0.10

# Add Final Price
df["Final Price"] = df["Price"] - df["Discount"]

print("Updated DataFrame:")
print(df)