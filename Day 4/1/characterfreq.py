#Remove duplicate characters#
s = input("Enter a string: ")
result = ""

for ch in s:
    if ch not in result:
        result += ch

print("Without duplicates:", result)