#Random Number Generator (Generators)#
def number_generator(n):
    for i in range(1, n + 1):
        yield i

n = int(input("Enter N: "))
for num in number_generator(n):
    print(num)