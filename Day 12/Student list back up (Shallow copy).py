# Student list back up (Shallow copy)
marks = [50, 60, 70, 80]

# Assignment (not a real copy)
backup = marks

# Modify first element
marks[0] = 100

print("marks:", marks)
print("backup:", backup)