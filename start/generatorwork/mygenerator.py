# generator is a function which returns single value at a time instead of returning all values at once

# def count():
#     for i in range(1, 50):
#         yield i
#
#
# for num in count():
#     if num <= 20:
#         print(num, end=" ")


# even numbers
# def evennums():
#     for i in range(0, 20, 2):
#         yield i
#
# for num in evennums():
#     print(num, end=" ")


# # multiple of 3
# def multiples():
#     for i in range(1, 10):
#         yield 3*i
#
# for num in multiples():
#     print(num, end=" ")

# squre of previous number
def sqrofnums():
    num = 2;
    for i in range(5):
        yield num
        num = num ** 2

for num in sqrofnums():
    print(num)