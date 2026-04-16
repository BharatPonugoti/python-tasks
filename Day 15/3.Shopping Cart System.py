# Shopping Cart System
cart = []
prices = {"apple": 10, "banana": 5, "milk": 20}

# Add items
n = int(input("Enter number of items: "))

for _ in range(n):
    item = input("Enter item name: ")
    cart.append(item)

# Remove duplicates
unique_cart = set(cart)
print("Unique Items:", unique_cart)

# Calculate total cost
total = 0

for item in unique_cart:
    try:
        total += prices[item]
    except KeyError:
        print(f"Invalid item: {item}")

print("Total Cost:", total)