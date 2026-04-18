# Expense Distribution pie Chart
import numpy as np
import matplotlib.pyplot as plt

# Data
expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]

# Create pie chart
plt.pie(expenses, labels=labels, autopct='%1.1f%%')

# Optional: Title
plt.title("Monthly Expense Distribution")

# Show chart
plt.show()