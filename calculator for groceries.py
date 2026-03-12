
#import sys module with establishes parameters
import sys
from decimal import Decimal
#defining grocery items, price and units
items = {
    'apple': {'price': 1.50, 'unit': 'kg'},
    'banana': {'price': 0.75, 'unit': 'each'},
    'bread': {'price': 2.50, 'unit': 'loaf'}
}

cart = {}
#defining how things will be add to cart for calculation
def add_item(name):
    if name in items:
        item = items[name]
        while True:
            quantity = int(input("How many " + name + " do you want to buy? "))
            total_price = Decimal(quantity) * Decimal(item['price'])
            cart[name] = {'quantity': quantity, 'total_price': total_price}
            break
#what to do if they choose something not available
    else:
        print("Item not found.")
#creating a list of items for sale
def show_available_items():
    for key in items.keys():
        price_per_unit = items[key]['price']
        unit = items[key]['unit']
        print(key + ": " + str(format(price_per_unit, '.2f')) + ' per ' + unit)
#calculating cost of items they will purchase for the cart
def calculate_total_cost():
    total_cost = 0
    for item in cart.values():
        total_cost += item['quantity'] * item['total_price']
    return total_cost
#applying specific parameters to items in cart
while True:
    choice = input("Add an item, show available items or calculate the total cost? ").lower()
    if choice == 'add':
        name = input("Enter the item name: ")
        add_item(name)
    elif choice == 'show':
        show_available_items()
    #showing the total cost
    elif choice == 'total':
        print("Total cost: $" + str(format(calculate_total_cost(), '.2f')))
    else:
        break
