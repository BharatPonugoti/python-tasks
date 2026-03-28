#Count vowels using function#
def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

print("Vowels:", count_vowels("hello"))