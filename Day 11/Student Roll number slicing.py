#4. Student Roll Numbers Extraction (Slicing)
import numpy as np

# Original list
roll_numbers = np.array([101, 102, 103, 104, 105, 106])

# Extract middle students (index 2 to 4)
middle_students = roll_numbers[2:5]

print("Middle students:", middle_students)