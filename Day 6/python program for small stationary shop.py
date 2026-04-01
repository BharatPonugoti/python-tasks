#python program for small stationary shop#
# Dictionary: product name -> price
products = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5
}

# Set: product categories
categories = {"Stationery", "Office Supplies"}

# List: cart items (each item is a tuple: (product_name, quantity))
cart = []

# Function to display products
def display_products():
    print("Available Products:")
    for name, price in products.items():
        print(f"{name} : {price}")

# Function to add item to cart
def add_to_cart():
    try:
        name = input("Enter product name: ")

        # Raise NameError if product not found
        if name not in products:
            raise NameError

        qty = input("Enter quantity: ")

        # Convert quantity to int (may raise ValueError)
        qty = int(qty)

        # Store as tuple (product details)
        item = (name, qty)

        # Type check (simulate TypeError)
        if not isinstance(item, tuple):
            raise TypeError

        cart.append(item)
        print("Item added to cart successfully.")

    except ValueError:
        print("Invalid quantity! Please enter a number.")
    except NameError:
        print("Product not found in store.")
    except TypeError:
        print("Cart data type error.")

# Recursive function to calculate total
def calculate_total(cart_list, index=0):
    try:
        if index >= len(cart_list):
            return 0

        name, qty = cart_list[index]

        # Force a possible TypeError if wrong data exists
        if not isinstance(name, str) or not isinstance(qty, int):
            raise TypeError

        price = products[name]

        return (price * qty) + calculate_total(cart_list, index + 1)

    except TypeError:
        print("Cart data type error.")
        return 0
    except ZeroDivisionError:
        print("Calculation error: division by zero")
        return 0

# Function to view total bill
def view_bill():
    try:
        if not cart:
            print("Cart is empty.")
            return

        print("Items in Cart:")
        for name, qty in cart:
            print(f"{name} x {qty}")

        total = calculate_total(cart)

        # Artificial ZeroDivisionError check (for requirement)
        test = total / 1  # change to 0 to simulate error

        print(f"Total Bill: {total}")

    except ZeroDivisionError:
        print("Calculation error: division by zero")

# Main program loop
while True:
    print("\n1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        display_products()
    elif choice == '2':
        add_to_cart()
    elif choice == '3':
        view_bill()
    elif choice == '4':
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice. Please try again.")