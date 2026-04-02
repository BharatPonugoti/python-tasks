#palindrome number#
num = 121
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if reverse == num:
    print("121 is a Palindrome number")
else:
    print("121 is not a Palindrome number")