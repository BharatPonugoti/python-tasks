# Notes Reader Program #
# Step 1: Open the file in read mode
try:
    with open("notes.txt", "r") as file:
        # Step 2: Read all contents
        contents = file.read()
        
        # Step 3: Display contents
        print("Your Notes:")
        print(contents)
except FileNotFoundError:
    print("The file notes.txt does not exist.")