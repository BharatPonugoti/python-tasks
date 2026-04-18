# Employee Salary Insights
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

# Create DataFrame
df = pd.DataFrame({
    "Department": departments,
    "Salary": salaries
})

print(df)

plt.figure()
plt.plot(range(len(df)), df["Salary"], marker='o')
plt.title("Salary Trend")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.grid()
plt.show()

dept_salary = df.groupby("Department")["Salary"].mean()

plt.figure()
plt.bar(dept_salary.index, dept_salary.values)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

dept_count = df["Department"].value_counts()

plt.figure()
plt.pie(dept_count.values, labels=dept_count.index, autopct='%1.1f%%')
plt.title("Employee Distribution by Department")
plt.show()

plt.figure()
plt.hist(df["Salary"], bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.scatter(range(len(df)), df["Salary"])
plt.title("Index vs Salary")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.show()