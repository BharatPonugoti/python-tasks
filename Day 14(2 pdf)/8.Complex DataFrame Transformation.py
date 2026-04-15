# Complex DataFrame Transformation
import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [50, 80, 30, 90]
})

# 1. Create Status column
df["Status"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

print("Data with Status:")
print(df)

# 2. Filter passed students
passed_df = df[df["Status"] == "Pass"]

print("\nPassed Students:")
print(passed_df)

# 3. Average marks of passed students
avg_marks = passed_df["Marks"].mean()

print("\nAverage Marks (Passed Students):", avg_marks)