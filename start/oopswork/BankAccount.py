class Bank:
    def __init__(self):
        self.__balance = 0.00

    def deposit(self, bal):
        self.__balance += bal
        print(f"INR '{bal}' credited to your account!!")

    def withdraw(self, bal):
        if bal > self.__balance:
            print("insufficient balance")
        else:
            self.__balance -= bal
            print(f"INR '{bal}' debited from your account!!")

    def check_bal(self):
        print(f"available balance: INR {self.__balance}")


b = Bank()
b.deposit(5000)
b.check_bal()
b.withdraw(99.99)
b.check_bal()
