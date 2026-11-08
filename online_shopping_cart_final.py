class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_cost(self):
            item_total=self.item_price * self.item_quantity
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${item_total:.2f}")

class ShoppingCart:
    def __init__(self, customer_name = "none", current_date = "January 1, 2020"): 
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item): 

        self.cart_items.append(item) 

    def remove_item(self, item_name): 
        for item in self.cart_items: 
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
            
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, new_item):
            for item in self.cart_items:
                if item.item_name == new_item.item_name: 
                    if new_item.item_description != "none": 
                        item.item_description = new_item.item_description 
                    if new_item.item_price != 0:
                        item.item_price = new_item.item_price 
                    if new_item.item_quantity != 0: 
                        item.item_quantity = new_item.item_quantity 
                    return 
        
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self): 
            total_quantity = 0 
            for item in self.cart_items: 
                total_quantity += item.item_quantity
            return total_quantity

    def get_cost_of_cart(self): 
            total_cost = 0 
            for item in self.cart_items: total_cost += item.item_price * item.item_quantity
            return total_cost 

    def print_total(self):
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            if len(self.cart_items) == 0:
                print("SHOPPING CART IS EMPTY")
            else:
                for item in self.cart_items:
                    item.print_item_cost()

            print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            for item in self.cart_items:
                print(f"{item.item_name}: {item.item_description}")

def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")

customer_name = input("Enter customer's name: \n")
current_date = input("Enter today's date: \n")
print()
print(f"Customer name: {customer_name}")
print(f"Today's date: {current_date}") 

cart = ShoppingCart(customer_name, current_date) 


# Main Program

#Menu Loop

command = ""

while command != "q":
    print_menu()
    command = input("Choose an option: \n")

    if command == "q":
        break 

    elif command == "a":
        print("ADD ITEM")
        item = ItemToPurchase() 

        print("Enter the item name:")
        item.item_name = input()

        print("Enter the item description:")
        item.item_description = input() 

        print("Enter the item price:")
        item.item_price = float(input())

        print("Enter the item quantity:")
        item.item_quantity = int(input())

        cart.add_item(item)

    elif command == "r":
        print("REMOVE ITEM")
        item_name = input("Enter name of item to remove: \n")
        cart.remove_item(item_name) 

    elif command == "c":
        print("CHANGE ITEM QUANTITY")
        item = ItemToPurchase()

        print("Enter the item name:")
        item.item_name = input()

        print("Enter the new quantity:")
        item.item_quantity = int(input())

        cart.modify_item(item)

    elif command == "i":
        print("OUTPUT ITEM'S DESCRIPTIONS") 
        cart.print_descriptions()

    elif command == "o": 
        print("OUTPUT SHOPPING CART")
        cart. print_total()

    else:
        print("Invalid option. Please try again.")