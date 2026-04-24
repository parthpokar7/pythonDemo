class Person:
    name = None
    age = None

    def display_data(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)


class Student(Person):
    course = None
    marks = None

    def display_details(self, course, marks):
        self.course = course
        self.marks = marks
        print(self.course, self.marks)


std = Student()
std.display_data("parth", 26)
std.display_details("ML/AI", 96)
