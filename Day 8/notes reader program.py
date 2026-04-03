#notes reader program#
# Notes Reader Program

try:
    # Open the file in read mode
    with open("notes.txt", "r") as file:
        content = file.read()
        print("Contents of notes.txt:\n")
        print(content)

except FileNotFoundError:
    print("Error: notes.txt file not found.")