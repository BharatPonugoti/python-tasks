#prime number#
num = 7
flag = 0

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break

if flag == 0 and num > 1:
    print("Factors = 1,", num)
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")