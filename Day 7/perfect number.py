#perfect number#
num = 6
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("6 is a Perfect number")
else:
    print("6 is not a Perfect number")