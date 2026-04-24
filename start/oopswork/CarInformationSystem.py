class Car:
    def __init__(self):
        self.brand = "Hyundai"
        self.model = "I20"
        self.price = 900000

    def display_details(self):
        print(self.brand, self.model, self.price)


c = Car()
c.display_details()