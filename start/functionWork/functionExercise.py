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
    #     if num != 0:
    #         return num * fact(num - 1)
    #     else:
    #         return 1
    #
    # print(fact(5))

# def printData(myDictionary):
#     for key, value in myDictionary.items():
#         print(f"{key}: {value}")
#
# printData({"a": 1, "b": 2, "c": 3})

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
#     max = 0
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


# def fact(num):
#     factNum = 1
#     for i in range(num,0, -1):
#         factNum *= i
#     return factNum
#
# print(fact(5))

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

# def convertToFahrenheit(degrees):
#     print(degrees * 9 / 5 + 32)
#
# convertToFahrenheit(5)

# def fibSeries(num):
#     fib = [0, 1]
#     for i in range(num + 1):
#         fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
#     print(fib)
#
# fibSeries(5)


# def secLargeNumber(num):
#     max = 0
#     second = 0
#     for i in num:
#         if i > max:
#             second = max
#             max = i
#         elif i > second and i != max:
#             second = i
#     print(second)
#
#
# secLargeNumber([1,8,2,345,52,6,5,45,65,100])


# def countvowels(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     count = 0
#     for ch in string:
#         if ch in vowels:
#             count += 1
#     print(count)
#
# countvowels("hello, how are you?")

# def is_anagram(string1, string2):
#     if len(string1) != len(string2):
#         return False
#     else:
#         sorted_string1 = sorted(string1)
#         sorted_string2 = sorted(string2)
#         print(sorted_string1 == sorted_string2)
#
# is_anagram("silent", "listen")

# def intersection(list1, list2):
#     result = []
#     for item in list1:
#         if item in list2:
#             result.append(item)
#             list2.remove(item)
#     return result
#
# print(intersection([1,2,3,4,5,6,5,8,9,1,8,6,7], [5,6,8,9,3,4,5,6]))