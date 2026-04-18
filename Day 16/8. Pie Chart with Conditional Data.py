# Pie Chart with Conditional Data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
scores = np.array([40, 60, 80, 30, 90])

# 1. Categorize using Pandas
df = pd.DataFrame({"Scores": scores})
df["Result"] = df["Scores"].apply(lambda x: "Pass" if x > 50 else "Fail")

# 2. Count categories
counts = df["Result"].value_counts()

# 3. Plot pie chart
plt.pie(counts, labels=counts.index, autopct='%1.1f%%')

# Title
plt.title("Pass vs Fail Distribution")

# Show plot
plt.show()