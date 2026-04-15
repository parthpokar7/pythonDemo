def myfunc():
    print("welcome to the Python Method")

myfunc()

def addNumber():
    print(10+20)

addNumber()

def addNumberUsingArgs(a, b):
    print(a+b)

addNumberUsingArgs(20, 30)

def defValueArgs(a, b=40):
    print(a+b)

defValueArgs(20)

def defValueArgs2(a, b=40):
    print(a+b)

defValueArgs(20, 70)

def returnValues(a, b):
    return a+b

print(returnValues(50,60))


def greetUser(name):
    print("hello", name)

greetUser(input("enter your name: "))

def myFuction(name, city):
    print("Hello " + name + ", " + "welcome to WayToCode! at " + city)

myFuction(city="Ahmedabad", name="Parth")


def greetUsers(*names): #what does *names called
    print(len(names))
    for name in names:
        print(name)

greetUsers("Parth", "Jack", "John", "James", "Jerry")
