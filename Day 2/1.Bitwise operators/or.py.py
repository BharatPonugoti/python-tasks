#Left Shift (<<) and Right Shift (>>)#
# Bitwise Shift Operations
num = int(input("Enter a number: "))
shift = int(input("Enter number of positions to shift: "))

left_shift = num << shift
right_shift = num >> shift

print("Left Shift result:", left_shift)
print("Right Shift result:", right_shift)
