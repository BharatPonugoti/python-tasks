#Write a recursive function to reverse a string.#
def reverse_string(s):
    if len(s) == 0:   # base case
        return s
    return reverse_string(s[1:]) + s[0]

# Example
print(reverse_string("hello"))  # Output: "olleh"