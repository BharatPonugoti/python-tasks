#Remove duplicate values from a list using a set#
my_list = [1, 2, 2, 3, 4, 4, 5]

unique_list = list(set(my_list))
print("List after removing duplicates:", unique_list)