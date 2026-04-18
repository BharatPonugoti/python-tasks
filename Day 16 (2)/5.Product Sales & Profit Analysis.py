# Product Sales & Profit Analysis
import numpy as np
import pandas as pd
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({
    "Product": products,
    "Sales": sales,
    "Profit": profit
})

print(df)

import matplotlib.pyplot as plt 
plt.figure()
plt.plot(df["Product"], df["Sales"], marker='o')
plt.title("Sales Trend")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.grid()
plt.show()

plt.figure()
plt.bar(df["Product"], df["Sales"])
plt.title("Product vs Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

plt.figure()
plt.pie(df["Sales"], labels=df["Product"], autopct='%1.1f%%')
plt.title("Sales Contribution by Product")
plt.show()

plt.figure()
plt.hist(df["Profit"], bins=5)
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.scatter(df["Sales"], df["Profit"])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()
