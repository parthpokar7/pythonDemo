items = {}

menuList = ["Add Item", "Remove Item", "View Cart", "Total Price", "exit"]


def menu():
    print("Main Menu:")
    for i in range(1, len(menuList)+1):
        print(f"{i}: {menuList[i-1]}")


def add_item(name, price):
    if price <= 0:
        return "enter valid price"
    else:
        items[name] = price
        return f"{name} added to cart"


def remove_item(name):
    if name in items.keys():
        items.pop(name)
        return f"{name} removed from cart"
    else:
        return f"{name} is not available in cart"


def view_cart():
    if len(items.keys()) > 0:
        return items
    else:
        return "cart is empty"

def total_price():
    total = 0
    if len(items.keys()) > 0:
        for item in items.keys():
            total += items[item]
        return total
    else:
        return "Cart is Empty!!"