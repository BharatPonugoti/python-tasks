# Student Performance Dashboard
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

# Create DataFrame
df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

print(df)

plt.figure()
plt.plot(df["Student"], df["Marks"], marker='o')
plt.title("Trend of Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid()
plt.show()

plt.figure()
plt.bar(df["Student"], df["Marks"])
plt.title("Student vs Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Pass > 50
pass_count = (df["Marks"] > 50).sum()
fail_count = (df["Marks"] <= 50).sum()

labels = ["Pass", "Fail"]
sizes = [pass_count, fail_count]

plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pass vs Fail Distribution")
plt.show()

plt.figure()
plt.scatter(range(len(df)), df["Marks"])
plt.title("Index vs Marks")
plt.xlabel("Index")
plt.ylabel("Marks")
plt.show()