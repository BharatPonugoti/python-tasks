# Student Marks Analysis
import numpy as np
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [50, 65, 70],
    [90, 95, 85],
    [40, 55, 60]
])

totals = np.sum(marks, axis=1)
avg_total = np.mean(totals)

above_avg_students = np.where(totals > avg_total)

print("Totals:", totals)
print("Average Total:", avg_total)
print("Students above average (index):", above_avg_students)