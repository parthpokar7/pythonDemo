from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass

class Ractangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2*(self.width + self.length)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return f"{2 * (3.14 * self.radius):.2f}"


r = Ractangle(10, 20)
print(r.area())
print(r.perimeter())

c = Circle(10)
print(c.area())
print(c.perimeter())

