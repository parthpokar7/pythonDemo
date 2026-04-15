# def sum(a, b):
#     return a + b
#
# print(sum(10, 20))
#
#
# def greetUser(name):
#     print("Hello, " + name + "!")
#
# greetUser("parth")
#
#
# def checkIfEven(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("odd")
#
# checkIfEven(int(input("enter a number: ")))



# def stringLen(str):
#     return len(str)
#
# print(stringLen("abcdefghijkl"))



# def findMax(a, b, c):
#     if a > b:
#         if (a > c):
#             print(a)
#         else:
#             print(c)
#     elif (b > c):
#         print(b)
#     else:
#         print(c)
#
# findMax(1000, 200, 30)


# def findArea (length, width):
#     print(length*width)
#
# findArea(10, 20)

# def sumOfList(mylist):
#     return sum(mylist)
#
# print(sumOfList([10, 20, 30, 700]))


#
# def swap(a, b):
#     print("before Swap")
#     print("a:", a, "b:", b)
#     a, b = b, a
#     print("before Swap")
#     print("a:", a, "b:", b)
#
# swap(10, 50)

# def swap(a, b):
#     a = a + b
#     b = a - b
#     a = a - b
#     print(a, b)
#
# swap(50, 60)

# def greeting(name="guest"):
#     print("Hello, " + name)
#
# greeting("Parth")

# def productOfNumbers(*mylist):
#     product = 1
#     for number in mylist:
#         product *= number
#
#     return product
#
# print(productOfNumbers(1,2,3,4))
#
#
# def scrAndCube(num):
#     print(num ** 2)
#     print(num ** 3)
#
# scrAndCube(2)
#
#


# def pelindromeString(str):
#     if str == str[::-1]:
#         print(True)
#     else:
#         print(False)
#
#
# pelindromeString("aba")

#
# def fact(num):
#
#
# print(fact(5))

# def revStr(str):
#     print(str)
#     myList = list(str)
#     rev = []
#     for i in range(len(myList)-1, -1, -1):
#         print(myList[i], end="")
#
# revStr("parth")

# def primeN(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5)+1):
#         if num%i == 0:
#             return False
#     else:
#         return True
# print(primeN(4))

# def findMax(myList):
#     max = 1
#     for i in myList:
#         if max > i:
#             continue
#         else:
#             max = i
#     return max
# print(findMax([1,2,3,40,5,6,7,8]))


# def removeDup(myList):
#     seenList = []
#     for i in myList:
#         if i in seenList:
#             pass
#         else:
#             seenList.append(i)
#
#     return seenList
#
# print(removeDup([1,1,1,2,4,3,5,6,7,6,5,4,3,2,10,5,5,5,8,6,5,5,6,7,7,7,8,2,1,3,55,64,8]))


# def factNum(num):
#     fact=1
#     for i in range(1, num+1):
#         fact *= i
#
#     return fact
# print(factNum(5))

# def sumOfList(myList):
#     sum = 0
#     for i in myList:
#         sum += i
#     return sum
# print(sumOfList([1,2,3,4]))

# def sortList(myList):
#     for i in range(len(myList)):
#         for j in range(i+1, len(myList)):
#             if myList[i] > myList[j]:
#                 myList[i], myList[j] = myList[j], myList[i]
#
#
#     return myList
# print(sortList([10,4,5,2,7,8,6,1]))

def fibSeries(num):
    fib = [0, 1]
    for i in range(num + 1):
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    print(fib)

fibSeries(5)