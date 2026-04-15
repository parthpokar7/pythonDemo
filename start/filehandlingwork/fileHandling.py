# data = open("data.txt", "r")
# if data:
#     print("file is accessible")
# else:
#     print("file not found")

# data = open("data.txt", "x")
# if data:
#     print("file is accessible")
# else:
#     print("file not found")

# data= open("data.txt", "w")
#
# data.write("Hello, Welcome to Python file handling.")
#
# data.close()

# data = open("data.txt", "r")
# getdata = data.read(11)
# print(getdata)
# data.close()


# data = open("data.txt", "a")
# data.write("\nThis is second line")
#
# data.close()


# data = open("data.txt", "r")
# getData = data.readline()
# print(getData)
# data.close()

# data = open("data.txt", "r")
# for i in data.readlines():
#     print(i)
# data.close()

# data = open("data.txt", "r")
# getData = data.readlines()
# print(getData)
# data.close()


# data = open("data.txt", "r")
# getData = data.read()
# print(getData)
# data.close()

# import os
# data = os.rename("data.txt", "data1.txt")


# data = open("parth.txt", "r")
# # getData = data.read()
# for word in data.read():
#     print(word)
# # print(getData)
# data.close()

data=open('parth.txt', 'r')
word='Hello'
for i in data:
    if word in i:
        print("matched")