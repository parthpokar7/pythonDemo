# class Parent:
#     def parent_fun(self):
#         print("Parent called")
#
# class Parent2:
#     def parent2_fun(self):
#         print("Parent2 called")
#
# class Child1(Parent):
#     def child1_fun(self):
#         print("Child1 called")
#
# class Child2(Child1, Parent2):
#     def child2_fun(self):
#         print("child2 called")
#
#
# obj = Child2()
# obj.parent_fun()
# obj.parent2_fun()
# obj.child1_fun()
# obj.child2_fun()


class Company:
    employee = {}
    def register_data(self, name, idnum):
        self.employee[idnum] = name
        print("values registered successfully")

    def show_data(self):
        print(self.employee)


class Employee(Company):

    def get_data(self):
        eid = input("Enter your id: ")
        ename = input("Enter your name: ")
        print("values entered successfully")
        super().register_data(ename, eid)


e = Employee()
e.get_data()
e.show_data()
