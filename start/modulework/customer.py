import bank

bank.menu()
choice = int(input("select action from above Menu: "))

while choice != 5:
    if choice == 1:
        name = input("enter your name: ")
        balance = float(input("enter amount: "))
        print(bank.create_acc(name, balance), "\n")
    elif choice == 2:
        name = input("enter account holder name: ")
        balance = float(input("enter amount: "))
        print(bank.deposit(name, balance), "\n")
    elif choice == 3:
        name = input("enter account holder name: ")
        balance = float(input("enter amount: "))
        print(bank.withdraw(name, balance), "\n")
    elif choice == 4:
        name = input("enter account holder name: ")
        print(bank.check_balance(name), "\n")
    else:
        print("Invalid Selection!\n")
    bank.menu()
    choice = int(input("select action from above Menu: "))
