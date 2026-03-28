#Sum of list elements (user-defined function)#
def list_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total

print("Sum:", list_sum([1, 2, 3, 4]))