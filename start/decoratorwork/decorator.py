# decorator is a method to modify existing function without changing its code
# def mydecor(func):
#     def wrapper():
#         print("this is decorator method")
#         func()
#     return wrapper
#
# @mydecor
# def myfunc():
#     print("this is main function")
#
# myfunc()

'''create decorator that prints:
"function is starting" before execution
"function ended" after execution'''
# def dec(fun):
#     def wrap():
#         fun()
#         print("function ended")
#     return wrap
#
# @dec
# def main_fun():
#     print("function is starting")
# main_fun()


'''create decorator that multiplies the return value by 2'''
# def my_dec(fun):
#     def wrap():
#         result = fun()*2
#         return result
#     return wrap
#
# @my_dec
# def main_fun():
#     value = int(input("enter any integer value: "))
#     return value
# print(main_fun())


'''
create a decorator that checks if input number is negative
if negative -> print "invalid input"
'''
# def my_dec(fun):
#     def wrap():
#         result = fun()
#         if result < 0:
#             return "invalid input"
#         else:
#             return result
#     return wrap
#
# @my_dec
# def main_fun():
#     value = int(input("enter a number: "))
#     return value
# print(main_fun())


'''
create a decorator that counts how many times a function is called
'''
# def my_dec(fun):
#     counter = 0
#     def wrap():
#         nonlocal counter
#         counter += 1
#         fun()
#         return counter
#     return wrap
#
# @my_dec
# def main_fun():
#     print("hello")
#
# print(main_fun())
# print(main_fun())
# print(main_fun())
# print(main_fun())
# print(main_fun())
# print(main_fun())
# print(main_fun())


'''
create a decorator that adds "result:" before output
'''
# def my_dec(fun):
#     def wrap(*args):
#         print(f"result: {fun(*args)}")
#     return wrap
# @my_dec
# def main_fun(a, b):
#     return a+b
#
# main_fun(10, 20)


'''
create a decorator to check login is successful or not
'''
# def my_dec(fun):
#     def wrap():
#         is_logged_in = True
#         if is_logged_in:
#             fun()
#         else:
#             print("please login !!")
#     return wrap
#
# @my_dec
# def main_fun():
#     print("welcome to waytocode!")
# main_fun()


'''
create a decorator that delays function execution by 2 sec
'''
# import time
# def my_dec(fun):
#     def wrap():
#         time.sleep(2)
#         return fun()
#     return wrap
#
# @my_dec
# def main_fun():
#     print('hello, thank you for waiting!')
# main_fun()

'''
create a decorator that allows only even numbers
'''
# def my_dec(fun):
#     def wrap(*args):
#         for i in args:
#             if i % 2 != 0:
#                 return "odd numbers are not allowed"
#             else:
#                 pass
#         return fun(*args)
#     return wrap
# @my_dec
# def main_fun(num1, num2):
#     return num1, num2
# print(main_fun(2,4))

'''
create deorator that runs function 2 times
'''
# def my_dec(fun):
#     def wrap():
#         fun()
#         fun()
#     return wrap
#
# @my_dec
# def main_fun():
#     print('hello')
# main_fun()

'''
create decorators that prints function arguments
'''
# def my_dec(fun):
#     def wrap(*args):
#         for i in args:
#             print(i)
#         return fun(*args)
#     return wrap
#
# @my_dec
# def main_fun(*num):
#     return f"sum: {sum(num)}"
# print(main_fun(1,2,3,4,5,6,7,8))

'''
create decorator for safe division
'''
# def my_dec(fun):
#     def wrap(num1, num2):
#         try:
#             if num2 == 0:
#                 raise ZeroDivisionError("can not divide by zero")
#             else:
#                 fun(num1, num2)
#         except ZeroDivisionError as e:
#             print(e)
#     return wrap
#
# @my_dec
# def main_fun(n1, n2):
#     print(n1/n2)
# main_fun(10,0)