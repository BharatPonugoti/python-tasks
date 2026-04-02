num = 153
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print("153 is an Armstrong number")
else:
    print("153 is not an Armstrong number")