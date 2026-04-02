# strong number 145#
num = 145
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    
    # factorial calculation
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    
    sum += fact
    temp //= 10

if sum == num:
    print("145 is a Strong number")
else:
    print("145 is not a Strong number")