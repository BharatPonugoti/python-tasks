#Employee Data Copy Issue (Shallow vs Deep Copy)
employees = [[101, "A"], [102, "B"], [103, "C"]]

# Shallow copy
shallow_copy = employees.copy()

# Modify nested element
employees[0][1] = "Z"

print("Original:", employees)
print("Shallow Copy:", shallow_copy)

# Fixing by Deep Copy 
import copy

employees = [[101, "A"], [102, "B"], [103, "C"]]

# Deep copy
deep_copy = copy.deepcopy(employees)

# Modify original
employees[0][1] = "Z"

print("Original:", employees)
print("Deep Copy:", deep_copy)