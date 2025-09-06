# Online Shopping Cart - Combined Milestone 1 & 2 + Final Steps (7–10)

from dataclasses import dataclass, field
from typing import List


def _fmt_money(value: float) -> str:
    if float(value).is_integer():
        return f"${int(value)}"
    return f"${value:.2f}"


#  Step 1: ItemToPurchase 
@dataclass
class ItemToPurchase:
    item_name: str = "none"
    item_price: float = 0.0
    item_quantity: int = 0
    item_description: str = "none"

    def print_item_cost(self) -> None:
        # Example: Bottled Water 10 @ $1 = $10
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ {_fmt_money(self.item_price)} = {_fmt_money(total)}")

    def print_item_description(self) -> None:
        # Example: Nike Romaleos: Volt color, Weightlifting shoes
        print(f"{self.item_name}: {self.item_description}")


#  Step 4: ShoppingCart 
@dataclass
class ShoppingCart:
    customer_name: str = "none"
    current_date: str = "January 1, 2020"
    cart_items: List[ItemToPurchase] = field(default_factory=list)

    def add_item(self, item: ItemToPurchase) -> None:
        self.cart_items.append(item)

    def remove_item(self, item_name: str) -> None:
        # --- case-insensitive match ---
        target = item_name.strip().lower()
        for i, it in enumerate(self.cart_items):
            if it.item_name.strip().lower() == target:
                self.cart_items.pop(i)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item: ItemToPurchase) -> None:
        # --- case-insensitive match ---
        target = item.item_name.strip().lower()
        for it in self.cart_items:
            if it.item_name.strip().lower() == target:
                if item.item_description != "none":
                    it.item_description = item.item_description
                if item.item_price != 0:
                    it.item_price = item.item_price
                if item.item_quantity != 0:
                    it.item_quantity = item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self) -> int:
        return sum(it.item_quantity for it in self.cart_items)

    def get_cost_of_cart(self) -> float:
        return sum(it.item_price * it.item_quantity for it in self.cart_items)

    def print_total(self) -> None:
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = self.get_num_items_in_cart()
        print(f"Number of Items: {num_items}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            print("Total: $0")
            return
        for it in self.cart_items:
            it.print_item_cost()
        print(f"Total: {_fmt_money(self.get_cost_of_cart())}")

    def print_descriptions(self) -> None:
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for it in self.cart_items:
            it.print_item_description()


#  Step 5: Menu 
def print_menu(cart: ShoppingCart) -> None:
    menu = (
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
        print(menu)
        choice = input("Choose an option:\n").strip().lower()

        if choice == "q":
            break
        elif choice == "a":
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            desc = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            qty = int(input("Enter the item quantity:\n"))
            cart.add_item(ItemToPurchase(item_name=name, item_description=desc, item_price=price, item_quantity=qty))
        elif choice == "r":
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)
        elif choice == "c":
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            qty = int(input("Enter the new quantity:\n"))
            # create a new ItemToPurchase, then modify
            temp = ItemToPurchase(item_name=name, item_quantity=qty)
            cart.modify_item(temp)
        elif choice == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()
        else:
            continue


#  Step 7–10: Driver 
def main():
    print("Enter customer's name:")
    customer_name = input()
    print("Enter today's date:")
    current_date = input()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    cart = ShoppingCart(customer_name=customer_name, current_date=current_date)
    print_menu(cart)


if __name__ == "__main__":
    main()
