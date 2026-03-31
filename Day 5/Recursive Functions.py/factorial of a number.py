#Write a recursive function to find the nth Fibonacci number.#
def fibonacci(n):
    if n == 0:   # base case
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example
print(fibonacci(6))  # Output: 8