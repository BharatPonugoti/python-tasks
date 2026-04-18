# Monthly Sales Line Graph
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# داده (Data)
sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]

# 1. Convert to DataFrame
df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

# 2. Plot line graph
plt.plot(df["Month"], df["Sales"], marker='o')

# 3. Label axes
plt.xlabel("Months")
plt.ylabel("Sales")

# Optional: Title
plt.title("Monthly Sales")

# Show graph
plt.show()