# Student Marks Bar Chart
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])

# 1. Create DataFrame
df = pd.DataFrame({
    "Student": names,
    "Marks": marks
})

# 2. Plot bar graph
plt.bar(df["Student"], df["Marks"])

# 3. Label axes
plt.xlabel("Students")
plt.ylabel("Marks")

# Optional: Title
plt.title("Student Marks Bar Chart")

# Show graph
plt.show()