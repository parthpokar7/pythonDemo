all_acc = {}
menuList = ["Create Account", "Deposit", "Withdraw", "Check Balance", "exit"]


def menu():
    print("Main Menu:")
    for i in range(1, len(menuList)+1):
        print(f"{i}: {menuList[i-1]}")


def create_acc(name, bal):
    if name in all_acc.keys():
        return "Account already exists with this name!!"
    else:
        if bal >= 0:
            all_acc[name] = bal
        else:
            return "enter valid amount"
        return "your account is created!"


def deposit(name, amount):
    if name in all_acc.keys():
        all_acc[name] += amount
        return f"{amount} is deposited in your account"
    else:
        return "invalid account"


def withdraw(name, amount):
    if name in all_acc.keys():
        if all_acc[name] < amount:
            return "insufficient balance !!"
        else:
            all_acc[name] -= amount
            return f"{amount} is withdrawn from your account"
    else:
        return "invalid account"


def check_balance(name):
    if name in all_acc.keys():
        return f"available balance is '{all_acc[name]}'"
    else:
        return "invalid account"
