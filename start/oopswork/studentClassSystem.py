class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print(self.name, self.age, self.course)


name = input("enter your name: ")
age = int(input("enter your age: "))
course = input("enter course name: ")

std = Student(name, age, course)
std.display_details()