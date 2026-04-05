#Infinite Even Number Generator (Generators)#
def even_generator():
    num = 2
    while True:
        yield num
        num += 2

n = int(input("Enter N: "))
gen = even_generator()

for i in range(n):
    print(next(gen))