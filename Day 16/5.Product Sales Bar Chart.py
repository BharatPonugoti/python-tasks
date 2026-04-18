# Product Sales Bar Chart
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])

# 1. Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

# 2. Plot bar chart
plt.bar(df["Product"], df["Sales"])

# 3. Add labels and title
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales Chart")

# Show plot
plt.show()