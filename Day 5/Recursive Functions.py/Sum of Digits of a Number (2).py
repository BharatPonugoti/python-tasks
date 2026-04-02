#Write a recursive function to calculate the sum of digits of a number.#
#Example: Input = 123 → Output = 6#
def sum_of_digits(n):
    if n == 0:   # base case
        return 0
    return (n % 10) + sum_of_digits(n // 10)

# Example
print(sum_of_digits(123))  # Output: 6
