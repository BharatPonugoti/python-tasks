#Convert a tuple to a list and modify the element#
my_tuple = (10, 20, 30)

# Convert to list
my_list = list(my_tuple)

# Modify element
my_list[1] = 99

# Convert back to tuple (optional)
my_tuple = tuple(my_list)

print("Modified tuple:", my_tuple)