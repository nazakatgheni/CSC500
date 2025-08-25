# STEP 4: Classes and required methods

#  ItemToPurchase 
class ItemToPurchase:
    def __init__(self, name="none", price=0, quantity=0, description="none"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    def item_cost(self):
        return self.price * self.quantity


#  ShoppingCart 
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Adds an item to cart_items
    def add_item(self, item):
        self.cart_items.append(item)

    # Removes an item by name
    def remove_item(self, item_name):
        for i, it in enumerate(self.cart_items):
            if it.name == item_name:
                self.cart_items.pop(i)
                return
        print("Item not found in cart. Nothing removed.")

    # Modifies an item (by name); only non-default fields are applied
    def modify_item(self, item):
        for it in self.cart_items:
            if it.name == item.name:
                if item.description != "none":
                    it.description = item.description
                if item.price != 0:
                    it.price = item.price
                if item.quantity != 0:
                    it.quantity = item.quantity
                return
        print("Item not found in cart. Nothing modified.")

    # Returns total quantity of items
    def get_num_items_in_cart(self):
        return sum(it.quantity for it in self.cart_items)

    # Returns total cost of cart
    def get_cost_of_cart(self):
        return sum(it.item_cost() for it in self.cart_items)

    #  STEP 6: Output shopping cart (print_total) 
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        total_items = self.get_num_items_in_cart()
        print(f"Number of Items: {total_items}")
        if total_items == 0:
            print("SHOPPING CART IS EMPTY")
            return
        for it in self.cart_items:
            print(f"{it.name} {it.quantity} @ ${it.price} = ${it.item_cost()}")
        print(f"Total: ${self.get_cost_of_cart()}")

    #  STEP 6: Output items' descriptions (print_descriptions) 
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for it in self.cart_items:
            print(f"{it.name}: {it.description}")


# STEP 5: Menu loop (print_menu) and driver

def print_menu(cart: ShoppingCart):
    MENU = (
        "MENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit"
    )

    choice = ""
    while choice != "q":
        print()
        print(MENU)
        choice = input("Choose an option: ").strip().lower()

        if choice == "a":
            print("\nADD ITEM TO CART")
            name = input("Enter the item name: ").strip()
            description = input("Enter the item description: ").strip()
            price = float(input("Enter the item price: ").strip())
            quantity = int(input("Enter the item quantity: ").strip())
            cart.add_item(ItemToPurchase(name, price, quantity, description))

        elif choice == "r":
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove: ").strip()
            cart.remove_item(name)

        elif choice == "c":
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name: ").strip()
            quantity = int(input("Enter the new quantity: ").strip())
            cart.modify_item(ItemToPurchase(name=name, quantity=quantity))

        elif choice == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()   # STEP 6 call

        elif choice == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()          # STEP 6 call

        elif choice == "q":
            pass  # Quit

        else:
            continue  # invalid → reprint menu


def main():
    customer_name = input("Enter customer's name: ").strip()
    current_date = input("Enter today's date: ").strip()
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}\n")

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


if __name__ == "__main__":
    main()
