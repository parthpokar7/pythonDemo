from calculation import add
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))

print("Addition = 1"
      "\nSubstraction = 2"
      "\nMultiplication = 3"
      "\nDivision = 4")
operation = int(input("enter operation you want to perform: "))

print(add(num1, num2, operation))