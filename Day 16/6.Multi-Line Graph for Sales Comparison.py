# Multi-Line Graph for Sales Comparison
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Month": ["Jan", "Feb", "Mar"],
    "Store_A": [100, 150, 200],
    "Store_B": [90, 140, 210]
}

# 1. Create DataFrame
df = pd.DataFrame(data)

# 2. Plot multiple lines
plt.plot(df["Month"], df["Store_A"], marker='o', label="Store A")
plt.plot(df["Month"], df["Store_B"], marker='o', label="Store B")

# 3. Add legend
plt.legend()

# Optional labels and title
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales Comparison Between Stores")

# Show plot
plt.show()