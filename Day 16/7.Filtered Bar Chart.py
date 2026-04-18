# Filtered Bar Chart
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

# 1. Convert to DataFrame
df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

# 2. Filter students with marks > 50
filtered_df = df[df["Marks"] > 50]

# 3. Plot bar chart
plt.bar(filtered_df["Name"], filtered_df["Marks"])

# Labels & title
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students with Marks > 50")

# Show plot
plt.show()