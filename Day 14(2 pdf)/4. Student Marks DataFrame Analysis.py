# Student Marks DataFrame Analysis
import pandas as pd

data = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Math": [80, 70, 60],
    "Science": [90, 60, 70]
})

# Add Total column
data["Total"] = data["Math"] + data["Science"]

print("Data with Total:")
print(data)

# Find student with highest total
top_student = data.loc[data["Total"].idxmax()]

print("\nTop Student:")
print(top_student)
