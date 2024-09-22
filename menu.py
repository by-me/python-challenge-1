# Menu dictionary containing various categories and their items with prices
menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Initialize the order list to store customer orders with their quantity and price
order_list = []

# Welcome message
print("Welcome to the variety food truck.")

# A flag to keep the order loop running until the customer decides to stop
place_order = True

# Main loop to handle continuous ordering
while place_order:
    # Step 1: Ask the customer which menu category they would like to order from
    print("\nFrom which menu would you like to order?")

    # Print menu categories
    for i, category in enumerate(menu.keys(), 1):
        print(f"{i}: {category}")

    # Step 2: Prompt the customer to select a category by inputting a number
    menu_category = input("Type menu number: ")

    # Check if input is a digit and valid
    if menu_category.isdigit() and int(menu_category) in range(1, len(menu) + 1):
        # Retrieve the menu category name based on user input
        menu_category_name = list(menu.keys())[int(menu_category) - 1]
        print(f"You selected {menu_category_name}")

        # Print menu items for the selected category
        print("Item # | Item name                | Price")
        print("-------|--------------------------|-------")
        
        menu_items = {}
        i = 1

        for key, value in menu[menu_category_name].items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    print(f"{i:<7}| {key} - {sub_key:<24} | ${sub_value:.2f}")
                    menu_items[i] = {"Item name": f"{key} - {sub_key}", "Price": sub_value}
                    i += 1
            else:
                print(f"{i:<7}| {key:<24} | ${value:.2f}")
                menu_items[i] = {"Item name": key, "Price": value}
                i += 1

        # Step 4: Ask customer to input menu item number
        menu_selection = input("Please enter the item number you wish to order: ")

        # Step 5: Validate the menu selection input
        if menu_selection.isdigit() and int(menu_selection) in menu_items:
            menu_selection = int(menu_selection)
            item_name = menu_items[menu_selection]["Item name"]
            price = menu_items[menu_selection]["Price"]

            # Ask for quantity
            quantity = input(f"How many {item_name}s would you like?")

            # Validate quantity input + ensure that the quantity must be at least 1
            if quantity.isdigit() and int(quantity) >0:
                quantity = int(quantity)
            else:
                quantity = 1  # Default to 1 if invalid
                print("Invalid quantity. Please enter a valid number.")


            # Add to the order list
            order_list.append({"Item name": item_name, "Price": price, "Quantity": quantity})
            print(f"{quantity} x {item_name} added to your order.")

            # Step 6: Ask if the user wants to continue ordering
            while True:
                keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()
                if keep_ordering in ['y', 'yes']:
                    break
                elif keep_ordering in ['n', 'no']:
                    place_order = False
                    print("Thank you for your order.")
                    break
                else:
                    print("Invalid input, please enter Y or N.")
        else:
            print("Invalid menu selection.")
    else:
        print("Invalid menu category selection.")

# Print out the order receipt
print("\nThis is what we are preparing for you:\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# Step 7: Loop through the items in the customer's order
for order in order_list:
    item_name = order["Item name"]
    price = order["Price"]
    quantity = order["Quantity"]

    # Step 8: Calculate the number of spaces for formatted printing
    num_item_spaces = 26 - len(item_name)
    num_price_spaces = 8 - len(f"${price:.2f}")
    num_quantity_spaces = 10 - len(str(quantity))

    # Step 9: Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces
    quantity_spaces = " " * num_quantity_spaces

    # Step 10: Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${price:.2f}{price_spaces}| {quantity}{quantity_spaces}")

# Step 11: Calculate the total price of the order
total_price = sum(order["Price"] * order["Quantity"] for order in order_list)
print(f"\nTotal price: ${total_price:.2f}")
