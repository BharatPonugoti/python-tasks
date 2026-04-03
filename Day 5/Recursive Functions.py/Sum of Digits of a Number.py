# Notes reader program #
# Open the file in read mode
file = open("notes.txt", "r")

# Read all contents of the file
content = file.read()

# Display the contents
print(content)

# Close the file
file.close()