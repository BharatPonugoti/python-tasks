# Grocery List#
# Grocery List Manager

# Open the file in write mode
with open("grocery.txt", "w") as file:
    print("Enter your grocery items (type 'done' to finish):")
    
    while True:
        item = input("Enter item: ")
        
        if item.lower() == "done":
            break
        
        file.write(item + "\n")

print("Grocery list saved to grocery.txt")