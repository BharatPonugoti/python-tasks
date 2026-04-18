# Combined Visualization Dashboard
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]

# 1. Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

# 2. Create subplots
plt.figure(figsize=(12, 4))

# Line graph (trend)
plt.subplot(1, 3, 1)
plt.plot(df["Product"], df["Sales"], marker='o')
plt.title("Sales Trend")

# Bar chart (comparison)
plt.subplot(1, 3, 2)
plt.bar(df["Product"], df["Sales"])
plt.title("Sales Comparison")

# Pie chart (distribution)
plt.subplot(1, 3, 3)
plt.pie(df["Sales"], labels=df["Product"], autopct='%1.1f%%')
plt.title("Sales Distribution")

# Adjust layout
plt.tight_layout()

# Show all plots
plt.show()