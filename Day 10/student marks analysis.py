#Student Marks Analysis
import numpy as np

# Given marks
marks_list = [45, 67, 89, 56, 72]

# Convert list to NumPy array
marks_array = np.array(marks_list)

# Add 5 grace marks to each student
updated_marks = marks_array + 5

# Print updated marks
print("Updated Marks:", updated_marks)