# Monthly Sales Analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# Create DataFrame
df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

print(df)

plt.figure()
plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.show()

plt.figure()
plt.bar(df["Month"], df["Sales"])
plt.title("Month-wise Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

plt.figure()
plt.pie(df["Sales"], labels=df["Month"], autopct='%1.1f%%')
plt.title("Sales Contribution by Month")
plt.show()

plt.figure()
plt.hist(df["Sales"], bins=5)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.scatter(range(len(df)), df["Sales"])
plt.title("Month Index vs Sales")
plt.xlabel("Index")
plt.ylabel("Sales")
plt.show()