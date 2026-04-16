# Advanced Simulation System
import numpy as np
import pandas as pd
import random
import math

# OOP Class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 75:
            return "A"
        elif self.marks >= 50:
            return "B"
        else:
            return "Fail"

# Generate random marks
names = ["A", "B", "C", "D", "E"]
marks = np.array([random.randint(30, 100) for _ in names])

students = []

try:
    for i in range(len(names)):
        students.append(Student(names[i], marks[i]))

    # Convert to DataFrame
    df = pd.DataFrame({
        "Name": names,
        "Marks": marks,
        "Grade": [s.grade() for s in students]
    })

    print("Student Report:\n", df)

    # Statistics using math
    avg = sum(marks) / len(marks)
    print("Average Marks:", avg)

    # Save to file
    df.to_csv("report.csv", index=False)

except Exception as e:
    print("Error occurred:", e)