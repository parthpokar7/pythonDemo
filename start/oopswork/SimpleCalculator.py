class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return f"{self.num1} + {self.num2} = {self.num1 + self.num2}"

    def substraction(self):
            return f"{self.num1} - {self.num2} = {self.num1 - self.num2}"

    def multiplication(self):
            return f"{self.num1} * {self.num2} = {self.num1 * self.num2}"

    def division(self):
            return f"{self.num1} / {self.num2} = {self.num1 / self.num2}"


num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))

calc = Calculator(num1, num2)
print(calc.addition())
print(calc.substraction())
print(calc.multiplication())
print(calc.division())
