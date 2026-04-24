class Animal:

    def sound(self):
        print("Generic Sound")


class Dog(Animal):
    def sound(self):
        print("Bark !!")


class Cat(Animal):
    def sound(self):
        print("Meow !!")


d = Dog()
d.sound()

c = Cat()
c.sound()