import cart

cart.menu()
choice = int(input("select action from above Menu: "))

while choice != 5:
    if choice == 1:
        name = input("enter item name: ")
        price = float(input("enter amount: "))
        print(cart.add_item(name, price), "\n")
    elif choice == 2:
        name = input("enter item name to remove: ")
        print(cart.remove_item(name), "\n")
    elif choice == 3:
        print(cart.view_cart(), "\n")
    elif choice == 4:
        print(cart.total_price(), "\n")
    else:
        print("Invalid Selection!\n")
    cart.menu()
    choice = int(input("select action from above Menu: "))
