# Step 1: Define the ItemToPurchase class
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")



# Step 2: Main program
if __name__ == "__main__":
    print("Item 1")
    name1 = input("Enter the item name:\n")
    price1 = float(input("Enter the item price (numbers only):\n"))
    quantity1 = int(input("Enter the item quantity:\n"))
    item1 = ItemToPurchase(name1, price1, quantity1)

    print("\nItem 2")
    name2 = input("Enter the item name:\n")
    price2 = float(input("Enter the item price (numbers only):\n"))
    quantity2 = int(input("Enter the item quantity:\n"))
    item2 = ItemToPurchase(name2, price2, quantity2)

    # Step 3: Output total cost
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print(f"\nTotal: ${float(total)}")
