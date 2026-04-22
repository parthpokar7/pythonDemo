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


'''
create a decorator that logs the execution of a function
'''
# def my_dec(fun):
#     def wrap():
#        print(f"executing '{fun.__name__}' function")
#        fun()
#     return wrap
#
# @my_dec
# def main_fun():
#     print(10 + 20)
#
# main_fun()

# @my_dec
# def main_fun():
#     for i in range(1, 6):
#         time.sleep(1)
#         print(i)

'''
write a decorator that measure and print the execution time
'''
# import time
# def my_dec(fun):
#     def wrap():
#         start = time.time()
#         fun()
#         end = time.time()
#         print(f"{fun.__name__} took {(end - start):.2f} seconds")
#     return wrap
# main_fun()


'''
create decoratore that converts the return value of a function to uppercase
'''
# def my_dec(fun):
#     def wrap():
#         print(fun().upper())
#     return wrap
#
# @my_dec
# def main_fun():
#     return "hello world"
#
# main_fun()

'''
implement a decorator that checks
if function args are positive int
if not print error message
'''
# def my_dec(fun):
#     def wrap(*args):
#         for i in args:
#             if i < 0:
#                 return "only positive values are allowed !!!"
#         return fun(*args)
#     return wrap
# @my_dec
# def main_fun(a, b):
#     return a+b
# print(main_fun(-4,5))

'''
create a decorator that retires execution of a function up to 3 times it it raises an exception
'''
# import random
# def my_dec(fun):
#     def wrap():
#         for i in range(3):
#             try:
#                 print(f"attempt {i+1}")
#                 return fun()
#             except ValueError as e:
#                 print(e)
#         return "all attempts failed"
#     return wrap
#
# @my_dec
# def main_fun():
#
#     if random.random() < 0.7:
#         raise ValueError("value is very less")
#     return "success"
# print(main_fun())



