#Add an element to a set#
my_set = {1, 2, 3}
my_set.add(4)
print("After adding 4:", my_set)
#Remove an element from a set#
my_set = {1, 2, 3, 4}
my_set.remove(3)  # Raises error if element not present
# my_set.discard(3)  # Safer, does not raise error
print("After removing 3:", my_set)
