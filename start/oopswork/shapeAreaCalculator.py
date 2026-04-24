class Shape:
    def area(self):
        return None


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        ara = 3.14 * (self.radius ** 2)

        return ara


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        ara = self.width * self.length
        return ara



rec = Rectangle(10, 20)
print(rec.area())

cir = Circle(10)
print(cir.area())